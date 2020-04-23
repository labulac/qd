import requests
import codecs

name='抖音短视频'
baseurl='https://tools.lancely.tech'
nameurl = baseurl + '/apple/app-search?country=cn&query='+name
a=requests.get(nameurl)


visionurl =baseurl+'/apple/app-version/cn/1142110895'
b=requests.get(visionurl)
print(b.text)