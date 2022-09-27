import sys
from PyQt5.QtCore import pyqtSignal, QProcess
from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar, QVBoxLayout, QApplication, QPlainTextEdit
from PyQt5 import QtCore


class Execute(QWidget):
    """Initialises Qwidget window that contains the 'Run' (execute) button and text dialog box."""

    def __init__(self):
        super(Execute, self).__init__()
        self.p = None
        self.setWindowTitle('Stocks Fund Tracker')
        self.btn = QPushButton('Run')
        self.btn.setGeometry(QtCore.QRect(10, 100, 113, 32))
        self.btn.clicked.connect(self.start_process)
        self.resize(600, 300)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn)
        self.vbox.addWidget(self.text)
        self.setLayout(self.vbox)
        self.show()

    def message(self, s):
        """ Called by function "handle_state" Write messages into the UI text field
        to show current stage of program."""

        self.text.appendPlainText(s)

    def start_process(self):
        """ Execute an external program by creating a QProcess object then call .start()
        with a list argument of the filename to execute.
        Returns new data through standard output channel from stdout within '../app/main.py'.
        """

        self.message("Updating Stocks Fund Tracker.")
        self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.p.readyReadStandardOutput.connect(self.handle_stdout)
        self.p.stateChanged.connect(self.handle_state)
        self.p.finished.connect(self.process_finished)  # Clean up once complete.
        self.p.start("python3", ['../app/main.py'])

    def handle_stdout(self):
        """Returns all data available from the output of the process.
        Function "start_process" is where ".p" (output) is initialised.
        """

        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        """Emits signal when process status changes and displays current status in UI text field."""

        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        """Returns instance of QProcess back to "None" to ensure process can be executed again
        the next time. """

        self.message("Process finished. \nReady to close window.")
        self.p = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Execute()
    ex.show()
    sys.exit(app.exec_())
