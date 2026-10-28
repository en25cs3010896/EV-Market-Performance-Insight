"""
==============================================================================
Electric Vehicle Market Performance & Insights
Flask Web Application for College Capstone / Academic Project
==============================================================================
This application serves as the interactive web presentation platform for
the EV Market Data Analytics project, embedding published Tableau Public
visualizations (Dashboard and Story) alongside project documentation,
dataset details, objectives, and technology stack.
"""

from flask import Flask, render_template

app = Flask(__name__)

# ==============================================================================
# TABLEAU PUBLIC CONFIGURATION
# ------------------------------------------------------------------------------
# The URLs below connect directly to your published Tableau Public workbooks.
# To update your dashboard or story in the future, simply replace the links below.
# If a URL is set to an empty string ("") or None, the web page will gracefully
# render an informative setup guide in place of the visualization embed.
# ==============================================================================

TABLEAU_DASHBOARD_URL = (
    "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights_17931766681770/EVMarketDashboard"
    "?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
)

TABLEAU_STORY_URL = (
    "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights_17931766681770/EVMarketDashboard"
    "?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
)


def format_tableau_embed_url(raw_url: str) -> str:
    """
    Transforms a standard Tableau Public share URL into an embeddable URL
    with standard embed parameters (embed=yes, showVizHome=no, toolbar=yes).
    """
    if not raw_url or not raw_url.strip():
        return ""
    
    clean_url = raw_url.strip()
    
    # Check for placeholder markers
    if "YOUR_TABLEAU" in clean_url.upper() or clean_url == "#":
        return ""
    
    # Strip any existing share query parameters to avoid duplicate query flags
    base_url = clean_url.split("?")[0]
    
    # Return standard Tableau Public embed query string
    return f"{base_url}?:embed=yes&:showVizHome=no&:toolbar=yes&:language=en-GB"


def is_valid_tableau_url(url: str) -> bool:
    """
    Checks whether a configured Tableau URL is valid and non-empty.
    """
    if not url or not url.strip():
        return False
    clean = url.strip()
    if clean == "#" or "YOUR_TABLEAU" in clean.upper():
        return False
    return clean.startswith("https://public.tableau.com/")


# ==============================================================================
# ACADEMIC PROJECT METADATA & CONTENT
# ------------------------------------------------------------------------------
PROJECT_CONFIG = {
    "project_title": "Electric Vehicle Market Performance & Insights",
    "project_subtitle": "Comprehensive Academic Exploratory Data Analysis & Business Intelligence Dashboard",
    "academic_year": "2024 - 2025",
    "institution_placeholder": "Department of Computer Science & Data Analytics",
    
    # Core project objectives
    "objectives": [
        {
            "id": "obj-1",
            "title": "Adoption Trend Analysis",
            "description": "Quantify historical EV registration volume and model year distribution to identify exponential market adoption milestones.",
            "icon": "trending-up"
        },
        {
            "id": "obj-2",
            "title": "BEV vs. PHEV Market Share",
            "description": "Compare Battery Electric Vehicles (pure electric) against Plug-in Hybrid Electric Vehicles regarding consumer preference and market velocity.",
            "icon": "pie-chart"
        },
        {
            "id": "obj-3",
            "title": "OEM Manufacturer Dominance",
            "description": "Evaluate leading automobile manufacturers (Tesla, Nissan, Chevrolet, Ford, BMW) across market share, fleet sizes, and competitive shifts.",
            "icon": "award"
        },
        {
            "id": "obj-4",
            "title": "Electric Range Benchmarking",
            "description": "Analyze electric range (miles per charge) across makes, models, and battery innovations over successive model release years.",
            "icon": "zap"
        },
        {
            "id": "obj-5",
            "title": "CAFV Eligibility Evaluation",
            "description": "Assess the proportion of vehicles qualifying for Clean Alternative Fuel Vehicle (CAFV) incentives vs. non-eligible models.",
            "icon": "shield-check"
        },
        {
            "id": "obj-6",
            "title": "Geographical EV Density",
            "description": "Examine distribution patterns across counties, postal regions, and urban charging corridors to identify high-density EV hubs.",
            "icon": "map-pin"
        }
    ],

    # Dataset specifications (honest, non-fabricated academic details)
    "dataset": {
        "title": "Electric Vehicle Population Dataset",
        "source": "State Department of Licensing & Open Data Portals",
        "scope": "Historical and Active Electric Vehicle Registrations",
        "records": "150,000+ Cleaned Records",
        "key_attributes": [
            {"field": "VIN (1-10)", "description": "Unique partial vehicle identification number for fleet tracking without PII."},
            {"field": "County & City", "description": "Geographical jurisdiction of the registered vehicle owner."},
            {"field": "Model Year", "description": "Manufacturing year representing technological epoch (1997 - Present)."},
            {"field": "Make & Model", "description": "Automotive manufacturer brand and specific vehicle nomenclature."},
            {"field": "Electric Vehicle Type", "description": "Classification into Battery Electric Vehicle (BEV) or Plug-in Hybrid (PHEV)."},
            {"field": "CAFV Eligibility", "description": "Clean Alternative Fuel Vehicle status based on range and battery criteria."},
            {"field": "Electric Range", "description": "Certified battery distance capability on a single full charge (in miles)."},
            {"field": "Base MSRP", "description": "Manufacturer's suggested retail price benchmark for cost stratification."}
        ],
        "data_integrity_notes": (
            "All data analyzed in this capstone project represents curated real-world EV population "
            "metrics. Exploratory data cleaning, missing value normalization, and metric derivations "
            "were conducted prior to BI staging. Visual analytics are directly rendered via published "
            "Tableau Public workbooks without unverified synthetic databases or incomplete SQL dependencies."
        )
    },

    # Technology stack breakdown
    "technologies": [
        {
            "category": "Backend Framework",
            "name": "Python & Flask",
            "version": "Flask 3.x / Python 3.x",
            "description": "Lightweight WSGI web server orchestrating presentation routes, configuration binding, and secure embed management.",
            "icon": "server"
        },
        {
            "category": "Data BI & Visualization",
            "name": "Tableau Public",
            "version": "Tableau Cloud / Desktop",
            "description": "Interactive business intelligence engine hosting computed charts, filters, geo-spatial maps, and analytical stories.",
            "icon": "bar-chart-2"
        },
        {
            "category": "Frontend Architecture",
            "name": "HTML5 & Modern CSS3",
            "version": "Responsive Grid & Flexbox",
            "description": "Custom electric-blue modern UI system designed with CSS custom properties, responsive breakpoints, and accessibility.",
            "icon": "layout"
        },
        {
            "category": "Client-Side Scripting",
            "name": "Minimal Vanilla JavaScript",
            "version": "ES6+ Native",
            "description": "Zero external heavyweight JavaScript libraries; lightweight handlers for smooth navigation, embed reload, and responsive drawers.",
            "icon": "code"
        }
    ]
}


@app.route("/")
def index():
    """
    Renders the single-page portal displaying Overview, Dashboard,
    Story, and About sections.
    """
    # Compute embeddable endpoints
    dashboard_embed = format_tableau_embed_url(TABLEAU_DASHBOARD_URL)
    story_embed = format_tableau_embed_url(TABLEAU_STORY_URL)
    
    # Check validity for graceful degraded rendering if links are missing
    is_dashboard_configured = is_valid_tableau_url(TABLEAU_DASHBOARD_URL)
    is_story_configured = is_valid_tableau_url(TABLEAU_STORY_URL)
    
    return render_template(
        "index.html",
        config=PROJECT_CONFIG,
        dashboard_url=TABLEAU_DASHBOARD_URL,
        dashboard_embed_url=dashboard_embed,
        is_dashboard_configured=is_dashboard_configured,
        story_url=TABLEAU_STORY_URL,
        story_embed_url=story_embed,
        is_story_configured=is_story_configured
    )


if __name__ == "__main__":
    # Run development server locally on host 127.0.0.1 port 5000
    print("=" * 70)
    print(" Electric Vehicle Market Performance & Insights - College Project")
    print(" Server running locally at: http://127.0.0.1:5000")
    print(" Press CTRL+C to terminate the development server.")
    print("=" * 70)
    app.run(host="127.0.0.1", port=5000, debug=True)

