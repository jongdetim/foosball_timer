# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['gui.py', 'training_timer.py'],
             pathex=['C:\\Users\\Tim\\Desktop\\Coding things\\foosball_timer\\gitmap'],
             binaries=[],
             datas=[ ('football_icon.ico', '.') ],
             hiddenimports=['pyttsx3.drivers', 'pyttsx3.drivers.dummy', 'pyttsx3.drivers.espeak', 'pyttsx3.drivers.nsss', 'pyttsx3.drivers.sapi5'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Foos Trainer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
		  icon='football_icon.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Foos Trainer')
