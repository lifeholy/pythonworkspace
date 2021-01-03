@echo off 
set exename=%~nx1  
makensis.exe /V0 Scratch_Project.nsi  
del %1 
ren pro.exe %exename%  
move %exename% %1  
Del Scratch.exe  
Del Scratch.image  
Del Scratch.ini  
Del ScratchPlugin.dll  
Del Mpeg3Plugin.dll  
Del UnicodePlugin.dll  
Del CameraPlugin.dll  
Del WeDoPlugin.dll  
Del README.txt  
Del License.txt  
Del project.sb  
del makensis.exe  
RMDir /s /q Include  
RMDir /s /q Plugins  
RMDir /s /q Stubs  
del Scratch_Project.nsi  
del COPYING 
del icon.ico 
del newexe.bat 
