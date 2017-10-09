# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='col-md-5 col-sm-5 productinfo-rightwrapper']/h4[@class='title']",
    'price' : "//div[@class='productprice-amount']/span[@class='productSale']|//div[@class='productprice-amount']/p[@class='productSale']",
    'category' : "//div[@class='breadcrumbs']/span",
    'description' : "//div[@class='row productinfo-container']/div[@class='product_info_tab wow fadeInUp animated animated']",
    'images' : "//a[@id='zoom1']/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'sieuthimynghe.vn'
allowed_domains = ['sieuthimynghe.vn']
start_urls = ['http://sieuthimynghe.vn/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9-]+-myngheviet\.vn/$']), 'parse_item'),
    Rule(LinkExtractor(allow=['/[a-zA-Z0-9]+/$'], deny=['/[a-zA-Z0-9]+-myngheviet\.vn/$']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
