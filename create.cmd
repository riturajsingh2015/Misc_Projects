@echo off

SETLOCAL
CALL :Create %1 %2
EXIT /B %ERRORLEVEL%

:Create
python create.py %~1 %~2

cd %~1
git init
git add README.md
git add .
git commit -m "first commit"
git config --global user.email riturajsingh2015@gmail.com
git config --global user.name riturajsingh2015

git remote add origin https://github.com/riturajsingh2015/%~1.git
git push -u origin master

atom %CD%

EXIT /B 0
