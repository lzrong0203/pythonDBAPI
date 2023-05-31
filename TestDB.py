import sqlite3

conn = sqlite3.connect("testDB.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Accounts")
cur.execute("CREATE TABLE Accounts (name TEXT, balance FLOAT )")
cur.execute("INSERT INTO Accounts (name, balance) VALUES (?, ?)", ("Steve", 1000))
cur.execute("INSERT INTO Accounts (name, balance) VALUES (?, ?)", ("Alan", 2000))
cur.execute("INSERT INTO Accounts (name, balance) VALUES (?, ?)", ("Sam", 100))
conn.commit()

print("===============")
print("After insert...")
print("===============")
row = cur.execute("SELECT * FROM Accounts")
for r in row:
    print(r)


cur.execute("UPDATE Accounts SET balance = 20000 where name = (?)", ("Steve",))

print("===============")
print("After update...")
print("===============")
row = cur.execute("SELECT * FROM Accounts")
for r in row:
    print(r)

cur.execute("DELETE FROM Accounts where name = (?)", ("Sam",))

print("===============")
print("After delete...")
print("===============")
row = cur.execute("SELECT * FROM Accounts")
for r in row:
    print(r)
