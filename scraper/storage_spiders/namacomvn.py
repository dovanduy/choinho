# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//div[@class='pdt_top']/div[@class='pdt_tt']/h1",
    'price' : "//div[@class='pdt_gia']/form/div[1]/b/font/span",
    'category' : "//div[@class='ap_linkC']/a",
    'description' : "//div[@class='tab_cont']/table",
    'images' : "//div[@class='img_pdt']/div[@class='imgs']//ul/li/a/@href",
    'canonical' : "",
    'base_url' : "//base/@href",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'nama.com.vn'
allowed_domains = ['nama.com.vn']
start_urls = ['http://nama.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow = ['-d+\d+\.html']), 'parse_item'),
    Rule(LinkExtractor(allow = ['-p+\d+\.html']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
