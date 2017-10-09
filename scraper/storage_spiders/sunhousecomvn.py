# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='w-p-detail']/div[@class='w-p-detail-r']/h1",
    'price' : "//div[@class='w-p-detail-r']/p[@class='pro-detail-lable'][2]/span",
    'category' : "//div[@class='w-p-path']/ul[@class='lt']/li/h2/a",
    'description' : "//div[@class='pr-l-snv']/div[@id='pf-l-summary']",
    'images' : "//div[@class='pro-detail-image']/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'sunhouse.com.vn'
allowed_domains = ['sunhouse.com.vn']
start_urls = ['http://sunhouse.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/sp/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/dm/[a-zA-Z0-9-]+/($|\?page=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
