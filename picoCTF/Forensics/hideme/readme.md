# hideme

## Description
> Every file gets a flag.
> The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/hideme/flag.png).

## Solution

Sử dụng `binwalk` để kiểm tra xem có file nào được giấu ở trong file png này hay không?
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ file flag.png 
flag.png: PNG image data, 512 x 504, 8-bit/color RGBA, non-interlaced
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ binwalk flag.png                                               

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2858, uncompressed size: 3015, name: secret/flag.png
42897         0xA791          End of Zip archive, footer length: 22
```

Ta thấy có file zip được nén ở trong, extract file:
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ binwalk --dd='.*' flag.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 512 x 504, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
39739         0x9B3B          Zip archive data, at least v1.0 to extract, name: secret/
39804         0x9B7C          Zip archive data, at least v2.0 to extract, compressed size: 2858, uncompressed size: 3015, name: secret/flag.png
42897         0xA791          End of Zip archive, footer length: 22

                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ ls
flag.png  _flag.png.extracted
```

Giải nén file zip và ta được flag
![image](https://github.com/user-attachments/assets/03db20c5-fff8-4e7d-bdc0-4926a8c36d2f)

### Flag picoCTF{Hiddinng_An_imag3_within_@n_ima9e_96539bea}
