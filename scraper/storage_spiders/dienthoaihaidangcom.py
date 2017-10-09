# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//h1",
    'price' : "//div[@class='div_gia']/span[@class='giavnd ']/span",
    'category' : "",
    'description' : "//div[@class='noidungchitiet']/p",
    'images' : "//img[@id='anh_chitiet_sanpham']/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : ""
}
name = 'dienthoaihaidang.com'
allowed_domains = ['dienthoaihaidang.com']
start_urls = ['http://dienthoaihaidang.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-id\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-d\d+(p\d+)*\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
