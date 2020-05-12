'''
Created on 2020年1月20日

@author: Baran
'''


class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)

    
    def output_html(self):
        fout=open('output.html','w',encoding='utf-8')
        fout.write('<html><style>p{width:90%;white-space: nowrap;text-overflow: ellipsis;overflow: hidden;}</style>')
        fout.write('<body>')
        
        fout.write('<table>')
        fout.write('<thead>')
        
        fout.write('<tr>')
        fout.write('<td width="20%">链接</td>')
        fout.write('<td width="20%">标题</td>')
        fout.write('<td width="60%">内容</td>')
        fout.write('</tr>')
        
        fout.write('</thead>')
        fout.write('<tbody>')
        #ascii
        for data in self.datas:
            fout.write('<tr>')
            
            fout.write('<td><p>%s</p></td>' % data['url'])
            
            tit=data['title']
            #try:
            #except:
            cont=data['cont']
            fout.write('<td><p>'+tit+'</p></td>')
            fout.write('<td><p>'+cont+'</p></td>')
            
            
            
            #fout.write('<td><p>%s</p></td>' % data['cont'].encode('utf-8'))
            fout.write('</tr>')
        
        fout.write('</tbody>')
        fout.write('</table>')
        
        fout.write('</body>')
        fout.write('</html>')
    
        fout.close()
    
    
    



