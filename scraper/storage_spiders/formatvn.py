# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='vmMainPage']/table//tr/td/div/h2",
    'price' : "//span[@class='productPrice']/b",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='flexible-zoom-additionalImages']/a/@href | //div[@id='ja-current-content']/div[@id='vmMainPage']//a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'format.vn'
allowed_domains = ['format.vn']
start_urls = ['http://format.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
