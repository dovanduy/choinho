# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pd-name']/h1",
    'price' : "//div[@class='product-description']/div[@class='sub1']",
    'category' : "//div[@class='lead_sub']/a",
    'description' : "//div[@class='pcdetails']/div/div[@id='tab1']",
    'images' : "//div[@class='thumb-view']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'trungmobile.com.vn'
allowed_domains = ['trungmobile.com.vn']
start_urls = ['http://trungmobile.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/category/'], deny=['filter=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
