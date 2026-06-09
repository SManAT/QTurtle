#!/usr/bin/env python3
"""Build an application executable with PyInstaller using TOML configuration.

Reads [tool.<app>.build] from pyproject.toml. The app section is either
passed via --app=<name> or auto-detected as the only section containing
an 'app_module' key.
"""

import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

import PyInstaller.__main__


def load_config(app_name: str | None = None):
    """Load build configuration from pyproject.toml.

    Looks for [tool.<app_name>.build]. When app_name is None, auto-detects
    by finding tool sub-sections that contain 'app_module'.
    """
    config_path = Path("pyproject.toml")

    if not config_path.exists():
        raise FileNotFoundError("pyproject.toml not found")

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    tool = config.get("tool", {})

    if app_name:
        section = tool.get(app_name, {}).get("build", {})
        if not section:
            raise ValueError(f"No [tool.{app_name}.build] section found in pyproject.toml")
        return section, app_name

    # Auto-detect: find all [tool.*.build] sections that have app_module
    candidates = [
        name for name, value in tool.items()
        if isinstance(value, dict) and "app_module" in value.get("build", {})
    ]

    if not candidates:
        raise ValueError(
            "No [tool.<app>.build] section with 'app_module' found in pyproject.toml.\n"
            "Use --app=<name> to specify the section explicitly."
        )
    if len(candidates) > 1:
        names = ", ".join(candidates)
        raise ValueError(
            f"Multiple build sections found: {names}\n"
            f"Use --app=<name> to specify which one to build."
        )

    name = candidates[0]
    return tool[name]["build"], name


def get_python_env():
    """Determine Python environment to use"""
    venv_dir = Path(".venv")

    # Check if .venv exists
    if venv_dir.exists():
        env_type = ".venv (virtual environment)"
        using_venv = True
    else:
        env_type = "system Python"
        using_venv = False

    print("=" * 60)
    print("Environment Information")
    print("=" * 60)
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Using: {env_type}")
    print(f"Current directory: {Path.cwd()}")
    print("=" * 60 + "\n")

    return using_venv


def build_config_to_args(config):
    """Convert TOML config to PyInstaller arguments"""
    if not config:
        raise ValueError("No build configuration found in pyproject.toml")

    # Platform separator for add-data paths
    sep = ";" if sys.platform == "win32" else ":"

    # Required fields
    app_module = config.get("app_module", "src/app.py")
    app_name = config.get("app_name", "App")

    args = [
        app_module,
        f"--name={app_name}",
    ]

    # Optional: icon
    icon = config.get("icon")
    if icon and Path(icon).exists():
        args.append(f"--icon={icon}")

    # Optional: windowed mode
    if config.get("windowed", True):
        args.append("--windowed")

    # Build mode (onedir or onefile)
    build_mode = config.get("build_mode", "onedir")
    args.append(f"--{build_mode}")

    # Optional: clean and noconfirm
    if config.get("clean", True):
        args.append("--clean")
    if config.get("noconfirm", True):
        args.append("--noconfirm")

    # Add data files
    data_files = config.get("data_files", [])
    for data_file in data_files:
        if Path(data_file).exists():
            args.append(f"--add-data={data_file}{sep}{Path(data_file).name}")

    # Hidden imports
    hidden_imports = config.get("hidden_imports", [])
    for imp in hidden_imports:
        args.append(f"--hidden-import={imp}")

    # Collect all packages
    collect_all = config.get("collect_all", [])
    for pkg in collect_all:
        args.append(f"--collect-all={pkg}")

    # Exclude modules (e.g., PyQt6 if using PySide6)
    excludes = config.get("exclude_modules", [])
    for exc in excludes:
        args.append(f"--exclude-module={exc}")

    # Strip debug symbols (Unix only — strip binary doesn't exist on Windows)
    if config.get("strip", False) and sys.platform != "win32":
        args.append("--strip")

    # UPX compression (enabled by default in PyInstaller 6.x when upx is in PATH)
    if not config.get("upx", True):
        args.append("--noupx")
    else:
        upx_dir = config.get("upx_dir")
        if upx_dir and Path(upx_dir).exists():
            args.append(f"--upx-dir={upx_dir}")
        for exc in config.get("upx_exclude", []):
            args.append(f"--upx-exclude={exc}")

    # Log level (for verbosity control)
    log_level = config.get("log_level", "WARN")
    args.append(f"--log-level={log_level}")

    return args


def add_python_interpreter(args: list, sep: str) -> tuple:
    """Bundle the current python.exe into _internal/ for subprocess script execution.

    Also writes a python3XX._pth file next to it so the bundled interpreter can
    resolve stdlib from _internal/ (base_library.zip + individual .pyc files).
    Returns (updated_args, list_of_temp_files_to_clean_up).
    """
    cleanup = []
    python_exe = Path(sys.executable)

    if not python_exe.exists() or not python_exe.stem.lower().startswith("python"):
        print("⚠️  WARNING: sys.executable does not look like Python, skipping interpreter bundling")
        return args, cleanup

    args = list(args)
    args.append(f"--add-binary={python_exe}{sep}.")

    # A ._pth file next to python.exe in _internal/ overrides default sys.path.
    # "."            → _internal/ itself (all .pyc files PyInstaller placed there)
    # base_library.zip → PyInstaller's bootstrap zip (abc, codecs, io, …)
    ver = f"{sys.version_info.major}{sys.version_info.minor}"
    pth_name = f"python{ver}._pth"
    pth_path = Path(pth_name)
    # "import site" re-enables PYTHONPATH processing (._pth files disable it by default)
    pth_path.write_text(".\nbase_library.zip\nimport site\n", encoding="utf-8")
    args.append(f"--add-data={pth_path}{sep}.")
    cleanup.append(str(pth_path))

    print(f"  Bundling interpreter : {python_exe}")
    print(f"  Stdlib path config   : {pth_name}")
    return args, cleanup


def parse_args():
    """Parse --app=<name> from sys.argv, return app name or None."""
    for arg in sys.argv[1:]:
        if arg.startswith("--app="):
            return arg.split("=", 1)[1].strip()
    return None


def build():
    """Build the application defined in pyproject.toml."""
    cli_app = parse_args()
    print("📋 Loading configuration from pyproject.toml...\n")
    config, section_name = load_config(cli_app)

    app_name = config.get("app_name", section_name)

    print(f"📦 Build Configuration for {app_name}")
    print("=" * 60)
    print(f"App module: {config.get('app_module', 'src/app.py')}")
    print(f"Icon: {config.get('icon', 'Not set')}")
    print(f"Build mode: {config.get('build_mode', 'onedir')}")
    print(f"Data files: {', '.join(config.get('data_files', []))}")
    print(f"Hidden imports: {len(config.get('hidden_imports', []))} packages")
    print("=" * 60 + "\n")

    get_python_env()

    args = build_config_to_args(config)
    sep = ";" if sys.platform == "win32" else ":"

    cleanup_files = []
    if config.get("include_python_interpreter", False):
        print("\n🐍 Bundling Python interpreter for subprocess execution...")
        args, cleanup_files = add_python_interpreter(args, sep)

    try:
        print("\n🔨 Building with PyInstaller...\n")
        PyInstaller.__main__.run(args)
    finally:
        for f in cleanup_files:
            try:
                Path(f).unlink(missing_ok=True)
            except Exception:
                pass

    output_dir = config.get("output_dir", "dist")
    print(f"\n✅ Build complete!")
    print(f"   Executable: {output_dir}/{app_name}/")


if __name__ == "__main__":
    try:
        build()
    except KeyboardInterrupt:
        print("\n\n❌ Build cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
