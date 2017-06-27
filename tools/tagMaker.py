from bs4 import BeautifulSoup

def function(): 
    soup = BeautifulSoup("<addtag></addtag>", "html.parser")

    soup.addtag.append(soup.new_tag("article"))
    soup.addtag.article.append(soup.new_tag("span"))
    soup.addtag.article.span.append(soup.new_tag("img"))
    soup.addtag.article.append(soup.new_tag("a"))
    soup.addtag.article.a.append(soup.new_tag("h2"))
    soup.addtag.article.a.append(soup.new_tag("div"))
    soup.addtag.article.a.div.append(soup.new_tag("p"))

    #print "=== appended tags ==="
    #print soup.prettify()

    soup.addtag.article["class"] = "style1"
    soup.addtag.article.span["class"] = "image"
    soup.addtag.article.span.img["alt"] = ""
    soup.addtag.article.span.img["src"] = ""
    soup.addtag.article.a["href"] = ""
    soup.addtag.article.a.div["class"] = "content"

    #print "=== appended attrs ==="
    #print soup.prettify()

    tmpArticle = soup.addtag.article
    tmpArticle.find("h2").string = "TITLE"
    tmpArticle.find("span", attrs={"class" : "image"}).find("img")["src"] = "IMAGE_SRC"
    tmpArticle.find("span", attrs={"class" : "image"}).find("img")["alt"] = "IMAGE_ALT"
    tmpArticle.find("a")["href"] = "LINK"
    tmpArticle.find("div", attrs={"class" : "content"}).find("p").string = "SENTENCE"


    #print "=== result ==="
    #print soup.addtag.article.prettify()

    return soup.addtag.article


if __name__ == "__main__":
    returnStr = function()
    print returnStr.prettify()

    print "=== print test ==="
    soup = BeautifulSoup("<hoge></hoge>", "html.parser")
    soup.append(returnStr)
    print soup.prettify()
