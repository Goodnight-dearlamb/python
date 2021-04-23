import re
import sys
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from methods.getHtmlElement import *

class jinSe(object):
    """docstring for jinSe."""

    def __init__(self):
        super(jinSe, self).__init__()

    # 爬取目标链接的文章内容
    def getArticleContent(this, articleId):
        url = "https://www.jinse.com/blockchain/" + articleId + ".html"
        html = getHtmlElement(url)
        soup = bs(html, 'html.parser')
        print(soup)


# 主函数
if __name__ == "__main__":
    this = jinSe()
    this.getArticleContent("1072658")
