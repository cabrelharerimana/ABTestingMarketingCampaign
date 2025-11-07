import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_confint
import matplotlib.pyplot as plt

def summarize_conversion(df):
    """Compute conversion rates per group."""
    summary = df.groupby('test_group').agg(
        users=('user_id', 'nunique'),
        conversions = ('converted', 'sum')
    ).reset_index()
    summary['conversion_rate'] = summary['conversions'] / summary['users']
    print(summary)
    return summary

def run_ab_test(summary):
    """Run two-proportion z-test to compare conversion rates."""
    count = summary['conversions'].values
    nobs = summary['users'].values

    stat, pval = sm.stats.proportions_ztest(count, nobs)
    print(f"\n z-test result:\nz-statistic = {stat:3f}, p-value = {pval:.4f}")

    if pval < 0.05:
        print("Statistically significant difference (p < 0.05)")
    else:
        print("No statistically significant difference")

    return stat, pval
def plot_conversion_rates(summary):
    """Visualize conversion rates for both groups."""
    plt.bar(summary['test_group'], summary['conversion_rate'], color=['skyblue', 'orange'])
    plt.title("Conversation Rate by Group")
    plt.ylabel("Conversation Rate")
    plt.xlabel("Group")
    plt.show()

def confidence_intervals(summary):
    """Print 95% confidence intervals for each group."""
    for _, row in summary.iterrows():
        conv = int(row['conversions'])
        total = int(row['users'])
        lower, upper = proportion_confint(conv, total, alpha=0.05, method='normal')
        print(f"{row['test_group']} 95% CI: ({lower:.3f}, {upper:.3f})")