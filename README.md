[![CodeQL](https://github.com/Ylacat/pylog/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)](https://github.com/Ylacat/pylog/actions/workflows/codeql-analysis.yml)
# PyLogs
A Python 🐍 error handler, make logs to file or to console.

No more making it impossible to handle the large amount of errors 
in your project or code. Now you can just install the package and let
the package handle the rest.

## Development
### Requirements
It's important that you install the dependencies
* pip
* pytest
### Logfile
PyLogs creates a file called "log.txt" containng the time/date for errors.
```bash
PyLogs File Fri Jul 16 19:21:52 2021
```
## Use example:
```bash
pylog.info('This is a log message!')
pylog.error('This is an error message.')
```
