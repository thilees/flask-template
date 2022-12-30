from app import app 
@app.route("/admin")
def admin():
    return "Admin"

@app.route("/contact")
def contact():
    return "<h1>contact</h1>"