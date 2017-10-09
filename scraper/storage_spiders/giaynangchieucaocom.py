# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='module']/h2[@class='title_h2']/a[2]",
    'price' : "//div[@class='muasanpham']/div[@class='thongtin']/b[6]",
    'category' : "//div[@class='module']/h2[@class='title_h2']/a[1]",
    'description' : "//div[@class='thongtinc']/div[@id='mota']/p[1]",
    'images' : "//div[@class='h_daidien']/img[@class='daidien']/@src | //div[@class='img_album']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'giaynangchieucao.com'
allowed_domains = ['giaynangchieucao.com']
start_urls = ['http://giaynangchieucao.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/san-pham/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]