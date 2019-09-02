# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class AmazonPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("care.db")
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""drop table if exists laps""")
        self.cur.execute("""create table laps(
                name text,
                location text,
                tag text
        )""")
        self.conn.commit()

    def process_item(self, item, spider):
        self.cur.execute("""insert into laps values(?,?,?)""", (
            item["name"],
            item["location"],
            item["tag"]
        ))
        self.conn.commit()
        return item
