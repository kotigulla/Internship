#!/usr/bin/env python
# coding: utf-8

# ### (1) Write a python program to display all the header tags from wikipedia.org.

# In[14]:


import  requests
from  bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[15]:


soup=BeautifulSoup(page.content)
soup


# In[17]:


header_tags=[]
for i in soup.find_all('li',class_="mw-list-item"):
    header_tags.append(i.text)
header_tags


# ### (2)  IMDB’s Top rated 100 movies’ data 

# In[2]:


import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://www.imdb.com/chart/top/')
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[10]:


movies=[] #empty list for the store
for i in soup.find_all('td', class_="titleColumn"):
    movies.append(i.text.replace('\n', ""))
movies


# In[11]:


ratings=[] 
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    ratings.append(i.text.replace('\n', ""))
ratings


# In[12]:


years=[] 
for i in soup.find_all('span',class_="secondaryInfo"):
    years.append(i.text.replace('\n', ""))
years


# In[13]:


df=pd.DataFrame({'Movie':movies,'Rating':ratings,'Year':years})
df.head(100)


# ### (3) IMDB’s Top rated 100 Indian movies’ data

# In[34]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[35]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page


# In[36]:


soup=BeautifulSoup(page.content)
soup


# In[37]:


titles=[] 
for i in soup.find_all('td',class_="titleColumn"):
    titles.append(i.text.replace('\n',''))
titles


# In[38]:


ratings=[] #empty list for the store
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    ratings.append(i.text.replace('\n',''))
ratings


# In[39]:


years=[] 
for i in soup.find_all('span',class_="secondaryInfo"):
    years.append(i.text.replace('\n',''))
years


# In[40]:


df=pd.DataFrame({'Title':titles,'Rating':ratings,'Year':years})
df.head(100)


# ### (4) meesho

# In[15]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[16]:


page=requests.get('https://meesho.com/bags-ladies/pl/p7vbp')
page


# In[17]:


soup=BeautifulSoup(page.content)
soup


# In[52]:


products=[] 
for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
    products.append(i.text)
products


# In[53]:


price=[] 
for i in soup.find_all('h5',class_="Text__StyledText-sc-oo0kvp-0 hiHdyy"):
    price.append(i.text.replace('₹',''))
price


# In[54]:


discount=[] 
for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 fCJVtz NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 kmYsnm NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 kmYsnm"):
    discount.append(i.text.replace('₹','').replace('discount on 1st order',''))
discount


# In[55]:


print(len(products),len(price),len(discount))


# In[56]:


df=pd.DataFrame({'Product':products,'Price':price,'Discount':discount})
df


# ### (5) Write a python program to scrape cricket rankings from icc-cricket.com.

# #### (a) Top 10 ODI teams in men’s cricket

# In[60]:


import  requests
from  bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page


# In[61]:


soup=BeautifulSoup(page.content)
soup


# In[108]:


teams=[] 
for i in soup.find_all('span',class_="u-hide-phablet"):
    teams.append(i.text)
teams


# In[113]:


teams.remove('')
teams


# In[114]:


matches=[] 
for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    matches.append(i.text)
matches


# In[115]:


ratings=[] 
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
ratings


# In[116]:


ratings.insert(0,'121')
ratings


# In[117]:


print(len(teams),len(ratings))


# In[99]:


df=pd.DataFrame({'Team':teams,'Rating':ratings})
df


# ### (7) scrape details of all the posts from coreyms.com.

# In[78]:


import  requests
from  bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://coreyms.com/')
page


# In[79]:


soup=BeautifulSoup(page.content)
soup


# In[80]:


headings=[] 
for i in soup.find_all('a',class_="entry-title-link"):
    headings.append(i.text)
headings


# In[81]:


dates=[] 
for i in soup.find_all('time',class_="entry-time"):
    dates.append(i.text)
dates


# In[82]:


content=[] 
for i in soup.find_all('div',class_="entry-content"):
    content.append(i.text.replace('\n',''))
content


# In[90]:


videos=[] 
for i in soup.find_all('iframe',class_="youtube-player"):
    videos.append(i)
videos


# ### (9)  scrape  details from dineout.co.in :

# In[35]:


import  requests
from  bs4 import BeautifulSoup
import pandas as pd
page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[36]:


soup=BeautifulSoup(page.content)
soup


# In[37]:


names=[] 
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    names.append(i.text)
names


# In[40]:


cuisine=[] 
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text)
cuisine


# In[41]:


locations=[] 
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    locations.append(i.text)
locations


# In[42]:


ratings=[] 
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)
ratings


# In[44]:


images=[] 
for i in soup.find_all('img',class_="no-img"):
    images.append(i)
images

