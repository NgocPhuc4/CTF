# endianness-v2

## Description
> Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.
> Download it [here](https://github.com/NgocPhuc4/CTF/blob/main/picoCTF/Forensics/endianness-v2/challengefile) and see what you can get out of it

## Solution

```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ file challengefile          
challengefile: data
```
Kiểm tra magic bytes của file, ta thấy đây có vẻ tương đồng với magic bytes của file jpeg
![image](https://github.com/user-attachments/assets/3771635b-b1cd-4105-b9db-807df8a32b05)       
![image](https://github.com/user-attachments/assets/f0cc9505-1604-47d1-afcc-e7c92c4d727c)         

Ta có thể thấy quy luật mà các bytes của file đã bị đổi như sau: Lần lượt 4 bytes sẽ bị đảo ngược vị trí. Ví dụ: E0 FF D8 FF 46 4A 10 00 01 -> FF D8 FF E0 | 01 00 4A 46      
Ta có đoạn code sau để chuyển đổi lại toàn bộ các byte của file theo quy luật trên để khôi phục lại file jpeg.
```python
def convert_to_little_endian(data):
    converted_data = bytearray()
    # Chia dữ liệu thành các cụm 4 bytes
    for i in range(0, len(data) - len(data) % 4, 4):
        converted_data.extend(data[i:i+4][::-1])  # Đảo ngược từng cụm 4 bytes

    # Xử lý phần dư (nếu có)
    remainder = len(data) % 4
    if remainder > 0:
        converted_data.extend(data[-remainder:][::-1])  # Đảo ngược phần dư

    return converted_data


def process_file(input_file, output_file):
    try:
        # Đọc tệp gốc
        with open(input_file, 'rb') as file:
            data = file.read()

        # Chuyển đổi dữ liệu
        little_endian_data = convert_to_little_endian(data)

        # Ghi dữ liệu đã chuyển đổi vào tệp mới
        with open(output_file, 'wb') as file:
            file.write(little_endian_data)

        print(f"Dữ liệu đã được chuyển đổi và lưu vào {output_file}")

    except FileNotFoundError:
        print("Tệp không tồn tại!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")


# Ví dụ sử dụng
input_file = "challengefile"   # Tên tệp gốc
output_file = "flag.jpeg" # Tên tệp đầu ra

process_file(input_file, output_file)
```

Chạy file và ta được kết quả
```                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ python solve.py
Dữ liệu đã được chuyển đổi và lưu vào flag.jpeg
```

![image](https://github.com/user-attachments/assets/5ccfe0df-9be1-47b4-bed9-ccb28933cd30)            

### Flag picoCTF{cert!f1Ed_iNd!4n_s0rrY_3nDian_188d7b8c}
