import os
import sys

if os.environ.get('SERVER_ENV') is None:
    # Local Development
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from GUI.About import About
    from data import readDatabase
    from GUI.Diagnose import Diagnose

    if __name__ == "__main__":
        database = readDatabase('./data')
        app = QApplication(sys.argv)
        diagnose = Diagnose(database)
        about = About(diagnose)
        about.show()
        sys.exit(app.exec_())
else:
    # Server Mode
    print("Running in server mode - GUI components disabled")
    # You can add server-specific logic here
