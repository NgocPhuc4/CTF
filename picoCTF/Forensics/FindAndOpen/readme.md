# FindAndOpen

## Description
> Someone might have hidden the password in the trace file.
> Find the key to unlock [this file](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/FindAndOpen/flag.zip). [This tracefile](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/FindAndOpen/dump.pcap) might be good to analyze.

## Solution
Đầu tiên, kiểm tra file pcap trước. Ta có thể thấy các đoạn thông điệp trong các gói Ethernet như sau:                 
![image](https://github.com/user-attachments/assets/b7560f1b-945a-463b-88eb-e2e2cbe21e74)                 
![image](https://github.com/user-attachments/assets/7df29749-2246-42a2-b869-2b2c6e2f43e4)                  
![image](https://github.com/user-attachments/assets/b4b3f419-2465-4bce-a411-a01df19bb2fe)                
Với đoạn này có vẻ như là được mã hóa base64 `VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=`
Decode base 64 ta được: `This is the secret: picoCTF{R34DING_LOKd_`

Sử dụng secret trên làm password cho file `flag.zip`, ta có được flag
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ unzip flag.zip 
Archive:  flag.zip
[flag.zip] flag password: 
password incorrect--reenter: 
 extracting: flag                    
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ ls
dump.pcap  flag  flag.zip  ok.txt
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ file flag    
flag: ASCII text
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ cat flag        
picoCTF{R34DING_LOKd_fil56_succ3ss_c2e6d949}
```

### Flag `picoCTF{R34DING_LOKd_fil56_succ3ss_c2e6d949}`
