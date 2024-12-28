from flask_frozen import Freezer
from app import create_app
import os

app = create_app()
freezer = Freezer(app)

@freezer.register_generator
def url_generator():
    # Generate URLs for all pages
    yield 'main.index'
    yield 'main.projects'
    yield 'main.experience'
    yield 'main.skills'
    yield 'main.resume'

if __name__ == '__main__':
    # Clean up existing build directory
    build_dir = app.config['FREEZER_DESTINATION']
    if os.path.exists(build_dir):
        print(f"Removing existing build directory: {build_dir}")
        for root, dirs, files in os.walk(build_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(build_dir)
    
    # Create fresh build directory
    print(f"Creating fresh build directory: {build_dir}")
    os.makedirs(build_dir, exist_ok=True)
    
    # Create static directories
    os.makedirs(os.path.join(build_dir, 'static', 'css'), exist_ok=True)
    
    # Run freeze
    print("Starting freeze process...")
    freezer.freeze()
    print("Freeze complete!")
    
    # Debug output
    print("\nGenerated files:")
    for root, dirs, files in os.walk(build_dir):
        level = root.replace(build_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}") 