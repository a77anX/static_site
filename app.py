from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    # Render the HTML and save to a file
    with app.app_context():
        with open("static_site/index.html", "w") as file:
            file.write(render_template("index.html"))
    print("Static site generated in static_site/index.html")
