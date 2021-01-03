@echo off
cls
echo ┌─────────────────────────────┐
echo │ - 스크래치 EXE 변환기 한글화 Ver. 1.1                 │
echo │ - 제작자 : meowmeow55                                    │
echo │ - 한글화 : Linerunner(linerunner15@naver.com)            ㅣ
echo │ - EXE 변환시 한글 지원 : purum5548@naver.com             ㅣ
echo └─────────────────────────────┘
echo  ─ 실행 전 주의사항 ─
echo  ├ EXE화 할 프로그램의 이름을 project로 해주십시오.
echo  └ EXE화 된 프로그램을 종료시 가끔 프로그램이 없어지는 경우가 발생합니다.
:choosename
echo.
set /p choice= - EXE 파일의 이름을 입력해주세요.(/, \, :, *, ?, ", <, >, |, & 제외):
set choice2=%choice%
md garbage_dirs
cd garbage_dirs
md "%choice%.12345"
if errorlevel 1 (
echo 특수문자가 포함되어있습니다. 다른 이름을 입력해주세요.
goto choosename
)
if not exist *.12345 (
echo 특수문자가 포함되어있습니다. 다른 이름을 입력해주세요.
goto choosename
)
if not exist *.exe.12345 set choice2=%choice%.exe
rd "%choice%.12345"
cd ..
rd /s /q garbage_dirs
set /p EXEnameconfirm= - EXE 파일의 이름이 %choice% (이)가 맞습니까? [예 또는 아니오] 
if "%EXEnameconfirm%"=="예" (
goto endchooseEXEname
) ELSE (
goto choosename
)
)
:endchooseEXEname
if "%confirm%"=="name" goto confirm
:choosetitle
echo.
set /p name= - EXE의 타이틀 이름을 입력해 주세요.(만약 실행여부를 묻지 않으면 나오지 않습니다.):
if "%name%"=="default" set name=Scratch Project
set /p titleconfirm= - 이 EXE의 타이틀 이름이 %name% (이)가 맞습니까? [예 또는 아니오] 
if "%titleconfirm%"=="예" (
goto endchoosetitle
) ELSE (
goto choosetitle
)
)
:endchoosetitle
if "%confirm%"=="title" goto confirm
:choosemsg
echo.
set /p messageyn= - EXE파일 실행여부를 물어보시겠습니까? [예 또는 아니오] 
if "%messageyn%"=="예" (
goto choosemsgcode
) ELSE (
if "%messageyn%"=="아니오" (
goto endchoosemsg
) ELSE (
goto choosemsg
)
)
)
)
:choosemsgcode
set msgactivate=1
set /p message= - 실행여부 창에 넣을 말을 설정하세요.( " 없이 "기본" 을 입력하시면 다음처럼 설정됩니다. "이 스크래치 프로젝트를 실행하시겟습니까?"):
if "%message%"=="기본" set message=이 스크래치 프로젝트를 실행하시겟습니까?
set /p msgtextyn= - 넣을 말이  %message% 가 맞습니까?[예 또는 아니오] 
if "%msgtextyn%"=="예" (
goto endchoosemsg
) ELSE (
goto choosemsg
)
)
:endchoosemsg
if "%confirm%"=="message" goto confirm
:repackrequest
echo.
set /p repackyn= - 다시 EXE화 할경우 사용자에게 묻겠습니까? [예 또는 아니오] 
if "%repackYN%"=="예" (
goto endrepackreq
) ELSE (
if "%repackYN%"=="아니오" (
goto repackreqcode
) ELSE (
goto repackrequest
)
)
)
)
:repackreqcode
set /p autorepackYN= - 자동으로 EXE화 할것입니까? [예 또는 아니오] 
if "%autorepackYN%"=="예" (
set autorepack=1
) ELSE (
if "%autorepackYN%"=="아니오" (
set autorepack=0
) ELSE (
goto repackrequest
)
)
)
)
:endrepackreq
if "%confirm%"=="repack" goto confirm
:customicon
echo.
set /p customiconYN= - 사용자 지정 EXE파일 아이콘을 사용하실겁니까? (icon.ico라는이 파일이 원래 배치된 파일과 같은 폴더에 있어야 합니다.) [예 또는 아니오] 
if "%customiconYN%"=="예" (
set customicon=1
) ELSE (
if "%customiconYN%"=="아니오" (
set customicon=
goto confirm
) ELSE (
goto customicon
)
)
)
)
:confirm
echo.
set confirm=
echo Final Confirmation
echo  - EXE 파일의 이름 : %choice%
echo  - EXE 타이틀의 이름 : %name%
if "%msgactivate%"=="1" ( echo  - EXE 실행확인 창: %message% ) ELSE ( echo  - EXE 실행확인 창 : 사용하지 않음 )
if "%autorepack%"=="1" echo  - 재 EXE화 확인 창 : 사용하지 않음, - 자동 EXE화
if "%autorepack%"=="0" echo  - 재 EXE화 확인 창 : 사용하지 않음, - EXE화 건너뛰기
if "%autorepack%"=="" echo  - 재 EXE화 확인 창 : 사용함
if "%customicon%"=="1" ( echo  - 사용자지정 EXE 아이콘 : 사용함) else (  - echo 사용자지정 EXE 아이콘 : 사용하지 않음)
set /p confirm=이 설정이 맞습니까? 만약 아니라면 "name" 를 입력해 EXE파일의 이름을 변경하거나 "title" 를 입력해 EXE 타이틀의 이름을 변경, "message" 를 입력해 실행여부 메세지를 변경, "repack" 를 입력해 재 EXE화 변경, 또는 "icon" 를 입력해 아이콘을 변경할 수 있습니다.( " 없이 소문자로만) - 맞으면 Enter를 눌러주십시오 :
if "%confirm%"=="name" goto choosename
if "%confirm%"=="title" goto choosetitle
if "%confirm%"=="message" goto choosemsg
if "%confirm%"=="repack" goto repackrequest
if "%confirm%"=="icon" goto customicon
if "%confirm%"=="some garbage" echo Congratulations! You took the instructions literally and found this easter egg! :P & pause
if exist project.sb.sb ren project.sb.sb project.sb
if "%customicon%"=="1" (
if exist icon.ico.ico ren icon.ico.ico icon.ico
ren "Required Files\icon.ico" icon_scratch.ico & copy icon.ico "Required Files\icon.ico"
)
move "Required Files\Scratch_Project.nsi" Scratch_Project.nsi
echo Name "%name%" > Scratch_Project.nsi
echo OutFile "%choice2%" >> Scratch_Project.nsi
echo Icon "icon.ico" >> Scratch_Project.nsi
echo RequestExecutionLevel user >> Scratch_Project.nsi
echo SilentInstall silent >> Scratch_Project.nsi
if "%msgactivate%"=="1" (
echo Function .onInit >> Scratch_Project.nsi
echo   MessageBox MB_YESNO "%message%" IDYES gogogo >> Scratch_Project.nsi
echo     Abort >> Scratch_Project.nsi
echo   gogogo: >> Scratch_Project.nsi
echo FunctionEnd >> Scratch_Project.nsi
)
echo Section "Go" >> Scratch_Project.nsi
echo   System::Call 'kernel32::GetModuleFileNameA(i 0, t .R0, i 1024) i r1' >> Scratch_Project.nsi
echo   SectionSetFlags 1 SF_SELECTED >> Scratch_Project.nsi
echo   SetOutPath $TEMP >> Scratch_Project.nsi
echo   File "Scratch.exe" >> Scratch_Project.nsi
echo   File "Scratch.image" >> Scratch_Project.nsi
echo   File "Scratch.ini" >> Scratch_Project.nsi
echo   File "ScratchPlugin.dll" >> Scratch_Project.nsi
echo   File "Mpeg3Plugin.dll" >> Scratch_Project.nsi
echo   File "UnicodePlugin.dll" >> Scratch_Project.nsi
echo   File "CameraPlugin.dll" >> Scratch_Project.nsi
echo   File "WeDoPlugin.dll" >> Scratch_Project.nsi
echo   File "README.txt" >> Scratch_Project.nsi
echo   File "License.txt" >> Scratch_Project.nsi
echo   File "project.sb" >> Scratch_Project.nsi
echo   File "makensis.exe" >> Scratch_Project.nsi
echo   File /r "Plugins" >> Scratch_Project.nsi
echo   File /r "Stubs" >> Scratch_Project.nsi
echo   File /r "locale" >> Scratch_Project.nsi
echo   File "Scratch_Project.nsi" >> Scratch_Project.nsi
echo   File "newexe.bat" >> Scratch_Project.nsi
echo   File "icon.ico" >> Scratch_Project.nsi
echo   File "COPYING" >> Scratch_Project.nsi
echo   ExecWait '"Scratch.exe" "Scratch.image" presentation "$TEMP\project.sb"' >> Scratch_Project.nsi
if "%autorepack%"=="" (
echo   MessageBox MB_YESNO "Repack the project? (If you didn't save the project, select No.)" IDNO exit >> Scratch_Project.nsi
echo    Exec '"newexe.bat" "$R0"' >> Scratch_Project.nsi
echo 	Abort >> Scratch_Project.nsi
)
if "%autorepack%"=="1" (
echo    Exec '"newexe.bat" "$R0"' >> Scratch_Project.nsi
echo 	Abort >> Scratch_Project.nsi
)
echo   exit: >> Scratch_Project.nsi
echo   Delete "Scratch.exe" >> Scratch_Project.nsi
echo   Delete "Scratch.image" >> Scratch_Project.nsi
echo   Delete "Scratch.ini" >> Scratch_Project.nsi
echo   Delete "ScratchPlugin.dll" >> Scratch_Project.nsi
echo   Delete "Mpeg3Plugin.dll" >> Scratch_Project.nsi
echo   Delete "UnicodePlugin.dll" >> Scratch_Project.nsi
echo   Delete "CameraPlugin.dll" >> Scratch_Project.nsi
echo   Delete "WeDoPlugin.dll" >> Scratch_Project.nsi
echo   Delete "README.txt" >> Scratch_Project.nsi
echo   Delete "License.txt" >> Scratch_Project.nsi
echo   Delete "project.sb" >> Scratch_Project.nsi
echo   Delete "makensis.exe" >> Scratch_Project.nsi
echo   RMDir /r "Plugins" >> Scratch_Project.nsi
echo   RMDir /r "locale" >> Scratch_Project.nsi
echo   RMDir /r "Stubs" >> Scratch_Project.nsi
echo   Delete "Scratch_Project.nsi" >> Scratch_Project.nsi
echo   Delete "newexe.bat" >> Scratch_Project.nsi
echo   Delete "icon.ico" >> Scratch_Project.nsi
echo   Delete "COPYING" >> Scratch_Project.nsi
echo SectionEnd >> Scratch_Project.nsi
move Scratch_Project.nsi "Required Files\Scratch_Project.nsi"
echo @echo off > "Required Files\newexe.bat"
echo set exename=%%~nx1  >> "Required Files\newexe.bat"
echo makensis.exe /V0 Scratch_Project.nsi  >> "Required Files\newexe.bat"
echo del %%1 >> "Required Files\newexe.bat"
echo ren %choice2% %%exename%%  >> "Required Files\newexe.bat"
echo move %%exename%% %%1  >> "Required Files\newexe.bat"
echo Del Scratch.exe  >> "Required Files\newexe.bat"
echo Del Scratch.image  >> "Required Files\newexe.bat"
echo Del Scratch.ini  >> "Required Files\newexe.bat"
echo Del ScratchPlugin.dll  >> "Required Files\newexe.bat"
echo Del Mpeg3Plugin.dll  >> "Required Files\newexe.bat"
echo Del UnicodePlugin.dll  >> "Required Files\newexe.bat"
echo Del CameraPlugin.dll  >> "Required Files\newexe.bat"
echo Del WeDoPlugin.dll  >> "Required Files\newexe.bat"
echo Del README.txt  >> "Required Files\newexe.bat"
echo Del License.txt  >> "Required Files\newexe.bat"
echo Del project.sb  >> "Required Files\newexe.bat"
echo del makensis.exe  >> "Required Files\newexe.bat"
echo RMDir /s /q Include  >> "Required Files\newexe.bat"
echo RMDir /s /q Plugins  >> "Required Files\newexe.bat"
echo RMDir /s /q Stubs  >> "Required Files\newexe.bat"
echo del Scratch_Project.nsi  >> "Required Files\newexe.bat"
echo del COPYING >> "Required Files\newexe.bat"
echo del icon.ico >> "Required Files\newexe.bat"
echo del newexe.bat >> "Required Files\newexe.bat"
copy project.sb "Required Files\project.sb"
"Required Files\makensis.exe" /V1 "Required Files\Scratch_Project.nsi"
if errorlevel 1 goto fail
del "Required Files\project.sb"
if "%customicon%"=="1" del "Required Files\icon.ico" & ren "Required Files\icon_scratch.ico" icon.ico
move "Required Files\%choice2%" "%choice2%"
echo Done.
echo.
echo meowmeow55의 스크래치 EXE 변환기를 이용해주셔서 감사합니다!
pause
exit /b
:fail
del "Required Files\project.sb"
echo EXE를 제작중에 문제가 발생했습니다. project.sb 파일이 폴더안에 있는지 확인하십시오.
echo 위 사항대로 했는데도 오류가 발생할경우 다음대로 해 주십시오. 1)재 다운로드 2) 문의:
echo http://scratch.mit.edu/forums/viewtopic.php?id=46159
pause