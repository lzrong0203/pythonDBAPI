import requests
from bs4 import BeautifulSoup


class Ptt_crawler:

    def __init__(self, board):
        self.baseUrl = "https://www.ptt.cc{}"
        self.bbsString = "/bbs/"
        self.board = board

    def get_page_soup(self):
        try:
            if not self.board.startswith(self.bbsString):
                real_url = self.baseUrl.format(self.bbsString + self.board)
                # print(real_url)
            else:
                real_url = self.baseUrl.format(self.board)
                # print(real_url)
            r = requests.get(real_url)
        except requests.RequestException as e:
            print("Except, Error:", e)
            return None
        return BeautifulSoup(r.text, "html.parser")

    def get_title_url(self):
        soup = self.get_page_soup()
        href = []
        for title in soup.find_all("div", {"class": "title"}):
            dict1 = {}
            if title.a is not None:
                dict1["title"] = title.a.text
                dict1["href"] = title.a["href"]
                href.append(dict1)
        return href

    def get_upper_page_url(self):
        soup = self.get_page_soup()
        return soup.find_all("a", {"class": "btn wide"})[1].get("href")


if __name__ == "__main__":
    stock = Ptt_crawler("Stock")
    print(stock.get_title_url())
