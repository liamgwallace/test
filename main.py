import requests
import json

# Base URL of the API
BASE_URL = "http://localhost:8000"

def list_automations():
    try:
        response = requests.get(f"{BASE_URL}/automation/list_all/")
        if response.status_code == 200:
            automations = response.json()
            if automations:
                print("\n=== List of Automations ===")
                for task_id, details in automations.items():
                    print(f"- Task ID: {task_id}")
                    print(f"  Code: {details.get('code')}")
                    print(f"  Schedule: {details.get('schedule')}")
                    print(f"  Run on Startup: {details.get('run_on_startup')}")
                    print(f"  Run Once: {details.get('run_once')}\n")
            else:
                print("No automations found.")
        else:
            print(f"Failed to list automations. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while listing automations: {str(e)}")

def list_repositories():
    try:
        response = requests.get(f"{BASE_URL}/repo/list_all/")
        if response.status_code == 200:
            repos = response.json()
            if repos:
                print("\n=== List of Repositories ===")
                for repo_name, details in repos.items():
                    print(f"- Repo Name: {repo_name}")
                    print(f"  GitHub URL: {details.get('repo_url')}")
                    print(f"  Schedule: {details.get('schedule')}")
                    print(f"  Run on Startup: {details.get('run_on_startup')}")
                    print(f"  Run Once: {details.get('run_once')}\n")
            else:
                print("No repositories found.")
        else:
            print(f"Failed to list repositories. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while listing repositories: {str(e)}")

def main():
    print("Running Github Repo Test")
    list_automations()
    list_repositories()

if __name__ == "__main__":
    main()
