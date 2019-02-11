import hashlib

md5=hashlib.md5()
sign_str='@admin123'#目标字符串
sign_byte_utf8=sign_str.encode(encoding='utf-8')#目标字符串编码
md5.update(sign_byte_utf8)#编码后的字符串进行升级
print(md5.hexdigest())#打印编码后的结果