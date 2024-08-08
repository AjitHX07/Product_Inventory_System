# Inventory Management System

A full-stack web application for managing inventory using Django (backend) and React (frontend).

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Features

- Inventory CRUD operations
- User authentication and authorization
- Real-time updates

## Installation

### Backend

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/inventory_system.git
   cd inventory_system/backend

2. **Create a virtual environment and activate it**
   ```sh
   python3 -m venv venv
   source venv/bin/activate

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt

4. **Run the migrations:** 
   ```sh
   python manage.py migrate
5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
6. **Run the development server:**
    ```sh

    python manage.py runserver
    
### Frontend
1. **Navigate to the frontend directory:**
    ```sh
    cd ../frontend
2. **Install the dependencies:**
    ```sh
    npm install
3. **Run the development server:**
    ```sh
    npm start

### Usage
- Access the backend:
Open your browser and go to http://127.0.0.1:8000 to access the Django backend.

- Access the frontend:
Open your browser and go to http://localhost:3000 to access the React frontend.

### Technologies Used
- Django
- Django REST framework
- React
- Redux
- Webpack
- Tailwind

### Contributing
1. **Fork the repository.**

2. **Create a new branch:**

   ```sh
   git checkout -b feature/your-feature-name
   
3. **Make your changes and commit them:**

   ```sh
   git commit -m 'Add some feature'
   
4. **Push to the branch:**
   ```sh
   git push origin feature/your-feature-name

5. **Create a pull request.**

### License
- This project is licensed under the MIT License.

### Contact
- Name: Ajith Santhosh
- Email: ajithsanthoshcode07@gmail.com
