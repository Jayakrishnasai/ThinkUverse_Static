# ThinkUverse

ThinkUverse is a simple Flask application that displays a random inspirational quote and a table of cosmic data. The name is a portmanteau of "Think" and "Universe," reflecting the project's theme of blending imagination and intelligence with the vastness of space.

## Features

-   Displays a random quote from a predefined list.
-   Shows a table of celestial bodies and their properties.
-   Responsive design with a futuristic, space-themed aesthetic.

## Setup and Installation

To get the application running locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ThinkUverse.git
    cd ThinkUverse
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

Once the setup is complete, you can run the application with the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

## Running the Tests

The project includes a test suite to ensure the application is working correctly. To run the tests, first install the testing dependencies:

```bash
pip install pytest pytest-mock
```

Then, run the tests from the root directory:

```bash
python -m pytest tests/
```
