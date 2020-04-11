import requests

with open('1.py', 'r') as f:
    a = f.read()

r = requests.get("https://qd.labulac.top/1.py")
b = r.text

if a != b:
    print("检测到更新")
    with open("1.py", 'w') as f:
        f.write(b)
    print("已更新完成")

else:
    print("没有更新")
