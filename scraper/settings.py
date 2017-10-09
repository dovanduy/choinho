# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 AlexaToolbar/alxg-3.1'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'
USER_AGENT = '%s' % BOT_NAME
ITEM_PIPELINES = {'scraper.pipelines.SavingPipeline': 1}
EXTENSIONS = {
    'extension.ExtensionThatAccessStats': 500,
}

DOWNLOAD_DELAY = 2.0
CONCURRENT_REQUESTS = 1
DOWNLOADER_CLIENTCONTEXTFACTORY = 'scraper.contextfactory.TLSFlexibleContextFactory'

# Config cache images
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
IMAGES_STORE = "s3://bucket/images/"
# IMAGES_STORE = "/extra/data/images"
IMAGES_THUMBS = {
    'small': (50, 50),
    'normal': (180, 180),
    'big': (270, 270)
}

CRAWL_SERVER_ID	= 1
MONGODB_SERVER 	= 'localhost'
MONGODB_PORT	= 27017
MONGODB_DB		= 'crawler' 
#DEPTH_LIMIT = 5
LOG_LEVEL = 'INFO'


