#!/usr/bin/python

import os

# host = str(input("Host:"))
# user = str(input("Username:"))
# passwd = str(input("Password:"))
# lcd = str(input("LCD String:"))

host = 'host_cidr'
user = 'username'
passwd = 'password'
lcd = 'foobar'

strHex = ''

Len = len(lcd)
cmd = 'ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passwd + ' raw 0x6 0x58 193'

for x in lcd:
    strHex += hex(ord(x))
    strHex += " "

if Len <= 14:
    print('ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passwd + ' raw 0x6 0x58 193 0 0 ' + str(Len) + ' ' + strHex)
else:
    first = lcd[:14]
    strFirst = ''
    for x in first:
        strFirst += hex(ord(x))
        strFirst += " "
    print('ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passwd + ' raw 0x6 0x58 193 0 0 ' + str(Len) + ' ' + strFirst)
    lcd = lcd[14:]
    nLen = Len - 14
    for i in range(nLen // 16 + 1):
        strHex = ''
        for x in lcd[i * 16:min(nLen + 1, (i + 1) * 16)]:
            strHex += hex(ord(x))
            strHex += ' '
        print('ipmitool -I lanplus -H ' + host + ' -U ' + user + ' -P ' + passwd + ' raw 0x6 0x58 193 ' + str(i + 1) + ' ' + strHex)


# if (ret == 0):
#     print('LCD string changed successfully.n')
# else:
#     print('Non-zero return value, something went wrong.')
#     print('Make sure IPMI is enabled on the remote host and the DNS or IP is correct.')
