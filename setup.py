from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pylog',
  version='0.0.1',
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