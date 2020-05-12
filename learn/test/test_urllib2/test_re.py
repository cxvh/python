'''
Created on 2020年1月21日

@author: Baran
'''
import re

arr=['/jquery/jquery_callback.asp','/jquery/jquery_call_back.asp']
pattern=re.compile(r"/jquery/\w+\.asp")
#pattern=re.compile(r"_")
for i in arr:
    print(pattern.match(i))
    #print(re.match('\w',i))


