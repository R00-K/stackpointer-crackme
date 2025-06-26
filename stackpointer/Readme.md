# 🎩 CrackMe Reverse Engineering: Multi-Stage Analysis & Key Recovery

This repository documents the full reverse engineering and patching process of a multi-stage CrackMe binary. The binary consists of three unique stages, each with custom logic designed to block progression until bypassed or solved:

* **Stage 0** – Anti-debugging check (patched via control flow redirection).
* **Stage 1** – Heap pointer validation (bypassed by modifying user input behavior).
* **Stage 2** – Obfuscated key validation (solved via encryption pair-matching).

🔗 [Challenge Link – CrackMes.One](https://crackmes.one/crackme/68439ee62b84be7ea7743690#close)

---

## 🏁 Stage Breakdown

### ❌ Stage 0 – Anti-Debugging & Control Flow Obfuscation

* Implements anti-debugging techniques like `ptrace`, exceptions, or timing logic.
* Bypassed by **patching a ****************`jmp`**************** instruction** that skips over the anti-debug logic entirely.
* Achieved using tools like **Ghidra** or a hex editor.

---

### 🔐 Stage 1 – Heap Pointer Corruption Gate

* Allocates heap memory and initializes it with a value (`0x1337`).


### 🔒 Stage 2 – Encrypted Name Validation

* Accepts a 12-character name from the user.
* Applies a **pair-based custom encryption** using a `puzzle[]` table, bit manipulation, XOR, and dynamic byte modification.
* Produces a 14-byte encrypted array.
* A **checksum** is computed over these 14 bytes.
* Compares this result with a hardcoded encrypted reference and checksum.

---

## 🔓 Key Recovery via Encryption Matching (Not Brute Force)

Unlike brute-forcing the entire 12-character key space, a smarter and more efficient approach was used by analyzing how the binary encrypted character pairs.

### ✅ Methodology:

1. The 12-character input is encrypted **pairwise** — 2 characters at a time.
2. For each 2-byte segment in the 14-byte encrypted target:

   * A Python script **replicates the encryption logic**.
   * Iterates over all printable ASCII character pairs.
   * Encrypts each candidate pair.
   * Compares the result with the encrypted target bytes.
   * If matched, the original characters are recorded.
3. This continues until all pairs are recovered.
4. Finally, the XOR checksum of the encrypted result is verified to be `0x40`.

### 🔄 Why It Works:

* The encryption is pairwise and **does not depend on other character pairs**.
* This enables **segment-wise reversal**, reducing computation from `95^12` to `95^2 × 7`.

---

```python
```

### ✅ Final Recovered Key:

```txt
stackpointer
```

The recovered name passed all validations, including checksum matching.

---

## 🛠️ Tools & Environment

* **Ghidra** – For decompilation and patching analysis
* **Python** – For character pair matching script
* **GDB** – For dynamic debugging
* **Linux / GCC** – For experimentation and patching

---

##

---

## 📓 License

This project is for **educational and ethical use only**.
Do not use these techniques for malicious purposes or unauthorized software cracking.

---

## 🢚 Author

Reverse engineered and documented by **R00-K**.
If you found this project helpful, give it a ⭐ on GitHub!
