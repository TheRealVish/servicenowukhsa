import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()

# JIRA API integration
def create_jira_issue(jira_url, jira_username, jira_api_token, project_key, issue_type, summary, description):
    url = f"{jira_url}/rest/api/2/issue"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    auth = HTTPBasicAuth(jira_username, jira_api_token)
    
    issue_data = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": issue_type
            }
        }
    }
    
    response = requests.post(url, json=issue_data, headers=headers, auth=auth)
    
    if response.status_code == 201:
        print("JIRA issue created successfully!")
        return response.json()
    else:
        print(f"Failed to create JIRA issue: {response.status_code}")
        print(response.text)
        return None

# ServiceNow API integration
def create_servicenow_incident(snow_instance, snow_username, snow_password, short_description, description, category):
    url = f"https://{snow_instance}.service-now.com/api/now/table/incident"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    auth = (snow_username, snow_password)
    
    incident_data = {
        "short_description": short_description,
        "description": description,
        "category": category
    }
    
    response = requests.post(url, json=incident_data, headers=headers, auth=auth)
    
    if response.status_code == 201:
        print("ServiceNow incident created successfully!")
        return response.json()
    else:
        print(f"Failed to create ServiceNow incident: {response.status_code}")
        print(response.text)
        return None

# Example usage
if __name__ == "__main__":
    # JIRA credentials and details
    jira_url = os.getenv("JIRA_URL")
    jira_username = os.getenv("JIRA_USERNAME")
    jira_api_token = os.getenv("JIRA_API_TOKEN")
    jira_project_key = os.getenv("JIRA_PROJECT_KEY")
    jira_issue_type = "Task"
    jira_summary = "vish Sample issue from API"
    jira_description = "vish This issue was created using the JIRA API."

    # ServiceNow credentials and details
    snow_password = os.getenv("SNOW_PASSWORD")
    snow_username = os.getenv("SNOW_USERNAME")
    snow_instance = os.getenv("SNOW_INSTANCE")
    snow_short_description = "vish Sample incident from API"
    snow_description = "vish This incident was created using the ServiceNow API."
    snow_category = "Software"

    # Create JIRA issue
    jira_response = create_jira_issue(jira_url, jira_username, jira_api_token, jira_project_key, jira_issue_type, jira_summary, jira_description)

    # Create ServiceNow incident
    if jira_response:
        snow_response = create_servicenow_incident(snow_instance, snow_username, snow_password, snow_short_description, snow_description, snow_category)