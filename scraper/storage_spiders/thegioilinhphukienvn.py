# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='padding']/h1",
    'price' : "//span[@class='price_km']/strong",
    'category' : "//div[@class='breadcrumb wrapper']/a",
    'description' : "//div[@class='tab_wrapper']/div[@class='tab_content entry']/ul[@class='product_option']|//div[@class='tab_wrapper']/div[@class='tab_content entry']/p",
    'images' : "//div[@class='imageDetail']/div[@class='slider-for']/div/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "//ul/li[2]/span/strong",
    'in_stock' : "//div[@class='inner']/div[@class='padding']/ul/li[4]/span",
    'guarantee' : "//div[@class='inner']/div[@class='padding']/ul/li[3]/span",
    'promotion' : ""
}
name = 'thegioilinhphukien.vn'
allowed_domains = ['thegioilinhphukien.vn']
start_urls = ['http://thegioilinhphukien.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html($|/p-\d+$)']), 'parse_item_and_links'),
]
