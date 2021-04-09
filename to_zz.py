import datetime
import sys,os
import requests

import openpyxl
from PyQt5.QtGui import QCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from dingtalkchatbot.chatbot import DingtalkChatbot
from openpyxl import load_workbook
import xlrd
import xlwt
from openpyxl.styles import Font, colors, Alignment


from PyQt5.QtCore import QSettings, Qt, QUrl, QTimer
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox,QWidget

from zsq import Ui_Form

# 定位桌面路径
def desktop_path():
    return os.path.join(os.path.expanduser('~'),"Desktop")
print(desktop_path())




class AutoExcel(QWidget,Ui_Form):

    def __init__(self):
        super(AutoExcel,self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setting = QSettings("config.ini", QSettings.IniFormat)
        self.xxlist = [0,1,2,3,4,5,6,7]
        self.num  = 0
        self.lineInit()
        self.cheBoxConn()
        self.lineConn()
        self.btnConn()
        self.webEngineInit()
        self.web_qtimer()
        self.set_text()
        self.name_dict = {0:"王",1:"周",2:"彭",3:"李",4:"贺",5:"余",6:"郎",7:"尹"}

    def webEngineInit(self):
        self.barBrowser = QWebEngineView()
        self.tq_verticalLayout.addWidget(self.barBrowser)
        self.barBrowser.load(QUrl('https://weather.seniverse.com/?token=98ba7a01-1834-4a58-96e9-87de6b7cae6e'))

    def web_qtimer(self):
        timer = QTimer()
        timer.timeout.connect(self.tq_updata)
        timer.start(1800000)

    def tq_updata(self):
        self.barBrowser.load(QUrl('https://weather.seniverse.com/?token=98ba7a01-1834-4a58-96e9-87de6b7cae6e'))

    def lineInit(self):
        webHook = self.setting.value('SETUP/WEBHOOK')
        self.webHookLineEdit.setText(webHook)
        sercreat = self.setting.value('SETUP/SERCRET')
        self.sercertLineEdit.setText(sercreat)

        self.webHookLineEdit.setVisible(False)
        self.sercertLineEdit.setVisible(False)
        # self.label_7.setVisible(False)
        # self.label_8.setVisible(False)

    def cheBoxConn(self):
        self.checkBox1.stateChanged.connect(self.changeBox1)
        self.checkBox2.stateChanged.connect(self.changeBox2)
        self.checkBox3.stateChanged.connect(self.changeBox3)
        self.checkBox4.stateChanged.connect(self.changeBox4)
        self.checkBox5.stateChanged.connect(self.changeBox5)
        self.checkBox6.stateChanged.connect(self.changeBox6)
        self.checkBox7.stateChanged.connect(self.changeBox7)
        self.checkBox8.stateChanged.connect(self.changeBox8)
        self.hlCheckBox.stateChanged.connect(self.changeCheck)
        self.ltCheckBox.stateChanged.connect(self.changeCheck1)
        self.bd_checkBox.stateChanged.connect(self.changeCheck2)

    def changeCheck(self):
        if self.hlCheckBox.checkState() == Qt.Checked:
            self.ltCheckBox.setChecked(False)
            self.bd_checkBox.setChecked(False)

    def changeCheck1(self):
        if self.ltCheckBox.checkState() == Qt.Checked:
            self.hlCheckBox.setChecked(False)
            self.bd_checkBox.setChecked(False)
    def changeCheck2(self):
        if self.bd_checkBox.checkState() == Qt.Checked:
            self.ltCheckBox.setChecked(False)
            self.hlCheckBox.setChecked(False)
    def changeBox1(self):
        if self.checkBox1.isChecked():
            self.xxlist.remove(0)
        else:
            self.xxlist.append(0)


    def changeBox2(self):
        if self.checkBox2.isChecked():
            self.xxlist.remove(1)

        else:
            self.xxlist.append(1)

    def changeBox3(self):
        if self.checkBox3.isChecked():
            self.xxlist.remove(2)
        else:
            self.xxlist.append(2)

    def changeBox4(self):
        if self.checkBox4.isChecked():
            self.xxlist.remove(3)
        else:
            self.xxlist.append(3)

    def changeBox5(self):
        if self.checkBox5.isChecked():
            self.xxlist.remove(4)
        else:
            self.xxlist.append(4)

    def changeBox6(self):
        if self.checkBox6.isChecked():
            self.xxlist.remove(5)
        else:
            self.xxlist.append(5)

    def changeBox7(self):
        if self.checkBox7.isChecked():
            self.xxlist.remove(6)
        else:
            self.xxlist.append(6)

    def changeBox8(self):
        if self.checkBox8.isChecked():
            self.xxlist.remove(7)
        else:
            self.xxlist.append(7)

    def comchange(self):
        num = self.comboBox.currentIndex()
        try:
            index = self.xxlist.index(num)
            self.num = index
        except:
            QMessageBox.information(self,"提示","你选择了一个需要跳过的目标")


    def lineConn(self):
        self.webHookLineEdit.textChanged.connect(self.changeWeb)
        self.sercertLineEdit.textChanged.connect(self.changeSer)

    def changeSer(self):
        sercreat = self.sercertLineEdit.text()
        self.setting.setValue('SETUP/SERCRET',sercreat)

    def changeWeb(self):
        webHook = self.webHookLineEdit.text()
        self.setting.setValue('SETUP/WEBHOOK',webHook)

    def btnConn(self):
        # 发送按钮
        self.sendPushButton.clicked.connect(self.sendTo)
        # 创建EXCEL按钮
        # self.crearExPushButton.clicked.connect(self.createExcel)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.showMinimized)

        self.comboBox.activated.connect(self.comchange)
        self.flushed_pushButton.clicked.connect(self.set_text)


    def sendTo(self):
        # 获取当前输入内容
        phone = self.phoneLineEdit.text()
        name = self.comboBox.currentText()

        path = desktop_path()
        desc = self.textEdit.toPlainText()
        if phone == '' or desc == '':
            QMessageBox.information(self,'提示','内容或者手机号未填写！')
        else:
           try:
                # 如果勾选华律
                if self.hlCheckBox.isChecked():
                    excel_name = "华律网分案"
                    laiyuan = "华律网"
                    self.writExcel(excel_name, phone)
                    self.send_to_dd(name,desc,phone,laiyuan)

                elif self.ltCheckBox.isChecked(): # 勾选律图
                    excel_name = "律图案源"
                    laiyuan = "律图"
                    self.writExcel(excel_name, phone)
                    self.send_to_dd(name, desc, phone, laiyuan)

                elif self.bd_checkBox.isChecked():
                    laiyuan = "百度"
                    excel_name = "百度分案"
                    self.writExcel(excel_name, phone)
                    self.send_to_dd(name, desc, phone, laiyuan)


                # 自动跳转
                if self.autoJumCheckBox.isChecked():
                    self.xxlist.sort()
                    sortlist = self.xxlist

                    if sortlist[-1] == sortlist[self.num]:
                        self.num = 0
                        self.comboBox.setCurrentIndex(sortlist[self.num])
                    else:
                        self.num += 1
                        self.comboBox.setCurrentIndex(sortlist[self.num])

                # 自动清空
                self.textEdit.clear()
                self.phoneLineEdit.clear()
           except:
               QMessageBox.information(self,"提示","EXCEL未关闭！")

    # 钉钉发送
    def send_to_dd(self,name,desc,phone,laiyuan):
        if self.comboBox.currentIndex() == 0:
            mobiles = ['15334578885']
        elif self.comboBox.currentIndex() == 1:
            mobiles = ['15823576135']
        elif self.comboBox.currentIndex() == 2:
            mobiles = ['17815014641']
        elif self.comboBox.currentIndex() == 3:
            mobiles = ['18523469626']
        elif self.comboBox.currentIndex() == 4:
            mobiles = ['13399866710']
        elif self.comboBox.currentIndex() == 5:
            mobiles = ['17308369667']
        elif self.comboBox.currentIndex() == 6:
            mobiles = ['18723238385']
        elif self.comboBox.currentIndex() == 7:
            mobiles = ['19923304908']
        msg = "{}  {}\n手机号：{} \n{} ".format(name, desc, phone,laiyuan)
        webhook = self.webHookLineEdit.text()
        secret = self.sercertLineEdit.text()
        xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
        # xiaoding = DingtalkChatbot(webhook, pc_slide=True)  # 方式三：设置消息链接在PC端侧边栏打开（v1.5以上新功能）
        # Text消息@所有人
        if self.atcheckBox.isChecked():
            xiaoding.send_text(msg=msg, is_at_all=False, at_mobiles=mobiles)
        else:
            xiaoding.send_text(msg=msg, is_at_all=False)
    # 写入Excel
    def writExcel(self,excel_name,phone):
        # 第A列字体
        font_A = Font(name="宋体", size=11)
        today = datetime.date.today().strftime('%Y.%m.%d')
        desk_path=desktop_path()
        path = desk_path+'\{}.xlsx'.format(excel_name)
        # 打开桌面excel
        wb = load_workbook(path)
        sheet1 = wb['总表']
        # 获取当前发送人索引
        index = self.comboBox.currentIndex()
        # 创建发送人sheet
        name = self.name_dict[index]
        sheet_name = wb[name]
        # 追加到EXCEL的列表
        excel_list = [today,name,int(phone),"√"]
        sheet_name.append(excel_list)
        sheet1.append(excel_list)
        # sheet1.column_dimensions['A'].font= font_A
        # sheet1.column_dimensions['B'].font= font_A
        # sheet1.column_dimensions['C'].font= font_A
        # sheet1.column_dimensions['D'].font= font_A
        # # sheet1.column_dimensions['A'].alignment = Alignment(horizontal='center', vertical='center')
        # # sheet1['B13'].alignment = Alignment(horizontal='center', vertical='center')
        # # sheet1.column_dimensions['C'].alignment = Alignment(horizontal='center', vertical='center')
        # # sheet1.column_dimensions['D'].alignment = Alignment(horizontal='center', vertical='center')
        #
        # sheet_name.column_dimensions['A'].font = font_A
        # sheet_name.column_dimensions['B'].font = font_A
        # sheet_name.column_dimensions['C'].font = font_A
        # sheet_name.column_dimensions['D'].font = font_A

        for i in sheet1:
            for cell in i:
                cell.font = font_A
                cell.alignment = Alignment(horizontal='center', vertical='center')

        for i in sheet_name:
            for cell in i:
                cell.font = font_A
                cell.alignment = Alignment(horizontal='center', vertical='center')

        wb.save(path)

    def day_talk(self):
        re = requests.get(url="https://api.mcloc.cn/love?type=json")
        talk_dict = re.json()
        talk = talk_dict["data"]
        return talk

    def set_text(self):
        self.textBrowser.clear()
        text = self.day_talk()
        self.textBrowser.setText("To宝宝："+ "\n {}".format(text))

    # 鼠标按下事件函数
    def mousePressEvent(self, event):
        if self.isMaximized():
            pass
        else:
            if event.button() == Qt.LeftButton:
                self.m_flag = True
                self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QCursor(Qt.OpenHandCursor))

        # 鼠标移动事件函数

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

        # 鼠标释放事件函数

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutoExcel()
    window.show()
    sys.exit(app.exec_())

