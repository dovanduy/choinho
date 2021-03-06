# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='top-dt']/div[@class='pd-infoRight']/div[@class='pd-name']/h1",
    'price' : "//div[@class='pd-detail']/div[@class='top-dt']/div[@class='pd-infoRight']/div[@class='big-price']",
    'category' : "//div[@class='col-left fl']/div[@class='bread-cum']/p/a",
    'description' : "//div[@class='box-chitiet']/div[@class='top-chitiet']",
    'images' : "//div[@class='hbimg zoomp']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'maytinhvietnam.vn'
allowed_domains = ['maytinhvietnam.vn']
start_urls = ['http://www.maytinhvietnam.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c\d+\.html'], deny=['\?']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
