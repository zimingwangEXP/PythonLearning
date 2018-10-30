import requests
import urllib3
import time
from bs4 import BeautifulSoup as  bs
import operator
class VariFlight:
#Hear为对应web服务器的URL地址
 Header="http://www.variflight.com";
#RawHeader为原始web地址，从这个页面获取所有的航班的详细链接将其存入UrlList中用于爬取
 RawUrl="http://www.variflight.com/sitemap.html?AE71649A58c77=";
#urllib3获取爬虫
 connection = urllib3.PoolManager();
#数据列表，二维列表，存每个航班的相关信息
 DataList=[];
 UrlList=[];
#设置RawUrl的成员函数
 def SetUrl(self,url):
     self.RawUrl=url;
#获取URLList的私有成员方法
 def __GetUrlList(self):
     #从RawURL使用get方法发起请求,获得response对象
     response=self.connection.request("get",self.RawUrl);
     #根据response对象生成相应的html过滤器
     filt=bs(response.data,"html.parser")
     #在文档书上查找所有tag名为a的节点
     list=filt.find_all(name="a")
     for one in list:
         #根据对应page源代码特点，过滤掉不属于航班编号的节点#存取所有的航班的详细介绍的URL地址

        if(len(one.text)>0 and '9'>=one.text[len(one.text)-1]>='0'):
            # print(one.text) 输出调试
            #将航班对应完整的URL加入URLList
            self.UrlList.append(self.Header+one.get("href"));
#Graph转为文本，暂时没有实现
 def __Graph2Text(self,work):
     return "test";
#核心爬取
 def Spider(self):
     #先获取要爬取的URL列表
     #self.__GetUrlList();
     self.UrlList=["http://www.variflight.com/flight/fnum/3U5034.html?AE71649A58c77="]
     for one in self.UrlList:
         #隔1s爬一次，以防被封IP（或使用ip代理）
         time.sleep(4);
         #对相关页面发起请求
         response=self.connection.request("get",one);
         #生成过滤器
         filt=bs(response.data,"html.parser");
         #print(response.data);
         #先过滤出主要的信息区块
         list=filt.find(class_="li_com");
         if(list is None or len(list)==0):
             print("*************")
             continue;
         #存每个页面爬到的数据
         cur=[];
         #记录图片个数
         cnt=0;
         #更精确的数据筛选
         for one in list.children:
           print(one)
           try:
            #第一层筛选
            if(one.name=='span'):
                #print(one)
                #对非图像信息的处理
                if(not one.img):
                    #处理结构中嵌套循环的部分
                    if(operator.eq(one["class"],['w260'])):
                        cur.extend([i.string for i in one.b.children if i.string!='\n'])
                    else:
                        #处理单节点的信息
                        tmp=str(one.string)
                        #替换无效字符
                        tmp=tmp.replace("\t","")
                        tmp = tmp.replace("\n", "")
                        tmp = tmp.replace("\r", "")
                        cur.append(tmp)
                else:
                    print("occur_occur_occur\n")
                    #获取图片地址
                    addr=self.Header+one.img['src'];
                    print(addr)
                    #计数
                    cnt+=1;
                    #图片存储地址
                    path='./picture/'+str(cnt)+ '.png';
                    #下载图片
                    r=requests.get(addr);
                    with open(path, 'wb') as f:
                        f.write(r.content)
                    #图片处理存在问题
                    cur.append("暂未确定")
                    # c = pytesseract.image_to_string(Image.open(path))
                    # print(c)
                    # if len(c) < 5:  # 若识别不出‘:’或者‘.’ 进行拼接
                    #     c = c[:2] + ':' + c[2:]
                    # print(pytesseract.image_to_string(, lang='chi_sim'));
           except Exception:#异常处理
               print("存在URL无效\n")
               continue;
         print(cur);#输出调试
         #记录数据
         self.DataList.append(cur)
#将相关数据以文本文件的方式存储
 def Save(self):
     out=open("data.txt","w");
     for one in self.DataList:
        out.writelines(" ".join(one));

#主函数
#新建VariFlight对象
a=VariFlight();
#开始爬取工作
a.Spider();
#存储文件
a.Save();

