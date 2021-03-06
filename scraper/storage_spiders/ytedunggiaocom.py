# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/form[@id='Form1']/div[@class='page']/div[@class='main']/div[@class='col-right']/div[@class='content_main']/div[@id='MainContent_ProductDetails1_pnlDetail']/div[@class='productdetailtop']/div/h2[@class='title-detial-pr']/span[@id='MainContent_ProductDetails1_proname']",
    'price' : "/html/body/form[@id='Form1']/div[@class='page']/div[@class='main']/div[@class='col-right']/div[@class='content_main']/div[@id='MainContent_ProductDetails1_pnlDetail']/div[@class='productdetailtop']/div/div[@id='ctl00_ContentMain_rptpd_ctl00_pricedefault']/span[@class='price-total']/span[@id='MainContent_ProductDetails1_price']",
    'category' : "",
    'description' : "/html/body/form[@id='Form1']/div[@class='page']/div[@class='main']/div[@class='col-right']/div[@class='content_main']/div[@id='MainContent_ProductDetails1_pnlDetail']/div[@class='detail-product-show']/div[@class='tab_container2']/div[@id='tab1']/div",
    'images' : "/html/body/form[@id='Form1']/div[@class='page']/div[@class='main']/div[@class='col-right']/div[@class='content_main']/div[@id='MainContent_ProductDetails1_pnlDetail']/div[@class='productdetailtop']/div[@id='MainContent_ProductDetails1_img']/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'ytedunggiao.com'
allowed_domains = ['ytedunggiao.com']
start_urls = ['http://ytedunggiao.com']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/i+\d+.*']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c+\d+.*']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
