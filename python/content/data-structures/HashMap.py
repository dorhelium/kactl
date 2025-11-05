"""
 * Author: Simon Lindholm, chilli
 * Date: 2018-07-23
 * License: CC0
 * Source: http://codeforces.com/blog/entry/60737
 * Description: Hash map with custom hash function.
 * Python's dict is already highly optimized, so this is a wrapper with custom hashing option.

"""

import time
import math

class HashMap(dict):
    """
    Custom hash map. In Python, dict is already highly optimized,
    but this provides interface for custom hashing if needed.
    """
    def __init__(self, use_random=False):
        super().__init__()
        if use_random:
            self.RANDOM = int(time.time() * 1e9) % (2**63)
            self.C = int(4e18 * math.acos(0)) | 71
        else:
            self.RANDOM = 0
            self.C = int(4e18 * math.acos(0)) | 71

    def _hash(self, x):
        """Custom hash function to use most bits"""
        if self.RANDOM:
            x ^= self.RANDOM
        # Python equivalent of __builtin_bswap64
        x = int.from_bytes(x.to_bytes(8, 'little', signed=True), 'big', signed=True)
        return (x * self.C) % (2**64)

# For most purposes, Python's built-in dict is sufficient and fast
