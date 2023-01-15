import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):

    def __init__(self):
        super().__init__()

        # Create a QWebEngineView
        self.view = QWebEngineView(self)

        # Set the url
        self.view.setUrl(QUrl("https://www.google.com"))

        # Create the URL bar
        self.url_bar = QLineEdit(self)

        # Create the back button
        self.back_button = QPushButton("<", self)
        self.back_button.clicked.connect(self.view.back)

        # Create the forward button
        self.forward_button = QPushButton(">", self)
        self.forward_button.clicked.connect(self.view.forward)

        # Create the refresh button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.view.reload)

        # Create the bookmark button
        self.bookmark_button = QPushButton("Add Bookmark", self)
        self.bookmark_button.clicked.connect(self.add_bookmark)

        # Create the bookmark bar
        self.bookmark_bar = QLineEdit(self)
        self.bookmark_bar.setReadOnly(True)

        # Create the layout
        layout = QVBoxLayout()

        # Add the URL bar and the web view to the layout
        layout.addWidget(self.url_bar)
        layout.addWidget(self.view)

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Add the buttons to the layout
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.bookmark_button)

        # Add the button layout and the bookmark bar to the main layout
        layout.addLayout(button_layout)
        layout.addWidget(self.bookmark_bar)

        # Create a central widget to hold the layout
        widget = QWidget(self)
        widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(widget)

    def add_bookmark(self):
        url = self.view.url().toString()
        self.bookmark_bar.setText(url)

# Create a QApplication
app = QApplication(sys.argv)

# Create and show the browser
browser = Browser()
browser.show()

# Run the main Qt loop
sys.exit(app.exec_())