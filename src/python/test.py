import requests
import bs4

dic = dict()
req = requests.get("http://quotes.toscrape.com/")
print(str(req.text))
soupdata = bs4.BeautifulSoup(req.text, features="html.parser")
print(str(soupdata))
print(str(soupdata.title.text))
divs = soupdata.findAll("div",{"class":"quote"})
print(str(divs))

for i in range(len(divs)):
    text = divs[i].find("span",{"class":"text"}).text
    print(text)
    author = divs[i].find("small", {"class":"author"}).text
    print(author)
    dic[f"quote{i}"] = {"quote":text,"author":author}

print(dic)