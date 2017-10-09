# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-content']/h1",
    'price' : "//p[@class='noidung']/span[@class='ogrcolor']",
    'category' : "//div[@class='breadcrumb']/div[@class='breadcrumbs']/a",
    'description' : "//div[@class='block products-tab']/div[@id='prodtab1']",
    'images' : "//div[@class='product-img']/img[@class='zoomz pdtail']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'tragop.com'
allowed_domains = ['tragop.com']
start_urls = ['http://www.tragop.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+/','page=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
