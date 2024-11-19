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
