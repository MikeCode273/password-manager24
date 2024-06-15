# Password Manager

A simple password manager built with Python and Tkinter. This application allows users to generate secure passwords, save them along with associated website and email/username, and retrieve saved passwords.

## Features

- **Password Generation**: Generate strong and random passwords.
- **Save Passwords**: Save website, email/username, and password pairs to a JSON file.
- **Retrieve Passwords**: Search and retrieve saved passwords.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)
- JSON (included in the Python standard library)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/password-manager.git
    cd password-manager
    ```

2. **Ensure you have Python and Tkinter installed:**

    - For most systems, Tkinter is included with Python. If not, install it using your package manager.

3. **Run the application:**

    ```sh
    python password_manager.py
    ```

## Usage

1. **Generate Password:**
    - Click the "Generate Password" button to create a random password. The generated password will be inserted into the password input field.

2. **Save Password:**
    - Enter the website, email/username, and password.
    - Click the "Add" button to save the information. The data is saved in `data.json`.

3. **Search Password:**
    - Enter the website name in the website input field.
    - Click the "Search" button to retrieve the saved email/username and password for the website.

## File Structure

- `password_manager.py`: Main application code.
- `data.json`: JSON file where the passwords and associated data are stored.
- `logo.png`: Image file for the application logo.

## Screenshots

![App Screenshot](screenshot.png)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various password manager applications.
- Built with [Tkinter](https://docs.python.org/3/library/tkinter.html) and Python.
