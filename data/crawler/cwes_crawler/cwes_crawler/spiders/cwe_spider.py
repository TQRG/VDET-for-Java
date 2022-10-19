import csv
import scrapy


abstraction_keywords = {
    'Abstraction: ', 'Structure: '
}


abstraction_fieldnames = {
    'CWE', 'NAME', 'TYPE', 'STRUCTURE', 'DESCRIPTION', 'PLATFORMS'
}


class CWESpider(scrapy.Spider):
    name = "cwes"
    cwe_number = 1
    start_urls = [
        'https://cwe.mitre.org/data/definitions/1.html'
    ]

    def parse(self, response):
        # extract weakness_id, weakness_name
        res_title = response.xpath('//h2/text()').extract()[0]
        weakness_id = res_title.split(':')[0] #if weakness_id.startwith('CWE-') else None # >>>>>>>>>>>>>> ! ALTERAR EM BAIXO SE DER

        if weakness_id.startswith('CWE-'): # deprecated, ignore 
            weakness_name = res_title.split(': ')[1]

            # extract abtraction info (type, structure)
            res_abstraction = response.xpath('//span/text()').extract()
            abstraction = {}

            for _elem in abstraction_keywords:
                if _elem in res_abstraction:
                    abstraction[_elem.split(":")[0]] = res_abstraction[res_abstraction.index(_elem) + 1] # text is in the form: "Abstraction: X"


            # extract description
            res_description = response.xpath("//div[@id='Description']/div[2]/div[@class='detail']/div/text()").extract() 
            description = res_description[0]

            # extract target languages
            res_languages = response.xpath("//div[@id='Applicable_Platforms']/div[2]/div/div/div/p/text()").extract()

            for _language in res_languages:
                _language.replace(" ", "")
                _language.replace("Class:", "")
                
            
            res_languages = ''.join(res_languages)


            row = [
                weakness_id,
                weakness_name,
                abstraction['Abstraction'],
                abstraction['Structure'],
                description,
                res_languages
            ]

            with open('./docs/cwes.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row)

            yield row


        # go to next page
        if CWESpider.cwe_number < 1395:
            CWESpider.cwe_number += 1
            next_page = f'https://cwe.mitre.org/data/definitions/' + str(CWESpider.cwe_number) + '.html'
            yield scrapy.Request(response.urljoin(next_page))
