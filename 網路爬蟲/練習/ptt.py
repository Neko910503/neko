# 連線至 批踢踢實業坊 - 八卦版
# https://www.ptt.cc/bbs/Gossiping/index6.html
import urllib.request as req
import bs4

# 包裝函式
def getTitle(url):
    Url = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    })
    with req.urlopen(Url) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    text_titles = root.find_all("div", class_="title")
    for title in text_titles:
        if title.a != None:
            print(title.a.string)
    
    # 利用特殊的「‹ 上頁」字樣，找到 <a> 標籤
    nextlink = root.find("a", string="‹ 上頁")
    if "disabled" in nextlink["class"]:
        return None               # 有 disabled 時，回傳 None
    else:
        return nextlink["href"]   # 沒有 disabled 時，回傳網址


# 使用函式
url = "https://www.ptt.cc/bbs/Gossiping/index6.html"
isEnd = False
while isEnd != True:
    prev_page_url = getTitle(url)
    if prev_page_url == None:
        isEnd = True
        break
    url = "https://www.ptt.cc" + prev_page_url