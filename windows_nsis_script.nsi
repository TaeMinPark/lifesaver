!define Name "lifesaver"
!define CapitalName "Lifesaver"

# define name of installer
OutFile "${Name}_installer.exe"

# define installation directory
InstallDir "$ProgramFiles\${Name}"
 
# For removing Start Menu shortcut in Windows 7
RequestExecutionLevel admin

# start default section
Section
    RMDir /R $INSTDIR
    # set the installation directory as the destination for the following actions
    SetOutPath $INSTDIR
    File /r 'dist\*.*'
    # create the uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    # create a shortcut named "new shortcut" in the start menu programs directory
    # point the new shortcut at the program uninstaller

    # Start Menu
	createDirectory "$SMPROGRAMS\${CapitalName}"
    createShortCut "$SMPROGRAMS\${CapitalName}\${Name}_uninstaller.lnk" "$INSTDIR\uninstall.exe"
    createShortCut "$SMPROGRAMS\${CapitalName}\${CapitalName}.lnk" "$INSTDIR\${Name}.exe" "" "$INSTDIR\resources\icon.ico"

    # Desktop
    createShortcut "$desktop\${CapitalName}.lnk" "$instdir\${Name}.exe" "" "$INSTDIR\resources\icon.ico"

    # Create shortcut to install flder
    createShortCut "$INSTDIR\${Name}.lnk" "$INSTDIR\${Name}.exe" "" "$INSTDIR\resources\icon.ico"

    # Create shortcut to Startup folder
    createShortcut "$APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\${Name}.lnk" "$instdir\${Name}.exe" "" "$INSTDIR\resources\icon.ico"

	# Registry information for add/remove programs
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "DisplayName" "${CapitalName} - Save your works automatically"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "InstallLocation" "$\"$INSTDIR$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "DisplayIcon" "$\"$INSTDIR\resources\icon.ico$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "Publisher" "$\"Taem$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "HelpLink" "$\"github.com/taeminpark/lifesaver$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "URLUpdateInfo" "$\"github.com/taeminpark/lifesaver$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "URLInfoAbout" "$\"github.com/taeminpark/lifesaver$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "DisplayVersion" "$\"0.0.1$\""

	# There is no option for modifying or repairing the install
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "NoModify" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}" "NoRepair" 1
SectionEnd
 
# uninstaller
Section "uninstall"
    #Delete "$SMPROGRAMS\new shortcut.lnk"
    UNINSTALLATION:
        Delete "$INSTDIR\lifesaver.exe"
        iffileexists "$INSTDIR\lifesaver.exe" RUNNING NOT_RUNNING
    RUNNING:
        MessageBox MB_RETRYCANCEL "Lifesaver is still running. Retry after close the program." IDRETRY UNINSTALLATION IDCANCEL CANCELINS
        Goto END
    NOT_RUNNING:
        # Remove install folder
        RMDir /R $INSTDIR
        # Remove Start Menu launcher
	    delete "$SMPROGRAMS\${Name}\${Name}.lnk"
	    # Try to remove the Start Menu folder - this will only happen if it is empty
	    rmDir "$SMPROGRAMS\${Name}"
        DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${Name} ${CapitalName}"
        Goto COMPLETEINS
    CANCELINS:
        MessageBox MB_OK "Uninstallation cancelled."
        Goto END
    COMPLETEINS:
        MessageBox MB_OK "Uninstallation completed."
    END:
        
SectionEnd