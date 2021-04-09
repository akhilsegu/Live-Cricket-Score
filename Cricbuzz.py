#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import time
url="https://www.cricbuzz.com/live-cricket-scores/35612/mi-vs-rcb-1st-match-indian-premier-league-2021"
while True:
    time.sleep(20)
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    score_card=soup.find('div',class_='cb-col cb-col-67 cb-scrs-wrp').span.text
    print("current score is \n {} ".format(score_card))

