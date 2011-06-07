import os 
import sys
import ConfigParser

from threading import Thread
from os.path import exists

def daemonize():
    pid = os.fork()
    if pid > 0:
        sys.exit(0)

def parse_config(file):
    config = ConfigParser.RawConfigParser()
    config.read(config))

def main():
    

if __name__ == '__main__':
    main()
