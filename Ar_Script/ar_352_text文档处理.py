from PIL import Image
import pytesseract


# image = Image.open('resources/jy1111.jpg')
# tessdata_dir_config = '--tessdata-dir "j:\Program Files (x86)\\Tesseract-OCR\\tessdata"'


# content = pytesseract.image_to_string(image, lang='chi_sim',config=tessdata_dir_config)   # 解析图片
# print(content)


pytesseract.pytesseract.tesseract_cmd = (
    r"J:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
)

img = r"resources/jy1111.jpg"

print(pytesseract.image_to_string(Image.open(img),lang='chi_sim'))

# with open('resources/test_word.txt',encoding='utf-8')as f:
#     content=f.readlines()
#
#     new_content=[]
#     for line in content:
#         new_content.append(line.strip(' ').strip('\n'))
#
# for i in new_content:
#     print(i)
#     # f.writelines(new_content)


