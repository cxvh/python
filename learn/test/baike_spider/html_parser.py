'''
Created on 2020年1月20日

@author: Baran
'''
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls=set()

        #https://baike.baidu.com/item/Python/407313
        #links=soup.find_all('a',href=re.compile(r"https://baike.baidu.com/item/"))

        #http://baike.baidu.com/view/23884.htm
        #links=soup.find_all('a',re.compile(r"/jquery/\w+\.asp"))

        #//www.chinaz.com/web/2019/1122/1066836.shtml


        links=soup.find_all('a',href=re.compile(r"//www.chinaz.com/web/\d+/\d+/\d+\.shtml"))
        for link in links:
            new_url=link['href']
            new_full_url=urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data['url']=page_url

        title_node=soup.find('div',class_="article-detail-hd").find('h2')

        res_data['title']=title_node.get_text()

        p_nodes=soup.find('div',id="ctrlfscont").find_all('p')
        cont_node=''
        for item in p_nodes:
            nt=item
            cont_node=cont_node+item.get_text()
        
        res_data['cont']=cont_node
        return res_data
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return 
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        
        return new_urls,new_data
    
    



