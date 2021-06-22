import requests

def get_staking_projects():
    PAGE_SIZE = 200 # max page size is 200

    r = requests.get(f"https://www.binance.com/bapi/earn/v1/friendly/pos/union?pageSize={200}&pageIndex=1&status=ALL")

    data = r.json()["data"]

    staking_projects = []

    for d in data:
        asset_name = d["asset"]
        projects = d["projects"]
        for p in projects:
            '''
            projectId, asset, upLimit, purchased, duration, config-annualInterestRate
            '''
            project_dict = {}
            project_dict["projectId"] = p["projectId"]
            project_dict["asset"] = p["asset"]
            project_dict["upLimit"] = p["upLimit"]
            project_dict["purchased"] = p["purchased"]
            project_dict["duration"] = p["duration"]
            project_dict["annualInterestRate"] = p["config"]["annualInterestRate"]
            project_dict["sellOut"] = p["sellOut"]

            staking_projects.append(project_dict)
    
    return staking_projects
