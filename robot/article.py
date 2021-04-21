from getHtmlElement import *
from bs4 import BeautifulSoup as bs

# 构建Request
req = getHtmlElement("https://www.jinse.com/news")

print(req)
