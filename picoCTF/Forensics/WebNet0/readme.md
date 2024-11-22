# WebNet0

## Description
> We found this [packet capture](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/WebNet0/capture.pcap) and [key](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/WebNet0/picopico.key). Recover the flag.

## Solution
Tham khảo [trang này](https://blog.didierstevens.com/2020/12/14/decrypting-tls-streams-with-wireshark-part-1/) để import file key vào trong file pcap để decrypt TLS stream.                

Edit -> Preferences -> Protocols -> TLS            
![image](https://github.com/user-attachments/assets/74b825e9-5277-4860-8072-2a5325d7ed27)          

Trong mục RSA key lists, chọn Edit, sau đó copy đường dẫn file key vào trong cột Key File    
![image](https://github.com/user-attachments/assets/018c30cd-7c8a-4c30-be7b-33eb0a479ded)         

Sau khi thêm xong thì ta Follow -> TLS Stream thì sẽ thấy flag ngay tại stream 0                       
![image](https://github.com/user-attachments/assets/7a0641a5-1320-4a30-896b-7a0ba1a7752b)         

### Flag `picoCTF{nongshim.shrimp.crackers}`
