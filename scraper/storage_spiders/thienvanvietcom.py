# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='info_product']/h1",
    'price' : "//div[@class='info_product']/span[@class='money']",
    'category' : "//div[@id='ja-content-top']/span/a/span",
    'description' : "//div[@class='TabView']/div[@class='Pages']/div[@class='Page'][1]",
    'images' : "//div[@class='product_detail_image']/div[@id='slides']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "//div[@class='info_product']/p[5]/span/b",
    'guarantee' : "",
    'promotion' : ""
}
name = 'thienvanviet.com'
allowed_domains = ['thienvanviet.com']
start_urls = ['http://www.thienvanviet.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-p\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-c\d+s0r0(t\d+)*\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
