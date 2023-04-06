from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import pymongo
import time
from datetime import date
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pymongo
import calendar
import time
import time
from datetime import datetime, timedelta
from driverpath import torPath
from startDisplay import *

client=pymongo.MongoClient("mongodb+srv://emseccomandcenter:TUXnEN09VNM1drh3@cluster0.psiqanw.mongodb.net/?retryWrites=true&w=majority")
db=client['rohan        ']
collection=db['dread']

start_xvfb()
with TorBrowserDriver(torPath) as driver:
    driver.get('http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion')
    time.sleep(80)
        
        
    Link=[]
    for i in range(1,1000):
        driver.get(f'http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion/d/all?p={i}')
        
        link=driver.find_elements(By.XPATH," /html/body/div/div/div/div/div/a")
        for l in link:
            Link.append(l.get_attribute('href'))


    for lnk in Link:
        try:
            driver.get(lnk)
        except:
            pass
        time.sleep(0.44)


        try:
            title=driver.find_element(By.CLASS_NAME,'title')
            title=title.text
        except:
            title='not found'        

        allPosts=[]
        if title!='not found' :
            while True:
                data=driver.find_elements(By.CSS_SELECTOR,"div.postBoard.viewPost")

                for d in data:
                    temp=''
                    imgsrc=''
                    try:
                        author_name= d.find_element(By.CSS_SELECTOR,".author > a")
                        author_name=author_name.text
                    except:
                        author_name='not found' 
                    
                    try:        
                        profile_link= d.find_element(By.CSS_SELECTOR,".author > a")
                        author_profile_link=profile_link.get_attribute('href')
                    except:
                        author_profile_link='not available'
                        
                        
                    try:
                        post_time=d.find_element(By.CSS_SELECTOR,".author > span")
                        postTime=post_time.text
                        current_timeStamp=1678529576
                        s=postTime
                        if ('hour' in s) or ('hours' in s): 
                            times=3600
                        elif ('min' in s) or ('minutes' in s) or ('minute' in s): 
                            times=60
                        elif ('years' in s) or ('year' in s) : 
                            times=31560000
                        elif ('month' in s) or ('months' in s) : 
                            times=2630000 
                        elif ('day' in s) or ('days' in s) : 
                            times=86400
                        elif ('sec' in s) or ('second' in s) or ('seconds' in s): 
                            times=1
                        try:
                            integer=s.split()[0]
                            timeStamp=current_timeStamp-(int(integer)*times)
                        except:
                            current_GMT = time.gmtime()
                            ts = calendar.timegm(current_GMT)
                            timeStamp=ts
                    except:
                        timeStamp='not found'  
                    

                    try:
                        paras=d.find_elements(By.CSS_SELECTOR,"div.postContent")
                        for para in paras:
                            element_html=para.get_attribute('outerHTML')
                            para=BeautifulSoup(element_html,'html.parser')
                            try:
                                para
                            except:
                                pass
                            temp+=para.text+' '
                    except:
                        pass
                    if temp!="":
                            post={'author_name':author_name,'author_profile_link':author_profile_link,'date':postTime,'post':temp,'media_links':''}
                            allPosts.append(post)

                data=driver.find_elements(By.CSS_SELECTOR,"div.comment")

                for d in data:
                    temp=''
                    imgsrc=''
                    try:
                        author_name= d.find_element(By.CSS_SELECTOR,"div.commentContent> div>a")
                        author_name=author_name.text
                    except:
                        author_name='not found' 
                    
                    try:        
                        profile_link= d.find_element(By.CSS_SELECTOR,"div.commentContent> div>a")
                        author_profile_link=profile_link.get_attribute('href')
                    except:
                        author_profile_link='not available'
                    
                    try:
                        post_time=d.find_element(By.CSS_SELECTOR,"div.commentContent> div.top>div.timestamp>span")
                        postTime=post_time.text
                        current_timeStamp=1678529576
                        s=postTime
                        if ('hour' in s) or ('hours' in s): 
                            times=3600
                        elif ('min' in s) or ('minutes' in s) or ('minute' in s): 
                            times=60
                        elif ('years' in s) or ('year' in s) : 
                            times=31560000
                        elif ('month' in s) or ('months' in s) : 
                            times=2630000 
                        elif ('day' in s) or ('days' in s) : 
                            times=86400
                        elif ('sec' in s) or ('second' in s) or ('seconds' in s): 
                            times=1
                        try:
                            integer=s.split()[0]
                            timeStamp=current_timeStamp-(int(integer)*times)
                        except:
                            current_GMT = time.gmtime()
                            ts = calendar.timegm(current_GMT)
                            timeStamp=ts
                    except:
                        timeStamp='not found'  
                    

                    try:
                        paras=d.find_elements(By.CSS_SELECTOR,"div.commentContent> div.commentBody")
                        for para in paras:
                            element_html=para.get_attribute('outerHTML')
                            para=BeautifulSoup(element_html,'html.parser')
                            temp+=para.text+' '
                    except:
                        pass  
                    if temp!="":
                        post={'author_name':author_name,'author_profile_link':author_profile_link,'date':timeStamp,'post':temp,'media_links':''}
                        allPosts.append(post)
                    
                try:
                    next_btn=driver.find_element(By.CSS_SELECTOR,"a.pagination_next")    
                    next_btn.click()
                    time.sleep(0.44)
                except:
                    break
            if len(allPosts)>0 and title!='not found':
                try:
                    timestamp = allPosts[-1]['date']
                    date_time = datetime.fromtimestamp(int(timestamp))
                    d = date_time.strftime("%Y-%m-%dT%H:%M:%SZ")
                    lastModDate=d
                except:
                    current_GMT = time.gmtime()
                    ts = calendar.timegm(current_GMT)
                    lastModDate=ts
                
            if title  !='not found' and len(allPosts)>0 :  
                
                dct={'title':title,'url':lnk,'posts':allPosts,'lastModifiedDate':lastModDate}
                collection.insert_one(dct)
                print(dct)               

stop_xvfb()                