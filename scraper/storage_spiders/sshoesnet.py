# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title']/h1",
    'price' : "//div[@class='product-price']/span",
    'category' : "//ol[@class='breadcrumb breadcrumb-arrow hidden-sm hidden-xs']/li/a",
    'description' : "//div[@class='product-comment']/div[@id='mota']",
    'images' : "//img[@class=' product-image-feature']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 's-shoes.net'
allowed_domains = ['s-shoes.net']
start_urls = ['http://s-shoes.net/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/products/[a-zA-Z0-9-]+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/collections/'], deny=['/products/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
