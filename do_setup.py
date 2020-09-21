import sys
text = """
from distutils.core import setup

setup(name='configg',
      version='{version}',
      description='Config data manager',
      author='Oliver',
      author_email='mail.ok65@googlemail.com',
      url='https://github.com/ok65/Configg',
      packages=['configg'],
     )
"""
with open("setup.py", "w+") as fp:
    fp.write(text.format(version=sys.argv[1]))