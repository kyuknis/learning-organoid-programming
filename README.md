# learning-organoid-programming

Study notes and experiments using [`cl-sdk`](https://github.com/Cortical-Labs/cl-sdk), the Python SDK from Cortical Labs for targeting organoid computers.

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda

## Setup

```bash
conda env create -f environment.yml
conda activate organoid-programming
python -m ipykernel install --user --name organoid-programming
```

Copy the environment file and fill in any required values:

```bash
cp .env.example .env
```

Launch JupyterLab:

```bash
jupyter lab
```

## Notebooks

| Notebook | Description |
|---|---|
| `00_getting_started.ipynb` | SDK import, system attributes, reading HDF5 recordings |
| `01_hello_liveliness.ipynb` | Running a liveliness recording and capturing spike data |

## Project structure

```
.
├── notebooks/        # Jupyter notebooks (numbered by topic)
├── src/              # Shared Python utilities (imported by notebooks)
├── tests/            # Unit tests for src/
├── data/             # Local data files (gitignored)
├── assets/           # Static assets (plots, diagrams)
├── environment.yml   # Conda environment spec
└── pyproject.toml    # Project metadata and tool config
```

## Running tests

```bash
pytest
```

## Notes

- Requires **Python 3.12+** — `cl-sdk` uses `TemporaryDirectory(delete=True)` (3.12+) and `typing.Self` (3.11+)
- HDF5 recordings are written to the `notebooks/` directory by default and are gitignored
- Use `pd.Series(cl.get_system_attributes()).rename_axis("attribute").to_frame("value")` for a clean Jupyter display of system info
