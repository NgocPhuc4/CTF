# Blast from the past

## Description
> The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?                                          
> Set the timestamps on this picture to 1970:01:01 00:00:00.001+00:00 with as much precision as possible for each timestamp. In this example, +00:00 is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: 1969:12:31 19:00:00.001-05:00. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.                          
> Use this [picture]().

## Solution
Sử dụng `exiftool` để kiểm tra metadata của hình ảnh
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ exiftool original.jpg             
ExifTool Version Number         : 12.76
File Name                       : original.jpg
Directory                       : .
File Size                       : 2.9 MB
File Modification Date/Time     : 2024:03:13 13:44:58-04:00
File Access Date/Time           : 2024:11:18 22:14:02-05:00
File Inode Change Date/Time     : 2024:11:18 22:14:02-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Little-endian (Intel, II)
Image Description               : 
Make                            : samsung
Camera Model Name               : SM-A326U
Orientation                     : Rotate 90 CW
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : MediaTek Camera Application
Modify Date                     : 2023:11:20 15:46:23
Y Cb Cr Positioning             : Co-sited
Exposure Time                   : 1/24
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 500
Sensitivity Type                : Unknown
Recommended Exposure Index      : 0
Exif Version                    : 0220
Date/Time Original              : 2023:11:20 15:46:23
Create Date                     : 2023:11:20 15:46:23
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/24
Aperture Value                  : 1.9
Brightness Value                : 3
Exposure Compensation           : 0
Max Aperture Value              : 1.8
Metering Mode                   : Center-weighted average
Light Source                    : Other
Flash                           : On, Fired
Focal Length                    : 4.6 mm
Sub Sec Time                    : 703
Sub Sec Time Original           : 703
Sub Sec Time Digitized          : 703
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 4000
Exif Image Height               : 3000
Interoperability Index          : R98 - DCF basic file (sRGB)
Interoperability Version        : 0100
Exposure Mode                   : Auto
White Balance                   : Auto
Digital Zoom Ratio              : 1
Focal Length In 35mm Format     : 25 mm
Scene Capture Type              : Standard
Compression                     : JPEG (old-style)
Thumbnail Offset                : 1408
Thumbnail Length                : 64000
Image Width                     : 4000
Image Height                    : 3000
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Time Stamp                      : 2023:11:20 15:46:21.420-05:00
MCC Data                        : United States / Guam (310)
Aperture                        : 1.8
Image Size                      : 4000x3000
Megapixels                      : 12.0
Scale Factor To 35 mm Equivalent: 5.4
Shutter Speed                   : 1/24
Create Date                     : 2023:11:20 15:46:23.703
Date/Time Original              : 2023:11:20 15:46:23.703
Modify Date                     : 2023:11:20 15:46:23.703
Thumbnail Image                 : (Binary data 64000 bytes, use -b option to extract)
Circle Of Confusion             : 0.006 mm
Field Of View                   : 71.5 deg
Focal Length                    : 4.6 mm (35 mm equivalent: 25.0 mm)
Hyperfocal Distance             : 2.13 m
Light Value                     : 4.0
```

Ta thấy các tag liên quan đến thời gian là
```
Modify Date                     : 2023:11:20 15:46:23
Time Stamp                      : 2023:11:20 15:46:21.420-05:00
Create Date                     : 2023:11:20 15:46:23.703
Date/Time Original              : 2023:11:20 15:46:23.703
Modify Date                     : 2023:11:20 15:46:23.703
```

Sử dụng `exiftool` để chỉnh sửa lại timestamp, vì timestamp lấy số tự nhiên, nên chuỗi đề cho quy về integer là bằng 1:
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ exiftool -TimeStamp=1 original.jpg 
    1 image files updated
```

Tiến hành chuyển toàn bộ các tag khác liên quan đến timestamp
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ exiftool -s original.jpg          
ExifToolVersion                 : 12.76
FileName                        : original.jpg
Directory                       : .
FileSize                        : 2.9 MB
FileModifyDate                  : 2024:11:18 22:23:49-05:00
FileAccessDate                  : 2024:11:18 22:23:50-05:00
FileInodeChangeDate             : 2024:11:18 22:23:49-05:00
FilePermissions                 : -rw-r--r--
FileType                        : JPEG
FileTypeExtension               : jpg
MIMEType                        : image/jpeg
ExifByteOrder                   : Little-endian (Intel, II)
ImageDescription                : 
Make                            : samsung
Model                           : SM-A326U
Orientation                     : Rotate 90 CW
XResolution                     : 72
YResolution                     : 72
ResolutionUnit                  : inches
Software                        : MediaTek Camera Application
ModifyDate                      : 2023:11:20 15:46:23
YCbCrPositioning                : Co-sited
ExposureTime                    : 1/24
FNumber                         : 1.8
ExposureProgram                 : Program AE
ISO                             : 500
SensitivityType                 : Unknown
RecommendedExposureIndex        : 0
ExifVersion                     : 0220
DateTimeOriginal                : 2023:11:20 15:46:23
CreateDate                      : 2023:11:20 15:46:23
ComponentsConfiguration         : Y, Cb, Cr, -
ShutterSpeedValue               : 1/24
ApertureValue                   : 1.9
BrightnessValue                 : 3
ExposureCompensation            : 0
MaxApertureValue                : 1.8
MeteringMode                    : Center-weighted average
LightSource                     : Other
Flash                           : On, Fired
FocalLength                     : 4.6 mm
SubSecTime                      : 703
SubSecTimeOriginal              : 703
SubSecTimeDigitized             : 703
FlashpixVersion                 : 0100
ColorSpace                      : sRGB
ExifImageWidth                  : 4000
ExifImageHeight                 : 3000
InteropIndex                    : R98 - DCF basic file (sRGB)
InteropVersion                  : 0100
ExposureMode                    : Auto
WhiteBalance                    : Auto
DigitalZoomRatio                : 1
FocalLengthIn35mmFormat         : 25 mm
SceneCaptureType                : Standard
Compression                     : JPEG (old-style)
ThumbnailOffset                 : 1408
ThumbnailLength                 : 64000
XMPToolkit                      : Image::ExifTool 12.76
TimeStamp                       : 1
ImageWidth                      : 4000
ImageHeight                     : 3000
EncodingProcess                 : Baseline DCT, Huffman coding
BitsPerSample                   : 8
ColorComponents                 : 3
YCbCrSubSampling                : YCbCr4:2:0 (2 2)
MCCData                         : United States / Guam (310)
Aperture                        : 1.8
ImageSize                       : 4000x3000
Megapixels                      : 12.0
ScaleFactor35efl                : 5.4
ShutterSpeed                    : 1/24
SubSecCreateDate                : 2023:11:20 15:46:23.703
SubSecDateTimeOriginal          : 2023:11:20 15:46:23.703
SubSecModifyDate                : 2023:11:20 15:46:23.703
ThumbnailImage                  : (Binary data 64000 bytes, use -b option to extract)
CircleOfConfusion               : 0.006 mm
FOV                             : 71.5 deg
FocalLength35efl                : 4.6 mm (35 mm equivalent: 25.0 mm)
HyperfocalDistance              : 2.13 m
LightValue                      : 4.0
```

3 tags DateTimeOriginal, CreateDate and ModifyDate có thể được chỉnh chung thông qua tag `AllDates`                      
![image](https://github.com/user-attachments/assets/59e36f9b-9460-4547-8517-16a25bbe36a6)                      

```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ exiftool -AllDates='1970:01:01 00:00:00.001' -SubSecCreateDate='1970:01:01 00:00:00.001' -SubSecDateTimeOriginal='1970:01:01 00:00:00.001' -SubSecModifyDate='1970:01:01 00:00:00.001' original.jpg
    1 image files updated
```

Đưa lên kiểm tra, tuy nhiên vẫn còn một case cuối chưa chính xác
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ nc mimas.picoctf.net 58712                    
MD5 of your picture:
74427a614e04909fc467e5d219e50082  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 2023:11:20 20:46:21.420+00:00
Oops! That tag isn't right. Please try again.
```

Tag cần chỉnh cuối rơi vào Group Samsung, Tag Timestamp. Tuy nhiên qua tìm hiểu, tag này không thể chỉnh sửa bằng `exiftool`             
![image](https://github.com/user-attachments/assets/cead7e18-ccee-4b37-bf8c-0aa297afb742)           

Không sửa được bằng `exiftool` thì ta sử dụng [HxD](https://mh-nexus.de/en/hxd/) để sửa trực tiếp byte ở đó
![image](https://github.com/user-attachments/assets/00a10af1-c744-4bb9-b7ed-a3cff717b492)                  

![image](https://github.com/user-attachments/assets/e7cf1bbe-e37d-4785-b077-74e16e8f94bb)                       

Sau khi chỉnh xong, ta kiểm tra lại bằng `exiftool`                  
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ exiftool -Samsung:TimeStamp original_modified.jpg
Time Stamp                      : 1969:12:31 19:00:00.001-05:00
```

Nộp lên server và ta thành công có flag
```
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ nc -w 2 mimas.picoctf.net 51835 < original_modified.jpg
                                                                                                                                                             
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ nc mimas.picoctf.net 58712                             
MD5 of your picture:
60ddd49f803fc0d9086952feb3550023  test.out

Checking tag 1/7
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 2/7
Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 3/7
Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 1970:01:01 00:00:00
Great job, you got that one!

Checking tag 4/7
Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 5/7
Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 6/7
Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001
Great job, you got that one!

Checking tag 7/7
Timezones do not have to match, as long as it's the equivalent time.
Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 1970:01:01 00:00:00.001+00:00
Great job, you got that one!

You did it!
picoCTF{71m3_7r4v311ng_p1c7ur3_a4f2b526}
```

### Flag `picoCTF{71m3_7r4v311ng_p1c7ur3_a4f2b526}`

## Reference
- [Samsung Tags](https://exiftool.org/TagNames/Samsung.html)
- [ExifTool by Phil Harvey](https://exiftool.org/)
- [Epoch Converter](https://www.epochconverter.com/)
