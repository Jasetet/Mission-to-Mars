#!/usr/bin/env python
# coding: utf-8

# In[86]:


#imports
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[87]:


# set up splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[88]:


#visit mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
#delay search
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[89]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[90]:


news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[91]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[92]:


# Visit URL
URL = 'https://spaceimages-mars.com'
browser.visit(URL)


# In[93]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[94]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[95]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[96]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[97]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[98]:


df.to_html()


# In[112]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[113]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for x in range(0,4):
    hemispheres = {}
    img_link = browser.links.find_by_partial_text('Hemisphere Enhanced')[x]
    img_link.click()
    
    html = browser.html
    img_soup = soup(html, 'html.parser')

    img_url = img_soup.find('img', class_='wide-image').get('src')
    full_img_url = url + hemi_url
    
    img_title = img_soup.find('h2', class_='title').text
    
    hemispheres['img_url']=full_img_url
    hemispheres['title']=img_title

    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[114]:


hemisphere_image_urls


# In[ ]:




