## Previous Works

- [Changing an LCD string on a Dell server remotely with Python](https://www.tannr.com/2010/03/20/changing-an-lcd-string-on-a-dell-server-remotely-with-python/)
- [\[Ipmitool-devel\] Fwd: LCD access on PowerEdge 1950](https://www.mail-archive.com/ipmitool-devel@lists.sourceforge.net/msg00352.html)
- [How can I set a custom text on the LCD display on Dell PowerEdge servers](https://serverfault.com/questions/81015/how-can-i-set-a-custom-text-on-the-lcd-display-on-dell-poweredge-servers)

## IPMI Registers

```
0x6             This is the network function (NetFn) number for Applications.
                See the IPMI spec for more information.
0x58            The operation number for setting system information. IPMI spec (page 572)
193 or 194      The selector for setting the Dell LCD text. 193 means
                set the string to this, 194 controls what string to show
                in the LCD.
0               Which chunk of 16 bytes of text you're editing (62 bytes are allowed).
0               Text encoding. This should always be 0 for ASCII.

6               This is the length of the string you're encoding.
                'foobar' is 6 characters. You can send 14 characters with each chunk.
                This is because you can only send 16 bytes total (1 byte for text
                encoding, 1 byte for length, 14 bytes for text).
                
0x66 0x6F 0x6F 0x62 0x61 0x72

                The ASCII codes for 'foobar'.
```


There are 2 registers:

0        Which chunk of 16 bytes of text you're editing (62 bytes are allowed).

0        Text encoding. This should always be 0 for ASCII.

They are a control bit of buffer inside IPMI. The LCD string is a buffer which has a width of 16 (each chunk), and has a height.

You can use the chunk register to control which row you are editing. And the text coding and length register only exist in the first row.
