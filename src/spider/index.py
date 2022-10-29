import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

cids = ['484724324',  # 守护解放西1
        '484726378',  # 守护解放西2
        '490185028',  # 守护解放西3
        '770109868',  # 守护解放西4
        '769940530',  # 守护解放西5
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

        file_name = '../train/' + str(i) + '.txt'
        dic = {
            'appear_time': appear_time,
            'comment': comment,
        }
        df = pd.DataFrame(dic)
        df.to_csv(file_name, header=False, index=False)


getComments(cids)
