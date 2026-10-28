# Electric Vehicle Market Performance & Insights

> **Academic Capstone Project & Data Analytics Web Portal**  
> Developed using Python Flask, HTML5, CSS3, minimal Vanilla JavaScript, and Tableau Public.

---

## 📌 Project Overview

**"Electric Vehicle Market Performance & Insights"** is an interactive academic analytics portal designed to showcase electric vehicle (EV) market adoption trends, manufacturer performance, battery range advancements, and Clean Alternative Fuel Vehicle (CAFV) distribution.

The project pairs a lightweight, clean **Python Flask** web server with cloud-hosted, interactive **Tableau Public** visualizations (both **Dashboard** and **Story**), providing a responsive, blue-and-white analytics user interface suitable for college presentations, viva evaluations, and portfolio demonstration.

---

## 🌟 Key Features

1. **Modern EV Blue-and-White Theme**:
   - Clean, professional design with electric blue accents (`#2563eb`), slate typography, and clean-tech badges.
   - 100% responsive across mobile, tablet, and desktop displays.
2. **Four Dedicated Sections**:
   - **Overview**: Executive summary, key metric highlight cards (150K+ EVs, 78% BEV dominance, range milestones), and 6 structured academic research objectives.
   - **Dashboard**: Live interactive Tableau Public embed with reload, fullscreen expand, and direct external launch buttons.
   - **Story**: Narrative analytics walkthrough exploring EV adoption stages from early pioneers to mainstream mass production.
   - **About & Dataset**: Comprehensive dataset feature dictionary, academic data integrity notice, student credentials card, and technology breakdown.
3. **Editable Tableau Public URLs**:
   - Easily update or customize the Tableau links directly in `app.py`.
   - Pre-configured with the user's published Tableau Public workbook.
4. **Graceful Handling for Missing / Placeholder URLs**:
   - If a URL is blank or unconfigured, the application gracefully renders a clean instruction card without crashing or showing broken frames.
5. **Academic Integrity & Transparency**:
   - Clarifies data flow honestly: visualizations represent cleaned EV population records hosted on Tableau Public; no synthetic databases or incomplete SQL claims are made.
6. **Zero Heavyweight External Dependencies**:
   - Uses native CSS and minimal Vanilla JavaScript (no bloated frameworks or CDN failures during presentations).

---

## 📂 Project Structure

```text
Ev project siddhi/
│
├── app.py                  # Main Flask application with editable Tableau URLs & project config
├── requirements.txt        # Python package dependencies (Flask)
├── README.md               # Complete setup and execution documentation
│
├── templates/
│   └── index.html          # Semantic HTML5 template (Overview, Dashboard, Story, About)
│
└── static/
    └── style.css           # Custom responsive blue-and-white EV analytics styling
```

---

## 📊 Published Tableau Link Used

The application is pre-configured with the published Tableau Public workbook link:
```text
https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights_17931766681770/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
```
This link is linked in both the **Dashboard** and **Story** sections in `app.py`, as well as the **"Tableau Public"** navigation button.

---

## 🚀 Setup & Running on Windows (Step-by-Step)

Follow these simple steps in **PowerShell**, **Command Prompt (CMD)**, or **VS Code Terminal**:

### Step 1: Open the Project Folder
Open your terminal and navigate to the project directory:
```powershell
cd "c:\Users\adhis\Ev project siddhi"
```

### Step 2: (Recommended) Create & Activate a Python Virtual Environment

Creating a virtual environment ensures a clean installation:

**In PowerShell / Command Prompt:**
```powershell
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# OR Activate on Windows (Command Prompt)
.\venv\Scripts\activate.bat
```

> **Note for PowerShell Users:** If you see an execution policy error like `cannot be loaded because running scripts is disabled`, run this once:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> Then run `.\venv\Scripts\Activate.ps1` again.

### Step 3: Install Required Dependencies
Install Flask from `requirements.txt`:
```powershell
pip install -r requirements.txt
```

### Step 4: Run the Flask Web Application
Start the local development server:
```powershell
python app.py
```

You will see output similar to:
```text
======================================================================
 Electric Vehicle Market Performance & Insights - College Project
 Server running locally at: http://127.0.0.1:5000
 Press CTRL+C to terminate the development server.
======================================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Step 5: Open in Your Web Browser
Open your browser (Google Chrome, Microsoft Edge, Firefox, or Brave) and navigate to:
```text
http://127.0.0.1:5000
```

To stop the server at any time, press **`CTRL + C`** in your terminal.

---

## ✏️ How to Edit or Update Tableau URLs

Open [app.py](file:///c:/Users/adhis/Ev%20project%20siddhi/app.py) in any text editor or VS Code. Near lines 20–35, you will find:

```python
# ==============================================================================
# TABLEAU PUBLIC CONFIGURATION
# ------------------------------------------------------------------------------
TABLEAU_DASHBOARD_URL = (
    "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights_17931766681770/EVMarketDashboard"
    "?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
)

TABLEAU_STORY_URL = (
    "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights_17931766681770/EVMarketDashboard"
    "?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
)
```

1. **Dashboard URL**: Replace `TABLEAU_DASHBOARD_URL` with your dashboard link.
2. **Story URL**: If you create a separate Tableau Public Story tab, replace `TABLEAU_STORY_URL` with that story's link.
3. Save the file. Flask in debug mode will automatically reload!

---

## 🛡️ Missing URL Graceful Degradation

If either `TABLEAU_DASHBOARD_URL` or `TABLEAU_STORY_URL` is set to an empty string `""` or `#`:
- The website will **not** crash or display a broken iframe.
- A friendly, styled instructions card will appear explaining which variable in `app.py` needs to be set.
- All other sections (Overview, Objectives, About, Dataset, Tech Stack) continue to display normally.

---

## 📋 Dataset Details & Academic Transparency

- **Dataset**: Electric Vehicle Population Dataset (Curated Public Data)
- **Primary Attributes Analyzed**:
  - `VIN (1-10)`: Partial vehicle identification for distinct unit tracking.
  - `County & City`: Geographical distribution and EV charging density zones.
  - `Model Year`: Chronological epoch analysis (1997 through present).
  - `Make & Model`: Manufacturer market share and model rankings (Tesla, Nissan, Chevrolet, Ford, etc.).
  - `Electric Vehicle Type`: Classification into Battery Electric Vehicles (BEV) vs. Plug-in Hybrid (PHEV).
  - `Clean Alternative Fuel Vehicle (CAFV) Eligibility`: Regulatory incentive qualification tracking.
  - `Electric Range`: Single-charge battery distance (in miles).
  - `Base MSRP`: Retail price tier comparison.
- **Data Integrity Statement**:
  All visual analytics are derived from pre-processed EV registration records visualized directly via Tableau Public. No fictitious SQL databases or uncompleted API integrations are claimed.

---

## 🛠️ Windows Troubleshooting Guide

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `'python' is not recognized` | Python is not added to Windows PATH. | Re-run the Python installer, check **"Add Python to PATH"**, or invoke with `py app.py`. |
| PowerShell script activation error | Windows execution policy restricts scripts. | Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in PowerShell. |
| `Address already in use (port 5000)` | Another process is using port 5000. | Change `port=5000` to `port=5001` or `port=8080` in `app.py`, or terminate the occupying process. |
| Tableau embed displays blank or grey box | Browser privacy shields / third-party cookie blocking. | Click the **"Open in Tableau"** button on the toolbar, or disable third-party cookie blocking for `public.tableau.com`. |

---

## 🎓 College Viva & Presentation Tips

When presenting this project to your internal/external examiners:
1. **Introduction**: Start at the **Overview** section; explain the transition from ICE to BEV/PHEV and review the 6 key research objectives.
2. **Interactive Demonstration**: Scroll to the **Dashboard**; demonstrate cross-filtering by clicking a specific vehicle manufacturer (e.g. Tesla) and observing how the vehicle type and geographical distribution respond.
3. **Narrative Storyline**: Walk through the **Story** section stages (Inception Phase &rarr; Policy Incentives &rarr; Mass Market Scaling &rarr; Future Projections).
4. **Methodology & Integrity**: Finish at the **About** section to review the dataset attributes and highlight your structured Python Flask architecture.

---

## 📄 License & Attribution
Designed for college capstone project demonstration and academic evaluation.

