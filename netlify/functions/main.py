import sys
from pathlib import Path

# Add the parent directory to the path to allow imports from the main app
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app
from netlify_functions import handler

def main_handler(event, context):
    return handler(app, event, context)
