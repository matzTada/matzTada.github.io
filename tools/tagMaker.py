from bs4 import BeautifulSoup

def writeArticle(title, img_src, img_alt, link, sentence): 
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
    tmpArticle.find("h2").string = title
    tmpArticle.find("span", attrs={"class" : "image"}).find("img")["src"] = img_src
    tmpArticle.find("span", attrs={"class" : "image"}).find("img")["alt"] = img_alt
    tmpArticle.find("a")["href"] = link
    tmpArticle.find("div", attrs={"class" : "content"}).find("p").string = sentence

    #print "=== result ==="
    #print soup.addtag.article.prettify()

    return soup.addtag.article #return PageElement


if __name__ == "__main__":
    title = "TITLE"
    img_src = "IMAGE_SRC"
    img_alt = "IMAGE_ALT"
    link = "LINK"
    sentence = "SENTENCE"
    returnPageElement = writeArticle(title, img_src, img_alt, link, sentence)
    print returnPageElement.prettify()

    print "=== print test ==="
    soup = BeautifulSoup("<hoge></hoge>", "html.parser")
    soup.append(returnPageElement)
    print soup.prettify()
