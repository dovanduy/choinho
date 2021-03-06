# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='proDetail-right']/h1[@class='proDetail']",
    'price' : "//div[@class='proDetail-right']/div[@class='proDetail-price']/b",
    'category' : "//div[@class='path-address']/a",
    'description' : "//div[@class='menu_detail']/div[@id='content_1']/p",
    'images' : "//div[@class='framehb imgd11']/div[@class='hbimg zoomp']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hoangaudio.com.vn'
allowed_domains = ['hoangaudio.com.vn']
start_urls = ['http://www.hoangaudio.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/viewproduct/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/productlist/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
