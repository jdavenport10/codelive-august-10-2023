# Codelive - August 10, 2023 - Integrating GPT into Salesforce

### Running this project

You'll need to have Python installed in your environment, if you don't have that go to https://www.python.org/downloads/ and install the proper version.

From the command line, in this directory, run the following commands:

1. Create a virtual environment: `python -m venv codelive`
2. Active our virtual environment: `source codelive/bin/activate`
3. Install required packages: `pip install -r requirements.txt`
4. Boot the API: `python -m uvicorn app.main:create_app --reload --port 8000`


If you want to work with the `.ipynb` notebook, you can just open it in VS Code, and choose your `codelive` environment from the drop down in the top right. You still need to go through steps 1-3 of the above, but you can avoid 4 for the notebook.
