# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='navation']/text()[last()]|//h1[@class='p_name']",
    'price' : "//div[@class='text-info']/span[@class='price']/b",
    'category' : "//div[@class='navation']/a",
    'description' : "//div[@class='desc']/p",
    'images' : "//img[@class='etalage_thumb_image']/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'bolzano.com.vn'
allowed_domains = ['bolzano.com.vn']
start_urls = ['http://www.bolzano.com.vn/vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/vn/[a-zA-Z0-9-]+/\d+/[0-9-]+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['mens-fashion','black-Label','phu-trang']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]