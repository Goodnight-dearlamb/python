import re
import os
import sys
import time
import math
import pymysql
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
            time.sleep(2)
            print("\r> 加载文章列表中: " + str((index + 1) * 25) + "%", end="")
            if index == 3:
                print("\n> 文章列表加载成功 ✔")
        this.getArticles(driver)

    # 获取文章集合
    def getArticles(this, driver):
        html_source = driver.page_source
        soup = bs(html_source, "html.parser")
        articles = soup.find_all("div", class_="js-article")                    # 文章列表
        print("> 开始过滤文章 ...")
        articles = this.topPass(articles)
        this.getMaxViews(articles)

    # 剔除置顶文章
    def topPass(this, articles):
        res = []
        pass_number = 0
        article_number = 0
        for article in articles:
            isTop = str(article.find("span", class_="js-tag-top"))
            isGeneralize = str(article.find("span", class_="js-single__foot-generalize"))
            isSole = str(article.find("span", class_="js-tag-sole"))
            isFilter = str(article.find("a", class_="js-single__foot-author"))

            if "display:none" in isTop and "display:none" in isGeneralize and "display:none" in isSole and "金色" in isFilter:
                article_number = article_number + 1
                res.append(article)
            else:
                pass_number = pass_number + 1
        print("\n> 过滤置顶文章完成 共" + str(pass_number) + "篇 ✔")
        print("\n> 符合要求文章 共" + str(article_number) + "篇 ✔")
        return res

    # 获取浏览量最高的文章
    def getMaxViews(this, articles):
        max_views = 0
        max_articles_id = 0
        for article in articles:
            view = article.find("span", class_="text").string.replace(" ", "")
            if int(view) > max_views:
                max_views = int(view)
                articles_id = article.find("a", class_="js-single__left").get("href")
                max_articles_id = articles_id.replace("https://www.jinse.com/blockchain/", "").replace(".html", "").replace("https://www.jinse.com/news/blockchain/", "")

        this.getArticleContent(max_articles_id)

    # 获取目标链接的tag对象
    def getArticleContent(this, articleId):
        url = "https://www.jinse.com/blockchain/" + articleId + ".html"
        html = getHtmlElement(url)
        soup = bs(html, 'html.parser')
        article = this.getArticleInfo(soup)
        article["id"] = articleId
        print(res)

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
        img = article.find_all("img" )                                           # 图片
        this.getArticleImg(img)                                                 # 保存图片
        article_str = str(article).replace("https://img.jinse.com/", "https://img.jinse.com/")    # 文章内容
        print ("> 当前文章内容获取完成 ✔")
        return {
            "article_titile":    title,
            "article_author_id": 11,
            # "author":   author,
            "article_time":      hour,
            "article_views":     views,
            "article_content":   article_str,
            "article_tag":       tag
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
    this.scrollPage("https://jinse.com")
