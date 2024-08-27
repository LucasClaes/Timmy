import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--add-data=Sugar.png;.',
    '--hidden-import=comtypes',
    '--hidden-import=comtypes.stream',
    '--hidden-import=sys',
    '--hidden-import=pywinauto',
    '--hidden-import=pyautogui',
    '--hidden-import=cv2',
    '--hidden-import=numpy',
    '--hidden-import=time',
    '--hidden-import=pywinauto.keyboard',
    '--hidden-import=pynput.keyboard',
    '--hidden-import=win32api'
])
