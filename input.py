
import os
import json
from colorama import Fore, Back
import sys
import termios
import tty
import signal
from time import sleep
from re import sub
from random import choice


class Cursor:
    def __init__(self):
        self.__hide_string = "\x1b[?25l"
        self.__show_string = "\x1b[?25h"

    def hide(self):
        print(self.__hide_string)

    def show(self):
        print(self.__show_string)


class Input:
    def _get_key_raw(self):
        fd = sys.stdin.fileno()
        self.old_config = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.buffer.raw.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, self.old_config)
        return ch

    def _timeout_handler(self, signum, frame):
        raise TimeoutError

    def get_parsed_input(self, timeout):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            ip = self._get_key_raw()
            signal.alarm(0)
            if ip in [b'q', b'Q']:
                key = 'q'
            elif ip in [b'w', b'W']:
                key = 'w'
            elif ip in [b's', b'S']:
                key = 's'
            elif ip in [b'a', b'A']:
                key = 'a'
            elif ip in [b'd', b'D']:
                key = 'd'
            elif ip == b' ':
                key = ' '
            elif ip in [b'e', b'E']:
                key = 'e' 
            elif ip in [b'r', b'R']:
                key = 'r' 
            elif ip in [b'h', b'H']:
                key = 'h' 
            elif ip == b'\r':
                key = 'enter'

            elif ip in [b'1']:
                key = '1'
            elif ip in [b'2']:
                key = '2'
            elif ip in [b'3']:
                key = '3'
            elif ip in [b'4']:
                key = '4'
            elif ip in [b'5']:
                key = '5'
            elif ip in [b'6']:
                key = '6'
            else:
                key = 'none'
            sleep(timeout)
            return key
        except TimeoutError:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None
