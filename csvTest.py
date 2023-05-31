import csv

with open("臺北捷運車站周邊轉乘停車場資訊.csv", encoding="big5") as parking:
    csv_content = csv.reader(parking)
    parking_list = []
    for line in csv_content:
        parking_list.append(line)
print(parking_list[10])
