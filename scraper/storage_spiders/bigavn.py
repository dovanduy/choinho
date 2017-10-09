# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='BlockContent']/h1",
    'price' : "//div[@class='ProductMain']/div[@class='WholesaleTable']/div[@class='WholesaleItem Item-0']/em",
    'category' : "//div[@class='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='ProductDescriptionContainer']/p",
    'images' : "//a[@rel='prodImage']/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'biga.vn'
allowed_domains = ['biga.vn']
start_urls = ['http://biga.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[\w\d-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w\d-]+-b\d+\.html($|\?pn=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
