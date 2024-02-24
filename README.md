# Logging Class

## Introduction
This project is designed to simplify log recording for applications. The idea is to provide an easy and straightforward way for users to record their logs. It can be saved in CSV, XLSX, or even a database. This tool is prepared for all these functionalities.

## Installation and Setup
To get started, follow these steps:
1. Clone the repository: `git clone [repository URL]`
2. Install the following libraries:
    - `pip install pandas`
    - `pip install sqlalchemy`
    - `pip install pymysql`
    - `pip install openpyxl`
    - Note: The `sqlalchemy` and `pymysql` librarys is only necessary if you wish to save data to a database.
3. Now you are ready to use the Logging Class.

## Usage
To use this project, access the `example.ipynb` file to understand its implementation. This file includes two examples: one on how to use the class to record data in a MySQL database and another on how to save data in CSV or XLSX format.

## Database Configuration
Remember, for the database, you must have a pre-configured MySQL database. To configure our class to store data in a database, simply set it up in the `db_config.json` file.

## Feedback
Feel free to use this class extensively, as you can never have too many logs, haha. If you have any criticism or suggestions for the class, I am open to new ideas.

## 📌 Version
The version of project is 1.0.0.0.0

## ✒️ Autor
* **Desenvolvedor** - *Developer of application* - [Matheus de Ornelas Vasconcellos](https://github.com/MatheusOrnelas)