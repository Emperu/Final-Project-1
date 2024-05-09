from PyQt5.QtWidgets import QApplication
from gui import GuiWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = GuiWindow()
    main_win.show()
    sys.exit(app.exec_())
