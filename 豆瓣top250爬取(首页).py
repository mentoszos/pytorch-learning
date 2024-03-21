########################################################
########################################################
##################爬取内容为豆瓣首页#####################
########################################################
########################################################
########################################################

from bs4 import BeautifulSoup
import requests
import pandas as pd
names = [] #影片名
ranks = [] # 排名
directors = []#导演
mainActors = []#部分主演，爬取内容来自首页，信息可能不全
dates = []#上映日期
regions = []#影片地区
types = []#影片类型
rating_nums = []#影片评分
numbers = []#评论人数

def getOnePage(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    resp = requests.get(url,headers = headers) #获取url的response对象,get方法
    soup = BeautifulSoup(resp.text,'html.parser')
    #print(soup.prettify())
    items = soup.select('.item') #获取页面中所有的电影,返回列表
    #print(items)

    for item in items:
        #影片名
        name = item.select('.hd a')[0].text #获取其中文本内容
        name = name.replace('\n', ' ').replace('\xa0',' ').strip() # 转换格式
        #print(name)
        names.append(name)

        #排名
        rank = item.select('em')[0].text
        #print(rank)
        ranks.append(rank)

        #导演
        message = item.select('.bd p')[0].text.strip()
        director = message.split('\n')[0].split('   ')[0]
        #print(director)
        directors.append(director)

        #主演（如果首页中显示，否则为空）
        try:
            actor = message.split('\n')[0].split('   ')[1]
            #print(actor)
            mainActors.append(actor)
        except:
            mainActors.append(None)

        #对大闹天宫特殊处理
        if '大闹天宫' in name :
            dates.append('1961(中国大陆) / 1964(中国大陆) / 1978(中国大陆)')
            regions.append('中国大陆')
            types.append('剧情 动画 奇幻 古装')

            #评分
            rating_num = item.select('.rating_num')[0].text
            #print(rating_num)
            rating_nums.append(rating_num)

            #评论人数
            number = item.select('.star span')[3].text.split('人')[0]
            #print(number)
            numbers.append(number)

        else:
            message = message.split('\n')[1].split('/')

            #上映时间，地区，类型
            dates.append(message[0].strip())
            regions.append(message[1].strip())
            types.append(message[2].strip())
            #print(dates)
            #print(regions)
            #print(types)

            #评分
            rating_num = item.select('.rating_num')[0].text
            #print(message)
            rating_nums.append(rating_num)
            #print(rating_nums)

            #评论人数
            number = item.select('.star span')[3].text.split('人')[0]
            numbers.append(number)

def ouput_to_csv():

    dic = {
        '排名':ranks,
        '影片名' : names,
        '导演':directors,
        '主演': mainActors,
        '导演': directors,
        '上映时间': dates,
        '地区': regions,
        '类型': types,
        '评分': rating_nums,
        '评论人数': numbers

    }
    df = pd.DataFrame(dic)

    #不是这个编码会乱码
    df.to_csv('豆瓣top250.csv',encoding='utf_8_sig')





if __name__ == "__main__":

    #每一页循环爬取
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=' + str(i*25) + '&filter='
        print('正在爬取第'+str(i+1)+'页')
        getOnePage(url)

    #导出csv
    ouput_to_csv()



