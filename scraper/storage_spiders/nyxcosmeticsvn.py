# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pro_name_detail']",
    'price' : "//div[@class='pro_prices_detail']/div[@class='pro_price_sale']",
    'category' : "//span[@class='title_news']/a",
    'description' : "//div[1]/div[@class='pro_des']",
    'images' : "//a/img[@id='abc']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'nyxcosmetics.vn'
allowed_domains = ['nyxcosmetics.vn']
start_urls = ['http://nyxcosmetics.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/vn[a-zA-Z0-9-/]+\.html($|\?\?&page=\d+$)']), 'parse_item_and_links'),
]
