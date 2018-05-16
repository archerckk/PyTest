import uiautomator2 as u2
from uiautomator import device as d1

# print(d1.info)
# d1.screen.off()
# d = u2.connect('127.0.0.1')
# print(d.info)

u = u2.connect_usb()
u.make_toast("Hello world", 3)