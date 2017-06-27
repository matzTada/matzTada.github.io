#read from file
import codecs
f = codecs.open("test.html", "r")
html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

#print(soup.body.header.div.a.find_all("span"))

#for tmpArticle in soup.find_all("article", attrs={"class" : "style4"}):

for tmpArticle in soup.find_all("article"): 
    print(tmpArticle.find("h2").string + " " + tmpArticle["class"][0].encode())
    
print("=== before ===")
print(soup.find("article", attrs={"class" : "style4"}).prettify())

print("=== change ===")
soup.find("article", attrs={"class" : "style4"}).find("h2").string.replace_with("NEW!!")

print("=== after ===")
print(soup.find("article").prettify())

#write to files
outputFile = open("new.html", "w")
outputFile.write(soup.prettify(formatter="html"))
outputFile.close()
