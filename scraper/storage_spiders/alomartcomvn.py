# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h2",
    'price' : "//p[@class='special-price1']/span[@class='price']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='tab-content']/div[@class='std']",
    'images' : "//div[@class='product-img-box']//ul/li/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'alomart.com.vn'
allowed_domains = ['alomart.com.vn']
start_urls = ['http://alomart.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danhmuc/\d+-[a-zA-Z0-9-]+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
