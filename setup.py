import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'easy'
AUTHOR = 'Ricardo Calura'
AUTHOR_EMAIL = 'ricardo.calura29@gmail.com'
URL = 'https://github.com/king-ds/easyds'
DOWNLOAD_URL = 'https://github.com/king-ds/easyds/archive/0.1.0.tar.gz'

LICENSE = 'MIT License'
DESCRIPTION = 'Personal Python library to make usual data science workflow easy.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'pandas',
]

SETUP_REQUIRES = [
    'pytest-runner',
]

TESTS_REQUIRE = [
    'pytest==4.4.1',
]

TEST_SUIT = 'tests'

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download=DOWNLOAD_URL,
      install_requires=INSTALL_REQUIRES,
      setup_requires=SETUP_REQUIRES,
      tests_require=TESTS_REQUIRE,
      test_suite=TEST_SUIT,
      packages=find_packages()
      )