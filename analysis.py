# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "unknown"
app = marimo.App(width="medium")


@app.cell
def _():
    # 21f3001973@ds.study.iitm.ac.in
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt

depends
@app.cell
def _(mo):
    # Create a slider to select the number of points
    n_points = mo.ui.slider(10, 100, value=50, label="Number of points")
    n_points  # Display the slider
    return (n_points,)


@app.cell
def _(n_points, np, plt):
    # Generate random data based on the slider value
    # This cell automatically re-executes when n_points.value changes
    x = np.random.rand(n_points.value)
    y = np.random.rand(n_points.value)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.7)
    plt.title(f"Scatter plot with {n_points.value} points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.gca()  # Return the current axes to display the plot
    return


@app.cell
def _(mo, n_points):
    # Dynamic markdown output based on the slider value
    mo.md(f"""
    ### Scatter Plot Details

    - **Number of Points:** {n_points.value}
    - **X and Y values** are randomly generated.

    Adjust the slider to change the number of points in the plot.
    """)
    return


@app.cell
def _():
    print("21f3001973@ds.study.iitm.ac.in")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
