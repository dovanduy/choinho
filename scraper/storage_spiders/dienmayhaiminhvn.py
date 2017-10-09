# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='span6 product-shop']/h1",
    'price' : "//div[@class='span6 product-shop']/div[@class='price1']/text()|//div[@class='price1']/span[@class='price-new']",
    'category' : "//div[@class='breadcrumb']/a",
    'description' : "//div[@class='wrap-tabs']/div[@class='tab-content']",
    'images' : "//img[@class='product-image-zoom']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dienmayhaiminh.vn'
allowed_domains = ['dienmayhaiminh.vn']
start_urls = ['http://dienmayhaiminh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/.+($|\?page=\d+$)'], deny=['index\.php']), 'parse_item_and_links'),
]
