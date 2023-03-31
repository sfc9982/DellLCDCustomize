#!/usr/bin/python

host = 'host_cidr'
user = 'username'
passwd = 'password'
lcd = 'foobar'

strHex = ''
offset = len(lcd)
prefix = 'ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passwd
cmd = prefix + ' raw 0x6 0x58 193'

for x in lcd:
    strHex += hex(ord(x)) + ' '

if offset <= 14:
    print(prefix + ' raw 0x6 0x58 193 0 0 ' + str(offset) + ' ' + strHex)
else:
    first = lcd[:14]
    strFirst = ''
    for x in first:
        strFirst += hex(ord(x)) + ' '
    print(prefix + ' raw 0x6 0x58 193 0 0 ' + str(offset) + ' ' + strFirst)
    lcd = lcd[14:]
    n = offset - 14
    for i in range(n // 16 + 1):
        strHex = ''
        for x in lcd[i * 16:min(n + 1, (i + 1) * 16)]:
            strHex += hex(ord(x))
            strHex += ' '
        print(prefix + ' raw 0x6 0x58 193 ' + str(i + 1) + ' ' + strHex)
