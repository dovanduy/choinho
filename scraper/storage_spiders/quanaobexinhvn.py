# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@id='title-page']",
    'price' : "//div[@class='price']/span[@class='price-new']",
    'category' : "//div[@class='clearfix']/ul/li/a",
    'description' : "//div[@id='tab-description']",
    'images' : "//img[@id='image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'quanaobexinh.vn'
allowed_domains = ['quanaobexinh.vn']
start_urls = ['http://quanaobexinh.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['product_id']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+'], deny=['product_id','\.html','tin-tuc','contact']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
