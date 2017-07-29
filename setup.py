from setuptools import setup

APP = ['WW.py']
OPTIONS = {
  'argv_emulation': True,
  'plist': {
    'LSUIElement': True,
  },
  'packages': ['rumps'],
}

setup(
  app=APP,
  options={'py2app': OPTIONS},
  setup_requires=['py2app'],
)
