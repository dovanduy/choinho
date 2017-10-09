# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='padL20']/h1",
    'price' : "//div[@class='dtlProductDetail']/div[@class='dtlColRight f16']",
    'category' : "//div[@class='navBar']/div[@class='navTxt']/a",
    'description' : "//div[@id='fullDes_content']",
    'images' : "//div[@class='dtlOtherPics']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'mvtek.vn'
allowed_domains = ['mvtek.vn']
start_urls = ['http://mvtek.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c/\d+/[a-zA-Z0-9-]+($|\?pagenumber=\d+)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
