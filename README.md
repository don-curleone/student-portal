# Student-Portal

Student-Portal is a Flask-based student portal designed to provide a simple platform for managing student information, courses, tasks, and account settings.

The project is being developed as part of a Git and GitHub workflow exercise, with a focus on practicing version control, branching, merging, conflict resolution, stashing, reflog recovery, and release tagging.


## Requirements

* Python 3.x
* Git
* Flask

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/don-curleone/student-portal.git
cd student-portal
```

### 2. Create a Virtual Environment

Create a Python virtual environment in the project directory:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Flask

With the virtual environment activated:

```bash
pip install Flask
```

## Running the Application

Once the Flask application entry point has been created, it can be started using:

```bash
python app.py
```

The development server will then be available at:

```text
http://127.0.0.1:5000
```
## Logging In

You will be able to login simply by entering anything in the login fields. This was done as this is a Git exercise.


## Project Structure

The project structure will evolve as new features are added.

Current structure:

```text
student-portal/
├── .gitignore
├── README.md
├── app.py
├── templates
    ├── home.html
└── .venv/
```

The `.venv/` directory is intentionally excluded from version control.