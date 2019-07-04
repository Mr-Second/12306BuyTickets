from resource.Login import Ui_MainWindow
from PyQt5.Qt import *
from API.API_Tool import APITool
from resource import images_rc
from API.YDMHTTPDemo import YDMHttp


class LoginPane(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.reFresh()

    def reFresh(self):
        print("刷新验证码")
        url = APITool.download_verification_code()
        self.current_url = url
        print(url)

        pixmap = QPixmap(url)
        self.picture_label.clear_points()
        self.picture_label.setPixmap(pixmap)

    def autoSelect(self):
        print("自动打码")
        dm = YDMHttp()
        result = dm.get_yzm_result(self.current_url)
        print(result)

    def login(self):
        print("验证登陆")
        result = self.picture_label.get_result()
        if APITool.check_verification_code(result):
            print("验证码正确")
        else:
            print("验证码错误")
            self.reFresh()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = LoginPane()
    mainWindow.show()
    sys.exit(app.exec_())
