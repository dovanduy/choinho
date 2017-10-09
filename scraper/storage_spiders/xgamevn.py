# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//td/div[@id='boderchitiet']/div[1]/span[@class='ct']",
    'price' : "//td/div[@id='boderchitiet']/div/span[@class='dongia']",
    'category' : "//div[@class='block2'][1]/div[@class='tit2']/div[@id='titlecenter']/h1",
    'description' : "//div[@class='nd-bk2']/div/div[@id='id_1']/table/tr/td",
    'images' : "//div[@id='dhtmlgoodies_slideshow']/div[@id='previewPane']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'xgame.vn'
allowed_domains = ['xgame.vn']
start_urls = ['http://xgame.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\d+/\d+$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
