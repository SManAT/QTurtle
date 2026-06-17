---
name: qturtle-build
description: Build QTurtle into a minimal standalone Windows executable with cx_Freeze. Use whenever the user wants to build, package, freeze, or create an .exe / distributable of QTurtle, or asks to shrink / optimize the build size. Always keeps the build as small as possible.
---

# Build QTurtle (minimal cx_Freeze build)

Goal: produce the **smallest working** standalone QTurtle build. Size is a
first-class requirement — never add a Qt module, plugin or language back
unless the app provably needs it.

QTurtle only imports **QtWidgets, QtGui, QtCore, QtPrintSupport**. Everything
else cx_Freeze pulls in (QML engine, PDF viewer, OpenGL, networking, virtual
keyboard, SVG, ~30 UI languages) is dead weight and is pruned automatically.

## How the minimal build works

`setup_cxfreeze.py` does the slimming itself, in two places:

1. **`build_exe_options["excludes"]`** — keeps heavy Python libs (numpy,
   matplotlib, PyQt6, test/unittest, zoneinfo, …) out of `library.zip`.
2. **`BuildExe._slim_pyside6()`** — runs *after* cx_Freeze's PySide6 hook
   (which copies the entire PySide6 tree) and deletes the unused payload. The
   prune lists are named constants near the top of the file:
   - `KEEP_TRANSLATIONS` — UI languages to keep (default `de`, `en`).
   - `PRUNE_QT_DLLS` — Qt6 feature DLLs to delete (Quick, Qml*, Pdf*, OpenGL,
     Network, VirtualKeyboard, Svg).
   - `PRUNE_QT_PYDS` — Python binding modules to delete (QtNetwork).
   - `PRUNE_PLUGIN_DIRS` — whole plugin folders to delete (tls,
     networkinformation, platforminputcontexts, iconengines, generic).
   - `KEEP_PLUGINS` — whitelist inside kept plugin folders (`platforms` →
     `qwindows.dll`; `imageformats` → `qico/qjpeg/qgif`).

The build prints `Slimmed PySide6: freed N MB` so you can confirm it ran.

## Build commands

Activate the venv if present, then build directly to the temp dir (skips the
interactive prompt in the .bat):

```bash
[ -d .venv ] && source .venv/Scripts/activate
rm -rf build/cxfreeze_temp
python setup_cxfreeze.py build_exe
```

Output lands in `build/cxfreeze_temp/`. To produce the final `dist/` copy with
the cleanup/size report, run the batch file instead (it answers `y`, copies
`cxfreeze_temp` → `dist/QTurtleCxFreeze/`, and prints the total size):

```bash
./build_cxfreeze.bat
```

## Verify the build (required after every change)

1. **Pruning ran** — confirm the build log shows `Slimmed PySide6: freed … MB`.
2. **Only the needed Qt6 DLLs remain** — expect exactly Core, Gui, Widgets,
   PrintSupport:
   ```bash
   ls build/cxfreeze_temp/lib/PySide6/Qt6*.dll | xargs -n1 basename
   ```
3. **Size** — total should be roughly ~80–85 MB (down from ~117 MB unpruned):
   ```bash
   du -sh build/cxfreeze_temp
   ```
4. **It launches** — GUI must stay alive (this proves the `qwindows` platform
   plugin, style and core DLLs survived the prune):
   ```bash
   cd build/cxfreeze_temp && ./QTurtle.exe & PID=$!; sleep 6; \
     kill -0 $PID 2>/dev/null && { echo "launch OK"; kill $PID; } || echo "CRASHED"
   ```
5. **Window/taskbar icon present** — `app.ico` must land where the app looks
   for it at runtime (`rootDir.parent/assets` → `lib/assets` in the build), and
   the `qico` imageformat plugin must survive the prune to decode it:
   ```bash
   ls build/cxfreeze_temp/lib/assets/app.ico \
      build/cxfreeze_temp/lib/PySide6/plugins/imageformats/qico.dll
   ```
   Both are required because `__main__.py` only calls `setWindowIcon()` when the
   file exists, and `SetCurrentProcessExplicitAppUserModelID` makes the taskbar
   use that window icon. Missing either → blank title bar + taskbar icon.
6. **Turtle still runs** — optionally launch and run a turtle script (F5) to
   confirm the `runtime/python.exe` + tkinter/turtle subprocess path works.
   The prune only touches PySide6, so a launch failure points at Qt; a turtle
   failure points at `runtime/`.

## Changing what's included — rules

- **Pruning broke the app?** Don't disable the whole prune. Find the one DLL /
  plugin / module the app actually needed and move it out of the prune list (or
  into a `KEEP_*` whitelist), then re-verify with the steps above.
- **App gains a new Qt module** (e.g. someone imports `QtSvg` or `QtNetwork`):
  remove that entry from `PRUNE_QT_DLLS` / `PRUNE_QT_PYDS` and add the matching
  plugin to `KEEP_PLUGINS` if needed. Grep the source first to be sure:
  ```bash
  grep -rn "PySide6.Qt" src/ --include=*.py
  ```
- **Need another UI language**: add its 2-letter code to `KEEP_TRANSLATIONS`.
- **Default to deleting, not keeping.** When unsure whether something is
  needed, prune it and verify — restore only if a check actually fails.

## Don't

- Don't edit files under `build/` or `dist/` directly — they're regenerated.
- Don't broaden `packages` or drop `excludes` for convenience; that re-bloats
  the build.
- Don't remove `runtime/`, the Tcl/Tk `share/` copy, or `library.zip` — the
  turtle subprocess interpreter needs them.
