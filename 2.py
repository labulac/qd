import requests

with open('1.txt', 'r') as f:
    a = f.read()

print(a)

r = requests.get("https://qd.labulac.top/1.txt")
b = r.text
print(b)

if a != b:
    k = requests.get("https://qd.labulac.top/1.py")
    with open("1.py", 'w') as f:
        f.write(k.text)
        print(k.text)
    j = requests.get("https://qd.labulac.top/1.sh")
    with open("1.sh", 'w') as f:
        f.write(j.text)
        print(j.text)
    with open("1.txt", 'w') as f:
        f.write(b)

else:
    print("无更新")