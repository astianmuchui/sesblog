# sesblog
Simple project for SES Django workshops
## How to Run

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/astianmuchui/sesblog.git
    cd sesblog
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **To activate on windows**:
    ```bash
    cd env/Scripts
    activate
    ```

4. **To activate on unix based systems**:
    ```bash
    source env/bin/activate
    ```

5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Run Database Migrations**:
    ```bash
    python manage.py migrate
    ```
7. **Run the server**:
    ```bash
    python manage.py runserver
    ```

8. **Open the url shown in the terminal**

## And that's it, Happy Hacking!!