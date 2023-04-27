import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import *


class MyView(QWidget):
    """ view 만 실행된다.
    Qwidget view로, 엑셀 경로 버튼, 엑셀 파일 경로 QliseEdit, 엑셀로 저장버튼, ui close 버튼이 있다.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SG Asset or Shot Excel Downloader')
        self.move(550, 300)
        self.resize(300, 250)
        # view instance
        self.dir_path_view = QLineEdit(self)
        # set layout
        asset_path_label = QLabel('Path (QLineEdit)')
        self.xls_dir_btn = QPushButton("Save As ...")
        self.xls_save_btn = QPushButton("Excel Save")
        self.close_btn = QPushButton("Close")
        layout = QVBoxLayout()
        qvbox_layout = QVBoxLayout()
        qhbox_layout_1 = QHBoxLayout()
        qhbox_layout_2 = QHBoxLayout()
        # addLayout,addWidget
        layout.addLayout(qvbox_layout)
        layout.addLayout(qhbox_layout_1)
        layout.addLayout(qhbox_layout_2)
        qvbox_layout.addWidget(asset_path_label)
        qhbox_layout_1.addWidget(self.dir_path_view)
        qhbox_layout_1.addWidget(self.xls_dir_btn)
        qhbox_layout_2.addWidget(self.xls_save_btn)
        qhbox_layout_2.addWidget(self.close_btn)
        self.setLayout(layout)
        # set python size & color
        self.dir_path_view.setMinimumSize(600, 80)
        self.dir_path_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.dir_path_view.setStyleSheet('background-color: #FFFFFF;font-size: 20px;')
        self.xls_dir_btn.setMinimumSize(200, 70)
        self.xls_dir_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.xls_dir_btn.setStyleSheet('font-size: 20px;color: #FFFFFF;background-color: #717171;')
        self.xls_save_btn.setMinimumSize(200, 50)
        self.xls_save_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.xls_save_btn.setStyleSheet('font-size: 20px;color: #FFFFFF;background-color: #717171;')
        self.close_btn.setMinimumSize(200, 50)
        self.close_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.close_btn.setStyleSheet('font-size: 20px;color: #FFFFFF;background-color: #717171;')
        asset_path_label.setStyleSheet('font-size: 17px;')
        self.setStyleSheet("background-color: #4D4D4D;")

    def window_close_callback(self, callback):
        """ ui가 cloase되는 함수를
        컨트롤에서 콜백 받아  close 버튼에 연결시킨다.
        """
        self.close_btn.clicked.connect(callback)

    def xls_dir_open_btn_callback(self, callback):
        """ asset dir open 버튼클릭시 폴더선택하는 것을
        컨트롤에서 콜백 받아 버튼에 연결시킨다.
        """
        self.xls_dir_btn.clicked.connect(callback)

    def upload_btn_callback(self, callback):
        """ upload 버튼클릭시 샷그리드에 에셋을 만드는 함수를
        컨트롤에서 콜백 받아 버튼에 연결시킨다.
        """
        self.xls_save_btn.clicked.connect(callback)


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    view = MyView()
    view.show()
    app.exec_()


if __name__ == "__main__":
    main()
