import sys
sys.path.append('./DiseaseDatabase-master')

from GUI.About import About
from GUI.Diagnose import Diagnose
from PyQt5.QtWidgets import QApplication
from WebMD.reader import readDatabase

if __name__ == '__main__':
    database = readDatabase('./DiseaseDatabase-master/data')
    print(database)
    app = QApplication(sys.argv)
    diagnose = Diagnose(database)
    about = About(diagnose)
    about.show()
    sys.exit(app.exec_())
