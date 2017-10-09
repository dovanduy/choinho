# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='motachu']/div[@class='nhommota']/span",
    'price' : "//div[@class='giachu']/div[@class='nhomgoc']/span | //div[@class='giachu']/div[@class='nhomban']/span",
    'category' : "",
    'description' : "//div[@class='cont-nhomchu2']/div[@class='cont-chitiet']",
    'images' : "//div[@class='hinhchu']/div[@id='team_images']/div[@class='mid']/ul/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dealshop.vn'
allowed_domains = ['dealshop.vn']
start_urls = ['http://dealshop.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/\?+p=ctsp+\&+cid=+\d+\&+id=+\d{0,3}']), 'parse_item'),
    Rule(LinkExtractor(allow=['/\?+p=nsp','/\?+p=nspbe']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]