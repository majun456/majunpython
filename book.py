import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text  
    except:
        return ""
 
def getBookSite(lst,bookURL):
    html = getHTMLText(bookURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href =i.attrs['href']
            #href1=i.get_attribute('href')
            #print(href)
            url1=re.findall(r"http://product.china-pub.com/\d{6}", href)[0]
            if url1 in lst:
                continue
            else:
                lst.append(url1)
                print(url1)
                #print(lst)
        except:
            continue
 
def getBookInfo(lst,fpath):
    for bookSite in lst:
        url = bookSite
        html = getHTMLText(url)
        try:
            if (html==""):
                print("dhvd")
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            bookInfo = soup.find('meta',attrs={'name':'keywords'})
            #print(bookInfo.attrs['content'])
            p=re.compile('所属分类')
            for elem in  soup (text=p):
                title=elem.parent.parent
            #title=soup(text=p)[0].parent.parent
            p1=re.compile('通信技术')
            category = title.find_all('a')[0]

            #category=title.find_all('a', attrs={'class':'blue13'})[0]
            #print(category)
            if(category.text.split()[0]=="通信技术"):
                infoDict.update({bookInfo.attrs['content']:category.text.split()[0]})
            #print(category.text.split()[0])
                with open(fpath, 'a', encoding='utf-8') as f:
                    f.write( str(infoDict) + '\n' )
                
        except:
            traceback.print_exc()
            continue
 
def main():
    output_file = 'D:/BaiduStockInfomath1.txt'
    list=[]
    book_started_url='http://search.china-pub.com/s/?key1=%cc%d8%bc%db%ca%e9&type=&pz=1&t=2&ts=2&zks=0.3&zke=0.5&page='
    length=100
    for i in range(length):
        try:
            url = book_started_url+str(i+1)

            getBookSite(list, url)
        except:
             continue
    getBookInfo(list,output_file)
 
main()
