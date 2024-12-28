from flask import render_template, jsonify
from flask_login import login_required
from app.main import bp
from app.models import Project, Experience, Achievement

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
            'image': 'ml_pipeline.jpg',
            'github_link': 'https://github.com/brianboler/ml-pipeline'
        },
        {
            'title': 'Data Visualization Dashboard',
            'description': 'Interactive dashboard for complex data analysis',
            'technologies': ['React', 'D3.js', 'Node.js'],
            'image': 'data_viz.jpg',
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

@bp.route('/api/profile')
def get_profile():
    profile = {
        'name': 'Brian Boler',
        'title': 'Software Engineer & Data Scientist',
        'bio': 'Experienced software engineer specializing in machine learning and data science',
        'skills': {
            'languages': ['Python', 'JavaScript', 'Java'],
            'frameworks': ['TensorFlow', 'PyTorch', 'React'],
            'tools': ['Docker', 'AWS', 'Git']
        }
    }
    return jsonify(profile) 