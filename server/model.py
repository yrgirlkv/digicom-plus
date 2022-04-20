def risk_model(id):
    score = 0

    factor_weights = {
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

    dummy_ratings = {
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
        "operation_tenure": 3,
        "size": 5,
        # management assessment
        "tenure": 5,
        "reliability": 7,
        "compliance": 3,
        "barrier_to_entry": 10,
        "BCI_comparison": 10,
        "country_risk": 10,
    }

    for key in dummy_ratings:
        score += dummy_ratings[key] * factor_weights[key]

    return {"id": id, "score": score}
