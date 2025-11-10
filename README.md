# FindSGJobs Interactive Search (Streamlit)

This is a Streamlit-based wrapper for the FindSGJobs API, providing an interactive job search interface. It abstracts the underlying API complexity while offering a user-friendly UI for searching Singapore job listings.

## Features
- Search Singapore job listings using the FindSGJobs API
- Filter by job category, employment type, and nearest MRT station
- View listings in a table and expand individual job descriptions

## Architecture
This application functions as an API wrapper, providing several layers of abstraction:

1. **API Integration Layer**
   - Encapsulates the FindSGJobs API endpoint
   - Handles HTTP requests and error management
   - Manages API parameters and response parsing

2. **Data Transformation Layer**
   - Converts API codes to human-readable labels
   - Formats salary ranges and concatenates multiple values
   - Structures job descriptions and company information

3. **Presentation Layer**
   - Interactive Streamlit widgets for filtering
   - Responsive data tables with expandable details
   - Clean, user-friendly interface

## API Documentation

### Base Endpoint
```
https://www.findsgjobs.com/apis/job/searchable
```

### Parameters
- `page`: Page number for pagination (default: 1)
- `per_page_count`: Results per page (default: 20, max: 50)
- `JobCategory`: Job category code (e.g., 1861 for IT)
- `EmploymentType`: Employment type code (e.g., 76 for Full Time)
- `id_Job_NearestMRTStation`: MRT station code
- `keywords`: Search terms for job titles/descriptions

### Response Format
The API returns JSON with:
- `data.result`: Array of job listings
- `data.result_count`: Total number of matching jobs
- Job details include:
  - Title, company info, salary range
  - Categories, employment types
  - Nearest MRT stations
  - Full job description (HTML format)

## Prerequisites

### Environment
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

## Technical Notes
- All API calls go through the wrapper function `fetch_jobs(params)` in `job_search_app.py`
- The wrapper includes error handling and timeout settings
- Network connectivity is required for searches to work.
- The `requirements.txt` lists the libraries detected in the code: `streamlit`, `pandas`, and `requests`.

## Troubleshooting
- If Streamlit fails to start, confirm the Python executable in your PATH or activated virtual environment.
- If API requests fail, ensure you have network access and the API endpoint is reachable.
- Common API errors are handled with user-friendly messages

## License
This repository does not include a license file. Add one if you plan to share the code publicly.
