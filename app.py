from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/attendance')
def attendance():
    return render_template('attendance.html')

if __name__ == '__main__':
    app.run(debug=True)