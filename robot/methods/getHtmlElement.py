from urllib import request
import chardet

# 获取目标网页的元素
def getHtmlElement(url):
    try:
        req = request.Request("https://www.jinse.com/news")
        print ("正在爬取````" + url + "```中的内容")
        reqHttpCode = response.getcode()
        if reqHttpCode == 200
            print("爬取目标页面成功")
            html = response.read().decode(charset['encoding'])
            return html
    except Exception as e:
        raise
