import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime # For handling dates

# --- 1. Data Generation ---
# Define parameters for synthetic data
num_months = 12 # For a full year
start_date = datetime.datetime(2023, 1, 1)
segments = ["Premium", "Standard", "Value"]

data = []
for i in range(num_months):
    current_date = start_date + datetime.timedelta(days=i*30) # Approximate monthly increment
    month_num = current_date.month # Get month number for seasonality

    for segment in segments:
        # Base revenue for each segment (different starting points)
        if segment == "Premium":
            base_rev = 5_000_000
            annual_growth_factor = 1.015 # 1.5% annual growth
        elif segment == "Standard":
            base_rev = 3_000_000
            annual_growth_factor = 1.01 # 1% annual growth
        else: # Value
            base_rev = 1_500_000
            annual_growth_factor = 1.005 # 0.5% annual growth

        # Apply monthly seasonality: higher towards year-end (Q4), lower in Q1/Q2
        # Using a sine wave: (amplitude * sin(2*pi*(month - phase)/period))
        # Phase ~ 10 shifts peak to Nov/Dec.
        seasonal_factor = 1 + 0.18 * np.sin(2 * np.pi * (month_num - 10) / 12)

        # Apply compounding growth over the months within the year
        # (annual_growth_factor)^(month_fraction_of_year)
        growth_over_time = annual_growth_factor**(month_num / 12.0)

        # Add some random noise for realism (e.g., +/- 2% of base revenue)
        noise = np.random.normal(0, base_rev * 0.02)

        # Calculate final revenue for the month
        revenue = base_rev * seasonal_factor * growth_over_time + noise
        revenue = max(500000, revenue) # Ensure revenue is at least a minimal value

        data.append({
            "Month": current_date,
            "Customer Segment": segment,
            "Revenue": revenue
        })

df = pd.DataFrame(data)

# Sort data to ensure line plot connects points correctly
df = df.sort_values(by=["Customer Segment", "Month"])

# --- 2. Chart Creation ---

# Set professional Seaborn style and context for presentation
sns.set_style("whitegrid") # Provides a clean grid background
sns.set_context("talk", font_scale=0.9) # "talk" context is suitable for presentations

# Create the figure with exact dimensions (512x512 pixels at 64 DPI)
# Calculation: 512 pixels / 64 dpi = 8 inches.
# The figsize determines the *canvas* size.
plt.figure(figsize=(8, 8))

# Create the lineplot
# `hue` differentiates lines by customer segment
# `marker='o'` adds points for each month for clearer data points
# `palette` chooses a distinct and professional color scheme
lineplot = sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Customer Segment",
    marker="o",
    palette="viridis", # 'viridis' is a perceptually uniform colormap
    linewidth=2.5 # Make lines slightly thicker for better visibility
)

# Customize plot titles and labels
plt.title("Monthly Revenue Trends by Customer Segment (2023)", fontsize=16, pad=20)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)

# Format y-axis to display currency in millions
plt.ticklabel_format(style='plain', axis='y') # Disable scientific notation
lineplot.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1_000_000:.1f}M'))

# Customize x-axis ticks to show abbreviated month names
months_abbr = pd.to_datetime(df['Month'].unique()).strftime('%b').tolist()
plt.xticks(df['Month'].unique(), months_abbr, rotation=45, ha='right')

# Add grid lines for easier readability
plt.grid(True, linestyle='--', alpha=0.6)

# Legend placement: Place inside the plot to guarantee it fits the fixed canvas size.
# loc='upper left' is generally safe and prevents legend from being cut off.
plt.legend(title="Customer Segment", loc='upper left')

# IMPORTANT: Do NOT use plt.tight_layout() or bbox_inches='tight' in savefig
# when exact pixel dimensions are required, as they can alter the canvas size.
# The figure size (figsize) and dpi directly control the output pixel dimensions.

# --- 3. Save Chart ---
# Save the figure as a PNG with the specified DPI (64 DPI for 512x512 pixels)
# Removing 'bbox_inches='tight'' is crucial for fixed dimensions.
plt.savefig('chart.png', dpi=64)

plt.close() # Close the plot to free up memory

print("chart.png generated successfully. Please verify its dimensions.")
