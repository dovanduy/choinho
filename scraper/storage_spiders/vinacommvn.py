# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-detail']/div[@class='info float-right']/ul/li/h1",
    'price' : "//div[@class='product-detail']/div[@class='info float-right']/ul/li/span[@class='price']",
    'category' : "//div[@class='breadcrumb']/itemscope/a/span",
    'description' : "//div[@class='product-detail']/div[@class='specs']",
    'images' : "//a[@rel='productphoto']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'vinacomm.vn'
allowed_domains = ['vinacomm.vn']
start_urls = ['http://www.vinacomm.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-]+-p+\d+\.vnc']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/[a-zA-Z0-9-]+/+\d+\.vnc'], deny=['to=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
