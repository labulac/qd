import pyperclip


a = [
    "/html/body[@id='nv_home']/div[@id='wp']/div[@id='ct']/div[@id='main_message']/div[@class='f_c altw']/div[@id='messagelogin']/div[@id='main_messaqge_LzFWi']/div[@id='layer_login_LzFWi']/form[@id='loginform_LzFWi']/div[@class='c cl']/div[@class='rfm'][1]/table/tbody/tr/td[1]/input[@id='username_LzFWi']"
]

v=a[0]

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
    if p[1]=='@':
        q.append(i)

print(q)

for i in range(len(q)):
    v=v.replace(e[q[i]],'')
print(v)
pyperclip.copy(v)
print("已复制")