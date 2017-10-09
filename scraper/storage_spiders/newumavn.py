# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-function']/h3[@class='product-function']|//div[@class='product-name']/h2[@class='text-uppercase']/strong",
    'price' : "//div[@class='price-info group']/div/span/span[@class='price']",
    'category' : "//ul[@class='breadcrumb']/li/a",
    'description' : "//div[@class='short-description group']/div[@class='value']",
    'images' : "//img[@class='gallery-image visible']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'new.uma.vn'
allowed_domains = ['new.uma.vn']
start_urls = ['https://new.uma.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html'], deny=['-\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]