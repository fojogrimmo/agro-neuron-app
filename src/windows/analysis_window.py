from PyQt6.QtWidgets import (QMainWindow, QPushButton, QLabel, 
                           QVBoxLayout, QWidget, QFileDialog, QHBoxLayout,
                           QFrame, QProgressBar)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6.QtCore import Qt

from ..styles.buttons import SECONDARY_BUTTON, DISABLED_BUTTON
from ..widgets.image_preview import ImagePreview

class AnalysisWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анализ всхожести")
        self.setFixedSize(1200, 800)
        self.setWindowIcon(QIcon("images/logo_green.png"))
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Заголовок с разными цветами
        title_layout = QHBoxLayout()
        word1 = QLabel("Анализ")
        word2 = QLabel("всхожести")
        title_font = QFont("Arial", 36, QFont.Weight.Bold)
        word1.setFont(title_font)
        word2.setFont(title_font)
        word1.setStyleSheet("color: #232a42;")
        word2.setStyleSheet("color: #2da884;")
        title_layout.addStretch()
        title_layout.addWidget(word1)
        title_layout.addWidget(word2)
        title_layout.addStretch()
        
        # Область для загрузки изображения
        self.upload_frame = QFrame()
        self.upload_frame.setStyleSheet("""
            QFrame {
                border: 2px dashed #2DA884;
                border-radius: 10px;
                background-color: #F8F9FA;
            }
        """)
        self.upload_frame.setMaximumHeight(400)  # Ограничиваем высоту фрейма
        upload_layout = QVBoxLayout(self.upload_frame)
        upload_layout.setSpacing(20)  # Добавляем отступы между элементами
        
        # Создаем контейнер для текста и кнопки
        text_button_container = QWidget()
        text_button_layout = QVBoxLayout(text_button_container)
        text_button_layout.setSpacing(10)  # Отступ между текстом и кнопкой
        
        self.image_label = QLabel("Выберите изображение для анализа")
        self.image_label.setStyleSheet("color: #232a42;")
        self.image_label.setFont(QFont("Arial", 14))
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.select_button = QPushButton("Выбрать файл")
        self.select_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.select_button.clicked.connect(self.select_image)
        self.select_button.setStyleSheet(SECONDARY_BUTTON)
        
        text_button_layout.addWidget(self.image_label)
        text_button_layout.addWidget(self.select_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Добавляем предпросмотр изображения
        self.image_preview = ImagePreview()
        
        # Добавляем все элементы в upload_layout
        upload_layout.addWidget(text_button_container)
        upload_layout.addWidget(self.image_preview, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Кнопка анализа
        self.analyze_button = QPushButton("Начать анализ")
        self.analyze_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.analyze_button.clicked.connect(self.start_analysis)
        self.analyze_button.setEnabled(False)
        self.analyze_button.setStyleSheet(DISABLED_BUTTON)
        
        # Область результатов (изначально скрыта)
        self.results_widget = QWidget()
        results_layout = QVBoxLayout(self.results_widget)
        
        result_title = QLabel("Результат")
        result_title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        result_title.setStyleSheet("color: #232a42;")
        
        self.percentage_label = QLabel("Процент всхожести: --%")
        self.percentage_label.setFont(QFont("Arial", 18))
        self.percentage_label.setStyleSheet("color: #232a42;")
        
        segmentation_title = QLabel("Размеченная фотография")
        segmentation_title.setFont(QFont("Arial", 18))
        segmentation_title.setStyleSheet("color: #232a42;")
        
        self.result_image = QLabel()
        self.result_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_image.setMinimumHeight(400)
        
        # Кнопки экспорта
        export_layout = QHBoxLayout()
        self.export_pdf = QPushButton("Сохранить в PDF")
        self.export_excel = QPushButton("Сохранить в Excel")
        for btn in [self.export_pdf, self.export_excel]:
            btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
            btn.setStyleSheet(SECONDARY_BUTTON)
        export_layout.addWidget(self.export_pdf)
        export_layout.addWidget(self.export_excel)
        
        results_layout.addWidget(result_title)
        results_layout.addWidget(self.percentage_label)
        results_layout.addWidget(segmentation_title)
        results_layout.addWidget(self.result_image)
        results_layout.addLayout(export_layout)
        
        self.results_widget.hide()
        
        # Добавляем все в главный layout
        layout.addLayout(title_layout)
        layout.addWidget(self.upload_frame)
        layout.addWidget(self.analyze_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.results_widget)
        
        # Прогресс бар (изначально скрыт)
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #2DA884;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #2DA884;
            }
        """)
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)
    
    def select_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )
        if file_name:
            self.selected_image = file_name
            self.image_label.setText(f"Выбрано: {file_name.split('/')[-1]}")
            self.image_preview.set_image(file_name)
            self.analyze_button.setEnabled(True)
            self.analyze_button.setStyleSheet(DISABLED_BUTTON)
    
    def start_analysis(self):
        # Здесь будет код для запуска нейронной сети
        self.upload_frame.hide()
        self.analyze_button.hide()
        self.progress_bar.show()
        self.progress_bar.setValue(0)
        # Имитация прогресса (в реальном приложении здесь будет работа нейросети)
        # После завершения анализа:
        self.show_results()
    
    def show_results(self):
        self.progress_bar.hide()
        self.results_widget.show()
        # Здесь будет код для отображения результатов 