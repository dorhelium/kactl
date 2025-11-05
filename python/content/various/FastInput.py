"""
 * Author: chilli
 * License: CC0
 * Source: Own work
 * Description: Read an integer from stdin. Usage requires your program to pipe in
 * input from file.
 * Note: In Python, sys.stdin.read() or input() are already quite efficient.
 * For competitive programming, using sys.stdin.buffer can provide speed improvements.
 * Usage: ./a.py < input.txt
 * Time: About 5x as fast as cin/scanf in C++. In Python, use sys.stdin for fast input.
 * Status: tested on SPOJ INTEST, unit tested

"""

import sys

class FastInput:
    """
    Fast input reader for competitive programming.
    Uses buffered reading for better performance.
    """
    def __init__(self, buffer_size=1 << 16):
        self.buffer = sys.stdin.buffer.read()
        self.pos = 0
        self.size = len(self.buffer)

    def read_char(self):
        """Read a single character"""
        if self.pos >= self.size:
            return 0
        c = self.buffer[self.pos]
        self.pos += 1
        return c

    def read_int(self):
        """Read an integer from input"""
        # Skip whitespace and other characters until digit or minus
        c = self.read_char()
        while c and c < 40:
            c = self.read_char()

        if c == ord('-'):
            return -self.read_int()

        # Read digits
        a = c
        c = self.read_char()
        while c >= 48:
            a = a * 10 + c - 480
            c = self.read_char()

        return a - 48

# Simpler Python alternative for fast input
def fast_input_setup():
    """
    Setup for fast input in Python.
    Call this at the start of your program for faster I/O.
    """
    import sys
    input = sys.stdin.readline
    return input

# Usage example:
# reader = FastInput()
# n = reader.read_int()
#
# Or simpler:
# input = fast_input_setup()
# n = int(input())
