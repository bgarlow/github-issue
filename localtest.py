import os
import sys
import requests
import json

from snyksummary import build_snyk_summary

def generate_summary(json_file_path):
    with open(json_file_path) as file:
        data = json.load(file)
    summary = build_snyk_summary(data)
    return summary

def main():
    json_file_path = sys.argv[1]
    print("in main: " + json_file_path)
    summary = generate_summary(json_file_path)

if __name__ == "__main__":
    main()