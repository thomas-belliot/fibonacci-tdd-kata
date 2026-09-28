Some commands to enter in the terminal to see if everything will compile on Github :

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest --cov=src/fibonacci_tdd_kata --cov-report=term-missing 

## Help from AI for Step 11
I used AI in order to complete the last step (11), because I had a white page for the website and I had no idea about how to fix this issue.
This is why the yml for the publication of the site is different from the one you gave. I had to adapt the yml file (among others) in order to be able to run my website. The following changes were implemented :
- Additional configuration was added to make the local src package accessible from the notebook. Since the notebook is exported as a WASM application, the package is also built as a wheel and made available to the browser so that fibonacci_tdd_kata can be imported when the notebook runs online.
- The GitHub Actions workflow was updated to install the project dependencies, build the Fibonacci package, prepare the package for the WASM notebook, export the notebook as HTML, and deploy it to GitHub Pages. These changes were necessary because the initial workflow could not find the project environment/package during the automated deployment.
