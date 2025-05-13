from PyQt6.QtWidgets import QLabel, QFrame
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class ImagePreview(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        self.setFixedSize(150, 150)
        self.setStyleSheet("""
            QFrame {
                border: 2px solid #2DA884;
                border-radius: 10px;
                background-color: #F8F9FA;
            }
        """)
        
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(130, 130)
        self.image_label.move(10, 10)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("""
            QLabel {
                border: none;
                background-color: transparent;
            }
        """)
        self.clear_preview()
    
    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(
            130, 130,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.image_label.setPixmap(scaled_pixmap)
    
    def clear_preview(self):
        self.image_label.setText("Нет\nизображения")
        self.image_label.setStyleSheet("""
            QLabel {
                border: none;
                background-color: transparent;
                color: #232a42;
            }
        """) 