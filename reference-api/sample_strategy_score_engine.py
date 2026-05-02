"""
Sanitized reference strategy score engine for NyxTrader.

This file is for portfolio demonstration only.
It does not include production NyxTrader source code, trading algorithms,
buy/sell signal rules, broker integrations, order execution logic,
proprietary strategy formulas, real market data, or financial advice.

All calculations below are simplified and synthetic.
"""


def calculate_strategy_score(win_rate, sample_size, risk_control_score, consistency_score):
    """
    Calculates a simplified paper-strategy confidence score.

    This is not a trading signal.
    This is not investment advice.
    This is only a sanitized example for architecture demonstration.
    """

    weights = {
        "win_rate": 0.35,
        "sample_size": 0.25,
        "risk_control": 0.25,
        "consistency": 0.15,
    }

    sample_size_score = min(sample_size / 50 * 100, 100)

    score = (
        win_rate * weights["win_rate"]
        + sample_size_score * weights["sample_size"]
        + risk_control_score * weights["risk_control"]
        + consistency_score * weights["consistency"]
    )

    return round(score, 2)


def classify_strategy_status(score, sample_size):
    if sample_size < 20:
        return "Learning"

    if score >= 85:
        return "High Confidence Paper Strategy"

    if score >= 70:
        return "Moderate Confidence Paper Strategy"

    return "Learning"


def generate_strategy_summary(strategy_name, score, status):
    return {
        "strategyName": strategy_name,
        "score": score,
        "status": status,
        "disclaimer": (
            "This is a paper-strategy learning summary only. "
            "It is not financial advice, not a trading signal, and not an execution instruction."
        ),
    }


if __name__ == "__main__":
    score = calculate_strategy_score(
        win_rate=71,
        sample_size=42,
        risk_control_score=80,
        consistency_score=76,
    )

    status = classify_strategy_status(score=score, sample_size=42)

    print(generate_strategy_summary("Iron Condor", score, status))
