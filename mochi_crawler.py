from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import time
import lxml

all_url = []

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://photos.google.com/share/AF1QipO3jwE6MIYWWSG0DwhvYxJswXHZgvJJ5J-6M8NgF_i86aWgpB8afkA5TMI3pysPJA?key=Mkd6bV96MVZIYUpUTXBoaGZMN2gzVE4zSGFYRGRn")
    page.locator(".p137Zd").first.click()
    while True:
        page.get_by_label("查看下一張相片").click()
        #page.get_by_label("View next photo").click()
        
        html = page.inner_html("css=body")
        html = BeautifulSoup(html, "lxml")
        
        check_bugtton_disables = html.find("div", class_="RDPZE")
        if check_bugtton_disables:
            break

        try:
            image_url = ("\"",end="")
            print(image_url)
            image_url = html.find("img", class_="BiCYpc").get("src")
            all_url.append(image_url)
            print(image_url)
        except:
            print("Get Error")
            pass

        time.sleep(1)
    # ---------------------
    context.close()
    browser.close()

    #write to file
    with open("url.txt", "w") as f:
        for url in all_url:
            f.write(url + "\n")

    print("Done")


with sync_playwright() as playwright:
    run(playwright)