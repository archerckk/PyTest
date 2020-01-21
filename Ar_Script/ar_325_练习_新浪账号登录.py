from weibo import APIClient
import requests

APP_KEY=3598817835
APP_SECRET="052fd3eab7101fb6b08dbf125891f628"
CALLBACK_URL="http://e.com/callback"

client=APIClient(app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL)
# print(client)
url=client.get_authorize_url()

print(url)

res=requests.get(url)
print(res.url)

# code_url='http://e.com/callback?code=d5a96655a8581b1abc4b6fd67f1a267d'
# r=client.request_access_token('d5a96655a8581b1abc4b6fd67f1a267d')
# access_token=r.access_token
# expires_in=r.expires_in
# client.set_access_token(access_token,expires_in)