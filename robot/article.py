from methods.getHtmlElement import *
from bs4 import BeautifulSoup as bs

# 当前最高浏览量
max_view = 0

class jinSe:
    # 初始化
    def __init__(self):
        # 过滤作者关键字
        self.filter_auths = ["金色", "比特白银"]
        # 过滤标题关键字
        self.filter_titles = ["金色", "比特白银"]
        # 当前最高浏览量
        self.max_view = 0
        # 浏览量数组
        self.views = []

    # 获取所有
    def getArticle(self):
        html = getHtmlElement("https://www.jinse.com")
        soup = bs(html, 'html.parser')
        articles = soup.find_all("div", class_="js-article")
        articles = self.spreadPass(articles=articles)
        self.getViews(articles)
        max_view = max(self.views)
        print(max_view)
            #
            # title = article.a.get("title")
            # articles.append(article.a.get("href"))

    # A是否包含B
    def contains(self, A, B):
        if B in A:
            return True
        else:
            return False

    # 返回存放浏览量的数组
    def getViews(self, articles):
        for article in articles:
            view = article.find("span", class_="js-single__footItem").find("span", class_="text").string
            self.views.append(view)

    # 剔除广告和推广
    def spreadPass(self, articles):
        # 存放真正文章的数组
        realArticles = []
        for article in articles:
            # 判断是否为推广
            isSpread = article.find("a", class_="js-single--spread")
            # 判断是否为广告
            ad = article.find("span", class_="js-single__foot-generalize")
            isAd = self.contains(str(ad), "display:none")
            if not isSpread and isAd:
                realArticles.append(article)
        return realArticles



# print (articles)


if __name__ == "__main__":
    jinSe = jinSe()
    jinSe.getArticle()
