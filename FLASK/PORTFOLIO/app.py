from flask import Flask, render_template, request

app = Flask(__name__)

# Sample skills data
skills = ["Python", "Flask", "HTML/CSS", "JavaScript", "SQL", "Git"]

@app.route('/')
def entry():
    return render_template('entry.html')

@app.route('/intro')
def intro():
    return render_template('home.html', skills=skills)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
