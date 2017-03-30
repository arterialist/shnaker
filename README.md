# Shnaker

## About
Shnaker is a tool to generate wordlists of any complexity. It has different ways to generate your wordlist.

## Features
- Generation with help of generation master
- Generation by pattern
- Generation by args

## Install
First of all you need to install required libs and modules:
```
apt-get install -y python3 python3-pip
pip install termcolor
```

Then simply clone this repo and run 
```
python3 shnaker.py
```
You can also `chmod +x shnaker.py` to run it as executable

## How to
All of this you can find in app's help

### Generation by args
You can do this in two ways:

- Pass pattern and path to file
- Pass pattern and -s or --silent flag and pipe output to file

Examples:
```
python3 shnaker.py '2/3.({az}{09}{AZ})' /root/example.txt
python3 shnaker.py '2/3.({az}{09}{AZ})' -s > /root/example.txt
python3 shnaker.py '2/3.({az}{09}{AZ})' --silent > /root/example.txt
```
Extra example - sort and pipe:
```
python3 shnaker.py '2/3.({az}{09}{AZ})' -s | sort > /root/example.txt
```

### Pattern rules

Here is an example pattern: 3/5.({az}{AZ|09}{09}{special}{09|[qwerty123]}) 
Let's take a closer look.

3 and 5 separated by a slash are min and max lengths of words.
After dot there are brackets with charsets in them.
Each group of charsets is surrounded by curly brackets.
If symbol should have more than one charsets, then they are separated by '|' symbol.
Custom charsets are surrounded by block brackets.

`NO SPACES IN PATTERN`

`-------------------------------------------------------------------------`

Any ideas, suggestions and improvements: [@Arterialist](https://t.me/arterialist) (Telegram)
