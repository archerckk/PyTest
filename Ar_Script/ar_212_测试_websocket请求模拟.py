import websocket

url='ws://www.xxxx.com/xxxx'
web_request=websocket.create_connection(url)
web_request.send("{'request:1111,'services:'1001,'name':123445}")
msg=web_request.recv()
print(msg)