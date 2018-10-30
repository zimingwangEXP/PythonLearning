from bs4 import BeautifulSoup
import urllib3
def func(url):
 http=urllib3.PoolManager();
 ans=http.request("get",url);
 file=open("local.html","wb");
 file.write(ans.data);
 print("\n\n")
 soup=BeautifulSoup(ans.data,"html.parser")
 for one in soup.find_all("img"):
    a=one.get("title");
    if(a):print(a+"\n\n")
func("http://www.scuinfo.com/")