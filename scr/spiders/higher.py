import scrapy


class HigherSpider(scrapy.Spider):
    name = "higher"
    allowed_domains = ["www.screener.in"]
    start_urls = ["https://www.screener.in/screens/355766/highest-return-in-1-year/?utm_source=email"]

    def parse(self, response):
        company=response.xpath('//div[@class="card card-large"]/div[5]/table/tbody/tr')
        for li in company:
            Number=li.xpath('.//td[1]/text()').get()
            Name=li.xpath('td[2]/a/text()').get()
            link=li.xpath('td[2]/a/@href').get()
            cmp=li.xpath('td[3]/text()').get()
            PE = li.xpath('td[4]/text()').get()
            MarCap = li.xpath('td[5]/text()').get()
            DivYld = li.xpath('td[6]/text()').get()
            NpQtr = li.xpath('td[7]/text()').get()
            QtrProfitVar=li.xpath('td[8]/text()').get()
            SalesQtr = li.xpath('td[9]/text()').get()
            QtrSalesVar = li.xpath('td[10]/text()').get()
            ROCE = li.xpath('td[11]/text()').get()
            oneYRetun = li.xpath('td[12]/text()').get()
            yield {
                "Number": Number,
                "Name": Name,
                "link": link,
                "cmp": cmp,
                "PE":PE,
                "MarCap": MarCap,
                "DivYld": DivYld,
                "NpQtr": NpQtr,
                "QtrProfitVar": QtrProfitVar,
                "SalesQtr": SalesQtr,
                "QtrSalesVar": QtrSalesVar,
                "ROCE": ROCE,
                "oneYRetun": oneYRetun


            }
        page_url = response.xpath('//div[@class="card card-large"]/div[6]/div/div/a')
        n=len(page_url)
        next_page_url = page_url[n - 1].xpath('@href').get()

        # Going to the "next_page_url" link
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)
