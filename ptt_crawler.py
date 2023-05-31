from bs4 import BeautifulSoup
import requests

baseUrl = "https://www.ptt.cc{}"
board = "/bbs/Stock"
cookies = {"over18": "1"}

r = requests.get(baseUrl.format(board))
soup = BeautifulSoup(r.text, "html.parser")
href = []
for title in soup.find_all("div", {"class": "title"}):
    dict1 = {}
    if title.a is not None:
        dict1["title"] = title.a.text
        dict1["href"] = title.a["href"]
        href.append(dict1)
print(href[0])
# print(soup.find_all("a", {"class": "btn wide"}))
# #
# soup2 = BeautifulSoup(requests.get(baseUrl.format(href[0]["href"])).text, "html.parser")
# print(soup2.find("div", {"id": "main-content"}).text)

