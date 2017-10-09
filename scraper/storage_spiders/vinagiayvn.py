# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='tab1']/p[1]|//div[@id='tab1']/h4[1]",
    'price' : "//form/div[@id='tab1']/p[4]/span",
    'category' : "",
    'description' : "",
    'images' : "//div[@class='warp']/div[@class='col2']/div[1]/div[2]/a[1]/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "//form/div[@id='tab1']/p[3]"
}
name = 'vinagiay.vn'
allowed_domains = ['vinagiay.vn']
start_urls = ['http://vinagiay.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['&id_s=\d+']), 'parse_item'),
    Rule(LinkExtractor(allow=['danh-muc.html','&cat=\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
