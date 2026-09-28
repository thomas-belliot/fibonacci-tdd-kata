import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():

    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_tdd_kata import fibonacci

    def _():
        mo.md(
            r"""
            # Fibonacci Explorer
    
            Pick a range below and see how fibonacci classifies each number
            in it, both as a list and as a chart of the distribution of
           outputs. This notebook consumes the published fibonacci_tdd_kata
           package — it does not reimplement the function.
           """
        )

    return fibonacci, mo, plt


@app.cell
def _(mo):
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, fibonacci, start):
    lo, hi = sorted((start.value, end.value))
    results = [fibonacci(n) for n in range(lo, hi + 1)]
    return hi, lo, results


@app.cell
def _(hi, lo, plt, results):
    # test = Counter("Number" if r.isdigit() else r for r in results)
    # triggers AttributeError : 'int' object has no attribute 'isdigit'

    counts = {}
    assert hi - lo + 1 == len(results)

    for k in range(lo, hi + 1):
        counts[k] = results[k - lo]

    fig, ax = plt.subplots()
    ax.bar(
        counts.keys(),
        counts.values(),
        color=["#4c72b0", "#dd8452", "#55a868", "#c44e52"],
    )
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Fibonacci outputs over the selected range")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
