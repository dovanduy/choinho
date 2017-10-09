# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='product-title defaultTitle']/h1",
    'price' : "//div[@class='Value']/em",
    'category' : "//div[@id='Breadcrumb']/ul/li/a",
    'description' : "",
    'images' : "//div[@class='ProductThumb']/div[@class='ProductThumbImage']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'anasportshop.com'
allowed_domains = ['anasportshop.com']
start_urls = ['http://anasportshop.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(deny = ['/khuyen-mai/', '/chinh-sach-ban-hang/', '/tin-tuc/', '/lien-he/', '/he-thong-cua-hang-cong-ty-anasport-viet-nam/'], allow=['/[a-zA-Z0-9-]+-b+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]