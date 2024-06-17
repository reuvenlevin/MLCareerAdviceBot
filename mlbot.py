import Constants
import sys
import openai
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixMap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGroupBox,
    QTextEdit
)
openai.api_key = Constants.API_KEY

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.logo_label = QLabel()
        self.logo_pixmao = QPixmap('robot.jpg').scaled(150,150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo.label.setPixmap(self.logo_pixmap)

        self.input_label = QLabel('Ask a question:')
        self.input_field = QLineEdit()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Type here:')

        self.answer_label = QLabel('Answer')
        self.answer_field.setReadOnly(True)
        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 15px 32px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 10px;

            }
            QPushButton:hover {
                background-color: #3e8e41
            }
            """
        )
        self.popolar_questions_group = QGroupBox('Populor Questions')
        self.popular_questions_layout = QVBoxLayout()
        self.popular_questions = ["What is Machine Learning?", "How to become a Machine Learning Engineer?", "What are the best Machine Learning tools and frameworks"]
        self.question_buttons = []

        # Create a layout
        layout = QVBoxLayout()
        layout.setContentMargins(20,20,20,20)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # Add logo
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        # Add input field and submit button
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.submit_button)
        layout.addLayout(input_layout)

        # Add answer field
        layout.addWidget(self.answer_label)
        layout.addWidget(self.answer_field)

        # Add populor questions button
        for question in self.popular_questions:
            button = QPushButton(question)
            button.setStyleSheet(
            """
            QPushButton {
                background-color: #FFFFFF;
                border: 2px solid #00AEFF;
                color: 00AEFF;
                padding: 10px 20px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 5px;

            }
            QPushButton:hover {
                background-color: #00AEFF
                color: #FFFFFF
            }
            """
            )
            button.clicked.connect(lambda _, q=question: self.input_field.setText(q))
            self.popular_questions_layout.addWidget(button)
        self.popolar_questions_group.setLayout(self.popular_questions_layout)
        layout.addWidget(self.popular_questions_group) 

        # Set the layout
        self.setLayout(layout)

        # Set windows property
        self.setWindowTitle("Machine Learning Career Advice Bot")
        self.setGeometry(200,200,600,600)

        # Connect submit button to Openai API
        self.submit_button.clicked.connect(self.get_answer)

        def get_answer(self):
            question = self.input_field.text()

            completion = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messeges = [{"role":"user", "content":"You are a machine learning engineer expert. Answer the following question in a concise way or with bullet points."},
                            {"role":"user", "content":f'{question}'}],
                max_tokens = 1024,
                n = 1,
                stop = None,
                temperature = 0.7            
            )

            answer = completion.choices[0].message.content

            self.answer_field.setText(answer)
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        






