# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title']/div[@class='product-name']/h1",
    'price' : "//div[@class='product-priceview']/div[@class='pricespecial']/p",
    'category' : "//div[@class='breadcrumbs']/ul/li/a",
    'description' : "//div[@id='productleft']/div[@class='block-description readmore '] | //div[@id='productleft']/div[@class='block-description']",
    'images' : "//div[@class='block-description readmore ']/p/img/@src | //a[@class='cloud-zoom']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'sieumua.com'
allowed_domains = ['sieumua.com']
start_urls = ['http://www.sieumua.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-sid+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html+$'], deny=['m.sieumua.com','p=','mucdichsudung=','special_price=','kieudang=']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
