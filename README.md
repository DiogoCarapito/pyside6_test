# pyside6_test

[![Github Actions Workflow](https://github.com/DiogoCarapito/pyside6_test/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/pyside6_test/actions/workflows/main.yaml)

Python PySide6 test project.

Python version: 3.12

## cheat sheet

### venv

create venv

```bash
python3.12 -m venv .venv
```

activate venv mac/linux

```bash
source .venv/bin/activate
```

activate venv windows (powershell)

```bash
.venv\Scripts\activate
```

### build

macos

```bash
nuitka --onefile --standalone --enable-plugin=pyside6 --output-filename=Pyside6_test --noinclude-qt-plugins=iconengines,imageformats --macos-app-icon=assets/logo.icns app.py
```

windows

```bash
nuitka --onefile --standalone --enable-plugin=pyside6 --windows-disable-console --output-filename=your_app_name --windows-icon-from-ico=assets/logo.ico app.py
```
