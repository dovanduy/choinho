# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='gallery']/div[@id='gallery_output']/a/img[@id='view_img_first']/@alt",
    'price' : "//div[@id='detail']/div[@class='option']/p[@class='price']/span",
    'category' : "//div[@class='content_middle']/ul[@id='breadcrumbs']/li/a",
    'description' : "//div[@id='tab1']/div/div/p",
    'images' : "//div[@id='gallery']/div[@id='gallery_output']/a/img[@id='view_img_first']/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dungcubepgiangtrinh.com'
allowed_domains = ['dungcubepgiangtrinh.com']
start_urls = ['http://dungcubepgiangtrinh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+$','/trang+_\d+$'], deny=['\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]