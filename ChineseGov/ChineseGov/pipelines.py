# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  os
openFile = "open.txt"

class ChinesegovPipeline(object):
    def process_item(self, item, spider):
        return item


    def open_spider(self, spider):

        f = open(openFile, "w")
        f.close()

    def close_spider(self, spider):

        if os.path.isfile(openFile):

            os.remove(openFile)
