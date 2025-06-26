from itertools import product
import string

# Encrypted result (array[4..0x11] ^ 0xA5)
encrypted = [
    0x3B, 0x24, 0x3E, 0x56, 0x75, 0x73, 0xA6, 0x11,
    0x4C, 0x82, 0xA5, 0xC3, 0x8E, 0xA0
]

# Puzzle table repeated twice (used in encryption)
puzzle = [
    0xe, 3, 0xb, 8, 1, 2, 0xd, 4,
    8, 10, 6, 0xc, 5, 9, 7, 0xf,
    0xe, 3, 0xb, 8, 1, 2, 0xd, 4,
    8, 10, 6, 0xc, 5, 9, 7, 0xf
]

# XOR keys from array[0..3] = 'Z', 'C', -0x3E, -8
xor_keys = [0x5A, 0x43, 0xC2, 0xF8]  # ASCII of Z, C, 0xC2, 0xF8

# Encrypt function from reverse engineered binary
def encrypt_pair(c1, c2, pair_index):
    local_83 = ord(c1)
    local_82 = ord(c2)
    for j in range(6):
        hi = (local_82 >> 4) + 0x10
        lo = local_82 & 0x0F
        val = ((puzzle[hi] << 4) | puzzle[lo]) & 0xFF
        val = (val + xor_keys[j & 3]) & 0xFF
        val = local_83 ^ val ^ ((val << 3 | val >> 5) & 0xFF)
        local_83, local_82 = local_82, val
    return local_83, local_82

# Define possible characters (printable + underscore)
chars = string.ascii_letters + string.digits + "_"

# Output key
key = ['?'] * 14

# Brute force each 2-character pair
for i in range(0, 14, 2):
    t1, t2 = encrypted[i], encrypted[i+1]
    found = False
    for c1, c2 in product(chars, repeat=2):
        e1, e2 = encrypt_pair(c1, c2, i)
        if e1 == t1 and e2 == t2:
            key[i], key[i+1] = c1, c2
            found = True
            break
    if not found:
        print(f"[-] Failed to find pair for encrypted bytes: {t1:02X}, {t2:02X}")
        break

# Final key
print("\n[+] Reconstructed Key:", ''.join(key))
