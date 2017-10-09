# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div/div[@class='giamoi']/strong/span[@class='price']",
    'category' : "",
    'description' : "//div[1]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]",
    'images' : "//div[1]/div/div/div[3]/div[2]/div[3]/div[1]/div[2]/div[1]/div/a[@class='other']/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'thietbiplaza.com'
allowed_domains = ['thietbiplaza.com']
start_urls = ['http://thietbiplaza.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['show1\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['pro1\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
