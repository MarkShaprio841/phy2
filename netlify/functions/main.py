import sys
from pathlib import Path
import awsgi

# Add the parent directory to the path to allow imports from the main app
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app

def handler(event, context):
    return awsgi.response(app, event, context)
