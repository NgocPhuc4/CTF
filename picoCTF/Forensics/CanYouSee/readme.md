# CanYouSee

## Description
> How about some hide and seek?
> Download this file [here]().

## Solution
`strings` để xem các chuỗi trong file thì ta thấy có một đoạn được mã hóa bằng `base64`
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ strings ukn_reality.jpg                    
JFIF
7http://ns.adobe.com/xap/1.0/
<?xpacket begin='
' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x='adobe:ns:meta/' x:xmptk='Image::ExifTool 11.88'>
<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'>
 <rdf:Description rdf:about=''
  xmlns:cc='http://creativecommons.org/ns#'>
  <cc:attributionURL rdf:resource='cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg=='/>
 </rdf:Description>
</rdf:RDF>
</x:xmpmeta>
```
Tiến hành giải mã thì ta được flag
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==" | base64 -d                                                      
picoCTF{ME74D47A_HIDD3N_6a9f5ac4}
```

### Flag `picoCTF{ME74D47A_HIDD3N_6a9f5ac4}`
