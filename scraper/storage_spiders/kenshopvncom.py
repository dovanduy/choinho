# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='box proView']/div[@class='bct']/div[@class='fr cr']/h1",
    'price' : "//div[@class='fr cr']//tr[1]/td/strong",
    'category' : "//div[@class='breadcrumbs']/div[@class='lnks']/a",
    'description' : "",
    'images' : "//tr/td[@id='Product_gallery']/a/@data-zoom-image",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'kenshopvn.com'
allowed_domains = ['kenshopvn.com']
start_urls = ['http://www.kenshopvn.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-b+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
