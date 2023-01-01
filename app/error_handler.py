from app import app 
from flask import render_template, request

@app.errorhandler(404)
def not_found(e):
    return f"page not found - custom page"