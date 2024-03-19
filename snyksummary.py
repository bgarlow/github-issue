def build_issue_block(issue):
    #TODO: add introduced through and fix lines to body of issue?
    #TODO: add module info to body of issue
    id = issue["id"]
    title = issue["title"]
    version = issue["version"]
    #module = issue["module"]
    issue_block = "ID: " + id + " Title: " + title + " Version: " + version
    return issue_block

def build_snyk_summary(data):
    summary = ""
    issues = data["vulnerabilities"]
    num_issues = len(issues)
    print("number of vulnerabiilties: ", num_issues)

    if num_issues > 0: 
        for issue_data in issues:
            issue_block = build_issue_block(issue_data)
            summary += issue_block + "\n"       
    
    #summary = summary[0:-2]
    return summary