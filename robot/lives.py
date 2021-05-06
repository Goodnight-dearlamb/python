#!/usr/bin/python
# coding=utf-8

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
from methods.Pdo import PDO

class lives(object):
    """docstring for lives."""
    def __init__(self):
      super(lives, self).__init__()

    # 获取快讯数据
    def getLivesData(this):
      driver = webdriver.Chrome()
      driver.set_window_size(1000,3000)
      driver.get("https://www.jinse.com/lives")
      time.sleep(3)
      this.getArticles(driver)

    def getArticles(this, driver):
      lives_info = []
      html_source = driver.page_source
      soup = bs(html_source, "html.parser")
      lives = soup.find_all("div", class_="js-lives__item")
      for live in lives:
        live_time = str(this.getId(live.find("div", class_="time").string))
        live_title = str(this.getId(live.find("a", class_="title").get_text()))
        content = live.find("div", class_="content")
        text = content.find_all("a")[1].get("href")
        live_id = this.getId(text)
        live_content = this.getId(content.find_all("a")[1].get_text())
        live_info_item = {
            "live_time":    live_time,
            "live_title":   live_title,
            "live_id":      live_id,
            "live_content": live_content
        }
        lives_info.append(live_info_item)
      print(lives_info)
      
    def getId(this, url):
      return url.replace("/lives/", "").replace(".html", "").replace(" ", "").replace("\n", "")


# 主函数
if __name__ == "__main__":
    this = lives()
    this.getLivesData()
