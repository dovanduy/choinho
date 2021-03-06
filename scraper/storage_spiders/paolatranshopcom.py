# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/div[@id='wrapper']/div[@id='body']/div[@id='bg_content']/div[@id='content']/div[@class='content_main']/div[@id='main']/div[@id='category_product']/div[@class='main']/ul[@class='products']/div[@id='product_detail']/h2[@class='title']",
    'price' : "/html/body/div[@id='wrapper']/div[@id='body']/div[@id='bg_content']/div[@id='content']/div[@class='content_main']/div[@id='main']/div[@id='category_product']/div[@class='main']/ul[@class='products']/div[@id='product_detail']/p/span",
    'category' : "/html/body/div[@id='wrapper']/div[@id='body']/div[@id='bg_content']/div[@id='content']/div[@class='content_main']/div[@id='main']/div[@id='category_product']/div[@class='head']/h2[@class='header']/a",
    'description' : "/html/body/div[@id='wrapper']/div[@id='body']/div[@id='bg_content']/div[@id='content']/div[@class='content_main']/div[@id='main']/div[@id='category_product']/div[@class='main']/ul[@class='products']/div[@id='product_detail']/div[@class='content']/p",
    'images' : "/html/body/div[@id='wrapper']/div[@id='body']/div[@id='bg_content']/div[@id='content']/div[@class='content_main']/div[@id='main']/div[@id='category_product']/div[@class='main']/ul[@class='products']/div[@id='product_detail']/div[@class='img']/a[@class='lightbox']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'paolatranshop.com'
allowed_domains = ['paolatranshop.com']
start_urls = ['http://paolatranshop.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/p+\d+[a-zA-Z0-9-_]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
