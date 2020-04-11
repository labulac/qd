import requests

with open('1.txt', 'r') as f:
    a = f.read()

print(a)

r = requests.get("https://qd.labulac.top/1.txt")
b = r.text
print(b)

if a != b:
    print("检测到更新")
    k = requests.get("https://qd.labulac.top/1.py")
    with open("1.py", 'w') as f:
        f.write(k.text)
    with open("1.txt", 'w') as f:
        f.write(b)
    print("已更新完成")

else:
    print("没有更新")