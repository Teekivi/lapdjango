# lapdjango
A basic news site project intended as a quick introduction to Django.


## Links

* [Introduction to Django (in Estonian)](https://docs.google.com/presentation/d/1rK1J2V_wk7GlBRs2fMXmEc-Zfuby_jPrlnA4q7-MMWM/edit?usp=sharing)
* [Tasks](https://docs.google.com/document/d/10XtiKnR107ajXBDEUUUz5LF1_WkwDlxRNaqRgH3EHiA/edit?usp=sharing)


## Requirements

* Python>=3.4
* Django==2.0


## Getting started

1. Clone the project or use "Checkout from Version Control" in PyCharm.
2. Create a new virtualenv and activate it either in PyCharm or in a command line:
    ```
    cd lapdjango
    python3 -m venv venv
    . venv/bin/activate    # Linux / macOS
    venv\Scripts\activate  # Windows
    ```
3. Install the dependencies either in PyCharm or in a command line:
    ```
    # Continuing in the lapdjango directory
    pip install -r requirements.txt
    ```
4. Run initial migrations, create a superuser and start the Django development server:
    ```
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```
5. The server now auto-reloads on (most) source file changes, so most of the time, there is no
   need to restart the server manually.


## Author

The project, introduction and tasks were authored by Magnus Teekivi.

&copy; 2018
