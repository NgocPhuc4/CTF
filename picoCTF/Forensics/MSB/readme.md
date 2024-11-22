# MSB

## Description
> This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...                   
> Download the image [here](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/MSB/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)

## Solution

Dựa vào tên đề bài, ta nghĩ tác giả sẽ giấu thông tin trong hình ảnh này sử dụng kĩ thuật MSB (ngược với LSB). Sử dụng [sigBits](https://github.com/Pulho/sigBits) để giải mã tin nhắn được ẩn giấu.          

```
┌──(kali㉿kali)-[~/Desktop/ctf/sigBits]
└─$ python sigBits.py -t=msb ../Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```

Ta được file `outputSB.txt`, tìm `picoCTF` là sẽ thấy flag            

![image](https://github.com/user-attachments/assets/71b3a27b-f5f7-4e7e-92fc-56cd26c60512)            

### Flag `picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_24d55bee}`
