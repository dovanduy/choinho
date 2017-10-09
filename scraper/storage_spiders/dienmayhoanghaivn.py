# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@class='details-info']/h1",
    'price' : "//div[@class='info']/div[@class='right']/span[@class='price']",
    'category' : "//div[@id='content']/ul[@id='crumbs']/li/a",
    'description' : "//div[@id='info-product']/div[@class='detail-content']",
    'images' : "//div[@id='detail_product_picture_main']/h1/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienmayhoanghai.vn'
allowed_domains = ['dienmayhoanghai.vn']
start_urls = ['http://dienmayhoanghai.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\d+.*\.aspx']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.aspx']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
