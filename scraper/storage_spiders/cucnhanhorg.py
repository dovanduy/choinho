# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='prd-details ']/div/div/h1/span",
    'price' : "//div[@class='ui-priceBox']/div/span[@class='prd-price']/span[@class='value']",
    'category' : "//div[@class='breadcrumb']/div/ul/li/a",
    'description' : "//section[@class='box  box-bgcolor']/div/div/div/div/div[@class='box-bd ui-tabViewContent']",
    'images' : "//div[@id='prdMedia']/div/a/span/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'cucnhanh.org'
allowed_domains = ['cucnhanh.org']
start_urls = ['http://cucnhanh.org']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
