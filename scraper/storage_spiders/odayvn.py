# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_form_oder']/h3",
    'price' : "//h5[@class='price']",
    'category' : "//div[@class='product_form_oder']/p[3]",
    'description' : "//div[@class='full-des']/div[@class='content']",
    'images' : "//div[@id='gallery']/ul/li/a/img/@src | //div[@class='product_images']/div[@class='main_image']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'oday.vn'
allowed_domains = ['oday.vn']
start_urls = ['http://www.oday.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+-detail+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
