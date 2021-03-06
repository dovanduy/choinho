# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td[@class='width500']/a[@class='bigtext']",
    'price' : "//td[@class='width500']/a[@class='price_text']",
    'category' : "//div[@id='loaisanpham']/span/a[@class='type']",
    'description' : "//div[@class='cm-tabs-content clear']/div[@class='wysiwyg-content']",
    'images' : "//table[@id='tbsanphamchitiet']//tr/td[1]/img/@src",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'flexoffice.com.vn'
allowed_domains = ['flexoffice.com.vn']
start_urls = ['http://flexoffice.com.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+-\d+\.htm']), 'parse_item_and_links'),
]
