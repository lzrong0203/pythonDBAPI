import sqlite3
from ptt_crawler_class import Ptt_crawler as pttc

board = "Stock"
stock = pttc(board)
# print(stock.get_title_url())

conn = sqlite3.connect("ptt_content.db")
cur = conn.cursor()

cur.execute(f"DROP TABLE IF EXISTS {board}")
cur.execute(f"CREATE TABLE {board} (title TEXT, href TEXT )")
for title in stock.get_title_url():
    # print(title["title"])
    # print(title["href"])
    cur.execute(f'INSERT INTO {board} (title, href) '
                f'VALUES (?, ?)', (title["title"], title["href"]))
# conn.commit()


# cur.execute(f'INSERT INTO {board} (title, href) VALUES (?, ?)', ("[情報] 3481.TW 群創 5月營收", "/bbs/Stock/M.1654755204.A.D0B.html"))

for i in cur.execute(f"SELECT * FROM {board}"):
    print(i)
# cur.execute("INSERT INTO Accounts (name, balance) VALUES (?, ?)", ("Steve", 1000))
# cur.execute("INSERT INTO Accounts (name, balance) VALUES (?, ?)", ("Alan", 2000))
# cur.execute("INSERT INTO Accounts (name, balance) VALUES (?, ?)", ("Sam", 100))