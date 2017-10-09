# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='div_chitietsanpham_detail']/h3",
    'price' : "//div[@class='div_chitietsanpham_detail']/table//tr[1]/td[2]/span[@class='span_price']",
    'category' : "",
    'description' : "//div[@class='div_chitietsanpham_noidung_content']",
    'images' : "//div[@id='carousel']/a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'thietbivanphonghcm.com'
allowed_domains = ['thietbivanphonghcm.com']
start_urls = ['http://thietbivanphonghcm.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\w\.html($|\?p=\d+$)']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
