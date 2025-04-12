import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_obsidian_connection():
    print("\n=== Testing Obsidian Connection ===")
    api_key = os.getenv('OBSIDIAN_API_KEY')
    api_url = os.getenv('OBSIDIAN_API_URL')
    
    print(f"Using URL: {api_url}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            api_url,
            headers=headers
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return True
    except Exception as e:
        print(f"Error connecting to Obsidian: {e}")
        return False

def test_create_note():
    print("\n=== Testing Note Creation ===")
    api_key = os.getenv('OBSIDIAN_API_KEY')
    api_url = os.getenv('OBSIDIAN_API_URL')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": "Test Note",
        "content": "# Test Note\n\nThis is a test note created via the API!",
        "folder": "Test"  # This folder will be created if it doesn't exist
    }
    
    try:
        response = requests.post(
            f"{api_url}notes",
            json=data,
            headers=headers
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error creating note: {e}")

if __name__ == "__main__":
    print("Starting connection tests...")
    
    # First test the basic connection
    if test_obsidian_connection():
        # If basic connection works, try creating a note
        test_create_note()