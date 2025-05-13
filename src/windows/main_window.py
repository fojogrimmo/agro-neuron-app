from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QPainter, QFont, QIcon
from PyQt6.QtCore import Qt, QPoint

from ..styles.buttons import PRIMARY_BUTTON
from .analysis_window import AnalysisWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анализ всхожести посевных площадей")
        self.setFixedSize(1200, 800)
        self.setWindowIcon(QIcon("images/logo_green.png"))
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Создаем заголовок
        title_label = QLabel("Анализ всхожести посевных площадей")
        title_label.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Создаем подзаголовок
        subtitle_label = QLabel("Искусственный интеллект проанализирует снимки полей и\nоценит всхожесть семян за минуты")
        subtitle_label.setFont(QFont("Arial", 18))
        subtitle_label.setStyleSheet("color: white;")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Создаем кнопки
        self.start_button = QPushButton("Начать анализ")
        self.how_it_works_button = QPushButton("Как это работает?")
        
        # Применяем стили к кнопкам
        self.start_button.setStyleSheet(PRIMARY_BUTTON)
        self.how_it_works_button.setStyleSheet(PRIMARY_BUTTON)
        
        # Подключаем обработчики кнопок
        self.start_button.clicked.connect(self.open_analysis_window)
        
        # Добавляем виджеты в layout
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addSpacing(30)
        layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.how_it_works_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        
        # Настраиваем фоновое изображение
        self.background_image = QPixmap("images/background_image.jpg")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        scaled_image = self.background_image.scaled(
            self.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        
        x = (self.width() - scaled_image.width()) // 2
        y = (self.height() - scaled_image.height()) // 2
        
        painter.drawPixmap(QPoint(x, y), scaled_image)
    
    def open_analysis_window(self):
        self.analysis_window = AnalysisWindow()
        self.analysis_window.show() 