# Torrent Analyze

## Description
> SOS, someone is torrenting on our network.                     
> One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded? The file name will be the flag, like picoCTF{filename}. [Captured traffic](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/TorrentAnalyze/torrent.pcap).

## Solution
Với protocol BH-DHT, ta thấy có thông tin hash                 
![image](https://github.com/user-attachments/assets/e33ce2a9-8d7a-41f9-a873-20bdd5e9dd9d)                

Tra cứu các hash này bên [VirusTotal](https://www.virustotal.com/gui) thì ta thấy hash `e2467cbf021192c241367b892230dc1e05c0580e` cho ta thông tin file `ubuntu-19.10-desktop-amd64.iso_torrent_info.dat`              
![image](https://github.com/user-attachments/assets/6202cf54-b85b-4072-b0c8-c51b540f26b0)

Nộp thì không đúng, sau đó bỏ đuôi phía sau đi, chỉ giữa lại tới `.iso` thì đúng

### Flag `picoCTF{ubuntu-19.10-desktop-amd64.iso}`
