import pyperclip

# 复制好了的内容直接运行即可！！！

vvv = pyperclip.paste()
a = [vvv]

v = a[0]

l = list(v)

b = []
d = []
for i in range(len(l)):
    if l[i] == "[":
        b.append(i)
    if l[i] == "]":
        d.append(i + 1)

e = []
for i in range(len(b)):
    ls3 = ''.join(l[b[i]:d[i]])
    e.append(ls3)

print(e)
q = []
for i in range(len(e)):

    p = list(e[i])
    if p[1] == '@':
        q.append(i)

print(q)

for i in range(len(q)):
    v = v.replace(e[q[i]], '')
print(v)
pyperclip.copy(v)
print("已复制")
