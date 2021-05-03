# -*- coding:utf-8 -*-
# ==========================================
#       author: ZiChen
#        mail: 1538185121@qq.com
#         time: 2021/05/03
#            网易云音乐歌词下载运行文件
# ==========================================
import window  # 填写导入的py文件名
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import traceback
import fc_lyricsDownloader_Netease
Log = '[{levelname}] - {funcName} - '.format(levelname='DEBUG',
                                             funcName='urlProcessing')


def Start():
    Url = ui.Url.text()
    # 歌曲
    try:
        ui.progressBar_download.setValue(0)
        fc_lyricsDownloader_Netease.urlProcessing(Url)
        ui.progressBar_download.setValue(100)
    except:
        traceback.print_exc()


print('欢迎使用网易云歌词下载助手 作者：梓宸\n版本号%s\n' % fc_lyricsDownloader_Netease.vision)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = window.Ui_MainWindow()  # 填写导入的py文件名以及内部类名
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 开始按钮与函数连接
    ui.start.clicked.connect(Start)
    sys.exit(app.exec_())
