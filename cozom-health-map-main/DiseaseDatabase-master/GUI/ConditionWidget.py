from PyQt5.QtWidgets import QWidget, QMessageBox
from .generated.Condition import Ui_condition
import webbrowser
import validators

class ConditionWidget(QWidget):
    def __init__(self, parent = None):
        super(ConditionWidget, self).__init__(parent)
        self.ui = Ui_condition()

        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    # Set fields to the given condition.
    def set(self, condition):
        self.condition = condition

        self.ui.condition_name.setText(condition.name)
        self.ui.condition_about.setText(condition.about)
        self.ui.weight_value.setText(str(condition.weight))

    def mousePressEvent(self, QMouseEvent):
        if validators.url(self.condition.about):
            # Update URL to Cozom branding if required
            updated_url = self.condition.about.replace("www.WebMD.com", "www.cozom.in")
            webbrowser.open(updated_url)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(self.condition.about)
            msg.setWindowTitle("Cozom - Condition Information")
            msg.exec_()
