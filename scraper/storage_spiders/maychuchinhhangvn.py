# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='BoxTopInfo']/div[@class='BoxTopInfo-row']/div/h1",
    'price' : "//div[@class='detail-mainInfo Category-main']/div[@class='BoxTopInfo']/div/div[@id='detail_price']",
    'category' : "//div[@class='breadcrum']/ul/li[@class='breadcrum-text']/a",
    'description' : "//div[@class='Home-layout BoxWrapCategory wraper-productDetail']/div[@class='detail-mainInfo Category-main']/div[@id='tab_detail_page']/div[@id='motasanpham']",
    'images' : "//div[@class='detail-left']/div[@class='img-product-detail']//img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'maychuchinhhang.vn'
allowed_domains = ['maychuchinhhang.vn']
start_urls = ['http://maychuchinhhang.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]