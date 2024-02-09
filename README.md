# BOOK MANAGEMENT SYSTEM

Book management system is a project created using Django Framework which is Python supported for dealing with implementation of website development.

## Django installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django. Type the below command in terminal.

```bash
pip install django
```

## Cloning

Navigate to the directory where you want to clone the project using the cd command. <br>
Use the git clone command followed by the repository URL.

```bash
git clone https://github.com/Gemish14/Book-Management-Task.git
```
This command will create a directory "Book Management Task" in your current location and clone the contents of the GitHub repository into that directory.


## Setup database

Run migrations in your terminal

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the server

To run your project go to your terminal
<br> Locate to the path where the project is cloned and type this

```bash
python manage.py runserver
```

## View the website 
After you start your server the terminal will prompt a URL
Redirect to main webpage by clicking with Ctrl + Right Click on that URL
<br>
<b>OR ELSE</b>
<br>
Open a web browser and go to this [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view and interact with the application.
