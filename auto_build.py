#!/usr/bin/env python3
"""Build script with automatic virtual environment detection"""

import os
import sys
from pathlib import Path

import PyInstaller.__main__


def check_virtual_env():
    """Check if running in virtual environment and show info"""
    in_venv = hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)

    venv_path = os.environ.get("VIRTUAL_ENV", None)

    print("=" * 60)
    print("Environment Check")
    print("=" * 60)
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Running in venv: {'✅ YES' if in_venv else '❌ NO'}")

    if venv_path:
        print(f"Virtual env path: {venv_path}")

    if not in_venv:
        print("\n⚠ WARNING: Not running in virtual environment!")
        print("   Recommendation: Activate .venv first")

        venv_dir = Path(".venv")
        if venv_dir.exists():
            if sys.platform == "win32":
                print("\n   Run: .venv\\Scripts\\activate")
            else:
                print("\n   Run: source .venv/bin/activate")

        response = input("\nContinue anyway? (y/n): ")
        if response.lower() != "y":
            print("Exiting...")
            sys.exit(0)

    print("=" * 60 + "\n")


def get_hidden_imports_from_venv():
    """Get packages installed in current environment"""
    import pkg_resources

    installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    # Package name mappings
    name_mappings = {
        "opencv-python": "cv2",
        "opencv-python-headless": "cv2",
        "pillow": "PIL",
        "pyyaml": "yaml",
        "scikit-learn": "sklearn",
        "beautifulsoup4": "bs4",
        "pyqt6": "PyQt6",
        "pyqt5": "PyQt5",
    }

    hidden_imports = []
    for pkg in installed_packages:
        if pkg in name_mappings:
            hidden_imports.append(name_mappings[pkg])
        elif pkg not in ["pip", "setuptools", "wheel", "pyinstaller"]:
            # Add package, converting dashes to underscores
            hidden_imports.append(pkg.replace("-", "_"))

    return hidden_imports


def build():
    """Build the application"""
    # Check environment
    check_virtual_env()

    # Get hidden imports from installed packages
    print("📦 Detecting installed packages...")
    hidden_imports = get_hidden_imports_from_venv()

    print(f"   Found {len(hidden_imports)} packages")
    print("\n🔍 Key packages detected:")
    key_packages = ["cv2", "PyQt6", "numpy", "PIL"]
    for pkg in key_packages:
        if pkg in hidden_imports:
            print(f"   ✓ {pkg}")

    # Platform separator
    sep = ";" if sys.platform == "win32" else ":"

    # Build arguments
    # add-data: what{sep}copy to
    args = [
        "src/BookImagerQT.py",
        # "--onefile",
        "--windowed",
        "--name=book-imager",
        "--icon=src/app.ico",
        # for runtime load, add the icon to root dir
        f"--add-data=src/app.ico{sep}.",
        f"--add-data=src/ui{sep}ui",
        f"--add-data=src/icons{sep}icons",
        f"--add-data=src/images{sep}images",
        f"--add-data=src/classes/logger_config.yaml{sep}classes",
        "--clean",
        "--noconfirm",
        "--onedir",
        "--console",
    ]

    # Add critical hidden imports
    critical_imports = [
        "cv2",
        "numpy",
        "PyQt6.QtCore",
        "PyQt6.QtGui",
        "PyQt6.QtWidgets",
    ]

    for imp in critical_imports:
        args.append(f"--hidden-import={imp}")

    # Collect data for critical packages
    args.extend(
        [
            "--collect-all=cv2",
            "--collect-all=numpy",
        ]
    )

    print("\n🔨 Building with PyInstaller...")
    PyInstaller.__main__.run(args)

    print("\n✅ Build complete!")
    print("   Executable: dist/book-imager")


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
