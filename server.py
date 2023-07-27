from flask import Flask, render_template, request, redirect, url_for
import subprocess
import sqlite3
import time


app = Flask(__name__)

# Configure SQLite database
DATABASE = "form_data.db"


def init_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS form_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        car_name TEXT NOT NULL,
        year TEXT NOT NULL,
        distance TEXT NOT NULL,
        owner TEXT NOT NULL,
        fuel TEXT NOT NULL,
        location TEXT NOT NULL,
        drive TEXT NOT NULL,
        type TEXT NOT NULL
    )
    """
    )
    conn.commit()
    conn.close()


init_database()


@app.route("/")
def index():

    car_names = ['maruti s presso' ,'hyundai xcent', 'Other', 'maruti vitara brezza'
 'tata tiago', 'maruti swift', 'hyundai i20' ,'renault kwid',
 'hyundai grand i10', 'maruti ignis', 'honda brio', 'hyundai elite i20',
 'honda city', 'maruti baleno', 'honda wr-v', 'honda amaze', 'maruti alto 800',
 'maruti celerio' ,'ford ecosport', 'maruti ciaz' ,'datsun redi go',
 'hyundai santro xing' ,'ford freestyle', 'maruti dzire', 'maruti alto',
 'hyundai new santro' ,'maruti alto k10', 'maruti swift dzire',
 'maruti wagon r 1.0' ,'hyundai grand i10 nios', 'maruti celerio x',
 'mahindra xuv500' ,'hyundai verna' ,'hyundai venue' ,'tata nexon',
 'toyota yaris', 'renault triber', 'renault duster' ,'hyundai i10',
 'nissan magnite', 'maruti ertiga' ,'honda jazz' ,'kia seltos',
 'volkswagen ameo' ,'renault kiger' ,'hyundai new i20', 'tata altroz',
 'maruti ritz', 'hyundai eon' ,'hyundai creta' ,'toyota etios liva',
 'maruti new wagon-r' ,'tata tigor' ,'volkswagen polo',
 'toyota corolla altis', 'volkswagen vento', 'maruti s cross',
 'hyundai i20 active' ,'hyundai aura' ,'skoda rapid', 'toyota etios']
    

    years = ['2022.0', '2018.0' ,'2021.0' ,'2019.0', '2017.0', '2012.0', '2015.0', '2014.0',
 '2016.0', '2010.0' ,'2011.0' ,'2013.0', '2020.0', 'None' , '2023.0']
    

    owners = ['1', '2', '3', '4']
    

    fuels = ['PETROL' ,'DIESEL', 'CNG', 'Other']
    
    

    drives = ["Manual","Automatic"]
    
    

    types = ['HatchBack', 'Sedan', 'SUV', 'Lux_SUV', 'Lux_sedan']

    # with open('readme.txt', 'r') as file:
    #     content = file.read()

    return render_template("index.html", car_names=car_names,  drives=drives, owners=owners, years=years, fuels=fuels ,types=types) 

def run_jupyter_notebook():
    try:
        # Replace 'your_notebook.ipynb' with the actual path to your Jupyter Notebook file.
        # You can use the full path or a relative path based on your project structure.
        process = subprocess.Popen(['jupyter', 'notebook', 'main_jupy_note.ipynb'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Jupyter Notebook is running in the background.")
    except subprocess.CalledProcessError as e:
        # Handle any errors if the notebook couldn't be launched.
        print(f"Error running Jupyter Notebook: {e}")


@app.route("/run_jupyter")
def run_jupyter():
    # Call the function to run the Jupyter Notebook in the background
    run_jupyter_notebook()
    return "Jupyter Notebook is running..."

@app.route("/wait")
def wait():
    # Render the wait.html template
    return render_template("wait.html")

    
@app.route("/success")
def success():

    # Read the content from result.txt after 40 seconds
    with open('result.txt', 'r') as file:
        content = file.read()
    
    # Pass the content to the success.html template and render it
    return render_template("success.html", content=content)


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    car_name = request.form["car_name"]
    year = request.form["year"]
    distance = request.form["distance"]
    owner = request.form["owner"]
    fuel = request.form["fuel"]
    location = request.form["location"]
    drive = request.form["drive"]
    car_type = request.form["type"]

    # Store the form data in the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO form_data (name, email, car_name, year, distance, owner, fuel, location, drive, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (name, email, car_name,  year, distance,owner, fuel, location, drive, car_type),
    )
    conn.commit()
    conn.close()

    return redirect(url_for("wait"))


# @app.route("/success")
# def success():
#     return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
