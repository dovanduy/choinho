# Auto generated by generator.py. Delete this line if you make modification.
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

XPATH = {
    'name' : "//body/div[@id='container']/div[@id='main']/div[@id='content']/div/table[@class='table1'][2]//tr[2]/td[3]/span",
    'price' : "//body/div[@id='container']/div[@id='main']/div[@id='content']/div/table[@class='table1'][2]//tr[4]/td[2]/font",
    'category' : "//body/div[@id='container']/div[@id='main']/div[@id='content']/div/table[@class='table1'][2]//tr[1]/td/a",
    'description' : "//div[@class='TabbedPanelsContent TabbedPanelsContentVisible']/table[@class='table1']//tr/td/p",
    'images' : "//body/div[@id='container']/div[@id='main']/div[@id='content']/div/table[@class='table1'][2]//tr[2]/td[1]/div/p[1]/img/@src",
    'canonical' : "",
    'base_url' : "",
    'brand' : "",
    'in_stock' : "",
    'guarantee' : "",
    'promotion' : ""
}
name = 'dogo.sieuthiphuyen.com'
allowed_domains = ['dogo.sieuthiphuyen.com']
start_urls = ['http://dogo.sieuthiphuyen.com/']
tracking_url = ''
sitemap_urls = ['']
sitemap_rules = [('', 'parse_item')]
sitemap_follow = ['']
rules = [
    Rule(LinkExtractor(allow=['b=ct&id=']), 'parse_item'),
    Rule(LinkExtractor(allow=['b=lsp&idl=\d+']), 'parse'),
    #Rule(LinkExtractor(), 'parse_item_and_links'),
]
