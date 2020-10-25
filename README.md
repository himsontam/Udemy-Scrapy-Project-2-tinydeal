# UdemyScrapyCourse-Project1-tinydeal

This is a Udemy tutorial to learn Scrapy. Modern Web Scraping with Python using Scrapy Splash Selenium

Link to scrapy: https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html

Scrapy command:
run scrapy script -----> scrapy crawl special_offers

run scrapy shell ------> scrapy shell

Create New Scrpay Project -------> scrapy startproject tinydeal

You can start your first spider with:

cd worldometers
scrapy genspider example example.com
Create Scrapy spider -------> scrapy genspider special_offers https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html

Export Excel Command -----> scrapy crawl countries -o special_offers_dataset.csv

Anaconda command:
install dependencies ----> conda install -c conda-forge scrapy==1.6 pylint autopep8 -y
install iPython ---------> conda install iPython
