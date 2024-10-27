import sys
import os

from WebMD.reader import readDatabase

# Check if the server environment is set
if os.environ.get('SERVER_ENV') is None:
    from PyQt5.QtWidgets import QApplication
    from GUI.About import About
    from GUI.Diagnose import Diagnose

    # Local Development
    if __name__ == '__main__':
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
