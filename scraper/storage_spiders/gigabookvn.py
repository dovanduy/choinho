# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product_info']/h2",
    'price' : "//div[@class='product_info']/div/div/span[@class='font_price']",
    'category' : "//div[@class='fullpage']/div[@class='bg_nav']/a",
    'description' : "//div[@class='intro']/div/p[2]",
    'images' : "//div[@class='fullpage']/div/div/img[@id='ContentPlaceHolder1_imgProduct']/@src | //div[@id='main1']/div[@class='fullpage']/div/div/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'gigabook.vn'
allowed_domains = ['gigabook.vn']
start_urls = ['http://gigabook.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/product+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/products/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
