from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you can add code to handle the form submission, like sending an email
        
        # For now, let's just print the values
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        return render_template('thankyou.html', name=name)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
