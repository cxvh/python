'''
Created on 2020年1月20日

@author: Baran
'''

import urllib.request


class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None

        response=urllib.request.urlopen(url)
        
        if response.getcode()!=200:
            return None
        return response.read()
    



