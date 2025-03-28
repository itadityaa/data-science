import os

def create_project_structure(base_dir):
    directories = [
        "data/raw",
        "data/processed",
        "models",
        "training",
        "utils",
        "notebooks",
        "tests",
        "saved_models"
    ]
    
    files = {
        "README.md": "# MyPyTorchProject\nA PyTorch-based deep learning project.",
        "requirements.txt": "torch\ntorchvision\ntorchaudio\nnumpy\nmatplotlib\npandas\nscikit-learn\ntqdm\njupyterlab",
        "main.py": "# Entry point for the project",
        "data/dataloader.py": "# Custom DataLoader classes",
        "models/base_model.py": "# Base model class",
        "training/train.py": "# Training script",
        "training/evaluate.py": "# Model evaluation script",
        "utils/config.py": "# Configuration settings",
        "utils/logging_utils.py": "# Logging functions",
        "tests/test_data.py": "# Test data loading",
        ".gitignore": "__pycache__/\nsaved_models/\ndata/raw/\n"
    }
    
    # Create directories
    for directory in directories:
        os.makedirs(os.path.join(base_dir, directory), exist_ok=True)
    
    # Create files with default content
    for file, content in files.items():
        with open(os.path.join(base_dir, file), "w") as f:
            f.write(content)
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    create_project_structure(base_dir)
