# WebNet1

## Description
> We found this [packet capture](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/WebNet1/capture.pcap) and [key](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/WebNet1/picopico.key). Recover the flag.

## Solution
Tương tự như bài trước, cũng thêm key: Edit -> Preferences -> Protocols -> TLS -> Edit RSA key lists, sau đó nhập đường dẫn của file key vào Key file để giải mã TLS stream               
![image](https://github.com/user-attachments/assets/71ff1180-a203-422c-8cf0-07f271342900) 

Sau đó, File -> Export Object -> HTTP. Ta thấy có một file có tên là vulture.jpg rất đáng nghi. Tiến hành export file này ra và phân tích sâu hơn:
![image](https://github.com/user-attachments/assets/84729ab2-9717-41b2-85c7-cf0735a6c9c1)          

Dùng `strings` để lấy các kí tự đọc được trong hình ảnh, ta được flag
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ strings vulture.jpg | grep pico
picoCTF{honey.roasted.peanuts}
```

### Flag `picoCTF{honey.roasted.peanuts}`
