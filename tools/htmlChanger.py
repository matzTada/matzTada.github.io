import codecs
f = codecs.open("test.html", "r")
html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

#print(soup.body.header.div.a.find_all("span"))

print(soup.find("article", attrs={"class" : "style3"}).prettify())
