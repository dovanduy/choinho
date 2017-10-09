# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@id='ProductDetails']/div[@class='BlockContent']/div[@class='product-title defaultTitle']/h1",
    'price' : "//div[@class='ProductDetailsGrid']/div[@class='DetailRow']/div[@class='Value']/em[@class='ProductPrice VariationProductPrice']",
    'category' : "//div[@id='Breadcrumb']/ul/li/a",
    'description' : "//div[@class='BlockContent']/div[@id='ProductDescription']/div[@class='ProductDescriptionContainer']/p",
    'images' : "//div[@class='ProductThumbImage']/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : ""
}
name = 'akita.com.vn'
allowed_domains = ['akita.com.vn']
start_urls = ['http://akita.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-b+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]