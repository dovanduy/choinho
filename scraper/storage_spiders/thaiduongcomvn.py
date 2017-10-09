# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='productDetails']/div[@class='width50 floatright']/h1",
    'price' : "//div[@class='PricesalesPrice']/span[@class='PricesalesPrice']",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@class='product-description']/div[@class='current']/dd[@class='tabs'][1]",
    'images' : "//div[@class='main-image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thaiduong.com.vn'
allowed_domains = ['thaiduong.com.vn']
start_urls = ['http://www.thaiduong.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-chi-tiet+$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
