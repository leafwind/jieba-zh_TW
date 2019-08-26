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
    author_email='leafwind.cs@gmail.com',
    url='https://github.com/leafwind/jieba',
    license="MIT",
    keywords='NLP,tokenizing,Chinese word segementation',
    install_requires=[
        "jieba",
    ],
    packages=find_packages(),
    package_dir={'jieba_zh_tw':'jieba_zh_tw'},
    package_data={'jieba_zh_tw':['*.*','finalseg/*','analyse/*','posseg/*','zh_tw_extra/*']}
)
