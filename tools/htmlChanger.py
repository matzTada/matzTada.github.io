#htmlChanger.py for index.html of matztada.github.io

# -*- coding: utf-8 -*-

#variables
inFileName = "../index_seed.html"
outFileName = "../index.html"

#initialize colorArray
colorArray = ["style1", "style2", "style3", "style4", "style5", "style6", "style7"] #values in colorArray must suit style in css
#colorArray = ["style1", "style2"] #values in colorArray must suit style in css
colorArrayItr = 0

#===append or modify artcile
#read from file
import codecs
f = codecs.open(inFileName, "r")
html = f.read()
#using BeautifulSoup to handle html files
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
#append or modify new article. commet this section usually
from tagMaker import writeArticle, modifyArticle
editMode = "modify" # ---clear BE SUPER CAREFULL!!
title = "matztada github website"
img_src = "" #image from youtube "http://img.youtube.com/vi/YOUTUBE_MOVIE_ID_HERE/0.jpg" #image from github "https://raw.githubusercontent.com/matzTada/PROJECT_NAME/BRANCH_NAME/PATH_OF_IMAGE"
img_alt = ""
link = "" #github.io page "http://matztada.github.io/"
sentence = "Linked"
style = "style" #style0 for gray window
if editMode == "append":
    returnPageElement = writeArticle(title, img_src, img_alt, link, sentence, style)
    print returnPageElement.prettify()
    soup.find("section", attrs={"class" : "tiles"}).append(returnPageElement)
elif editMode == "modify":
    for tmpArticle in soup.find_all("article"):
        if tmpArticle.find("h2").string.encode().strip() == title:
            modifyArticle(tmpArticle, title, img_src, img_alt, link, sentence, style)
            print "find the article!!"
            print tmpArticle.prettify()
            break
    else:
        print "cannot find the article."
elif editMode == "clear":
    for tmpArticle in soup.find_all("article"):
        if tmpArticle.find("h2").string.encode().strip() == title:
            tmpArticle.replace_with("")
inputFile = open(inFileName, "w")
inputFile.write(soup.prettify(formatter="html"))
inputFile.close()

#=== color change
#read from file
import codecs
f = codecs.open(inFileName, "r")
html = f.read()
#using BeautifulSoup to handle html files
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
#changing each article based on color array
for tmpArticle in soup.find_all("article"):
    # print "--- an article ---"
    # print "title   : " + tmpArticle.find("h2").string.encode()
    # print "style   : " + tmpArticle["class"][0].encode()
    # print "image   : " + tmpArticle.find("span", attrs={"class" : "image"}).find("img")["src"].encode()
    # print "link    : " + tmpArticle.find("a")["href"].encode()
    # print "content : " + tmpArticle.find("div", attrs={"class" : "content"}).find("p").string.encode()    

    if len(tmpArticle["class"][0]) > 0 and tmpArticle["class"][0] != "style0":
        tmpArticle["class"][0] = colorArray[colorArrayItr]
        colorArrayItr += 1
        if(colorArrayItr >= len(colorArray)):
            colorArrayItr = 0
    else:
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
