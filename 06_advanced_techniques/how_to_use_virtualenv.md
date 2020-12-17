# how to use virtual env


### installing
pip install virtual env

### version check
virtualenv --version

### prepration
mkdir project_folder
cd project_folder

### make virtualenv
virtualenv my_project

### virtual environment activate
source my_project/bin/activate

### install required libraries
(my_project)$ pip install requestes
(my_project)$ pip install freeze

### deactivate virtual env
deactivate



##### Creating virtual env failed with following error

FileNotFoundError: [Errno 2] No such file or directory: 'd:\\program files\\anaconda3\\Lib\\venv\\scripts\\nt\\python.exe'

1.Copy python.exe and pythonw.exe from D:\\program files\\anaconda3\\
2.Paste them in D:d:\\program files\\anaconda3\\Lib\\venv\\scripts\\nt\\