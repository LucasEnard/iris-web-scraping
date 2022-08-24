from grongier.pex import BusinessOperation
import iris
from msg import ScrapRequest,ScrapResponse,InspectRequest,InspectResponse

import requests
import bs4

class ScrapingOperation(BusinessOperation):

    def on_init(self):
        pass

    def on_message(self,request):
        return request

    def on_scrap_request(self,request:ScrapRequest):
        dic = dict()

        req = requests.get(request.url)
        soupdata = bs4.BeautifulSoup(req.text, features="html.parser")

        divs = soupdata.findAll("div",{"class":"quote"})
        for i in range(len(divs)):
            text = divs[i].find("span",{"class":"text"}).text
            author = divs[i].find("small", {"class":"author"}).text
            dic[f"quote{i}"] = {"quote":text,"author":author}
        return ScrapResponse(dic)

    def on_inspect_request(self,request:InspectRequest):

        req = requests.get(request.url)
        soupdata = bs4.BeautifulSoup(req.text, features="html.parser")
        return InspectResponse(str(soupdata))
