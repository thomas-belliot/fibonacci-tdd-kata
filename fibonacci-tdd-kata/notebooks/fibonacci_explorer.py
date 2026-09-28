import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
async def _(mo):
    import sys

    if sys.platform == "emscripten":
        import micropip

        wheel = (
            mo.notebook_location()
            / "public"
            / "fibonacci_tdd_kata-0.1.0-py3-none-any.whl"
        )

        await micropip.install(str(wheel))

    ready = True

    return (ready,)


@app.cell
def _(mo, ready):
    import matplotlib.pyplot as plt

    from fibonacci_tdd_kata import fibonacci

    mo.md(
        r"""
        # Fibonacci Explorer

        Choisissez une plage de nombres et observez les valeurs
        de Fibonacci correspondantes sous forme de liste et de graphique.
        """
    )

    return fibonacci, mo, plt


@app.cell
def _(mo):
    start = mo.ui.slider(
        0,
        200,
        value=0,
        label="Range start",
    )

    end = mo.ui.slider(
        0,
        200,
        value=20,
        label="Range end",
    )

    mo.hstack([start, end])

    return end, start


@app.cell
def _(end, fibonacci, start):
    lo, hi = sorted((start.value, end.value))

    results = [
        fibonacci(n)
        for n in range(lo, hi + 1)
    ]

    return hi, lo, results


@app.cell
def _(hi, lo, plt, results):
    counts = {}

    assert hi - lo + 1 == len(results)

    for k in range(lo, hi + 1):
        counts[k] = results[k - lo]

    fig, ax = plt.subplots()

    ax.bar(
        counts.keys(),
        counts.values(),
    )

    ax.set_xlabel("n")
    ax.set_ylabel("Fibonacci(n)")
    ax.set_title(
        "Fibonacci values over the selected range"
    )

    fig

    return


if __name__ == "__main__":
    app.run()