#htmlChanger.py
#variables
inFileName = "../index.html"
outFileName = "../index_mod.html"

#read from file
import codecs
f = codecs.open(inFileName, "r")
html = f.read()

#using BeautifulSoup to handle html files
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

for tmpArticle in soup.find_all("article"): 
    print(tmpArticle.find("h2").string + " : " + tmpArticle["class"][0].encode())
    tmpArticle["class"][0] = "style0"
    
#write to files
outputFile = open(outFileName, "w")
outputFile.write(soup.prettify(formatter="html"))
outputFile.close()

#unused codes
#print("=== before ===")
#print(soup.find("article", attrs={"class" : "style4"}).prettify())
#print("=== change ===")
#soup.find("article", attrs={"class" : "style4"}).find("h2").string.replace_with("NEW!!")
#print("=== after ===")
#print(soup.find("article").prettify())
#print(soup.body.header.div.a.find_all("span"))
#for tmpArticle in soup.find_all("article", attrs={"class" : "style4"}):
