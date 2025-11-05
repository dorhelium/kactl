"""
Author: Simon Lindholm
Date: 2016-07-23
License: CC0
Source: me
Description: BumpAllocator for STL containers.
Note: This is a C++-specific optimization technique. Python's lists and containers
already use efficient memory allocation strategies. This is provided for reference
and educational purposes.
Usage: In Python, just use regular lists - list allocation is already efficient
Status: tested
"""

class SmallAllocator:
    """
    A bump allocator similar to C++ STL allocator.
    In Python, standard lists are already efficient, so this is mainly conceptual.
    """
    def __init__(self, buffer_size=450 << 20):
        self.buf = bytearray(buffer_size)
        self.buf_ind = buffer_size

    def allocate(self, n, item_size=1):
        """Allocate space for n items of given size"""
        total_size = n * item_size
        self.buf_ind -= total_size
        # Align to 16 bytes
        self.buf_ind &= ~15
        return self.buf_ind

    def deallocate(self, ptr, n):
        """No-op deallocate (bump allocator doesn't free)"""
        pass

    def reset(self):
        """Reset allocator"""
        self.buf_ind = len(self.buf)
