# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='title-pro-detail']",
    'price' : "//td[@id='productInfoPrice']",
    'category' : "//div[@id='breadcrumbPath']/a",
    'description' : "//div[@id='tabFeatures']/div[@class='moduleBox']/div[@class='content'] | //div[@id='tabDescription']",
    'images' : "//div[@id='productImages']/a[2]/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hanam.com.vn'
allowed_domains = ['hanam.com.vn']
start_urls = ['http://hanam.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+-[a-zA-Z0-9-]+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]