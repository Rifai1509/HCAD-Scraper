import bs4
import requests

url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords={0}&location={1}&scrambleSeed=509559697&pageNum=1'.format(input('Enter term : '),input('Enter location :'))
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
num = 0
# datas=[]
req = requests.get(url, headers= headers)
soup = bs4.BeautifulSoup(req.text, 'html.parser')
product = soup.findAll('div', 'row businessCapsule--mainRow')
for x in product:
    try:
        name = x.find('span','businessCapsule--name').text
        address = x.find('span', {'itemprop':'streetAddress'}).text
        post = x.find('span', {'itemprop':'postalCode'}).text
        telp = x.find('span', 'business--telephoneNumber').text
        web = x.find('a', {'rel': 'nofollow noopener'})['href'].split('?')[0].replace('https://','').replace('http://','').replace('http:','').replace('www.','')
    except:
        web ='Nothing'
    print('Name      :',name)
    print('Addres    :',address)
    print('Post Code :',post)
    print('Tel       :',telp)
    print('Website   :',web,"\n")

# with open('yell.csv', 'w', newline='') as file:
#     writer = _csv.writer(file)
#     headers = ['Name','Address','Post Code', 'Telp','Website']
#
#     writer.writerow(headers)
#     for data in datas:
#         writer.writerow(data)
