# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "/html/body/form[@id='aspnetForm']/div[@class='pagecontainer']/div[@class='pagecontent']/div[@id='ctl00_pnDefault']/div[@class='maincol']/div[@id='ctl00_cpMainpage_Main1_ctl00_pnBox']/div[@class='contentbox']/div[@class='common']/p/strong",
    'price' : "/html/body/form[@id='aspnetForm']/div[@class='pagecontainer']/div[@class='pagecontent']/div[@id='ctl00_pnDefault']/div[@class='maincol']/div[@id='ctl00_cpMainpage_Main1_ctl00_pnBox']/div[@class='contentbox']/div[@class='productprice']",
    'category' : "/html/body/form[@id='aspnetForm']/div[@class='pagecontainer']/div[@class='pagecontent']/div[@class='topcol']/div[@class='path']/a/span",
    'description' : "/html/body/form[@id='aspnetForm']/div[@class='pagecontainer']/div[@class='pagecontent']/div[@id='ctl00_pnDefault']/div[@class='maincol']/div[@id='ctl00_cpMainpage_Main1_ctl00_pnBox']/div[@class='contentbox']/div[@class='content']",
    'images' : "/html/body/form[@id='aspnetForm']/div[@class='pagecontainer']/div[@class='pagecontent']/div[@id='ctl00_pnDefault']/div[@class='maincol']/div[@id='ctl00_cpMainpage_Main1_ctl00_pnBox']/div[@class='contentbox']/div[@class='common']/a/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : ""
}
name = 'suaongchuacuauc.com.vn'
allowed_domains = ['suaongchuacuauc.com.vn']
start_urls = ['http://suaongchuacuauc.com.vn']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = []
rules = [
    Rule(LinkExtractor(allow=['/p/']), 'parse_item'),
    Rule(LinkExtractor(allow=['/c/']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
