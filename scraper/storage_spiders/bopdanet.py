# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='detail']/div[@id='sanpham']/div[@id='ten']",
    'price' : "//div[@id='detail']/div[@id='sanpham']/div[@id='gia']",
    'category' : "//div[@class='pdpCustCare']/a",
    'description' : "//div[@id='detail']/div[@id='mota']/div[@id='mota2']",
    'images' : "//div[@id='imageViewer']/div[@id='mainImage']/img/@src | //div[@id='altImages']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'bopda.net'
allowed_domains = ['bopda.net']
start_urls = ['http://bopda.net/index.php']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_detail.htm']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+type.htm']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
