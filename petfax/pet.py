# from flask import Blueprint, render_template
# import json

# # Load pet data from 'pets.json'
# pets = json.load(open('pets.json'))
# print(pets)

# # Create a Blueprint named 'pet' with the URL prefix '/pets'
# bp = Blueprint('pet', __name__, url_prefix='/pets')

# # Define a route for the index page
# @bp.route('/')
# def index():
#     # Render the 'index.html' template and pass the 'pets' data
#     return render_template('index.html', pets=pets)
from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)