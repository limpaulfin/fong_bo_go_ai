@echo off
echo *** Starting Bo Go AI ***
cd /d "%~dp0"
start /b /min pythonw "%~dp0run_main.py"
echo *** Bo Go AI started in background ***
exit
