# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='css_content_detail']/h1",
    'price' : "//div[@class='price_detail']/span[@class='price_pr']",
    'category' : "",
    'description' : "//div[@class='box_info __MB_CONTAINER_READ3 __MB_CONTAINER_READ3_1 in-content']",
    'images' : "//div[@class='item large-image']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'misafashion.com'
allowed_domains = ['misafashion.com']
start_urls = ['http://misafashion.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?page=\d+$)']), 'parse_item_and_links'),
]
