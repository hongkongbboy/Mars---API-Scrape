import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from datetime import datetime

# Initialize browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

# NASA Mars News - functions to scrape for Mars (received errors here)
def scrape_news():
    news={}
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    div = soup.find('div', class_='content_title')
    news["news_headline"] = div.find('a').get_text()
    news["news_discription"] = soup.find('div', class_='article_teaser_body').get_text()

    return news

# JPL Mars Space Images - Featured Image
    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA22456_hires.jpg'

# Mars Weather
def scrape_weather():

    weather = {}
    tweeter_url = 'https://twitter.com/marswxreport?lang=en'
    browser = init_browser()
    browser.visit(tweeter_url)
    weather_html = browser.html
    weather_soup = BeautifulSoup(weather_html, 'html.parser')
    weather_twitter = weather_soup.find('li', class_='js-stream-item')
    weather["news_weather"] = weather_twitter.find('p', class_='tweet-text').get_text()

    return weather

# Mars Facts
def scrape_facts():

    fact_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(fact_url)
    df = tables[0]
    df.columns = ['description', 'value']
    df.set_index('description', inplace=True)
    html_table = df.to_html()
    html_table.replace('\n', '')
    facts = {
        "mars_facts": html_table
    }

    return facts

#Mars Hemisperes
def scrape_hemisperes():

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"}
    ]

    hemispere = {
        "hemisperes": hemisphere_image_urls
    }

    return hemispere