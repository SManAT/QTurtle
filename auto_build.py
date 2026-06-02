#!/usr/bin/env python3
"""Build QTurtle executable with PyInstaller using TOML configuration"""

import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

import PyInstaller.__main__


def load_config():
    """Load build configuration from pyproject.toml"""
    config_path = Path("pyproject.toml")

    if not config_path.exists():
        raise FileNotFoundError("pyproject.toml not found")

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    return config.get("tool", {}).get("qturtle", {}).get("build", {})


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
    app_module = config.get("app_module", "src/qturtle.py")
    app_name = config.get("app_name", "QTurtle")

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

    return args


def build():
    """Build the QTurtle application"""
    print("📋 Loading configuration from pyproject.toml...\n")
    config = load_config()

    if not config:
        print("❌ No [tool.qturtle.build] section found in pyproject.toml")
        sys.exit(1)

    app_name = config.get("app_name", "QTurtle")

    print(f"📦 Build Configuration for {app_name}")
    print("=" * 60)
    print(f"App module: {config.get('app_module', 'src/qturtle.py')}")
    print(f"Icon: {config.get('icon', 'Not set')}")
    print(f"Build mode: {config.get('build_mode', 'onedir')}")
    print(f"Data files: {', '.join(config.get('data_files', []))}")
    print(f"Hidden imports: {len(config.get('hidden_imports', []))} packages")
    print("=" * 60 + "\n")

    get_python_env()

    args = build_config_to_args(config)

    print("🔨 Building with PyInstaller...\n")
    PyInstaller.__main__.run(args)

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
