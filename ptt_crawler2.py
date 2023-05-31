from bs4 import BeautifulSoup
import requests

baseUrl = "https://www.ptt.cc{}"
board = "/bbs/Stock"
cookies = {"over18": "1"}


def get_ptt_page(url):
    try:
        r = requests.get(baseUrl.format(url))
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    return BeautifulSoup(r.text, 'html.parser')


def get_title_url(board_url):
    if not board_url.startswith("/bbs/"):
        board_url = "/bbs/" + board
    soup = get_ptt_page(board_url)
    print(f"Get title from {board_url}")
    href = []
    for title in soup.find_all("div", {"class": "title"}):
        dict1 = {}
        if title.a is not None:
            dict1["title"] = title.a.text
            dict1["href"] = title.a["href"]
            href.append(dict1)
    return href


def get_page_url(board_url):
    board_url = "/bbs/" + board_url
    soup = get_ptt_page(board_url)
    url = []
    for a in soup.find_all("a", {"class": "btn wide"}):
        url.append(a.get("href"))
    return url


if __name__ == "__main__":
    print(get_title_url(get_page_url("stock")[1]))
