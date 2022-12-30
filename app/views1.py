from app import app 
@app.route("/")
def index():
    return "Hello World"

@app.route("/aboutus")
def aboutus():
    return "<h1>About Us</h1>"