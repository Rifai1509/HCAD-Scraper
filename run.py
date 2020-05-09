import requests
from bs4 import BeautifulSoup
import _csv
hearders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'Referer': 'https://public.hcad.org/records/QuickRecord.asp'

            }

data = {
'searchtype': 'name',
'searchval': 'Michael',
'taxyear': '2020',
'submit2': 'View All'
}


url = "https://public.hcad.org/records/QuickRecord.asp"
response = requests.post(url, data=data, headers=hearders)
doc = BeautifulSoup(response.text, 'html.parser')

row_tags = doc.find_all('tr',{'bgcolor':"#ffffff"})
# print(row_tags)
datas = []
for row in row_tags:
    name = row.findAll('td',{'valign':"center"})[1].text.strip()
    # print(name)
    id = row.findAll('td',{'valign':"center"})[0].text.strip()
    # print(id)
    address = row.findAll('td',{'valign':"center"})[2].text.strip()
    # print(address)
    zip = row.findAll('td',{'valign':"center"})[3].text.strip()
    print(zip)
    datas.append([name,id,address,zip])

# with open('results.csv', 'w', newline='') as f:
#     writer = _csv.writer(f)
#     headers = ['Name', 'Account Number', 'Address', 'Zip Code']
#     writer.writerow(headers)
#     for data in datas:
#         writer.writerow(data)
