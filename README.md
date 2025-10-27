
# learn-numpy

A small collection of NumPy learning materials and exercises. This repository contains a Jupyter notebook with 100 NumPy exercises designed to help you practice and master NumPy fundamentals.

## Repository structure

- `main.py` — (optional) placeholder or runner script.
- `pyproject.toml` — project metadata and dependency list.
- `src/100_Numpy_exercises.ipynb` — the main Jupyter notebook with exercises and solutions.

## Prerequisites

- Python 3.12 or newer (as declared in `pyproject.toml`).
- pip (or an equivalent package manager).

The project depends on the packages listed in `pyproject.toml`, notably:

- numpy >= 2.3.4
- pandas >= 2.3.3
- jupyterthemes >= 0.20.0 (optional, for styling notebooks)
- mdutils >= 1.8.1 (optional)

## Quick start

1. Clone the repo (if you haven't already):

	git clone <repo_url>

2. Create and activate a virtual environment (recommended):

	python -m venv .venv
	source .venv/bin/activate

3. Install dependencies:

	pip install -r requirements.txt  # if you create one
	# or install directly from pyproject dependencies:
	pip install numpy pandas jupyterthemes mdutils

4. Start Jupyter and open the notebook:

	jupyter notebook src/100_Numpy_exercises.ipynb

	or

	jupyter lab src/100_Numpy_exercises.ipynb

Tips:

- If you prefer, create a `requirements.txt` from `pyproject.toml` dependencies:

  pip freeze | grep -E "numpy|pandas|jupyterthemes|mdutils" > requirements.txt

## What you'll find in the notebook

- A sequence of 100 NumPy exercises covering array creation, indexing, broadcasting, aggregation, reshaping, and simple linear algebra.
- Each exercise contains a problem statement and a solution (visible or hidden depending on how you use the notebook).

## Contributing

Contributions are welcome. A few ways you can help:

- Add more exercises or improve existing ones.
- Improve explanations and add visualizations where helpful.
- Add tests or small scripts that verify exercise outputs.

If you'd like to contribute, open an issue describing the change you want to make or submit a pull request.
