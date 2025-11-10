# FindSGJobs Interactive Search (Streamlit)

This is a small Streamlit app that queries the FindSGJobs API to provide an interactive job search UI (category, employment type, nearest MRT, keywords, pagination).

## Features
- Search Singapore job listings using the FindSGJobs API
- Filter by job category, employment type, and nearest MRT station
- View listings in a table and expand individual job descriptions

## Prerequisites
- Python 3.8 or newer
- Internet access (the app calls an external API)

## Install

You can use either a standard Python virtual environment (venv) or Conda. Choose the one you prefer.

Option A — using venv (built-in virtual environment)

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

2. Install dependencies with pip:

```powershell
pip install -r requirements.txt
```

Option B — using Conda

1. Create a new Conda environment (example uses Python 3.10):

```powershell
conda create -n jobsg python=3.10 -y
```

2. Activate the environment:

```powershell
conda activate jobsg
```

3. Install dependencies. You can install from conda-forge (recommended) or use pip inside the Conda env.

Conda-forge (preferred):

```powershell
conda install -c conda-forge streamlit pandas requests -y
```

Or install via pip inside the activated Conda env:

```powershell
pip install -r requirements.txt
```

## Run
Start the Streamlit app with:

```powershell
streamlit run job_search_app.py
```

Open the URL printed by Streamlit in your browser (usually http://localhost:8501).

## Notes
- The app uses the public API endpoint `https://www.findsgjobs.com/apis/job/searchable` as defined in `job_search_app.py`.
- Network connectivity is required for searches to work.
- The `requirements.txt` lists the libraries detected in the code: `streamlit`, `pandas`, and `requests`.

## Troubleshooting
- If Streamlit fails to start, confirm the Python executable in your PATH or activated virtual environment.
- If API requests fail, ensure you have network access and the API endpoint is reachable.

## License
This repository does not include a license file. Add one if you plan to share the code publicly.
