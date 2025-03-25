from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    project_data = [
        {
            'title': 'Facial Expression Recognizer',
            'description': 'A real-time emotion recognition system using a custom-trained CNN on FER-2013 and personal data. Built with TensorFlow and OpenCV, it detects expressions like happy, sad, disgust, fear, angry, neutral or surprise live from your webcam. The model was fine-tuned using class weighting and performance evaluated via confusion matrix and validation metrics.',
            'images': ['images/project11.png', 'images/project12.png']
        },
        {'title': 'Sentiment-Aware Stock Risk Analyzer for New Investors', 'description': 'Description of project 2', 'images': ['static/images/project2.jpg']},
        {'title': 'Air Quality Monitoring System', 'description': 'Description of project 3', 'images': ['static/images/project3.jpg']},
        {'title': 'Project 4', 'description': 'Description of project 4', 'images': ['static/images/project4.jpg']},
    ]
    return render_template('projects.html', projects=project_data)
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
