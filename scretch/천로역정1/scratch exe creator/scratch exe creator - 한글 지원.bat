@echo off
cls
echo ��������������������������������������������������������������
echo �� - ��ũ��ġ EXE ��ȯ�� �ѱ�ȭ Ver. 1.1                 ��
echo �� - ������ : meowmeow55                                    ��
echo �� - �ѱ�ȭ : Linerunner(linerunner15@naver.com)            ��
echo �� - EXE ��ȯ�� �ѱ� ���� : purum5548@naver.com             ��
echo ��������������������������������������������������������������
echo  �� ���� �� ���ǻ��� ��
echo  �� EXEȭ �� ���α׷��� �̸��� project�� ���ֽʽÿ�.
echo  �� EXEȭ �� ���α׷��� ����� ���� ���α׷��� �������� ��찡 �߻��մϴ�.
:choosename
echo.
set /p choice= - EXE ������ �̸��� �Է����ּ���.(/, \, :, *, ?, ", <, >, |, & ����):
set choice2=%choice%
md garbage_dirs
cd garbage_dirs
md "%choice%.12345"
if errorlevel 1 (
echo Ư�����ڰ� ���ԵǾ��ֽ��ϴ�. �ٸ� �̸��� �Է����ּ���.
goto choosename
)
if not exist *.12345 (
echo Ư�����ڰ� ���ԵǾ��ֽ��ϴ�. �ٸ� �̸��� �Է����ּ���.
goto choosename
)
if not exist *.exe.12345 set choice2=%choice%.exe
rd "%choice%.12345"
cd ..
rd /s /q garbage_dirs
set /p EXEnameconfirm= - EXE ������ �̸��� %choice% (��)�� �½��ϱ�? [�� �Ǵ� �ƴϿ�] 
if "%EXEnameconfirm%"=="��" (
goto endchooseEXEname
) ELSE (
goto choosename
)
)
:endchooseEXEname
if "%confirm%"=="name" goto confirm
:choosetitle
echo.
set /p name= - EXE�� Ÿ��Ʋ �̸��� �Է��� �ּ���.(���� ���࿩�θ� ���� ������ ������ �ʽ��ϴ�.):
if "%name%"=="default" set name=Scratch Project
set /p titleconfirm= - �� EXE�� Ÿ��Ʋ �̸��� %name% (��)�� �½��ϱ�? [�� �Ǵ� �ƴϿ�] 
if "%titleconfirm%"=="��" (
goto endchoosetitle
) ELSE (
goto choosetitle
)
)
:endchoosetitle
if "%confirm%"=="title" goto confirm
:choosemsg
echo.
set /p messageyn= - EXE���� ���࿩�θ� ����ðڽ��ϱ�? [�� �Ǵ� �ƴϿ�] 
if "%messageyn%"=="��" (
goto choosemsgcode
) ELSE (
if "%messageyn%"=="�ƴϿ�" (
goto endchoosemsg
) ELSE (
goto choosemsg
)
)
)
)
:choosemsgcode
set msgactivate=1
set /p message= - ���࿩�� â�� ���� ���� �����ϼ���.( " ���� "�⺻" �� �Է��Ͻø� ����ó�� �����˴ϴ�. "�� ��ũ��ġ ������Ʈ�� �����Ͻðٽ��ϱ�?"):
if "%message%"=="�⺻" set message=�� ��ũ��ġ ������Ʈ�� �����Ͻðٽ��ϱ�?
set /p msgtextyn= - ���� ����  %message% �� �½��ϱ�?[�� �Ǵ� �ƴϿ�] 
if "%msgtextyn%"=="��" (
goto endchoosemsg
) ELSE (
goto choosemsg
)
)
:endchoosemsg
if "%confirm%"=="message" goto confirm
:repackrequest
echo.
set /p repackyn= - �ٽ� EXEȭ �Ұ�� ����ڿ��� ���ڽ��ϱ�? [�� �Ǵ� �ƴϿ�] 
if "%repackYN%"=="��" (
goto endrepackreq
) ELSE (
if "%repackYN%"=="�ƴϿ�" (
goto repackreqcode
) ELSE (
goto repackrequest
)
)
)
)
:repackreqcode
set /p autorepackYN= - �ڵ����� EXEȭ �Ұ��Դϱ�? [�� �Ǵ� �ƴϿ�] 
if "%autorepackYN%"=="��" (
set autorepack=1
) ELSE (
if "%autorepackYN%"=="�ƴϿ�" (
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
set /p customiconYN= - ����� ���� EXE���� �������� ����Ͻǰ̴ϱ�? (icon.ico����� ������ ���� ��ġ�� ���ϰ� ���� ������ �־�� �մϴ�.) [�� �Ǵ� �ƴϿ�] 
if "%customiconYN%"=="��" (
set customicon=1
) ELSE (
if "%customiconYN%"=="�ƴϿ�" (
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
echo  - EXE ������ �̸� : %choice%
echo  - EXE Ÿ��Ʋ�� �̸� : %name%
if "%msgactivate%"=="1" ( echo  - EXE ����Ȯ�� â: %message% ) ELSE ( echo  - EXE ����Ȯ�� â : ������� ���� )
if "%autorepack%"=="1" echo  - �� EXEȭ Ȯ�� â : ������� ����, - �ڵ� EXEȭ
if "%autorepack%"=="0" echo  - �� EXEȭ Ȯ�� â : ������� ����, - EXEȭ �ǳʶٱ�
if "%autorepack%"=="" echo  - �� EXEȭ Ȯ�� â : �����
if "%customicon%"=="1" ( echo  - ��������� EXE ������ : �����) else (  - echo ��������� EXE ������ : ������� ����)
set /p confirm=�� ������ �½��ϱ�? ���� �ƴ϶�� "name" �� �Է��� EXE������ �̸��� �����ϰų� "title" �� �Է��� EXE Ÿ��Ʋ�� �̸��� ����, "message" �� �Է��� ���࿩�� �޼����� ����, "repack" �� �Է��� �� EXEȭ ����, �Ǵ� "icon" �� �Է��� �������� ������ �� �ֽ��ϴ�.( " ���� �ҹ��ڷθ�) - ������ Enter�� �����ֽʽÿ� :
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
echo meowmeow55�� ��ũ��ġ EXE ��ȯ�⸦ �̿����ּż� �����մϴ�!
pause
exit /b
:fail
del "Required Files\project.sb"
echo EXE�� �����߿� ������ �߻��߽��ϴ�. project.sb ������ �����ȿ� �ִ��� Ȯ���Ͻʽÿ�.
echo �� ���״�� �ߴµ��� ������ �߻��Ұ�� ������� �� �ֽʽÿ�. 1)�� �ٿ�ε� 2) ����:
echo http://scratch.mit.edu/forums/viewtopic.php?id=46159
pause