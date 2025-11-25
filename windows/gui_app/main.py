from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (
    FluentWindow,
    NavigationItemPosition,
    setTheme,
    Theme,
    setThemeColor,
    InfoBar,
    InfoBarPosition,
    PrimaryPushButton,
    FluentIcon as FIF,   # 图标枚举
)


class DevicePage(QWidget):
    # 设备相关页
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        title = QLabel("online device")
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title.setStyleSheet("font-size: 20px; font-weight: 600;")

        desc = QLabel("here show devices online")
        desc.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()


class LogPage(QWidget):
    # 日志页面
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        title = QLabel("log")
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title.setStyleSheet("font-size: 20px; font-weight: 600;")

        desc = QLabel("here show logs about down or login")
        desc.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()


class SettingsPage(QWidget):
    """设置页"""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        title = QLabel("setting")
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        title.setStyleSheet("font-size: 20px; font-weight: 600;")

        desc = QLabel("here you can custom")
        desc.setWordWrap(True)

        test_button = PrimaryPushButton("测试通知")
        test_button.clicked.connect(self.show_test_infobar)

        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addWidget(test_button)
        layout.addStretch()

    def show_test_infobar(self):
        InfoBar.success(
            title="测试通知",
            content="这是一条来自 WiFi Monitor 的测试消息。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=2000,
            parent=self
        )


class MainWindow(FluentWindow):
    # 主窗口
    def __init__(self):
        super().__init__()

        setTheme(Theme.AUTO)
        setThemeColor("#2563EB")

        self.setWindowTitle("NetWatch")
        self.resize(1000, 700)

        # 创建三个子页面
        self.device_page = DevicePage(self)
        self.log_page = LogPage(self)
        self.settings_page = SettingsPage(self)

        # 给每个子界面设置唯一的 objectName
        self.device_page.setObjectName("devices")
        self.log_page.setObjectName("logs")
        self.settings_page.setObjectName("settings")

        self._init_navigation()

    def _init_navigation(self):
        self.addSubInterface(
            self.device_page,
            FIF.HOME,         # 设备页图标
            "设备",
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.log_page,
            FIF.INFO,         # 日志页图标
            "日志",
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.settings_page,
            FIF.SETTING,      # 设置页图标
            "设置",
            NavigationItemPosition.BOTTOM
        )

        self.stackedWidget.setCurrentWidget(self.device_page)



def main():
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
