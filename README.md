# pytest automation
Weather API testing

The Framework dependecies: 
  - Python 3.8
  - PyCharm Community Edition
  - python virtual environment with required libraries


Setup Python Virtual Environment:
Make sure python 3 is your base interpreter. Use PyEnv and Homebrew to configure your global python version
https://opensource.com/article/19/5/python-3-default-mac

1) cd into the directory where you want to create you python virtual environment
2) python3 -m venv [name_of_virtual_env]         # Create virtual environment (if it doesn't work then use just python )
3) source [name_of_virtual_env]/bin/activate    # This activates the virtual environment
4) pip install -r ./requirements.txt # This installs all of the project requirements and the local packages 


Once you have this done you can either run your tests directly from the terminal by going into the directory
where the pytests are held or you can go into your pycharm preferences and attach the python executable of your created
virtual environment to the interpreter. This can be done under PyCharm-->Preferences-->Project Interpreter. Click the
wheel to add existing environment and navigate to the python executable of your virtual environment.

# Run these commands in the directory containing the Pytests
pytest -v --env=dev  # run all tests

pytest -v --env=dev  -m "smoke"          # run smoke tests in DEV

pytest -v --env=dev  -m "not smoke"     # run all tests except smoke test
