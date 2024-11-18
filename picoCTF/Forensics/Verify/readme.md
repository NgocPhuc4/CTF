# Verify

## Description
> People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.      
> `ssh -p 56105 ctf-player@rhea.picoctf.net`    
> Using the password `1db87a14`. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!             
> Checksum: `55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a`            
> To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.            

## Solution
SSH đến server sử dụng câu lệnh đã được cung cấp      
`ssh -p 56105 ctf-player@rhea.picoctf.net`     

Ta có nội dung của file `decrypt.sh` như sau:
```
        #!/bin/bash

        # Check if the user provided a file name as an argument
        if [ $# -eq 0 ]; then
            echo "Expected usage: decrypt.sh <filename>"
            exit 1
        fi

        # Store the provided filename in a variable
        file_name="$1"

        # Check if the provided argument is a file and not a folder
        if [ ! -f "/home/ctf-player/drop-in/$file_name" ]; then
            echo "Error: '$file_name' is not a valid file. Look inside the 'files' folder with 'ls -R'!"
            exit 1
        fi

        # If there's an error reading the file, print an error message
        if ! openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k picoCTF; then
            echo "Error: Failed to decrypt '$file_name'. This flag is fake! Keep looking!"
        fi
```
Nói chung, `decrypt.sh` sẽ nhận đầu vào là tên của 1 file, sau đó tiến hành giải mã nội dung của file bằng `openssl`.      
Trong thư mục `files` có rất nhiều file với tên là random
```
ctf-player@pico-chall$ cd files
ctf-player@pico-chall$ ls
0SgkM1fC  4BRDZhS7  8WA32dcd  C3l9qdYz  GFWqPjn6  L9tRKUkW  OkXybbh3  STlIDlxJ  WnOWGw9n  bVoP3eel  gr99Nl0G  mqsieQoa  pV3BIyJh  ud4LEsxA  z5y1jgty
0aer7B0J  4EqhTV10  8WYKhs9b  CChBmQFs  GhwoHV4M  LZgQIZ9b  OtnjktH8  Scml7yYd  WwobUdQA  bZEwUIec  gru5fnYQ  myF2mI2w  pVFybOWo  uhLtbHVL  zHpAJtSR
0b3lt0HK  4Fegg7AZ  8d6678sz  CDg6fdfa  Gpbebiyr  LnKLtxdL  PNNRiq3F  Sn9XVrp6  WzxM1rI6  blsMKCvn  hRF2XNzg  n1PE7llz  qAUGa8Jx  vQmN5k6y  zJHj9Wev
0ia8IBYb  4gMs4KnO  9LMKbufv  CTTDdMGJ  H6Mlhvd5  LoSmsO5t  PkxFO6fj  TWbymLFA  X3z7ayAf  bnahMLHf  iKH9t6m9  n6yqXRv8  qIqcOTDP  vQtPAQBH  zQZjRCvK
0uUAy06x  4l9DWh5d  9YFDyvy5  CXVq5spu  HS8wBLPJ  MAd4OQmU  PoAr7OrB  TXecNl9L  X5Vhdb8H  cO1o2qFY  ih4q9ziU  nSepPhk6  qKIr0SCL  vmLoCSN5  zmrLJtwD
17iH5ioj  5HAN1XjT  9rtRtn1R  Cwfv60OS  IMoTEVt4  MBaThKzn  PtRzswzh  Tx4sSuiN  Y4FnPPHX  cVywfT1b  jQXi84ic  nTEqj1Ol  qMqcX95Y  vt86VpBP  zoSxd2Nl
1CY2Hque  5ntikrlo  9wXkj9wB  DGOlVleK  IjkDI0gL  MLDxW9mt  QBtXtwy6  UCbhwrDb  YEOowfPv  cZXSF7wu  jnOnhjk8  nU797aVT  qfWh95Q9  vzBdlMd6  zp4ssY0Q
1LPOMJE7  5ymaOO07  9wzwojIO  DINN9cgG  IwVJbP5E  MV2AJR5r  QCHOeksH  UgDsmf5L  YZc8J6Vf  cdZ1Ao5D  kDlGNWXG  nVO17uZV  rPOS47wB  w2pqQhei
1P5dsfLj  6GzNwIbL  A2SZHgJV  DNwq8kf8  J7BJ7tAo  MXItXLsj  QOHEW95s  V3xeKcD7  YjEaz92U  chvVzQdY  kQMlzWUP  npy5LylP  rXWuGW1m  w80nVzZO
1Tst6fbt  6dZQoo4O  A8X4q2Hn  Dq8qjJ8S  JD0ZwfH8  MYdMdURn  QTetbcxE  VBHAXd7G  YkYjwuGz  cmhkISVH  kTDaKoIe  nxx3UCp8  rgZiIAPZ  w8E8Jd9J
2CyEUmhf  6mT8PiGl  ABh1G8a0  Dr3JaQz7  JIPRVMlG  MavUz60O  QcXjRtBd  VM5DLaA2  ZEEtJ79A  cvnPhBaQ  kvSPifOB  oLZldZsM  rjta4881  wHR2ydKC
2MgqiK3F  760ZV0rr  AUijzvDq  Dt7YKSAq  JLE4rtY5  Md3PHwRz  Qm0B85oQ  VU1Tnx8J  ZK4affS3  d0OYmJbG  kvpk6rIp  oNfmBvds  ryxNv3Er  wvNy3kRU
2R1dcXMM  7KoII9M8  AWnJiVoE  E1grB9Sb  JLuwL5UE  MvDDPtoW  Qxx5KB3R  VZqopSEM  ZO3IvMwL  d0rJvLyw  l70cIeRx  oWfAJ9wj  rzQKjmcB  xZDQnhCn
2SLEujSI  7NBIv8bi  AfnUEE9s  ETctMG1o  JVT3ckAg  NAwNCfiS  R84tLxGR  Vc1VEpYz  ZQ7ftng7  d1usLAwO  l8tB6vEL  ocTCyt2G  s3TrU3bC  y2XXKk9C
2cdcb2de  7Snixk9W  AgQhab96  EYaK1nX6  JhHZxLSp  NB0dzXJg  RKOBoCMd  Vc6sosw2  ZZzeAnnA  dxJZggkO  lEjMl22a  ocoustRi  sGOAdKy2  y8THzTYH
2eijwTPh  7eaPaid5  AlhLQIGI  FYfLvi5w  JrbVOugk  NHSLSull  RSQ5Ynin  VhrXhFPH  aDI9kNj8  eRcEh616  lMIM4IQe  orQXAz13  sKOkwRCd  yOmzIQym
3FOFUCD5  7ylewstJ  Au8Ov7jr  FcWqkSIP  KAS20Z1p  NYT2nPuv  RV6BgBu6  W7K36eZ0  aUzSODcp  eoW9IJAR  lbsGcfLr  oxeNN5uA  svPh5fI5  yTiWOwXD
3aMAegi2  7zsihLxd  B8RXEf4S  FhDH2g8j  KCoDTFB7  NlN25jkt  RWol5Yvg  WYlISi4n  agmwERM5  fpXvjTBY  lbszmcDf  oyrMYyZY  t4IiokLf  yb3Ro4yS
3laJICck  8N3DHyAn  BMlbLM49  FkO80Me6  Ka9uxW6u  NlymPzCl  RXQH6a3z  WaA6y2oF  b5TZpaRr  fw6XlbF3  mDzgzkrP  p0qmvEGQ  tenQzijC  ypzAaM0c
3mHrLQG2  8NfqFqEn  BpkwKiOq  FlEOSTL0  Kc5sfOun  NrbmwP3r  RrQhgxZJ  WjUfazgU  b8hbdeFv  g1qINnts  mMNEp8Zi  p3lVedu9  tkv0UoX3  yzW64294
3nroY5Wt  8OpGe3TY  C0PnAa7J  GEtA0Z9a  KhnreD4t  O3c1wd4r  Rrq6u3VG  WnH4XGQ0  bMcbuEVi  gewOpz6a  mg4g9Eoi  pREkecwB  tmkJMhbV  z1DTGQLy
```
Hiểu rồi, tất cả các file random này đều được mã hóa. Và chúng ta cần phải tìm đúng file có hash sha256 là `55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a`    
Ta tính mã hash 256 của tất cả các file trong thư mục `files` và xem thử file nào có mã hash trùng với mã hash cần tìm bằng cách sử dụng `grep`
```
ctf-player@pico-chall$ sha256sum files/* | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  files/2cdcb2de
```
Như vậy, file có mã hash trùng khớp là `files/2cdcb2de`, ta tiến hành giải mã nội dung của file
```
ctf-player@pico-chall$ ./decrypt.sh files/2cdcb2de
picoCTF{trust_but_verify_2cdcb2de}
```
