# CS4900-Project-1

### Setup Prerequisites
[1. Download Python 3.10.7](https://www.python.org/downloads/)

[2. Download PyCharm](https://www.jetbrains.com/pycharm/)

#### 3. Installing Pip

##### Unix/macOS
`python3 -m pip install --user --upgrade pip`
`python3 -m pip --version`

##### Windows
`py -m pip install --upgrade pip`
`py -m pip --version`

#### 4. Run the following to install pytest
`pip install -U pytest`

#### 5. Run the following to ensure that pytest installed successfully
`$ pytest --version
pytest 7.1.3`

#### 6. Run the following to install pytest-xdist
`pip install pytest-xdist`

#### 7. Run the following to ensuyre pytest-xdist installed successfully
`pip show pytest-xdist`

### Project Setup
1. On the 'Welcome to Python' window, click 'Get From VCS.'
2. In the 'Get from Version Control' window, paste this url into the URL text box: https://github.com/JakeKonkowski/CS4900-Project-1.git
3. Click Clone. The directory can be changed if desired.
4. Trust the project when prompted.
5. When the project opens, expand the 'External Libraries' folder in the project window to ensure the project is using Python 3.10. 
   1. If your project is not using Python 3.10, open the 'File' tab.
   2. Click settings.
   3. Expand 'Project: CS4900-Project-1' and click the 'Python Interpreter' tab.
   4. Select 'Python 3.10' from the 'Python Interpreter' drop-down.
   5. Click 'Ok'.
