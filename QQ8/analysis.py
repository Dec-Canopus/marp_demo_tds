import matplotlib.pyplot as plt
import numpy as np

def main():
    # Data
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    efficiency_rates = [71.75, 73.63, 73.21, 80.49]
    industry_target = 90
    average_efficiency = 74.77

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(quarters, efficiency_rates, marker='o', linestyle='-', color='b', label='Quarterly Efficiency Rate')
    plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target}%)')
    plt.axhline(y=average_efficiency, color='g', linestyle=':', label=f'Average Efficiency ({average_efficiency}%)')

    # Add titles and labels
    plt.title('Equipment Efficiency Rate - 2024 Quarterly Data')
    plt.xlabel('Quarter')
    plt.ylabel('Efficiency Rate (%)')
    plt.ylim(60, 100)
    plt.legend()
    plt.grid(True)

    # Save the plot
    plt.savefig('equipment_efficiency_analysis/efficiency_trend.png')
    print("Plot saved as equipment_efficiency_analysis/efficiency_trend.png")

if __name__ == '__main__':
    main()
