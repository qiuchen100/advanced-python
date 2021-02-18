# -*- coding: utf-8 -*-

import requests
from PIL import ImageFile
import numpy as np


class Downloader(object):
    """下载模块
    """

    def __init__(self):
        pass

    def _process(self, url):
        """实际下载逻辑
        :param url:
        :return:
        """
        response = requests.get(url)
        content = response.content

    def _process_single_thread(self, list_):
        """单线程下载
        :param list_: 下载链接列表
        :return:
        """
        for url in list_:
            self._process(url)
            # 图片下载
            pass

    def process(self, list_):
        """
        :param list_: 下载链接列表
        :return:
        """
        return self._process_single_thread(list_)
