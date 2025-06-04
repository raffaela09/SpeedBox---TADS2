# 🚀 SpeedBox

Delivery system with order management, developed with object-oriented structure.

## Index

- About

- Class Diagram

- Features

- Technologies

- How to Use

## 📑 About

SpeedBox is a Python-based delivery management system, using OOP with inheritance, encapsulation, and class association. It uses JSON files for data persistence and the bcrypt library for secure authentication via password hashing.  
The system manages orders with unique codes, supports multiple payment methods, offers flexibility for different types of transport, and integrates with the Open Route Service API to provide routing and geolocation features, ensuring scalability and security for operations.

## 📌 Class Diagram

![Class Diagram](image/diagrama.jpg)

## ✔️ Features

- Customer registration  
- Delivery estimation  
- Order management  
- History visualization  
- Login with authentication for multiple profiles  

## 💻 Technologies

- Python  
- JSON  
- bcrypt
- OpenRouter API 

## 🧪 How to Use

1. Clone the repository:  
Clone the project and access the folder:
```bash
git clone https://github.com/raffaela09/SpeedBox---TADS2.git
cd SpeedBox--TADS2
```

2. Download dependencies:  
```bash
pip install -r requirements.txt
```

3. Run the application:  
Execute the `main_menu.py` file with Python:
```bash
python main_menu.py
```
