# Secret of the Polyglot

## Description
> The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?
> Download the suspicious file [here](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/Secret%20of%20the%20Polyglot/flag2of2-final.pdf).

## Solution
Ta có một file pdf, tuy nhiên khi dùng `file` để kiểm tra loại file thật sự thì thấy đây lại là một file png
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ file flag2of2-final.pdf 
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
```
Đổi đuôi file sang `png` và sử dụng `eog` để mở file
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ mv flag2of2-final.pdf flag2of2-final.png                   
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ eog flag2of2-final.png
```
![image](https://github.com/user-attachments/assets/a1194f21-faf8-46a3-8d03-a08cc4edd215)          
Ta được một đoạn của flag: `picoCTF{f1u3n7_`     
Sử dụng `binwalk` để kiểm tra xem file hình ảnh này còn được giấu file nào ở trong nữa không
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ binwalk flag2of2-final.png              

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 50 x 50, 8-bit/color RGBA, non-interlaced
914           0x392           PDF document, version: "1.4"
1149          0x47D           Zlib compressed data, default compression
```
Ta thấy ngoài một file hình ảnh png, còn một file pdf được giấu ở trong, tiến hành extract file pdf. Sau đó sử dụng `pdf2txt` để chuyển các dòng text của file pdf sang txt cho dễ đọc
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ binwalk --dd='.*' flag2of2-final.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 50 x 50, 8-bit/color RGBA, non-interlaced
914           0x392           PDF document, version: "1.4"
1149          0x47D           Zlib compressed data, default compression

                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ ls
flag2of2-final.png  _flag2of2-final.png.extracted
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ cd _flag2of2-final.png.extracted 
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf/_flag2of2-final.png.extracted]
└─$ ls
0  392  47D  47D.zlib
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf/_flag2of2-final.png.extracted]
└─$ file *                 
0:        PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
47D:      ASCII text
47D.zlib: zlib compressed data
392:      PDF document, version 1.4, 1 page(s)
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf/_flag2of2-final.png.extracted]
└─$ mv 392 flag2.pdf                        
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf/_flag2of2-final.png.extracted]
└─$ pdf2txt flag2.pdf                                                
1n_pn9_&_pdf_724b1287}
```
Sau khi chuyển sang thì ta được đoạn flag còn lại `1n_pn9_&_pdf_724b1287}`
### Flag `picoCTF{f1u3n7_1n_pn9_&_pdf_724b1287}`
