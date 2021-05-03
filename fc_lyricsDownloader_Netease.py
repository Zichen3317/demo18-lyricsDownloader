# -*- coding:utf-8 -*-
# ==========================================
#       author: ZiChen
#        mail: 1538185121@qq.com
#         time: 2021/05/03
#           网易云歌词下载脚本
# ==========================================

# 请求及数据处理库
import re
from urllib import request
import json
import traceback
# 输出格式设置
from datetime import datetime
exampleUrl = 'https://music.163.com/song?id=1841810361&userid=398260812'
vision = '0.1.4'


def urlProcessing(songUrl):
    '''
    将输入的歌曲链接进行处理得到想要的歌曲链接

    songUrl 歌曲链接，如示例（网易云）
    '''
    Log = '[{levelname}] - {funcName} - '.format(levelname='DEBUG',
                                                 funcName='urlProcessing')
    # 通过分析链接识别歌曲或歌单来源
    if re.search(r'music.163.com/song', songUrl) != None:
        Type = 'Netease_Song'
    elif re.search(r'music.163.com/#/playlist|music.163.com/playlist', songUrl) != None:
        Type = 'Netease_PlayList'

# 示例歌曲
    if Type == 'Netease_Song':  # 网易云音乐歌曲链接
        patternID = re.compile(r'[id=]\d+[&]')  # 查找数字
        print(str(datetime.today()).split(' ')[
              1].split('.')[0]+Log+'识别到网易云音乐歌曲')
        print(str(datetime.today()).split(' ')[
              1].split('.')[0]+Log+'正在处理链接...')
        songID = re.sub(r'[=]|[&]', '', patternID.findall(songUrl)[0])
        print(str(datetime.today()).split(' ')[
              1].split('.')[0]+Log+'已获取歌曲id：%s' % songID)

        # 网易云音乐歌词api
        neteaseApiUrl_lyric = 'https://zichen-cloud-music-api.vercel.app/lyric?id=%s&realIP=116.25.146.177' % songID
        # 网易云音乐歌曲信息api
        neteaseApiUrl_detail = 'https://zichen-cloud-music-api.vercel.app/song/detail?ids=%s' % songID

        try:
            # 获得歌手名-歌曲名，用于歌词写入
            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'正在获取歌曲信息...')
            req_detail = request.Request(url=neteaseApiUrl_detail)
            res_detail = request.urlopen(req_detail)
            # 获取响应的json字符串
            str_json_detail = res_detail.read().decode('utf-8')
            # 把json转换成字典
            myjson_detail = json.loads(str_json_detail)
            # 从字典中获得歌曲的名字及作者/翻唱者
            songName = myjson_detail['songs'][0]['name']
            # 由于作者/翻唱者可能有多个故使用列表存储，最后用join拼接即可
            songAuthorLst = []
            for i in myjson_detail['songs'][0]['ar']:
                songAuthorLst.append(i['name'])
            songAuthor = re.sub(
                r'[/]', ',', ','.join(songAuthorLst))
            songDetail = '%s - %s' % (songAuthor, songName)
            print(str(datetime.today()).split(' ')[1].split(
                '.')[0]+Log+'已获取歌曲信息: %s\n' % songDetail)

            # 获得歌词文本
            print(str(datetime.today()).split(' ')
                  [1].split('.')[0]+Log+'发送请求中...')
            req_lyric = request.Request(url=neteaseApiUrl_lyric)
            res_lyric = request.urlopen(req_lyric)

            print(str(datetime.today()).split(' ')
                  [1].split('.')[0]+Log+'已接收数据√')
            # 获取响应的json字符串
            str_json_lyric = res_lyric.read().decode('utf-8')
            # 把json转换成字典
            myjson_lyric = json.loads(str_json_lyric)
            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'正在处理接受的数据...')
            # 从字典中获得歌词文本
            lyrics = myjson_lyric['lrc']['lyric']
            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'数据处理完毕，已取得歌词文本√\n')
            # print(lyrics+'\n')

            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'正在将歌词写入文件...')
            with open('./%s.lrc' % songDetail, 'w', encoding='utf-8') as f:
                f.write(lyrics)

            print(str(datetime.today()).split(' ')
                  [1].split('.')[0]+Log+'已保存歌词文件√\n')
        except:
            traceback.print_exc()
            print(str(datetime.today()).split(' ')
                  [1].split('.')[0]+Log+'错误！正在重试...\n')
            urlProcessing(songUrl)
    elif Type == 'Netease_PlayList':
        # 歌单
        try:
            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'识别到网易云音乐歌单')

            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'正在处理链接...')
            patternID = re.compile(r'[id=]\d+[&]')  # 查找数字

            playListID = re.sub(
                r'[=]|[&]', '', patternID.findall(songUrl)[0])
            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'已获取歌单id：%s' % playListID)

            limit = 1001  # 歌单中歌曲信息获取数量限制

            # 网易云音乐歌单详细信息api
            neteaseApiUrl_playList = 'https://zichen-cloud-music-api.vercel.app/playlist/detail?id=%s' % playListID
            print(str(datetime.today()).split(' ')[
                1].split('.')[0]+Log+'正在向：[%s] 获取歌单信息...' % neteaseApiUrl_playList)

            # 加标头
            header = {
                "User-Agent": "mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
            }

            req_playList = request.Request(
                url=neteaseApiUrl_playList, headers=header)
            res_playList = request.urlopen(req_playList)

            # 获取响应的json字符串
            str_json_playList = res_playList.read().decode('utf-8')
            # 把json转换成字典
            myjson_playList = json.loads(str_json_playList)

            # 逐个获取歌单内的歌曲名及相应作者/翻唱者
            songList = []
            for songTotal in myjson_playList["playlist"]["trackIds"]:
                songID = songTotal['id']  # 获得歌曲id

                # 网易云音乐歌词api
                neteaseApiUrl_lyric = 'https://zichen-cloud-music-api.vercel.app/lyric?id=%s&realIP=116.25.146.177' % songID
                # 网易云音乐歌曲信息api
                neteaseApiUrl_detail = 'https://zichen-cloud-music-api.vercel.app/song/detail?ids=%s' % songID

                req_detail = request.Request(url=neteaseApiUrl_detail)
                res_detail = request.urlopen(req_detail)
                # 获取响应的json字符串
                str_json_detail = res_detail.read().decode('utf-8')
                # 把json转换成字典
                myjson_detail = json.loads(str_json_detail)
                # 从字典中获得歌曲的名字及作者/翻唱者
                # Tip：由于获取的歌曲名有\xa0不间断符号故使用join+split消除该符号
                songName = "" .join(myjson_detail['songs'][0]['name'].split())
                # 由于作者/翻唱者可能有多个故使用列表存储，最后用join拼接即可
                songAuthorLst = []
                for i in myjson_detail['songs'][0]['ar']:
                    songAuthorLst.append(i['name'])
                songAuthor = re.sub(
                    r'[/]', ',', ','.join(songAuthorLst))
                # 将作者/翻唱者和歌曲名以字典形式存储
                songList.append((songAuthor, songName))
                print('\n'+str(datetime.today()).split(' ')[
                    1].split('.')[0]+Log+'已获取歌单信息，下载功能暂未开发！')
            print(songList)

            # 下载功能待更
        except:
            traceback.print_exc()
            print(str(datetime.today()).split(' ')
                  [1].split('.')[0]+Log+'错误！正在重试...\n')
            urlProcessing(songUrl)
