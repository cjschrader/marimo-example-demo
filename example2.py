# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.14",
#     "matplotlib==3.11.0",
#     "pandas==3.0.3",
# ]
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Example 2

    ## Learning goal

    Load a very small dataset, inspect it, calculate one summary, and create one simple chart.

    Run the cells from top to bottom.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def _(pd):
    data = pd.read_csv("data.csv")
    data
    return (data,)


@app.cell
def _(data):
    data["value"].mean()
    return


@app.cell
def _(data, plt):
    data.plot(kind="bar", x="category", y="value", legend=False)
    plt.title("Example 1 Values")
    plt.ylabel("Value")
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
