from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/flask')
def flask():
    return render_template("index.html")  
    # The "@" decorator associates this route with the function immediately following
    
@app.route('/jinja')
def jinja_test():
    return render_template("jinja.html")


def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/dojo')
def dojo(): 
    return "Dojo!"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return f"Hi {name}!"



@app.route('/<animal>')
def animals(animal):
    print(animal)
    return f"{animal}s are pretty cool"

# @app.route('/add/<int:x>/<int:y>')
# def calc(x,y):
#     answer = x+y
#     return f"The answer is: {answer}"

# @app.route('/repeat/<int:x>/<var>')
# def repeat(x,var):
#     str = ""
#     for i in range(x):
#         str +=(var)+""
#         return str

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.







# app.run(debug=True, host="localhost", port=8000)
