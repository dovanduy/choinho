# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='deal-intro']/h1",
    'price' : "//div[@class='main']/div[@class='deal-price-tag']",
    'category' : "",
    'description' : "//div[@class='diem-noi-bat']/div[@class='content']",
    'images' : "//div[@id='team_images']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'zenthoitrang.com'
allowed_domains = ['zenthoitrang.com']
start_urls = ['http://zenthoitrang.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['phong-cach/gia-re']), 'parse_item'),
    Rule(LinkExtractor(allow=['san-pham-moi-nhat']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
