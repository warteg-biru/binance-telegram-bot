import requests
from common.to_paragraph import to_paragraph

def get_staking_project_by_asset_name(bot, chat_id, asset_name):
    PAGE_SIZE = 200 # max page size is 200
    r = requests.get(f"https://www.binance.com/bapi/earn/v1/friendly/pos/union?pageSize={PAGE_SIZE}&pageIndex=1&status=ALL")
    
    data = r.json()["data"]
    staking_projects = []
    for d in data:
        projects = d["projects"]
        for p in projects:
            '''
            projectId, asset, upLimit, purchased, duration, config-annualInterestRate
            '''
            project_dict = {}
            project_dict["projectId"] = p["projectId"]
            project_dict["asset"] = p["asset"]
            project_dict["availablePurchase"] = str(float(p["upLimit"]) - float(p["purchased"]))
            project_dict["duration"] = p["duration"]
            project_dict["annualInterestRate"] = int(float(p["config"]["annualInterestRate"]) * 100)
            project_dict["soldOut"] = p["sellOut"]

            if project_dict["asset"] == asset_name:
                staking_projects.append(project_dict)

        if len(staking_projects) > 0:
            bot.send_message(chat_id=chat_id, text=to_paragraph(staking_projects))
        staking_projects = []