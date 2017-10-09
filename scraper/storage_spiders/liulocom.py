# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='product_detail_name']",
    'price' : "//table[@class='product_info']/tbody/tr[@class='price_detail']/td[@class='price']/span",
    'category' : "//p[@class='breadcumb']/span/a",
    'description' : "//div[@class='product_detail_Hi']",
    'images' : "//div[@class='product_img_big']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'liulo.com'
allowed_domains = ['liulo.com']
start_urls = ['http://liulo.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow = ['/[a-z0-9-]+_p\d+.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['/[a-z0-9-]+_[bc]\d+.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
