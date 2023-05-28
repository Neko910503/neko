import urllib.request as req
import bs4
url = "https://www.nature.com/nphys/"
request=req.Request(url, headers={
        #"cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    })
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("li", class_="app-trending-row__item")
for title in titles:
     if title.h3 != None:
        print(title.h3.string.strip())