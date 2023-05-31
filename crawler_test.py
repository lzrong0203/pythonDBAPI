from bs4 import BeautifulSoup

with open("sample.html") as sample:
    soup = BeautifulSoup(sample.read(), "html.parser")

print(soup.find("main").p)
