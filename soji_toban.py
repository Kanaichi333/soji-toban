import os
from datetime import datetime, timedelta


def read(txt):
    with open(txt, "r") as f:
        text = f.read()
        text = text.replace("\n\n", "\n").replace('"', "")
        text = text.replace("\n\n", "\n").replace("\n:", ":").replace("、", ", ")
        lines = text.splitlines()
        
    title_i = []
    titles = []
    for i in range(len(lines)):
        if "/" in lines[i]:
            date = lines[i].replace("日付: ", "")
        elif ":" not in lines[i]:
            title_i.append(i)
            titles.append(lines[i])
    title_i.append(len(lines))

    toban = []
    for i in range(len(titles)):
        li = []
        for j in range(title_i[i]+1, title_i[i+1]):
            li.append(lines[j].split(": "))
        toban.append(li)

    return date, titles, toban


def next_toban(txt):
    date, titles, toban = read(txt)

    date = datetime.strptime(date, "%Y/%m/%d")
    date = date + timedelta(days=7)
    date = date.strftime("%Y/%m/%d")

    for li in toban:
        li.append(li[0].copy())
        for i in range(len(li)-1):
            li[i][1] = li[i+1][1]
        del li[-1]
        
    return date, titles, toban


def write(date, titles, toban):
    print(f"{date}\n")

    for i in range(len(titles)):
        print(titles[i])

        for j in range(len(toban[i])):
            print(f"{toban[i][j][0]}: {toban[i][j][1]}")
            
        print("")


if __name__ == "__main__":
    print("次回の掃除当番は\n")

    txt = f"{os.path.dirname(__file__)}/soji_toban_input.txt"
    date, titles, toban = next_toban(txt)
    write(date, titles, toban)
