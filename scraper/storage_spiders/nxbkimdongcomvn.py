# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//tr/td/div[@class='info-item']/h3",
    'price' : "//tr[7]/td[2]/div[@class='info-item']/span",
    'category' : "//div[@id='cms-bread']/a",
    'description' : "//div[@class='book-intro-text']",
    'images' : "//div[@class='books-thumb']/a[@class='lightbox']/@href|//a[@class='lightbox']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'nxbkimdong.com.vn'
allowed_domains = ['nxbkimdong.com.vn']
start_urls = ['http://nxbkimdong.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/products/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/books/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
