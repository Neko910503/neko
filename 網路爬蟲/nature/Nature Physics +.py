import urllib.request as req
import bs4
import time
url = "https://www.nature.com/nphys/research"
request=req.Request(url, headers={
        #"cookie": "idp_marker=79477829-c967-45d0-a50d-c7df8f826de8; _ga=GA1.2.343970264.1599393450; permutive-id=156c7668-ae94-43bb-905a-5c2991680b21; _gac_UA-71668177-1=1.1606708409.EAIaIQobChMI0IbeyqGB7AIVBMEWBR3J2w_xEAAYASAAEgJ4z_D_BwE; OptanonAlertBoxClosed=2021-01-20T05:55:18.486Z; _gid=GA1.2.2068795888.1612850293; idp_session=sVERSION_1769bcf21-5dc5-4e13-8c82-76ce80b75b12; idp_session_http=hVERSION_18b5db5a7-94a1-4115-954a-784f4f31ce9f; Hm_lvt_485f8e597c8915da9aca0c37dca3f39f=1612850283,1612863665,1612934682,1613017227; CONTENT_USAGE_SESSIONID="utterlyidle:v1:MGVmNjRkN2UtNzc1Yi00MzRiLTliYjAtNDk5ZTE2NTU0MTY2"; _gat=1; OptanonConsent=isIABGlobal=false&datestamp=Thu+Feb+11+2021+15%3A48%3A46+GMT%2B0800+(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&version=6.12.0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0008%3A1%2CC0009%3A1&AwaitingReconsent=false&hosts=&geolocation=%3B; Hm_lpvt_485f8e597c8915da9aca0c37dca3f39f=1613029726; _uetsid=ca20da006a9b11eb998f3fa4a39e9c0e; _uetvid=087b4e405ae411ebae80d72b8a6b47ea; permutive-session=%7B%22session_id%22%3A%220a0f2ecd-c823-4a21-aa36-bbc0a2c5f531%22%2C%22last_updated%22%3A%222021-02-11T07%3A48%3A46.712Z%22%7D",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    })

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")
print(root)
titles = root.find_all("h3", class_="mb10 extra-tight-line-height word-wrap" , itemprop_="name headline")
print(titles)
for title in titles:
    if title.app != None:
        print(title.a.string.strip())


