"""
 * Author: Simon Lindholm
 * Date: 2016-08-23
 * License: CC0
 * Source: me
 * Description: A 32-bit pointer that points into BumpAllocator memory.
 * Note: This is a C++-specific optimization for reducing pointer size.
 * In Python, all object references are already optimized by the interpreter.
 * This implementation provides a conceptual equivalent for educational purposes.
 * Status: tested

"""

class SmallPtr:
    """
    A compact pointer representation that stores an index into a buffer.
    In Python, this is mainly for educational purposes as Python handles
    object references efficiently by default.
    """
    def __init__(self, buffer, index=0):
        """
        Initialize a small pointer.

        Args:
            buffer: The buffer this pointer refers to
            index: Index into the buffer (default 0 for null)
        """
        self.buffer = buffer
        self.ind = index

    def get(self):
        """Dereference the pointer"""
        if self.ind == 0:
            return None
        return self.buffer[self.ind]

    def set(self, value):
        """Set value at pointer location"""
        if self.ind == 0:
            raise ValueError("Cannot dereference null pointer")
        self.buffer[self.ind] = value

    def offset(self, delta):
        """Get pointer offset by delta"""
        return SmallPtr(self.buffer, self.ind + delta)

    def __bool__(self):
        """Check if pointer is non-null"""
        return self.ind != 0

    def __getitem__(self, offset):
        """Array-style access: ptr[offset]"""
        if self.ind == 0:
            raise ValueError("Cannot dereference null pointer")
        return self.buffer[self.ind + offset]

    def __setitem__(self, offset, value):
        """Array-style assignment: ptr[offset] = value"""
        if self.ind == 0:
            raise ValueError("Cannot dereference null pointer")
        self.buffer[self.ind + offset] = value

# Note: In Python, you typically don't need this pattern.
# Just use lists or arrays directly:
# buffer = [None] * size
# ptr = buffer[index]
