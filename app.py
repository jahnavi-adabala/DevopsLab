from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Registration.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the data from the form
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Print the data (or process it, e.g., save to a database)
    print(f"User registered: {username}, {email}")

    # Redirect back to the form
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
