import requests
from bs4 import BeautifulSoup as BS
url="https://www.ptt.cc"
count = 10
def ptt(queryLink,count): 
    if(count>0):
        rs = requests.session()
        res = rs.get(queryLink)
        soup = BS(res.text)
        title = []
        pageLink= []
        date = []
        rateing = []
        author = []
        
        pageup_link = "https://www.ptt.cc"+soup.find_all("a","btn wide")[1].get("href")
        
        for item in soup.select(".r-ent"):
            try:
                if "刪除".decode('utf-8') not in item.select(".title")[0].text:
                    block={}
                    block = {"title": item.select(".title")[0].text,"push": item.select(".nrec")[0].text,"date": item.select(".date")[0].text,"author": item.select(".author")[0].text,"link": "https://www.ptt.cc"+item.select("a")[0].get("href")}
#                    if "雙鴻".decode('utf-8') in block["title"] or "2836" in block["title"]:
                    if "1/19" in block["date"]:
                        print block["push"],block["date"],block["title"],block["author"],block["link"]
                    count = count-1
                    if(count>=1):
                        ptt(pageup_link,count)
            except IndexError:
                print item
                   
data ={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}

#rs.post("https://www.ptt.cc/ask/over18",verify=False,data=data)
#res = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html", verify=False)
dashboard="/bbs/stock/index.html"
queryLink=url+dashboard
ptt(queryLink,count)
