from suds.client import Client

url='http://ws.webxml.com/WebServices/MobieCodeWS.asmx?wsdl'
client=Client(url)
result=client.service.getMobileCodeInfo('1334535454')
print(result)