import json
import scrapy
from ..items import YahooprojectItem
from scrapy.crawler import CrawlerProcess

categories_ids = ['396545012', '396545144', '396545013', '396545311', '396545660', '396545014',
                  '396545327', '396545015', '396545016', '396545451', '396545433', '396545367',
                  '396545019', '396545018', '396545394', '396545401', '396545439', '396545443',
                  '396545444', '396546046', '396545122', '396545301', '396545454', '396545213',
                  '396545469', '396546089'
                  ]


class YahooAnswers(scrapy.Spider):
    name = "test"
    # API URL
    start_urls = 'https://answers.yahoo.com/_reservice_/'
    # API headers
    api_headers = {
        'content-type': 'application/json'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    # HTTP PUT request payload
    payload = {
        "type": "CALL_RESERVICE",
        "payload": {
            # change the category ID to retrieve proper questions
            # e.g. you have URL: https://answers.yahoo.com/dir/index/discover?sid=396545443
            # so you need to look at "?sid=396545443" string query parameter
            # and extract the number 396545443 to use it as the "categoryId" below
            "categoryId": '396545012',
            "lang": "en-US",
            "count": 20,
            "offset": "pc00~p:0"
        },
        "reservice": {
            "name": "FETCH_DISCOVER_STREAMS_END",
            "start": "FETCH_DISCOVER_STREAMS_START",
            "state": "CREATED"
        }
    }

    # data offset
    data_offset = 0

    # crawler's entry point
    def start_requests(self):
        # make HTTP PUT request to API URL
        # for i in categories_ids:
        #     self.payload["payload"]["categoryId"] = i
        yield scrapy.Request(
            url=self.start_urls,
            method='PUT',
            headers=self.api_headers,
            body=json.dumps(self.payload),
            callback=self.parse
            )


    # parse callback method
    def parse(self, response):
        items = YahooprojectItem()
        json_data = json.loads(response.text)
        for question in json_data['payload']['questions']:
            # check if next bunch of data available
            # items['qid'] = question['qid']
            # items['categoryname'] = question['category']['name']
            answer_url = 'https://answers.yahoo.com/question/index?qid=' + '20200704231815AAXWafx'
            yield response.follow(
                url=answer_url,
                headers=self.headers,
                callback=self.parse_answer,
            )

        if json_data['payload']['canLoadMore'] == True:
            # update data offset
            self.data_offset += 20

            # update payload offset
            self.payload['payload']['offset'] = 'pc' + str(self.data_offset) + '~p:0'

            # crawl next bunch of data
            # for i in categories_ids:
            #     self.payload["payload"]["categoryId"] = i
            yield scrapy.Request(
                url=self.start_urls,
                method='PUT',
                headers=self.api_headers,
                body=json.dumps(self.payload),
                callback=self.parse
                )

    def parse_answer(self, response):

        items = YahooprojectItem()
        for answer in response.css('ul[class="AnswersList__answersList___1GjcP"]').css('li'):
            # extract user name
            user_name = answer.css('div[class="UserProfile__userInfo___yViBh"] *::text').get()

            # append only available answers
            if user_name is not None:
                items['user_name'] = user_name

                items['answer'] = answer.css('div[class="ExpandableContent__content___NoJJI"] *::text') \
                    .get()

                items['comments'] = answer.css('p[class="Comment__text___3G8FQ"]::text') \
                        .getall()

                items['date'] = answer.css('div[class="Answer__subtitle___yrInO"]::text') \
                    .get()

                items['likes'] = answer.css('button[aria-label="Thumbs up for this answer."]') \
                    .css('span::text') \
                    .get()

                items['dislikes'] = answer.css('button[aria-label="Thumbs down for this answer."]') \
                    .css('span::text') \
                    .get()
                yield items


            # check if next bunch of data available


