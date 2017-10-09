# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='goodsInfo']/div/div[@class='itemInfoList']/h1/font",
    'price' : "//div[@class='itemInfoList']/form/ul/li/em[@id='ECS_SHOPPRICE']",
    'category' : "//div[@id='ur_here']/a",
    'description' : "//div[@id='itemContent']/div/div[@id='com_v']",
    'images' : "//div[@id='goodsInfo']/div/div[@class='imgInfo']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'congnghenhat.vn'
allowed_domains = ['congnghenhat.vn']
start_urls = ['http://congnghenhat.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/g+\d+-[a-zA-Z0-9-_]+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+-[a-zA-Z0-9-_]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
