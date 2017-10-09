# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='infoProduct']/h1[@class='tip']",
    'price' : "//div[@class='txPro ui-mark']/span[@id='_giasp']",
    'category' : "//div[@class='brc_con']/ul[@class='bc-menu']/li/a",
    'description' : "//div[@class='_mota']",
    'images' : "//div[@class='thumnailProduct']/div[@class='small-img']/img/@src | //ul[@id='mycarousel']//a/@data-zoom-image",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'noithatmiennam.com'
allowed_domains = ['noithatmiennam.com']
start_urls = ['http://noithatmiennam.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(), 'parse_item'),
    Rule(LinkExtractor(), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
