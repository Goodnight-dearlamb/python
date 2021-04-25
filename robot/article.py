import re
import os
import sys
import time
import math
from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from methods.getHtmlElement import *

class jinSe(object):
    """docstring for jinSe."""

    def __init__(self):
        super(jinSe, self).__init__()

    # 模拟页面滚动
    def scrollPage(this, url):
        driver = webdriver.Chrome()
        driver.set_window_size(1000,3000)
        driver.get(url)
        print("> 正在获取文章列表 ...")
        for index in range(4):
            js="const q = document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            time.sleep(1)
            print("\r> 加载文章列表中: " + str((index + 1) * 25) + "%", end="")
            if index == 3:
                print("\n> 文章列表加载成功 ✔")

    # 获取目标链接的tag对象
    def getArticleContent(this, articleId):
        url = "https://www.jinse.com/blockchain/" + articleId + ".html"
        html = getHtmlElement(url)
        soup = bs(html, 'html.parser')
        article = this.getArticleInfo(soup)
        article["id"] = articleId
        # print(article)

    # 获取文章信息
    def getArticleInfo(this, soup):
        print ("> 正在获取当前文章内容 ...")
        title = soup.find("h1").string                                          # 标题
        articleAuthor = soup.find("div", class_="js-article-author")            # 作者盒子
        article = soup.find("div", class_="js-article")                         # 文章盒子
        author = articleAuthor.find("a").string                                 # 作者
        ## TODO: 抓取动态页面
        hour = articleAuthor.find_all("span")[2].string                         # 时间
        views = articleAuthor.find_all("span")[3].string                        # 浏览量
        tag = soup.find("section", class_="js-article-tag").string              # 标签
        img = article.find_all("img")                                           # 图片
        this.getArticleImg(img)                                                 # 保存图片
        article_str = str(article).replace("https://img.jinse.com/", "test")    # 文章内容
        print ("> 当前文章内容获取完成 ✔")
        return {
            "title":    title,
            "author":   author,
            "hour":     hour,
            "views":    views,
            "article":  article_str,
            "tag":      tag
        }


    # 获取所有图片 加水印保存
    def getArticleImg(this, imgTag):
        print ("> 正在获取当前文章内的图片 ...")
        # 图片保存路径
        file_path = "./img/"
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        for index, img in enumerate(imgTag):
            src = img.get("src")
            file_name = src.replace("https://img.jinse.com/", "")
            file_init = '{}{}{}'.format(file_path, os.sep, file_name)
            request.urlretrieve(src, file_init)
            print("\r> 图片保存进度: " + str(index + 1) + "/" + str(len(imgTag)), end = "")
            if index + 1 == len(imgTag):
                print(" ✔")
        print ("> 当前文章内的图片获取完毕 ✔")


# 主函数
if __name__ == "__main__":
    this = jinSe()
    this.getArticleContent("1073049")
    this.scrollPage("https://jinse.com")
