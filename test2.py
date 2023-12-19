import requests
import pandas

url='http://api.coincap.io/v2/assets'

header={"Content-type":"application/json",
        "Accept-Encoding":"deflate"}

response = requests.get(url,headers=header)
print(response)

responseData= response.json()

df= pandas.json_normalize(responseData,'data')
print(df)

df.to_csv(r'./data.csv')