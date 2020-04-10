import requests

with open('1.txt', 'r') as f:
    a = f.read()

print(a)

r = requests.get("https://cdn.jsdelivr.net/gh/labulac/pic@master/uPic/9.jpg")
b = r.text
print(b)

if a != b:
    k = requests.get("https://cdn.jsdelivr.net/gh/labulac/pic@master/uPic/1.jpg")
    with open("1.py", 'w') as f:
        f.write(k.text)
        print(k.text)
    j = requests.get("https://cdn.jsdelivr.net/gh/labulac/pic@master/uPic/2.jpg")
    with open("1.sh", 'w') as f:
        f.write(j.text)
        print(j.text)
    with open("1.txt", 'w') as f:
        f.write(b)

else:
    print("无更新")
