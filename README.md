# Fast API Template


## What is this?
This is a simple Fast API project template that I use to test personal POC projects.


## Instructions For Local Development
- Verify Python version 3.9 is installed.
- Run `python -m venv venv` to create a new virtual environment.
- Run `venv\Scripts\activate` to activate the newly created VM.
- Run `python -m pip install -r requirements.txt` to install the packages in the requirements.txt file in the newly created VM.
    - If you need to install a new package, run `python -m pip freeze > requirements.txt` to save it to the requirements.txt file.
- Add a .env file to the solution for the environment variables.
- Run `uvicorn app.main:app --reload` to start the app.
- You can navigate to "{url}/docs" or "{url}/redoc" to load the interactive documentation (Swagger/ReDoc)

> Based on the PluralSight course [Fast API Fundamentals](https://app.pluralsight.com/library/courses/fastapi-fundamentals/table-of-contents) by Reindert-Jan Ekker.