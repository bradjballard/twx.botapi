from setuptools import setup

from subprocess import Popen, PIPE

revlist_count = None
long_rev = None

VERSION_MAJOR=1
VERSION_MINOR=0
VERSION_BETA=1

with Popen(['git', 'rev-list', 'HEAD', '--count'], stdout=PIPE) as f:
    revlist_count = f.stdout.read().decode().strip()

with Popen(['git', 'rev-parse', 'HEAD'], stdout=PIPE) as f:
    long_rev = f.stdout.read().decode().strip()

if revlist_count is None:
  raise Exception('Unable to determine short revision')

if long_rev is None:
  raise Exception('Unable to determine long revision')

import sys

version = '{}.{}'.format(VERSION_MAJOR, VERSION_MINOR)
if VERSION_BETA is not None:
  version = '{}b{}'.format(version, VERSION_BETA)
if 'pypitest' in sys.argv:
  version = '{}.dev{}'.format(version, revlist_count)

download_url = 'https://github.com/datamachine/twx/archive/{long_rev}.tar.gz'.format(long_rev=long_rev)

setup(
    name = 'twx',
    packages = ['twx', 'twx.botapi'],
    version = version,
    description = 'Unofficial Telegram Bot API Client',
    long_description = open("README.rst").read(),
    author = 'Vince Castellano, Phillip Lopo',
    author_email = 'surye80@gmail.com, philliplopo@gmail.com',
    keywords = ['datamachine', 'telex', 'telegram', 'bot', 'api', 'rpc'],
    url = 'https://github.com/datamachine/twx', 
    download_url = download_url, 
    install_requires=['requests'],
    platforms = ['Linux', 'Unix', 'MacOsX', 'Windows'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3 :: Only',
      'Programming Language :: Python :: 3.4',
      'Topic :: Communications :: Chat',
      'Topic :: Communications :: File Sharing'
      ]
)

setup(
    name = 'twx-botapi',
    package_dir = {'':'twx'},
    packages = ['botapi'],
    version = version,
    description = 'Standalone version of the Unofficial Telegram Bot API Client from TWX',
    long_description = open("README.rst").read(),
    author = 'Vince Castellano, Phillip Lopo',
    author_email = 'surye80@gmail.com, philliplopo@gmail.com',
    keywords = ['datamachine', 'telex', 'telegram', 'bot', 'api', 'rpc'],
    url = 'https://github.com/datamachine/twx', 
    download_url = download_url, 
    install_requires=['requests'],
    platforms = ['Linux', 'Unix', 'MacOsX', 'Windows'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3 :: Only',
      'Programming Language :: Python :: 3.4',
      'Topic :: Communications :: Chat',
      'Topic :: Communications :: File Sharing'
      ]
)
