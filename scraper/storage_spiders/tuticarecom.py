# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='txt_center txt_pink']",
    'price' : "//div[@id='overview']/div[@class='Dprice']/p[@class='txt_pink txt_30 txt_b']",
    'category' : "//div[@id='breadcrumb']/div/a/span",
    'description' : "//section[@id='content']/div[@id='tab-pro-info']/div[@class='content-tab-pro tab-cont']",
    'images' : "//div[@id='img-detail']/div[@class='one']/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'tuticare.com'
allowed_domains = ['tuticare.com']
start_urls = ['http://www.tuticare.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-item\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html($|\?p=\d+$)'], deny=['order_by=','\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]