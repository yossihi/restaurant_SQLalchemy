# Restaurant Management Web App

This is a web application built using Flask for managing restaurants and user authentication.

## Features

- **User Authentication**: Allows users to register, log in, and log out securely.
- **Restaurant Management**: CRUD (Create, Read, Update, Delete) operations for restaurants.
- **Secure Password Storage**: Passwords are securely hashed using Werkzeug's security features.

## Installation

1. Clone this repository:
    git clone https://github.com/yossihi/restaurant_SQLalchemy.git
2. Install dependencies:
    pip install -r requirements.txt

3. Set up the database:
    - Create a MySQL database named 'restaurants'.
    - Update the `SQLALCHEMY_DATABASE_URI` in `app.py` with your database credentials.

4. Run the application: python app.py

## Usage

- Access the web app through your browser at `http://localhost:5000`.
- Register as a new user or log in with existing credentials.
- Add, edit, or delete restaurants as a logged-in user.
- Log out when finished.

## Tech Stack

- Flask
- SQLAlchemy
- Werkzeug

## Folder Structure

- `templates/`: HTML templates for the web pages.
- `static/`: Static files like CSS, JS, and images.
- `app.py`: The main Flask application file.

## Contributing

Feel free to contribute by forking the repository, making changes, and creating a pull request. Any contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
