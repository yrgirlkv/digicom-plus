def financial_rating(figure, ratio):
    import pandas as pd

    df = pd.read_csv("/digicom-plus-financial-ratings.csv")

    # return the rating of the first figure lower than the given ratio

    rating = df[df[figure] < ratio].iloc[0][0]

    return rating
