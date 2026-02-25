🛒 E-Commerce Automation Framework
Python + Selenium + PyTest + POM
📌 Project Overview

This project is a scalable End-to-End Test Automation Framework developed using Python, Selenium WebDriver, and PyTest to automate an E-commerce web application.

The framework is built using the Page Object Model (POM) design pattern to improve maintainability, reusability, and readability. It automates critical business workflows such as login, product search, add to cart, checkout, and order confirmation.

🚀 Tech Stack

Python 3.x

Selenium WebDriver

PyTest

Page Object Model (POM)

PyTest HTML Reports

Python Logging Module

pytest-xdist (Parallel Execution)

Git & GitHub

Jenkins (CI/CD Integration)

📂 Project Structure
project_root/
│
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│
├── pages/                  # Page Object classes
│   ├── login_page.py
│   ├── product_page.py
│
├── utilities/              # Reusable utilities
│   ├── base_class.py
│   ├── custom_logger.py
│   ├── read_config.py
│
├── testdata/               # Test data files
│
├── reports/                # HTML test reports
│
├── conftest.py             # Fixtures (Setup & Teardown)
├── requirements.txt
├── pytest.ini
└── README.md
🏗 Framework Design Highlights

✔ Page Object Model (POM) implementation
✔ Reusable Base Class for WebDriver initialization
✔ Centralized configuration handling
✔ Custom Explicit Wait utilities
✔ Logging for debugging and traceability
✔ HTML reporting integration
✔ Cross-browser support
✔ Parallel execution support
✔ Command-line execution capability

🔑 Automated Test Scenarios

User Registration

Login / Logout

Product Search

Add to Cart

Remove from Cart

Checkout Process

Order Confirmation

⚙ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶ Running Tests
Run all tests
pytest -v
Run tests in parallel
pytest -n 2
Generate HTML report
pytest --html=reports/report.html --self-contained-html
📊 Reporting

HTML reports generated after execution

Logs captured for debugging

Reports available inside the /reports directory

🔄 CI/CD Integration

This framework supports CI/CD integration using Jenkins:

Automated test execution on code push

Scheduled nightly runs

HTML report publishing

Continuous feedback mechanism

🧠 Key Features

Modular and scalable framework design

Clean and maintainable code structure

Reusable components

Follows automation best practices

Easy to extend for new test scenarios

📌 Future Enhancements

Allure Reporting integration

Docker support

API + UI Hybrid framework

Database validation

Cloud execution (BrowserStack / Sauce Labs)

👤 Author

Omkar Lokare
Python Automation Test Engineer
