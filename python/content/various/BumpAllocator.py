"""
 * Author: Simon Lindholm
 * Date: 2015-09-12
 * License: CC0
 * Source: me
 * Description: When you need to dynamically allocate many objects and don't care about freeing them.
 * "new X" otherwise has an overhead of something like 0.05us + 16 bytes per allocation.
 * Note: This is a C++-specific optimization technique. In Python, memory management is automatic
 * and this pattern is not directly applicable. This implementation provides a conceptual equivalent
 * using a pre-allocated buffer with a simple bump allocator pattern.
 * Status: tested

"""

class BumpAllocator:
    """
    A simple bump allocator that allocates from a pre-allocated buffer.
    In Python, this is mainly for educational purposes as Python's memory
    management is automatic.
    """
    def __init__(self, size=450 << 20):
        self.buf = bytearray(size)
        self.index = size

    def allocate(self, size):
        """Allocate 'size' bytes from the buffer"""
        assert size < self.index, "Out of memory"
        self.index -= size
        return self.index

    def reset(self):
        """Reset the allocator to reuse the buffer"""
        self.index = len(self.buf)
