# To-do_List

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Description
TodoApp is a simple application for managing your tasks. It allows users to add and remove tasks locally on the system. The app provides an intuitive user interface to organize your tasks efficiently.

## Tech Stack
- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** MySQL

## Demo Video
![](/to-do_app/static/demo.gif)

[Download Demo Video](/to-do_app/static/demo.mp4)

## Installation
To run TodoApp locally, follow these steps:

1. Install the latest versions of Flask and MySQL.
2. Create a MySQL database named `todo`.
3. Create a table named `tasks` in the `todo` database with the following schema:

```sql
CREATE TABLE tasks (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    TASK VARCHAR(50)
);
```

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/Akshar-Vadwala/To-Do_List.git
    ```
2. Navigate to the project directory:
    ```bash
    cd To-Do_List
    ```
3. Run the Flask application:
    ```bash
    python app.py
    ```
4. Access the TodoApp in your web browser at [http://localhost:5000](http://localhost:5000)

