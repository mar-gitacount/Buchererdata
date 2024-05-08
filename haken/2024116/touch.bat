@echo off
setlocal EnableDelayedExpansion

REM Pythonのバージョン
set "python_version=3.8.5"

REM Pythonのインストール先ディレクトリ
set "install_dir=C:\Python38"

REM インストーラのダウンロード
curl -o python_installer.exe https://www.python.org/ftp/python/%python_version%/python-%python_version%-amd64.exe

REM インストール
python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM 必要なパッケージのインストール
python -m pip install requests beautifulsoup4

pip install pandas

echo Installation completed.

endlocal
