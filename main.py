from data_loader import load_data
from data_cleaning import Clean_data
from analysis import summarize_conversion, run_ab_test, plot_conversion_rates, confidence_intervals
from roi_calculator import calculate_roi

def main():
    # Load data
    df = load_data("marketing_AB.csv")
    if df is None:
        return
    # clean data
    df = Clean_data(df)

    #Analyze conversion rates
    summary = summarize_conversion(df)

    #confidence intervals
    confidence_intervals(summary)

    #Statistical test
    run_ab_test(summary)

    #Plot results
    plot_conversion_rates(summary)

    #ROI calculation (example values)
    revenue_per_conversion = 50.0
    cost_per_user = 1.0
    calculate_roi(summary, revenue_per_conversion, cost_per_user)

if __name__ == "__main__":
    main()

