# -*- coding:utf-8 -*-
# ==========================================
#       author: ZiChen
#        mail: 1538185121@qq.com
#         time: 2021/05/03
#            歌词下载运行文件
# ==========================================
import window  # 填写导入的py文件名
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import traceback
import fc_lyricsDownloader
Log = '[{levelname}] - {funcName} - '.format(levelname='DEBUG',
                                             funcName='urlProcessing')

# 2021/06/20 🎵编写了获取QQ音乐歌曲信息的本地API


def Start():
    Url = ui.Url.text()
    # 歌曲
    try:
        ui.progressBar_download.setValue(0)
        # 获得数据，如果是歌单的话需要进行下载确认
        Data = fc_lyricsDownloader.urlProcessing(Url)
        # print(type(Data))
        # 选中了下载
        if ui.check_PlayList_download.isChecked() == True and type(Data) == list:
            try:
                fc_lyricsDownloader.urlProcessing(Data)
            except:
                traceback.print_exc()

        ui.progressBar_download.setValue(100)
    except:
        traceback.print_exc()


print('欢迎使用歌词下载助手 作者：梓宸\n版本号%s\n' % fc_lyricsDownloader.version)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = window.Ui_MainWindow()  # 填写导入的py文件名以及内部类名
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 开始按钮与函数连接
    ui.start.clicked.connect(Start)
    sys.exit(app.exec_())
