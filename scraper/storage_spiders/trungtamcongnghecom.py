# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='product-detail']/div[@class='c2']/h1",
    'price' : "//div[@id='product-detail']/div[@class='c2']/div[@class='pro_price']/span",
    'category' : "//div[@id='PageContainer']/div[@id='MainContainer_f']/div[@class='nav_center ui-corner-all ui-state-default']/a",
    'description' : "//div[@id='overview']/div[@id='rs-tabs']/div[@id='rs-tabs-1']/ul[@class='sub-menu sub'] | //div[@id='product-detail']/div[@class='c2']/ul/li",
    'images' : "//div[@class='show_img_detail']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'trungtamcongnghe.com'
allowed_domains = ['trungtamcongnghe.com']
start_urls = ['http://www.trungtamcongnghe.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    #Rule(LinkExtractor(), 'parse_item'),
    #Rule(LinkExtractor(), 'parse'),
    Rule(LinkExtractor(allow=['/\d+/.+\.html$']), 'parse_item_and_links'),
]
