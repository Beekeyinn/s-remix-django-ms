# Django Project Setup

This is a boilerplate project for setting up a Django app as a microservice for a Shopify Remix app.

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- Python 3.x (recommended 3.10)
- Poetry

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Beekeyinn/s-remix-django-ms
   ```

2. Change into the project directory:

   ```bash
   cd s-remix-django-ms
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install Packages

   ```bash
   pip install poetry
   ```

   ```bash
   poetry install
   ```

6. Lets copy .env.example to .env

   ```bash
   cp .env.example .env
   ```

7. Fill all the required parameters in .env file.

8. Inspect Remix Database (incase of change in remix side. if its setup phase no need to run it)

   ```
   python manage.py inspectremix > apps/remix/models.py
   ```

9. Manage all the inspected models field for django admin side.

10. Create django schema in postgres before migrate

11. Run database migrations:

    ```bash
    python manage.py migrate
    ```

12. Start the development server:

    ```bash
    python manage.py runserver
    ```

13. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to see your Django app in action!

## Usage

- Update the Django app according to your project requirements.
- Integrate with Shopify API as needed.
- Customize the project structure and templates to fit your needs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
