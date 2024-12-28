from flask_frozen import Freezer
from app import create_app
from flask import url_for
import os
import shutil

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    # Generate URLs with url_for to ensure proper formatting
    yield 'main.index', {}
    yield 'main.projects', {}
    yield 'main.experience', {}
    yield 'main.resume', {}
    yield 'main.skills', {}

if __name__ == '__main__':
    # Clean up existing build directory
    build_dir = app.config['FREEZER_DESTINATION']
    try:
        if os.path.exists(build_dir):
            print(f"Removing existing build directory: {build_dir}")
            shutil.rmtree(build_dir)
            # Ensure the directory is completely removed
            while os.path.exists(build_dir):
                pass
        print(f"Creating fresh build in: {build_dir}")
        os.makedirs(build_dir, exist_ok=True)
    except Exception as e:
        print(f"Error handling build directory: {e}")
        exit(1)
    
    # Create fresh build
    print("Starting freeze process...")
    freezer.freeze()
    print("Freeze complete!") 