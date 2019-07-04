from PyQt5.Qt import *


# 重写QLabel
class MyLabel(QLabel):

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        print(evt.pos())
        point = QPushButton(self)
        point.resize(20, 20)
        point.move(evt.pos()-QPoint(10, 10))
        point.setStyleSheet("background-color:green; border-radius: 10px")
        point.show()

        point.clicked.connect(lambda _, btn=point: btn.deleteLater())

    # 15,13,17,89
    def get_result(self):

        result = ",".join(["{},{}".format(child.x()+10, child.y()-20)
                           for child in self.children()
                           if child.inherits("QPushButton")])
        print(result)
        return result

    def clear_points(self):
        [child.deleteLater() for child in self.children() if child.inherits("QPushButton")]