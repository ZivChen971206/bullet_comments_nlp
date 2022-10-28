import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

cids = ['870665763',  # 老婆：你现在都玩这么变态的吗！？
        '867666106',  # 既分高下，也决生死！
        '869269725',  # 我们采访了一位53岁“赛博”母亲，她正在现实中守护去世儿子的灵魂
        '866385231',  # 【鱼肉肉】Lovepotion宅舞 小飞棍摔咯~
        '872534063',  # 《我肯定在几百年前就不爱学习》
        ]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


def getComments(cids):
    for i in range(0, len(cids)):
        appear_time = []
        comment = []
        request = requests.get(url='https://comment.bilibili.com/' + cids[i] + '.xml', headers=headers)  # 获取页面
        request.encoding = 'utf8'  # 因为是中文，我们需要进行转码，否则出来的都是unicode
        soup = BeautifulSoup(request.text, 'lxml')
        for t in soup.find_all('d'):  # for循环遍历所有d标签，并把返回列表中的内容赋给t
            appear_time.append(round(float(t.attrs['p'].split(',')[0])))
            comment.append(t.text)

        file_name = '../train/' + str(i) + '.csv'
        dic = {
            'appear_time': appear_time,
            'comment': comment,
        }
        df = pd.DataFrame(dic)
        df.to_csv(file_name, index=False, header=None, encoding='utf_8_sig')


getComments(cids)
