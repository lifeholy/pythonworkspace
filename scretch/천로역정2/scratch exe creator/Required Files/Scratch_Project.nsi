Name "õ�ο���2" 
OutFile "pro.exe" 
Icon "icon.ico" 
RequestExecutionLevel user 
SilentInstall silent 
Section "Go" 
  System::Call 'kernel32::GetModuleFileNameA(i 0, t .R0, i 1024) i r1' 
  SectionSetFlags 1 SF_SELECTED 
  SetOutPath $TEMP 
  File "Scratch.exe" 
  File "Scratch.image" 
  File "Scratch.ini" 
  File "ScratchPlugin.dll" 
  File "Mpeg3Plugin.dll" 
  File "UnicodePlugin.dll" 
  File "CameraPlugin.dll" 
  File "WeDoPlugin.dll" 
  File "README.txt" 
  File "License.txt" 
  File "project.sb" 
  File "makensis.exe" 
  File /r "Plugins" 
  File /r "Stubs" 
  File /r "locale" 
  File "Scratch_Project.nsi" 
  File "newexe.bat" 
  File "icon.ico" 
  File "COPYING" 
  ExecWait '"Scratch.exe" "Scratch.image" presentation "$TEMP\project.sb"' 
  exit: 
  Delete "Scratch.exe" 
  Delete "Scratch.image" 
  Delete "Scratch.ini" 
  Delete "ScratchPlugin.dll" 
  Delete "Mpeg3Plugin.dll" 
  Delete "UnicodePlugin.dll" 
  Delete "CameraPlugin.dll" 
  Delete "WeDoPlugin.dll" 
  Delete "README.txt" 
  Delete "License.txt" 
  Delete "project.sb" 
  Delete "makensis.exe" 
  RMDir /r "Plugins" 
  RMDir /r "locale" 
  RMDir /r "Stubs" 
  Delete "Scratch_Project.nsi" 
  Delete "newexe.bat" 
  Delete "icon.ico" 
  Delete "COPYING" 
SectionEnd 
