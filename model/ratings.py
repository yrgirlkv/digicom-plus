def rate(category, figure):

    BTE = {
        "charterer": 5,
        "broker": 8,
        "country-agency": 8,
        "global-agency": 1,
        "ship-owner": 3,
        "port": 2,
        "dry": 3,
        "LNG": 2,
        "crude": 2,
        "bunker-supplier": 3,
        "intermediary": 6,
        "service-provider": 6,
        "shipbreaking": 7,
    }

    if category == "BTE":
        return BTE[figure]
    else:
        import pandas as pd

        df = pd.read_csv("digicom-plus-financial-ratings.csv")
        if type(figure) == str:
            rating = df[df[category] == figure].iloc[0][0]
        else:
            # return the rating of the first figure lower than the given ratio
            rating = df[df[category] < figure].iloc[0][0]
    return rating


# testing
# to customize, change args and run python3 ratings.py in terminal
# print(rate("Financial compliance", "N"))
