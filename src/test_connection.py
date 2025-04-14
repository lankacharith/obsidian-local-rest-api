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
    print(f"API Key (first 10 chars): {api_key[:10]}...")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(
            api_url,
            headers=headers,
            verify=False
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.json().get('authenticated') == True:
            print("✅ Successfully authenticated!")
        else:
            print("❌ Authentication failed. Check your API key.")
            
        return response.json().get('authenticated', False)
    except Exception as e:
        print(f"Error connecting to Obsidian: {e}")
        return False

def test_create_note():
    print("\n=== Testing Note Creation ===")
    api_key = os.getenv('OBSIDIAN_API_KEY')
    api_url = os.getenv('OBSIDIAN_API_URL').rstrip('/')
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": "Test Note",
        "content": "# Test Note\n\nThis is a test note created via the API!",
        "folder": "Test"
    }
    
    try:
        response = requests.post(
            f"{api_url}/notes",
            json=data,
            headers=headers,
            verify=False
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json() if response.content else 'No content'}")
    except Exception as e:
        print(f"Error creating note: {e}")

if __name__ == "__main__":
    print("Starting connection tests...")
    print(f"Current working directory: {os.getcwd()}")
    
    if test_obsidian_connection():
        test_create_note()
    else:
        print("\n❌ Please fix authentication before trying to create notes.")