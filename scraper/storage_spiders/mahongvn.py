# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/div[@class='bg']/div[@class='detail-sp']/div[@class='conten-sp']/div[@class='nd-sp']/span",
    'price' : "/html/body/div[@class='bg']/div[@class='detail-sp']/div[@class='conten-sp']/div[@class='nd-sp']/div[@class='info-gia']/div[@class='gia']/span",
    'category' : "/html/body/div[@class='bg']/div[@class='detail-sp']/div[@class='title-cart']/a",
    'description' : "//div[@class='conten-sp-l']/p",
    'images' : "/html/body/div[@class='bg']/div[@class='detail-sp']/div[@class='conten-sp']/div[@class='box-album']/div[@id='lofslidecontent45']/div[@class='lof-main-outer']/ul[@class='lof-main-wapper']/li/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mahong.vn'
allowed_domains = ['mahong.vn']
start_urls = ['http://mahong.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-_]+_\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]