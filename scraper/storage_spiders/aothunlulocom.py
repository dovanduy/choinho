# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='clearfix']/h1[@itemprop='name']",
    'price' : "//div[@class='clearfix rbox-price']/b",
    'category' : "//div[@class='container']/ol[@class='breadcrumb']/li[2]/a",
    'description' : "//div[@class='clearfix']/h2[@itemprop='description']",
    'images' : "//div[@class='clearfix']/img[@class='img-responsive img-lg']/@src|//ul[@id='pikame']/li/img/@src",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'aothunlulo.com'
allowed_domains = ['aothunlulo.com']
start_urls = ['http://www.aothunlulo.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['-p\d+\.html$']), 'parse_item'),
    Rule(LinkExtractor(allow=['[a-zA-Z0-9-]+\.html'], deny=['-p\d+\.html$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
