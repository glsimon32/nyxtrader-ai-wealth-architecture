"""
Sanitized reference portfolio risk summary for NyxTrader.

This file is for portfolio demonstration only.
It does not include production code, real portfolio data,
broker integrations, trading signals, or financial advice.
"""


def summarize_portfolio_risk(portfolio):
    allocation = portfolio.get("allocation", {})

    equity = allocation.get("equity", 0)
    mutual_funds = allocation.get("mutualFunds", 0)
    options_reserve = allocation.get("optionsReserve", 0)
    cash = allocation.get("unallocatedCash", 0)

    warnings = []

    if options_reserve > 30:
        warnings.append("Options reserve allocation is high and requires review.")

    if equity > 70:
        warnings.append("Equity concentration is high and should be reviewed.")

    if cash < 5:
        warnings.append("Cash buffer is low.")

    if not warnings:
        warnings.append("No major concentration warning detected in this synthetic sample.")

    return {
        "mode": portfolio.get("mode", "Paper"),
        "allocationSummary": {
            "equity": equity,
            "mutualFunds": mutual_funds,
            "optionsReserve": options_reserve,
            "unallocatedCash": cash,
        },
        "riskWarnings": warnings,
        "humanReviewRequired": True,
        "disclaimer": "This is a synthetic portfolio risk summary. It is not financial advice.",
    }


if __name__ == "__main__":
    sample_portfolio = {
        "mode": "Paper",
        "allocation": {
            "equity": 0,
            "mutualFunds": 0,
            "optionsReserve": 0,
            "unallocatedCash": 100,
        },
    }

    print(summarize_portfolio_risk(sample_portfolio))
