
import requests
import re
import datetime
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return"error"
#print(getHtmlText(url)[1:50])

def parsePage(ilt,html):
    
     



def printInfo():
    ""




def main():
    start_url='https://www.bilibili.com/list/rank-22.html#!range'
    time_start='2014-01-01'
    time1=datetime.datetime.strptime(time_start,'%Y-%m-%d')
    delta=datetime.timedelta(days=60)
    time2=(time1+delta).strftime('%Y-%m-%d')

    date=time1+'%2C'+time2
    url=start_url+date


    html=getHtmlText(url)
    parsePage()


    printInfo()



main()
    
    
        
        
    
    =2014-01-01%2C2014-04-01'
