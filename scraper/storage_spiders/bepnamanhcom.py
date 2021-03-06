# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='colleft-2']/div[@class='product-details']/div[@class='detali-detalt-sp']/h1[@class='title-dtsp']",
    'price' : "//div[@class='detali-detalt-sp']/p[5]/b[@class='color']",
    'category' : "//body/div[@id='menu_search']/div[@class='sitemap_boundery']/a",
    'description' : "//div[@class='product_content']/span",
    'images' : "//div[@class='img-details']/div/a/@href",
    'canonical' : "//link[@rel='canonical']/@href",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'bepnamanh.com'
allowed_domains = ['bepnamanh.com']
start_urls = ['http://bepnamanh.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['/p/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/pc/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
