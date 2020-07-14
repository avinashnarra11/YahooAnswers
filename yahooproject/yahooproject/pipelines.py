# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#import sqlite3


class YahooprojectPipeline:
    # def __init__(self):
    #     self.conn = sqlite3.connect('yahoo_answers.db')
    #     self.curr = self.conn.cursor()
    #     self.create_table()
    #
    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS answers_tb""")
    #     self.curr.execute("""create table answers_tb(
    #                     user_name text,
    #                     answer text,
    #                     comments text,
    #                     date text,
    #                     likes text,
    #                     dislikes text
    #                     ) """)
    #
    # def process_item(self, item, spider):
    #     self.store_db(item)
    #     return item
    #
    # def store_db(self, item):
    #     user_name = item['user_name']
    #     answer = item['answer']
    #     comments = item['comments']
    #     date = item['date']
    #     likes = item['likes']
    #     dislikes = item['dislikes']
    #
    #
    #     self.curr.execute("insert into answers_tb values (?,?,?,?,?,?)",
    #                       (
    #                          user_name, answer, comments, date, likes, dislikes
    #
    #                       ))
    #     self.conn.commit()
    pass
