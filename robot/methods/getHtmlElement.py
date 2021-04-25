from urllib import request
import chardet

def getHtmlElement(url):
    req = request.Request(url)
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset['encoding'])
    return html
    
