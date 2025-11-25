import sys
from PySide6.QtWidgets import QApplication

print("[DEBUG] before app")
app = QApplication(sys.argv)
print("[DEBUG] after app, before import qfluentwidgets")

from qfluentwidgets import FluentWindow
print("[DEBUG] after import qfluentwidgets")

w = FluentWindow()
w.setWindowTitle("Fluent Test 2")
w.resize(800, 600)
w.show()
sys.exit(app.exec())
