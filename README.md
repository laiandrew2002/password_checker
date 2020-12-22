# Password Checker
Simple python script to allow you to search across multiple data breaches to see your password has been compromised.

## Development

The script is written in python 3

The script uses an API from [HaveIBeenPwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) to search on their database on the password suubmitted.

In order to protect the value of the source password being searched for, Pwned Passwords also implements a [k-Anonymity](https://en.wikipedia.org/wiki/K-anonymity) model that allows a password to be searched for by partial hash. This allows the first 5 characters of a SHA-1 password hash (not case-sensitive) to be passed to the API

## How To Use

#### Prerequisites

1. Install [Python 3](https://www.python.org/downloads/)
2. Enjoy!

#### Quick Start

1. Clone this repository to obtain the script.
2. Create a new txt file or use the existing txt file to enter the password you want to check.
3. In the txt file, each password will be seperated with a new line.
4. Open your terminal (MacOs) or Command Prompt (Windows).
5. Run the following command (execute the python script followed by the txt file name at the same directory):
```
python3 password_checker.py password.txt
```
6. Sample response you will get on your terminal/cmd:
```
hahalolomg was seen 6 times. Please do not use this password.
lololo was seen 40638 times. Please do not use this password.
popopoeo was not seen, it's safe to use!
password check done!
```

## Contributor

1. Andrew Lai : laiandrew2002@gmail.com
