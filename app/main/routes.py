from flask import render_template, jsonify, request, current_app
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/projects')
def projects():
    projects = [
        {
            'title': 'Machine Learning Pipeline',
            'description': 'Automated ML pipeline for data processing and model training',
            'technologies': ['Python', 'TensorFlow', 'Docker'],
            'icon': 'cpu',
            'github_link': 'https://github.com/brianboler/ml-pipeline'
        },
        {
            'title': 'Data Visualization Dashboard',
            'description': 'Interactive dashboard for complex data analysis',
            'technologies': ['React', 'D3.js', 'Node.js'],
            'icon': 'bar-chart-2',
            'github_link': 'https://github.com/brianboler/data-viz'
        }
    ]
    return render_template('projects.html', projects=projects)

@bp.route('/experience')
def experience():
    experiences = [
        {
            'title': 'Senior Software Engineer',
            'company': 'Tech Company',
            'period': '2020 - Present',
            'description': 'Led development of machine learning systems and data pipelines',
            'achievements': [
                'Implemented ML models that improved prediction accuracy by 25%',
                'Built scalable data processing pipeline handling 1M+ daily records'
            ]
        }
    ]
    return render_template('experience.html', experiences=experiences)

@bp.route('/resume')
def resume():
    return render_template('resume.html')

@bp.route('/skills')
def skills():
    skills = {
        'languages': ['Python', 'JavaScript', 'Java', 'SQL'],
        'frameworks': ['TensorFlow', 'PyTorch', 'React', 'Flask'],
        'tools': ['Docker', 'AWS', 'Git', 'Linux']
    }
    return render_template('skills.html', skills=skills) 