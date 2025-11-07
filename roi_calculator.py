def calculate_roi(summary, revenue_per_conversion, cost_per_user):
    """Calculate ROI based on conversion lift and campain cost."""
    crA = summary.loc[summary['test_group'] == 'psa', 'conversion_rate'].values[0]
    crB = summary.loc[summary['test_group'] == 'ad', 'conversion_rate'].values[0]
    nB = summary.loc[summary['test_group'] == 'ad', 'users'].values[0]

    abs_lift = crB - crA
    added_conversions = abs_lift * nB
    extra_revenue = added_conversions * revenue_per_conversion
    extra_cost = nB * cost_per_user
    net_gain = extra_revenue - extra_cost
    roi = net_gain / extra_cost if extra_cost != 0 else 0

    print("\n Roi Analysis:")
    print(f"Absolute lift:{abs_lift:.4f}")
    print(f"Extra conversions: {added_conversions:.2f}")
    print(f"Extra revenue: ${extra_revenue:,.2f}")
    print(f"Extra cost: ${extra_cost:,.2f}")
    print(f"Net gain: ${net_gain:,.2f}")
    print(f"ROI: {roi*100:.2f}%")

    decision = "continue campain" if roi > 0 else "stop campain"
    print(f"\nRecommendation: {decision}")
    return roi, net_gain 