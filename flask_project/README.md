# Flask Project

This is a basic Flask project structure.

## Structure

- `app.py`: The main application file where the Flask app is defined.
- `config.py`: Configuration file for the Flask app.
- `requirements.txt`: List of dependencies to be installed.
- `.gitignore`: A list of files and directories to be ignored by git.
- `templates/`: Directory for Jinja2 templates.
- `static/`: Directory for static files like CSS, JavaScript, and images.
- `modules/`: Directory for modular components of the app such as blueprints.

## Setup

To set up the project, install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Then, run the Flask application:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.