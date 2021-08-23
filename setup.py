from setuptools import setup, find_packages

VERSION = '0.0.1'

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3'
]

setup(
    name='PyLog',
    version=VERSION,
    description='A Python error handler',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Frederick Ambo',
    author_email='frederick@tacaly.com',
    license='MIT',
    classifiers=classifiers,
    keywords='error',
    packages=find_packages(),
    install_requires=['']
)
