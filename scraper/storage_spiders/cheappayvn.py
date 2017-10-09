# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@id='deal-intro']/h1",
    'price' : "//div[@class='deal-buy']/p[@class='deal-price']/strong",
    'category' : "",
    'description' : "//div[@class='box-content cf']/div[@id='team_main_side']",
    'images' : "//div[@id='team_images']/div[@class='mid']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'cheappay.vn'
allowed_domains = ['cheappay.vn']
start_urls = ['http://cheappay.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/+[a-zA-Z0-9-]+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/danh-muc/+[a-zA-Z0-9-]+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
