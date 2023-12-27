# How It Works?

## Install the Project

First, download the project or clone it. Ensure that the project's inner folder is available on your machine.

**Inner Project Folder: BakeryMSys**

Once available, your folder content should look like this:

- BakeryMSys
- .gitignore
- requirements.txt

If everything is fine, then you have to run some commands in your terminal!

1. Install `virtualenv` if not available globally.

    ```bash
    pip list
    ```

    If you find `virtualenv`, that's fine. If not, run the following command:

    ```bash
    pip install virtualenv
    ```

2. Create a new virtual environment by running the following command:

    ```bash
    virtualenv venv
    ```

    Now you should see a new folder in your directory named `venv`. This is important to install the requirements.

3. Install the requirements by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure the `requirements.txt` is in the Present Working Directory (PWD).

4. If everything worked fine and no errors are found, then **Congratulations!** The installation worked as expected!

## Run the Project

Now it's time to run the project!

1. Assuming the installation process worked fine, the next step is to check the directory structure:

    - BakeryMSys
    - venv
    - .gitignore
    - requirements.txt

    If the directory structure is fine, it's time to run the project.

2. Run the following command in your terminal:

    ```bash
    cd BakeryMSys
    ```

    You should be able to see a file named `manage.py`. If yes, then run the following command in the terminal:

    ```bash
    python manage.py runserver
    ```

    If you see an output, **Congratulations**, the project is up and running!

3. Go into any browser on your machine and enter the following URL in the search bar:

    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    Now, log in to the site:

    - Email: example@gmail.com
    - Password: 123

    There will be some test data!

Now you can expand the project, fix any issues, and customize it as you want!
