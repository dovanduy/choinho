# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='bg_white']/div[@class='detailProduct']/div[@class='infoProduct']/h1",
    'price' : "//div[@class='myk']/div[@class='abc']/div[@class='txPro ui-mark']/span[@id='_giasp']",
    'category' : "//div[@id='breadcum_wp']/ul[@id='bcrumb']/li/a",
    'description' : "//div[@class='infobox']/div[@id='thongtinchitiet']/div[@class='info-chitiet']/div[@class='_tab-06 tab_link-02_01 boder_ttct hide']",
    'images' : "//ul[@id='mycarousel']/li[@class='jcarousel-item jcarousel-item-horizontal jcarousel-item-1 jcarousel-item-1-horizontal']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'maytinhhanoi.com.vn'
allowed_domains = ['maytinhhanoi.com.vn']
start_urls = ['http://maytinhhanoi.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-1+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
