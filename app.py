# pylint: disable=E0611

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.label = QLabel("", self)
        self.layout.addWidget(self.label)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.canvas)
        self.button = QPushButton("Show Text", self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.show_text)
        self.plot()

    def plot(self):
        ax = self.canvas.figure.add_subplot(111)
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 4, 9, 16, 25]
        ax.plot(x, y, marker="o")
        ax.set_title("Sample Graph")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")

    def show_text(self):
        self.label.setText("Button Pressed!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Graph Example")
        self.setCentralWidget(GraphWidget(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
