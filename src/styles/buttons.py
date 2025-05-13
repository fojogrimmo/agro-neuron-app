PRIMARY_BUTTON = """
    QPushButton {
        background-color: #2DA884;
        color: white;
        border: none;
        padding: 15px 25px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 18px;
    }

    QPushButton:hover {
        background-color: #6BC0A8;
        color: #fff;
    }

    QPushButton:pressed {
        background-color: #ABE6D5;
    }
"""

SECONDARY_BUTTON = """
    QPushButton {
        background-color: #2DA884;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: bold;
        border-radius: 15px;
    }

    QPushButton:hover {
        background-color: #6BC0A8;
    }

    QPushButton:pressed {
        background-color: #ABE6D5;
    }
"""

DISABLED_BUTTON = """
    QPushButton {
        background-color: #2DA884;
        color: white;
        border: none;
        padding: 15px 25px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 18px;
    }

    QPushButton:disabled {
        background-color: #cccccc;
    }

    QPushButton:hover:!disabled {
        background-color: #6BC0A8;
    }

    QPushButton:pressed:!disabled {
        background-color: #ABE6D5;
    }
""" 