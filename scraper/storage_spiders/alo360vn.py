# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-name']/h1",
    'price' : "//div[@class='detail_P01_price']//span[@class='price']",
    'category' : "//div[@class='breadcrumbs breadcrumb_url']/div/a/span",
    'description' : "//div[@class='detail_description']//div[@class='std']",
    'images' : "//div[@class='item']/img[@class='gallery-image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'alo360.vn'
allowed_domains = ['alo360.vn']
start_urls = ['http://www.alo360.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+($|\?p=\d+#cate)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
