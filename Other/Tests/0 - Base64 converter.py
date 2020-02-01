import base64

with open ("data.txt", "r") as myfile:
    data=myfile.readlines()
data = str(data)
b64 =(base64.b64encode(bytes(data, 'utf-8')))
print(len(data))
print(len(b64))
