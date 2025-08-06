# Dispatch.spec
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

# Main entry point
entry_point = "main.py"

# Collect hidden imports
hidden_imports = [
    "win32com.client",
    "flask",
    "flask_cors",
    "pandas",
    "csv",
    "io",
    "time",
    "os",
    "numpy",
]

# Collect all submodules from your SAP-related packages
hidden_imports += collect_submodules("GetDocument")
hidden_imports += collect_submodules("TransactionSecond")
hidden_imports += collect_submodules("TransactionThird")



a = Analysis(
    [entry_point],
    pathex=["."],
    binaries=[],
    datas=[],
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="Dispatch",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    icon='favicon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    name="Dispatch",
)
