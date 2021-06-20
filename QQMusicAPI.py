# -*- coding:utf-8 -*-
# ==========================================
#       Author: ZiChen
#        Mail: 1538185121@qq.com
#         Time: 2021/06/20
#           Version: 1.0
#             QQ音乐官方API
# ==========================================
from urllib import request, parse
import re
import base64


def Lyrics_GET(songmid):

    api_lyrics_Url = 'http://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg'  # 官方API

    # 发送的数据
    data = {
        "songmid": songmid,
        "g_tk": "5381",
        "loginUin": "0",
        "hostUin": '0',
        "inCharset": 'utf8',
        "outCharset": 'utf-8',
        "notice": "0",
        "platform": 'yqq',
        "needNewCode": "0",
    }

    # 表头，要加Referer
    headers = {
        "Referer": 'https://y.qq.com',
    }
    # 2021/06/20 将data转换为bytes，不然会报错
    params = parse.urlencode(data).encode(encoding='UTF8')
    req_detail = request.Request(
        url=api_lyrics_Url, data=params, headers=headers)
    res_detail = request.urlopen(req_detail)
    # 获取响应的json字符串
    str_json_detail = res_detail.read().decode('utf-8')
    # 直接提取歌词（base64，需要解码）
    lyrics_bytes = re.findall(
        r"(?<=\"lyric\"\:\")(.*)(?=\",)", str_json_detail)[0]

    # 解码后返回
    return {"lyric": str(base64.b64decode(lyrics_bytes), 'utf-8')}


def Details_GET(songmid):
    api_details_url = "https://y.qq.com/n/ryqq/songDetail/%s" % songmid
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
    }
    req_detail = request.Request(
        url=api_details_url, headers=headers)
    res_detail = request.urlopen(req_detail)
    # 获取响应的json字符串
    str_json_detail = res_detail.read().decode('utf-8')
    # 歌曲名
    name = re.findall(
        r"(?<=\<h1\sclass\=\"data__name_txt\")(.*)(?=\<\/h1\>)", str_json_detail)[0].split('>')[-1]
    # 原始数据，需要进一步处理
    singer_ori = re.findall(
        r"(?<=\"data__singer_txt\")(.*)(?=\<\/a\>\<\/div\>\<ul\sclass\=\"data__info\"\>)", str_json_detail)[0]
    # 多个歌手用列表
    singerLst = []
    for i in re.findall(r"(?<=title)=([^?&=h]*)", singer_ori):
        singerLst.append(i.replace('"', '').replace(' ', ''))

    if len(singerLst) > 1:  # 有两个作者及以上的时候再拼接
        singer = "/".join(singerLst)
    else:
        singer = singerLst[0]

    return {"name": name,
            "ar": singer}
