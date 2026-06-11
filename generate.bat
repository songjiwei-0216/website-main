@echo off
echo Generating data_songjiwei.js from GeoJSON files...
cd /d "%~dp0"
python generate_data_songjiwei.py
if %errorlevel% equ 0 (
    echo SUCCESS! data_songjiwei.js has been generated.
    echo File size:
    dir js\data_songjiwei.js
) else (
    echo FAILED! Make sure Python is installed.
)
pause
