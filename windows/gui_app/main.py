from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (
    FluentWindow,
    NavigationInterface,
    NavigationItemPosition,
    setTheme,
    Theme,
    setThemeColor,
    InfoBar,
    InfoBarPosition,
    PrimaryPushButton
)


class DevicePage(QWidget):
    #设备相关页
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
    #日志页面
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
    #主窗口
    def __init__(self):
        super().__init__()

        setTheme(Theme.AUTO)
        setThemeColor("#2563EB")

        self.setWindowTitle("NetWatch")
        self.resize(1000, 700)

        self.device_page = DevicePage(self)
        self.log_page = LogPage(self)
        self.settings_page = SettingsPage(self)

        self._init_navigation()

    def _init_navigation(self):
        nav = self.navigationInterface

        nav.addItem(
            routeKey="devices",
            icon=":/qfluentwidgets/images/icons/monitor.svg",
            text="设备",
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.device_page),
            position=NavigationItemPosition.TOP
        )

        nav.addItem(
            routeKey="logs",
            icon=":/qfluentwidgets/images/icons/history.svg",
            text="日志",
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.log_page),
            position=NavigationItemPosition.TOP
        )

        nav.addItem(
            routeKey="settings",
            icon=":/qfluentwidgets/images/icons/setting.svg",
            text="设置",
            onClick=lambda: self.stackedWidget.setCurrentWidget(self.settings_page),
            position=NavigationItemPosition.BOTTOM
        )

        self.addSubInterface(self.device_page, "设备", "devices")
        self.addSubInterface(self.log_page, "日志", "logs")
        self.addSubInterface(self.settings_page, "设置", "settings")

        # 默认显示设备页
        self.stackedWidget.setCurrentWidget(self.device_page)

def main():
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
