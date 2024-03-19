import os
import sys
import requests
import json
from snyksummary import build_snyk_summary

target_directory = os.environ['TARGET_DIRECTORY']
github_token = os.environ['GITHUB_TOKEN']
github_repo = os.environ['GITHUB_REPOSITORY']
github_api_url = 'https://api.github.com/repos/' + github_repo

def generate_summary(json_file_path):
    #TODO: address warning on open
    with open(json_file_path) as file:
        data = json.load(file)
    summary = build_snyk_summary(data)
    return summary

def create_github_issue(github_token, github_api_url, summary):
    auth_header_value = "Bearer " + github_token
    headers = {
        "Authorization": auth_header_value,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    #TODO: add assignees, project labels, etc.
    #TODO: definitely add more data about the issues in the body markdown
    issueRequest = {
        "title": "This is an issue submitted by the python script",
        "body": summary,
        "assignees": ["bgarlow"],
        "labels": ["bug"]
    }
    
    response = requests.post(github_api_url, headers=headers, json=issueRequest)
    return response

def main():
    print('current directory: ' + os.getcwd())
    json_file_name = sys.argv[1]    
    json_file_path = target_directory + '/' + json_file_name
    print("in main: " + json_file_path)
    summary = generate_summary(json_file_path)
    response = create_github_issue(github_token, github_api_url, summary)
    return response

if __name__ == "__main__":
    main()

