from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return """
    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask app.</p>
    <a href="/form">Go to the form</a>
    """

# Define a route for the form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"<h1>Thank You, {name}!</h1><p>Your message has been received.</p>"
    return """
    <h1>Contact Form</h1>
    <form method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br><br>
        
        <button type="submit">Submit</button>
    </form>
    """

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
