# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='content']/div/div[@class='info']/h1",
    'price' : "//div[@class='info']/p[@class='price']",
    'category' : "//h3[@class='title_h3']/a",
    'description' : "//div[@class='content']/div/div[@class='clearfix']/div/div",
    'images' : "//div[@class='image-product']/p/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'royalebaby.com'
allowed_domains = ['royalebaby.com']
start_urls = ['http://royalebaby.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['id=+\d+$']), 'parse_item'),
    Rule(LinkExtractor(allow = ['cate=+\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]