# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='content']/div[@id='deal-intro']/h1",
    'price' : "//div[@class='deal-buy']/p[@class='deal-price']/strong",
    'category' : "",
    'description' : "//div[@id='deal-intro']/div[@class='side']/div[2]/table//tr[2]/td[1]",
    'images' : "//div[@id='team_images']/div[@class='mid']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dealsaigon.com'
allowed_domains = ['dealsaigon.com']
start_urls = ['http://dealsaigon.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
