
import requests
from bs4 import BeautifulSoup as BS
url="https://www.ptt.cc"
count = 2
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
        
        for cdate in soup.select(".r-ent .date"):
            date.append(cdate.text)
        for ctitle in soup.select(".r-ent a"):
            title.append(ctitle.text)
        for cpageLink in soup.select(".r-ent a"):
            pageLink.append("https://www.ptt.cc"+cpageLink.get("href"))
        for crateing in soup.select(".r-ent .nrec"):
            rateing.append(crateing.text)
        for cauthor in soup.select(".r-ent .author"):
            #print cauthor
            author.append(cauthor.text)
        
        result = zip(rateing,date,title,author,pageLink)
        
        for item in result:
            print item[0],item[1],item[2],item[3],item[4]
        count = count-1
    if(count>=1):
        ptt(pageup_link,count)

dashboard="/bbs/stock/index.html"
queryLink=url+dashboard

ptt(queryLink,count)
