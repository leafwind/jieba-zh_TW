##
# Pack egg file for spark-submit
#   `python3 setup.py bdist_egg`
##

from setuptools import setup, find_packages

setup(
    name='jieba_zh_tw',
    version='1.0.0',
    description='jieba installable package for zh_TW',
    author='leafwind',
    packages=find_packages()
)
