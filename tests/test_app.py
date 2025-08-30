# pylint: disable=E0611,W0613,W0621

import sys
import pytest
from PySide6.QtWidgets import QApplication
from app import MainWindow, GraphWidget


@pytest.fixture(scope="module")
def qt_app():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app


def test_main_window_creation(qt_app):
    window = MainWindow()
    assert window is not None
    assert window.windowTitle() == "PySide6 Graph Example"


def test_graph_widget_creation(qt_app):
    widget = GraphWidget()
    assert widget is not None
