def rate(figure, ratio):
    import pandas as pd

    df = pd.read_csv("digicom-plus-financial-ratings.csv")

    # return the rating of the first figure lower than the given ratio

    rating = df[df[figure] < ratio].iloc[0][0]

    return rating


# testing
# to customize, change args and run python3 ratings.py in terminal
# print(rate("Current ratio", 1.35))
