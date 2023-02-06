import sys
from PyQt5.QtGui import QPixmap, QKeyEvent
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
import os

class ImageViewer(QMainWindow):
    def __init__(self, folder_path):
        super().__init__()

        self.folder_path = folder_path
        self.images = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]
        self.current_index = 0
        self.label = QLabel(self)
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)  # 設置初始大小
        self.setMinimumSize(400, 300)  # 設置最小大小限制
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)  # 禁止最大化
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)  # 禁止最小化
        try:
            with open("image_index.txt", "r") as f:
                self.current_index = int(f.read())
        except:
            pass

        self.show_image()


    def show_image(self):
        image = QPixmap(os.path.join(self.folder_path, self.images[self.current_index]))
        self.label.setPixmap(image)
        self.setCentralWidget(self.label)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Right:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.show_image()
        elif event.key() == Qt.Key_Left:
            self.current_index = (self.current_index - 1 + len(self.images)) % len(self.images)
            self.show_image()

    def closeEvent(self, event):
        with open("image_index.txt", "w") as f:
            f.write(str(self.current_index))
        event.accept()

if __name__ == '__main__':
    folder_path = "E:\Document\Data\python\manga reader\images"  # 指定資料夾
    app = QApplication(sys.argv)
    viewer = ImageViewer(folder_path)
    viewer.show()
    sys.exit(app.exec_())
