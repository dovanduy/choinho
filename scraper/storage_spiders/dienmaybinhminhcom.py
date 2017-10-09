# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prod_title']/h1",
    'price' : "//td[@class='table-value']/span[@id='ctl00__contentPlaceHolderMain__ctrlProduct__labelPriceSaleOff']",
    'category' : "//ul[@class='ul-breadcrumbs']/li/a",
    'description' : "//div[@class='block block-tabs tab-left']/div[@class='block-inner']",
    'images' : "//div[@class='easyzoom easyzoom--with-thumbnails']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienmaybinhminh.com'
allowed_domains = ['dienmaybinhminh.com']
start_urls = ['http://dienmaybinhminh.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/($|\?page=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
