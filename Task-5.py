# WEB SCRAPING PROGRAM

import requests
from bs4 import BeautifulSoup
import re

l=[]
o={}
specs_arr=[]
specs_obj={}

target_url="https://www.amazon.com/1920x1080-Protable-Computer-Speakers-Business/dp/B0D83M72RY/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.6afe7900-0834-4d0d-afa0-213431caed72&dib=eyJ2IjoiMSJ9.gJlZwJN0jRmzkaQaQ2cS00pn3L6uDQLEx1wfOWLrcC7-SJ6IVTTagl4o_FCue59nZeZGVCdYhrpCDVvCU6oZTNSPUME8npDYu7rIPjxYmgkHMy8HnT5NvZpX55aMJTQgPM1nA5mJgehue46c2GI2Ft9S-LUCTYmku6FWw1OX5MMJxisqMzis6wdTvStq2BFOShxVZ12Fhb1rMcArU3IoJ8ADZ_uYUhlxuukSwdzqF-0.R4_geJU22q6v0nHp_NyOTdHlUpKZAyEOh1RCSRkH3AU&dib_tag=se&keywords=computers&pd_rd_r=20aa566f-f452-428f-a2ab-f1246c19f016&pd_rd_w=GEXY5&pd_rd_wg=tpjIa&pf_rd_p=6afe7900-0834-4d0d-afa0-213431caed72&pf_rd_r=G702GDYAWZJP36P9B2M1&qid=1720881770&refinements=p_n_deal_type%3A23566065011&sr=8-1"

headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

resp = requests.get(target_url, headers=headers)
print(resp.status_code)
if(resp.status_code != 200):
    print(resp)
soup=BeautifulSoup(resp.text,'html.parser')


try:
    o["title"]=soup.find('h1',{'id':'title'}).text.lstrip().rstrip()
except:
    o["title"]=None


images = re.findall('"hiRes":"(.+?)"', resp.text)
o["images"]=images

try:
    o["price"]=soup.find("span",{"class":"a-price"}).find("span").text
except:
    o["price"]=None

try:
    o["rating"]=soup.find("i",{"class":"a-icon-star"}).text
except:
    o["rating"]=None


specs = soup.find_all("tr",{"class":"a-spacing-small"})

for u in range(0,len(specs)):
    spanTags = specs[u].find_all("span")
    specs_obj[spanTags[0].text]=spanTags[1].text


specs_arr.append(specs_obj)
o["specs"]=specs_arr
l.append(o)


print(l)