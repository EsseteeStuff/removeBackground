# removeBackground
Remove backgrounds from images

Needed: python >= 3.7

For windows users who don't have python installed, download the latest version from https://www.python.org.
Don't forget to check the option to add the python executable to your environment path!

If you get an error that you cannot execute scripts when you start your virtual environment:

Dutch : visit https://terryn-serge.be/html/8

English: right click start button -> Settings -> Update & Security -> For Developers -> Scroll to Powershell and click the Apply button.


1. Make a virtual environment.

    python3 -m venv venv

2. Activate the environment.

    a. linux and mac:
        source venv/bin/activate

    b. windows:
        venv\Scripts\Activate.ps1

3. In your virtual environment run:

    pip install -r requirements.txt

4. Run the application:

    python3 ./app.py

The first time you run the application it needs some extra time to show the interface.
It will pull from github some extra code from the developer Daniel Gatis github page.
https://github.com/danielgatis/rembg



