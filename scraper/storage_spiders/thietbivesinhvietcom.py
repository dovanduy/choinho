# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='entry-title']",
    'price' : "//div[@class='detail-product-all']/ul/li[@class='price']/span",
    'category' : "//div[@id='wrap']/div[@class='breadcrumb']/div[@class='wrap']/a",
    'description' : "//div[@class='entry-content']",
    'images' : "//div[@class='images-product-single']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thietbivesinhviet.com'
allowed_domains = ['thietbivesinhviet.com']
start_urls = ['http://thietbivesinhviet.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/[a-zA-Z0-9-]+/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+[/a-zA-Z-]+/$'], deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
