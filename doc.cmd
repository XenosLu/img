@echo off
set current=%~dp0
cd /d %current%

echo # Images > README.md
for /f %%i in ('dir /a:d-h /b') do call :MAIN %%i >> README.md
timeout 3
goto :EOF

::https://hub.docker.com/_/python?tab=description

:MAIN
if "%1"==".github" goto :EOF
echo - xenocider/img:%1
echo - registry.cn-shanghai.aliyuncs.com/xenocider/img:%1
goto :EOF
