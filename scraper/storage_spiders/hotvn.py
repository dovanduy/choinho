# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='fl w759 leftcontents']/div/div/a/h1",
    'price' : "//div[@class='fr fprice bg-icon top10']/div[@class='v6Price top10']",
    'category' : "//div[@class='fl top3 right8']/a/span",
    'description' : "//div[@id='diem-noi-bat']/span",
    'images' : "//div[@id='chi-tiet-deal']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'hot.vn'
allowed_domains = ['hot.vn']
start_urls = ['http://www.hot.vn/ha-noi/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+/\d+/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/ha-noi+/\d+/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
