from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleName': 'Internet Back Again',
        'CFBundleDisplayName': 'Internet Back Again',
        'CFBundleIdentifier': 'com.qubites.internetbackagain',
        'CFBundleVersion': '0.1',
        'CFBundleShortVersionString': '0.1',
    },
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)