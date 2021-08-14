def to_paragraph(staking_projects):
    paragraph = ""
    for p in staking_projects:
        paragraph += f'{p["asset"]} \n'
        paragraph += "-------------------------------------------- \n"
        paragraph += f'Project ID \t\t: {p["projectId"]}\n'
        paragraph += f'Available for Purchased \t: {p["availablePurchase"]}\n'
        paragraph += f'Duration \t\t: {p["duration"]}\n'
        paragraph += f'Annual Interest Rate \t: {p["annualInterestRate"]}%\n'
        paragraph += f'Sold Out? \t\t: {"Yes" if p["soldOut"] else "No"}\n'
        paragraph += "\n\n"

    return paragraph