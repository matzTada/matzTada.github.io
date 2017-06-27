#htmlChanger.py for index.html of matztada.github.io

#variables
inFileName = "../index_seed.html"
outFileName = "../index.html"
colorArray = []
colorArrayItr = 0

#initialize colorArray
colorArray = ["style1", "style2", "style3", "style4", "style5", "style6", "style7"] #values in colorArray must suit style in css
#colorArray = ["style1", "style2"] #values in colorArray must suit style in css

#read from file
import codecs
f = codecs.open(inFileName, "r")
html = f.read()

#using BeautifulSoup to handle html files
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

#changing each article based on color array
for tmpArticle in soup.find_all("article"): 
    print(tmpArticle.find("h2").string + " : " + tmpArticle["class"][0].encode())
    if not tmpArticle["class"][0] == "style0":
        tmpArticle["class"][0] = colorArray[colorArrayItr]
        colorArrayItr += 1
        if(colorArrayItr >= len(colorArray)):
            colorArrayItr = 0
    
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
