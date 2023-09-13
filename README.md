# git-workshop-python-web-app

This is a sample Python web application for a Git workshop.

## Project Structure

The project has the following files:

- `app/__init__.py`: This file is the entry point of the application. It creates an instance of the Flask app and sets up the routes.
- `app/routes.py`: This file exports the routes for the application. It uses the templates to render the HTML pages.
- `app/templates/base.html`: This file is the base template for the HTML pages. It defines the basic structure of the page and includes the CSS file.
- `app/templates/index.html`: This file is the template for the home page. It extends the base template and includes the content specific to the home page.
- `app/static/style.css`: This file contains the CSS styles for the application.
- `tests/__init__.py`: This file is the entry point for the tests. It sets up the test environment.
- `tests/test_routes.py`: This file contains the tests for the routes of the application. It uses the Flask test client to simulate requests and check the responses.
- `tests/test_templates.py`: This file contains the tests for the templates of the application. It uses the Flask test client to render the templates and check the HTML output.
- `.gitignore`: This file specifies the files and directories that should be ignored by Git.
- `requirements.txt`: This file lists the dependencies of the project.
- `run.py`: This file is the script to run the application. It imports the Flask app from the `app` package and starts the server.
- `README.md`: This file contains the documentation for the project.

## Getting Started

To run the application, you need to install the dependencies listed in `requirements.txt`. You can do this by running:

```
pip install -r requirements.txt
```

Then, you can start the server by running:

```
python run.py
```

The application will be available at `http://localhost:5000`.

## Testing

To run the tests, you need to install the testing dependencies listed in `requirements.txt`. You can do this by running:

```
pip install -r requirements.txt
```

Then, you can run the tests by running:

```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.