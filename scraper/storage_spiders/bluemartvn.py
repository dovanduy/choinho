# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='detail-top']/h2[@class='title-product']",
    'price' : "//div[@class='pull-left']/div[@class='price']",
    'category' : "//div[@class='site-location']/a",
    'description' : "//div[@class='detail-info']/table[@class='specifications']",
    'images' : "//div[@class='zoom-image-box clearfix']/ul[@id='imageZoom']/li/div/img/@src | //img[@class='etalage_thumb_image']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bluemart.vn'
allowed_domains = ['bluemart.vn']
start_urls = ['http://bluemart.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['-p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['-c+\d+\.html'], deny=['by=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
