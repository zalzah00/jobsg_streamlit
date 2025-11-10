import streamlit as st
import requests
import pandas as pd

# --- CONFIGURATION (Extracted from User's File Snippet) ---
# This dictionary separates configuration from application logic.
CONFIG = {
    # Full list of Job Categories from the file snippet
    "JOB_CATEGORIES": {
        "All Categories": None,
        "Information Technology": 1861,
        "F&B (Food & Beverage)": 1855,
        "Sales / Retail": 1875,
        "Healthcare / Phamautical": 1858,
        "General Worker": 1857,
        "General Management": 1856,
        "Events / Promotion": 1854,
        "Environment / Health": 1853,
        "Entertainment": 1852,
        "Engineering": 1851,
        "Education & Training": 1850,
        "Design": 1849,
        "Customer Service": 1848,
        "Consulting": 1847,
        "Building & Construction": 1846,
        "Banking & Finance": 1845,
        "Architecture / Interior Design": 1844,
        "Advertising / Media": 1843,
        "Admin / Secretarial": 1842,
        "Accounting / Auditing / Taxing": 1841,
        "Logistics / Supply Chain": 1864,
        "Legal": 1863,
        "Insurance": 1862,
    },
    
    # List of Employment Types from the file snippet
    "EMPLOYMENT_TYPES": {
        "Any Employment Type": None,
        "Full Time": 76,
        "Part Time": 977,
        "Permanent": 978,
        "Temporary": 979,
        "Contract": 980,
        "Internship": 981,
        "Freelance": 982,
        "Contract-to-Perm": 983,
    },

    # Exhaustive list of MRT Stations from the file snippet
    "MRT_STATIONS": {
        "Any MRT Station": None,
        "NS1/EW24 Jurong East": 1840, "NS2 Bukit Batok": 1839, "NS3 Bukit Gombak": 1838, "NS4/BP1 Choa Chu Kang": 1837,
        "NS5 Yew Tee": 1836, "NS8 Marsiling": 1834, "NS9/TE2 Woodlands": 1833, "NS10 Admiralty": 1832, 
        "NS11 Sembawang": 1831, "NS12 Canberra": 1830, "NS13 Yishun": 1829, "NS14 Khatib": 1828, 
        "NS16 Ang Mo Kio": 1826, "NS17/CC15 Bishan": 1825, "NS18 Braddell": 1824, "NS19 Toa Payoh": 1823, 
        "NS20 Novena": 1822, "NS22/TE14 Orchard": 1820, "NS23 Somerset": 1819, "NS25/EW13 City Hall": 1817, 
        "NS26/EW14 Raffles Place": 1816, "EW1 Pasir Ris": 1813, "EW2/DT32 Tampines": 1812, "EW3 Simei": 1811, 
        "EW4/CG Tanah Merah": 1810, "EW5 Bedok": 1809, "EW6 Kembangan": 1808, "EW7 Eunos": 1807, 
        "EW8/CC9 Paya Lebar": 1806, "EW9 Aljunied": 1805, "EW10 Kallang": 1804, "EW12/DT14 Bugis": 1802, 
        "EW17 Tiong Bahru": 1799, "EW18 Redhill": 1798, "EW19 Queenstown": 1797, "EW23 Clementi": 1793, 
        "EW25 Chinese Garden": 1792, "EW26 Lakeside": 1791, "EW27 Boon Lay": 1790,
        # Downtown and Thomson-East Coast Lines from back snippet:
        "DT1/BP6 Bukit Panjang": 1746, "DT2 Cashew": 1745, "DT3 Hillview": 1744, "DT5 Beauty World": 1743, 
        "DT6 King Albert Park": 1742, "DT7 Sixth Avenue": 1741, "DT8 Tan Kah Kee": 1740, "DT10/TE11 Stevens": 1739, 
        "DT13 Rochor": 1738, "DT17 Downtown": 1737, "DT18 Telok Ayer": 1736, "DT20 Fort Canning": 1735, 
        "DT21 Bencoolen": 1734, "DT22 Jalan Besar": 1733, "DT23 Bendemeer": 1732, "DT24 Geylang Bahru": 1731, 
        "DT25 Mattar": 1730, "DT27 Ubi": 1729, "DT28 Kaki Bukit": 1728, "DT29 Bedok North": 1727, 
        "DT30 Bedok Reservoir": 1726, "DT31 Tampines West": 1725, "DT33 Tampines East": 1724, "DT34 Upper Changi": 1723, 
        "TE1 Woodlands North": 1722, "TE3 Woodlands South": 1721, "TE4 Springleaf": 1720, "TE5 Lentor": 1719, 
        "TE6 Mayflower": 1718, "TE7 Bright Hill": 1717, "TE8 Upper Thomson": 1716, "TE12 Napier": 1715, 
        "TE13 Orchard Boulevard": 1714, "TE15 Great World": 1713,
    }
}
API_BASE_URL = "https://www.findsgjobs.com/apis/job/searchable"


def fetch_jobs(params):
    """Fetches job data from the API."""
    try:
        response = requests.get(API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from API: {e}")
        return None

def display_results(data):
    """Parses and displays the job results in a user-friendly format."""
    results = data.get("data", {}).get("result", [])
    result_count = data.get("data", {}).get("result_count", 0)

    st.success(f"Found {result_count} jobs matching your criteria.")

    if not results:
        st.info("No jobs found for this search. Try broadening your filters.")
        return

    jobs_data = []
    for item in results:
        job = item.get("job", {})
        company = item.get("company", {})

        # Extract names from codes
        categories = [cat.get('caption', 'N/A') for cat in job.get('JobCategory', [])]
        employment_types = [et.get('caption', 'N/A') for et in job.get('EmploymentType', [])]
        mrt_list = [mrt.get('caption') for mrt in job.get('id_Job_NearestMRTStation', [])]
        
        # Format Salary Range
        min_salary = job.get('id_Job_Salary')
        max_salary = job.get('id_Job_MaxSalary')
        currency = job.get('id_Job_Currency', {}).get('caption', 'SGD')
        
        salary_range = ""
        if min_salary and max_salary:
            salary_range = f"{currency} {min_salary:,} - {max_salary:,}"
        elif min_salary:
            salary_range = f"Min {currency} {min_salary:,}"
        else:
            salary_range = "Negotiable"

        jobs_data.append({
            "Job Title": job.get("Title"),
            "Company": company.get("CompanyName"),
            "Category": ", ".join(categories),
            "Employment Type": ", ".join(employment_types),
            "Salary Range": salary_range,
            "Nearest MRT": ", ".join(mrt_list),
            "Full Description": job.get("JobDescription", "No detailed description available.")
        })

    df = pd.DataFrame(jobs_data)
    
    # Display the core data table
    st.markdown("### Job Listings Summary")
    st.dataframe(df.drop(columns=["Full Description"]), use_container_width=True)

    # Display detailed job descriptions using expanders
    st.markdown("### Detailed Descriptions")
    for index, row in df.iterrows():
        with st.expander(f"**{row['Job Title']}** at **{row['Company']}**"):
            st.markdown(f"**Category:** {row['Category']}")
            st.markdown(f"**Employment Type:** {row['Employment Type']}")
            st.markdown(f"**Salary Range:** {row['Salary Range']}")
            st.markdown(f"**Nearest MRT Stations:** {row['Nearest MRT']}")
            st.markdown("---")
            # Clean up the HTML from the job description
            desc = row['Full Description'].replace('<p>', '').replace('</p>', '\n').replace('<ul>', '').replace('</ul>', '').replace('<li>', '- ').replace('</li>', '\n')
            st.markdown(desc, unsafe_allow_html=True)


# --- Streamlit App Layout ---
def main():
    st.set_page_config(layout="wide", page_title="FindSGJobs Advanced Search")
    st.title("🇸🇬 Interactive Job Search (FindSGJobs API)")
    st.markdown("Search Singapore job listings using full category and location filters.")
    st.markdown("---")

    # --- Sidebar Filters ---
    with st.sidebar:
        st.header("Search Filters")
        
        # 1. Category Dropdown
        selected_category_name = st.selectbox(
            "Select Job Category:",
            options=list(CONFIG["JOB_CATEGORIES"].keys()),
            key="category_select"
        )
        selected_category_code = CONFIG["JOB_CATEGORIES"][selected_category_name]
        
        # 2. Employment Type Dropdown
        selected_employment_name = st.selectbox(
            "Select Employment Type:",
            options=list(CONFIG["EMPLOYMENT_TYPES"].keys()),
            key="employment_select"
        )
        selected_employment_code = CONFIG["EMPLOYMENT_TYPES"][selected_employment_name]

        # 3. Nearest MRT Dropdown
        selected_mrt_name = st.selectbox(
            "Select Nearest MRT Station:",
            options=list(CONFIG["MRT_STATIONS"].keys()),
            key="mrt_select"
        )
        selected_mrt_code = CONFIG["MRT_STATIONS"][selected_mrt_name]

        # 4. Keyword Search Input
        keyword_query = st.text_input(
            "Keyword Search (e.g., Engineer, cook):",
            placeholder="Search by keywords"
        )

        # 5. Pagination Settings
        page = st.number_input("Page Number:", min_value=1, value=1, step=1)
        per_page_count = st.number_input("Results Per Page:", min_value=1, max_value=50, value=20, step=5)
        
        # Search Button
        search_button = st.button("Search Jobs", type="primary")

    # --- Main Content ---
    if search_button:
        
        # 1. Build the API Parameters Dictionary
        params = {
            "page": page,
            "per_page_count": per_page_count
        }

        if selected_category_code is not None:
            params["JobCategory"] = selected_category_code
        
        if selected_employment_code is not None:
            # Note: Multiple employment types can be queried with a comma (e.g., 76,978)
            # For simplicity, we only pass the single selected code here.
            params["EmploymentType"] = selected_employment_code

        if selected_mrt_code is not None:
            # Note: Multiple MRT codes can be queried with a comma (e.g., 1833,1840)
            params["id_Job_NearestMRTStation"] = selected_mrt_code
        
        if keyword_query:
            params["keywords"] = keyword_query.strip()
        
        st.info(f"Building API call with parameters: **{params}**")
        
        # 2. Fetch Data
        data = fetch_jobs(params)

        # 3. Display Results
        if data:
            display_results(data)

if __name__ == "__main__":
    main()