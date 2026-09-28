#!/data/data/com.termux/files/usr/bin/python3
import os
os.system('pkg update && pkg upgrade -y')
os.system('apt install python3-pip -y')
os.system('pip3 install phoneinfoga')