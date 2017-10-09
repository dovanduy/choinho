# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1[@class='productGeneral']",
    'price' : "//h2[@class='productGeneral']",
    'category' : "//div[@id='navBreadCrumb']/a",
    'description' : "//div[@class='productGeneral biggerText']",
    'images' : "//div[@class='centeredContent back']/a/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'meoheo.com'
allowed_domains = ['meoheo.com']
start_urls = ['http://meoheo.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[\w-]+-p-\d+']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[\w-]+-c-\d+'], deny=['/[\w-]+-p-\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
