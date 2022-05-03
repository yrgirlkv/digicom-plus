def risk_model(id):

    digicom_weights = {
        # financial risk - objective
        "liquid_ratio": 5,
        "current_ratio": 5,
        "growth_rate": 5,
        "operating_margin": 5,
        "debt_to_equity": 5,
        "financial_compliance": 5,
        # financial risk - subjective
        "market_feedback": 5,
        "defaults": 10,
        # operational risk
        "operation_tenure": 5,
        "size": 5,
        # management assessment
        "tenure": 5,
        "reliability": 7,
        "compliance": 3,
        "barrier_to_entry": 10,
        "BCI_comparison": 10,
        "country_risk": 10,
    }

    company_ratings = {
        # financial risk - objective
        "liquid_ratio": 1,
        "current_ratio": 1,
        "growth_rate": 1,
        "operating_margin": 1,
        "debt_to_equity": 1,
        "financial_compliance": 1,
        # financial risk - subjective
        "market_feedback": 1,
        "defaults": 1,
        # operational risk
        "operation_tenure": 1,
        "size": 1,
        # management assessment
        "tenure": 1,
        "reliability": 1,
        "compliance": 1,
        "barrier_to_entry": 1,
        "BCI_comparison": 1,
        "country_risk": 1,
    }

    # pass API data into ratings.py
    # populate company_ratings with appropriate figures

    total = sum(digicom_weights.values())
    score = (
        sum(company_ratings[key] * digicom_weights[key] for key in digicom_weights)
        / total
    )

    return {"id": id, "score": score}
