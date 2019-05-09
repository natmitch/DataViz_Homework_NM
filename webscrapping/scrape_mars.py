#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests
import lxml

def initBrowser():
    return Browser("chrome", headless=False)
# In[2]:
def scrape():
    mars_data={}
    mars_data["set1"]=set_1()
    mars_data["set2"]=set_2()
    mars_data["set3"]=set_3()
    mars_data["set4"]=set_4()
    mars_data["set5"]=set_5()
    return mars_data

def set_1():    

#nasa mars news
executable_path = {'executable_path': '/anaconda3/chromedriver'}
browser = Browser('chrome', headless=False)
url = ('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[3]:


print(soup.prettify())


# In[4]:


#jpl mars space images
things = soup.find_all('div', class_="slide")
for thing in things:
    content_title = thing.find('div', class_="content_title")
    content_title_inner = content_title.find('a').text
    rollover_description = thing.find('div', class_="rollover_description")
    rollover_description_inner = rollover_description.find('div', class_="rollover_description_inner").text
    print('____Next_____')
    print(content_title_inner)
    print(rollover_description_inner)


# In[5]:

return set1
def set_2():
url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[6]:


print(soup.prettify())


# In[7]:


images = soup.find_all('a', class_="fancybox")
print(images)


# In[8]:


pic_src = []
for image in images:
    pic = image['data-fancybox-href']
    pic_src.append(pic)
featured_image_url = 'https://www.jpl.nasa.gov' + pic
featured_image_url


# In[9]:
return def2
def set_3():

#twitter
url = ('https://twitter.com/marswxreport?lang=en')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[10]:


print(soup.prettify())


# In[11]:


tweets = soup.find_all("div",class_="content")
print(tweets)


# In[12]:


mars_weather = []
for twit in tweets:
    tweet = twit.find("div", class_="js-tweet-text-container").text
    mars_weather.append(tweet)
print(mars_weather)


# In[13]:
return set3
def set_4():


#factx
mpp = pd.read_html("https://space-facts.com/mars/")
mpp = pd.DataFrame(["demention", "measure"])


# In[14]:


fact = mpp.to_html()
fact = fact.replace("\n","")
fact


# In[15]:
return set4
def set_5():

url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[16]:


print(soup.prettify())


# In[17]:


cerberus = soup.find_all('div', class_="wide-image-wrapper")
print(cerberus)


# In[18]:


for cerberu in cerberus:
    who = cerberu.find('li')
    wut = who.find('a')['href']
    print(wut)
cerberusf = soup.find('h2', class_='title').text
print(cerberusf)
cerbs = {"Title": cerberusf, "url": wut}
print(cerbs)


# In[19]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[20]:


print(soup.prettify())


# In[21]:


schiaparelli = soup.find_all('div', class_="wide-image-wrapper")
print(schiaparelli)


# In[22]:


for schiaparell in schiaparelli:
    who = schiaparell.find('li')
    wut = who.find('a')['href']
    print(wut)
shiaparellif = soup.find('h2', class_='title').text
print(shiaparellif)
sherps = {"Title": shiaparellif, "url": wut}
print(sherps)


# In[23]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[24]:


print(soup.prettify())


# In[25]:


Syrtis = soup.find_all('div', class_="wide-image-wrapper")
print(Syrtis)


# In[26]:


for Syrti in Syrtis:
    who = Syrti.find('li')
    wut = who.find('a')['href']
    print(wut)
Syrtisf = soup.find('h2', class_='title').text
print(Syrtisf)
Syr = {"Title": Syrtisf, "url": wut}
print(Syr)


# In[27]:


url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[28]:


valles = soup.find_all('div', class_="wide-image-wrapper")
print(valles)


# In[29]:


for valle in valles:
    who = valle.find('li')
    wut = who.find('a')['href']
    print(wut)
vallesf = soup.find('h2', class_='title').text
print(vallesf)
valley = {"Title": vallesf, "url": wut}
print(valley)


# In[ ]:


return set5
if __name__=="__main__":
    print(scrape())

