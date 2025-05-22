from PyQt6.QtWidgets import (QMainWindow, QLabel, QVBoxLayout, 
                           QWidget, QHBoxLayout, QFrame, QSizePolicy,
                           QPushButton)
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt

from ..styles.buttons import PRIMARY_BUTTON

class InfoCard(QFrame):
    def __init__(self, image_path, title, description, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                padding: 15px;
            }
        """)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setFixedWidth(350)
        self.setFixedHeight(550)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Изображение
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Ошибка загрузки изображения: {image_path}")
            image_label.setText("Ошибка загрузки\nизображения")
            image_label.setStyleSheet("color: red;")
        else:
            scaled_pixmap = pixmap.scaled(320, 200, Qt.AspectRatioMode.KeepAspectRatio, 
                                        Qt.TransformationMode.SmoothTransformation)
            image_label.setPixmap(scaled_pixmap)
        image_label.setFixedSize(320, 200)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Заголовок
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #232A42;")
        title_label.setWordWrap(True)
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # Описание
        description_label = QLabel(description)
        description_label.setFont(QFont("Arial", 12))
        description_label.setStyleSheet("color: #525252;")
        description_label.setWordWrap(True)
        description_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        layout.addWidget(image_label)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addStretch()

class HowItWorksWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Как это работает?")
        self.setFixedSize(1200, 850)
        self.setWindowIcon(QIcon("images/logo_green.png"))
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(40, 40, 40, 40)
        
        # Заголовок с разными цветами
        title_layout = QHBoxLayout()
        word1 = QLabel("Принцип")
        word2 = QLabel("Работы")
        title_font = QFont("Arial", 36, QFont.Weight.Bold)
        word1.setFont(title_font)
        word2.setFont(title_font)
        word1.setStyleSheet("color: #232A42;")
        word2.setStyleSheet("color: #2DA884;")
        title_layout.addStretch()
        title_layout.addWidget(word1)
        title_layout.addWidget(word2)
        title_layout.addStretch()
        
        # Подзаголовок
        subtitle = QLabel("Как программа анализирует фото поля и определяет всхожесть пшеницы")
        subtitle.setFont(QFont("Arial", 16))
        subtitle.setStyleSheet("color: #525252;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Карточки с информацией
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(20)
        
        cards_data = [
            {
                "image": "images/infoimg_1.png",
                "title": "Захват и подготовка изображения",
                "description": "Пользователь загружает фото поля, сделанное с "
                             "дрона или телефона. Система автоматически "
                             "подготавливает изображение: изменяет размер, "
                             "повышает контраст и удаляет лишние элементы. "
                             "Это необходимо, чтобы модель могла точно "
                             "распознать участки почвы и всходы."
            },
            {
                "image": "images/infoimg_2.png",
                "title": "Обнаружение пустых участков нейросетью",
                "description": "Используется обученная нейросеть, которая "
                             "разбивает изображение на зоны и определяет "
                             "участки, где пшеница не взошла. Модель "
                             "обучена на более чем 14 тыс. изображений и "
                             "точно различает даже частичные всходы. "
                             "Результат — карта разметки с выделенными "
                             "\"проблемными\" зонами."
            },
            {
                "image": "images/infoimg_3.png",
                "title": "Подсчёт всхожести и создание отчёта",
                "description": "На основе анализа система вычисляет процент "
                             "всхожести и визуализирует пустые зоны на фото. "
                             "Результат можно сохранить в виде отчёта (PDF "
                             "или Excel). Программа поможет быстро оценить "
                             "эффективность посева и принять меры по "
                             "улучшению урожайности."
            }
        ]
        
        for card_data in cards_data:
            card = InfoCard(
                card_data["image"],
                card_data["title"],
                card_data["description"]
            )
            cards_layout.addWidget(card)
        
        # Добавляем все элементы в главный layout
        main_layout.addLayout(title_layout)
        main_layout.addWidget(subtitle)
        main_layout.addSpacing(20)
        main_layout.addLayout(cards_layout)
        main_layout.addStretch()
        
        # Добавляем кнопку закрытия
        close_button = QPushButton("Вернуться на главную")
       
        close_button.setStyleSheet(PRIMARY_BUTTON)
        close_button.clicked.connect(self.close)
        
        # Создаем контейнер для кнопки с центрированием
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        
        main_layout.addWidget(button_container)