import codecs
f = codecs.open("test.html", "r")
html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

#print(soup.body.header.div.a.find_all("span"))

print("=== before ===")
print(soup.find("article", attrs={"class" : "style4"}).prettify())

print("=== change ===")
soup.find("article", attrs={"class" : "style4"}).find("h2").string.replace_with("hogehogehoge")

print("=== after ===")
print(soup.find("article").prettify())

outputFile = open("new.html", "w")
outputFile.write(soup.prettify(formatter="html"))
outputFile.close()
