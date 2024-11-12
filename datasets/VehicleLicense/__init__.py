# -*- coding: utf-8 -*-

__version__ = ''
__author__ = ''
__email__ = ''
__url__ = ''

AUTHOR_INFO = ()

ENV_CONFIG = ("[配置环境]\n"
              "请按照给定的python版本配置环境，否则可能会因依赖不兼容而出错\n"
              "(1)使用anaconda新建python3.10环境:\n"
              "conda create -n env_rec python=3.10\n"
              "(2)激活创建的环境:\n"
              "conda activate env_rec\n"
              "(3)使用pip安装所需的依赖，可通过requirements.txt:\n"
              "pip install -r requirements.txt\n")

# with open('./环境配置.txt', 'w', encoding='utf-8') as f:
#     f.writelines(ENV_CONFIG + "\n\n" + AUTHOR_INFO)
