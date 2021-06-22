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
    
    return to_paragraph(staking_projects)


def to_paragraph(staking_projects):
    paragraph = ""
    for p in staking_projects:
        paragraph += f'{p["asset"]} \n'
        paragraph += "-------------------------------------------- \n"
        paragraph += f'Project ID \t\t: {p["projectId"]}\n'
        paragraph += f'Up Limit \t\t: {p["upLimit"]}\n'
        paragraph += f'Purchased \t\t: {p["purchased"]}\n'
        paragraph += f'Duration \t\t: {p["duration"]}\n'
        paragraph += f'Annual Interest Rate \t: {p["annualInterestRate"]}\n'
        paragraph += f'Sold Out? \t\t: {"Yes" if p["sellOut"] == True else "No"}\n'
        paragraph += "\n\n"

    print(paragraph)


get_staking_projects()
