import sys
from strings.KMP import pi

def gen(s, at, alpha, f):
    """Generate all strings of given length with alphabet size alpha"""
    if at == len(s):
        f()
    else:
        for i in range(alpha):
            s[at] = chr(ord('a') + i)
            gen(s, at + 1, alpha, f)

def test(s):
    """Test KMP prefix function"""
    p = pi(s)
    for i in range(len(s)):
        maxlen = -1
        for length in range(i + 1):
            valid = True
            for j in range(length):
                if s[j] != s[i + 1 - length + j]:
                    valid = False
                    break
            if valid:
                maxlen = length
        assert maxlen == p[i], f"Failed for string '{s}' at position {i}: expected {maxlen}, got {p[i]}"

def test_kmp():
    # Test ~3^12 strings
    for n in range(13):
        s = ['x'] * n
        gen(s, 0, 3, lambda: test(''.join(s)))

    # Test ~4^10 strings
    for n in range(11):
        s = ['x'] * n
        gen(s, 0, 4, lambda: test(''.join(s)))

    print("Tests passed!")

if __name__ == "__main__":
    test_kmp()
