# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='BoxTopInfo-row']/div/h1",
    'price' : "//div[@class='ListAttributePice']/span[@class='price-lb-right ColoTextPingBold']",
    'category' : "//div[@class='Home-layout wraper-productDetail']/div[@id='location']/a",
    'description' : "//div[@class='content_tab']/div[@id='tab1']",
    'images' : "//div[@class='img-product-detail']/div[@id='img_large']//a/@href",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'dienmaythudo.com'
allowed_domains = ['dienmaythudo.com']
start_urls = ['http://dienmaythudo.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
