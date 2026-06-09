# AI Adoption Opportunity Project
## Market Research and Business Case — Education Consulting / LATAM → Germany
**Student:** Lucas Barrios | **Programme:** Ironhack Berlin — AI & Integration Consulting | **Date:** June 2026

---

## What This Project Is

This project builds a complete AI adoption business case for a fictional client — Cleo, CEO of a small digital-first education consulting firm that helps Spanish-speaking Latin Americans navigate university, Ausbildung (vocational training), and work visa pathways into Germany.

The central question is not "should Cleo use AI?" The better question is: **where does market data show AI adoption is worth investing in for this sector and company size?**

The deliverable is a research-backed, evidence-driven recommendation supported by an interactive Plotly Dash dashboard built on 8 public datasets.

---

## Sector and Company Size

**Sector:** Education consulting — study abroad and immigration advisory
**Company size:** Small, digital-first, 1–10 employees, fully remote
**Target market:** Spanish-speaking Latin Americans (Colombia, Brazil, Mexico, Chile, Peru) pursuing German university, Ausbildung, or skilled work pathways

---

## Project Structure

```
ai-adoption-opportunity-project/
│
├── data/
│   ├── raw/                          # Original datasets (not committed to git)
│   │   ├── student_mobility/
│   │   ├── study_abroad_share/
│   │   ├── german_universities/
│   │   ├── global_migration/
│   │   ├── europe_jobs/
│   │   ├── student_demographics/
│   │   ├── german_courses/
│   │   └── ai_impact/
│   └── processed/                    # Cleaned data outputs
│
├── research/
│   ├── market_research.md            # TAM/SAM/SOM, PESTLE, Porter's Five Forces
│   ├── opportunities_risks.md        # Risk register, EU AI Act, GDPR, Green AI
│   └── use_case_discovery.md         # 10 AI use cases scored across 5 dimensions
│
├── dashboard/
│   ├── dashboard_dash.py             # Main Plotly Dash dashboard (PRIMARY)
│   ├── dashboard.py                  # Streamlit version (supplementary)
│   └── dashboard_documentation.md   # Dashboard design and data documentation
│
├── implementation/
│   ├── solution_proposal.md          # Full investment case for Cleo
│   └── implementation_plan.md        # 14-day sprint plan, tech stack, go-live checklist
│
├── cost_estimation/
│   ├── cost_analysis.md              # Per use case costs, Scenario A/B, ROI
│   └── timeline_estimate.md          # 14-day critical path, 12-month roadmap
│
├── .env                              # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Quick Start

### 1. Clone and set up environment

```bash
git clone https://github.com/Lucas-Barrios/ai-adoption-opportunity-project.git
cd ai-adoption-opportunity-project

python -m venv venv
source venv/bin/activate       # Mac/Linux
# venv\Scripts\activate        # Windows

pip install -r requirements.txt
```

### 2. Download the datasets

Requires a Kaggle account and CLI authentication.

```bash
# Authenticate
kaggle auth login

# Download all datasets
kaggle datasets download -d danielarivasu/international-student-mobility \
  --unzip -p data/raw/student_mobility

kaggle datasets download -d thedevastator/share-of-students-studying-abroad-by-country \
  --unzip -p data/raw/study_abroad_share

kaggle datasets download -d phoellermann/enrolled-students-in-german-universities \
  --unzip -p data/raw/german_universities

kaggle datasets download -d atharvasoundankar/global-student-migration-and-higher-education-trends \
  --unzip -p data/raw/global_migration

kaggle datasets download -d thedevastator/job-postings-in-europe \
  --unzip -p data/raw/europe_jobs

kaggle datasets download -d webdevbadger/international-student-demographics \
  --unzip -p data/raw/student_demographics

kaggle datasets download -d azdurjoy/germanyunivcoursescomprehensivecatalog \
  --unzip -p data/raw/german_courses

kaggle datasets download -d laveshjadon/ai-impact-on-students \
  --unzip -p data/raw/ai_impact
```

### 3. Run the dashboard

```bash
python dashboard/dashboard_dash.py
```

Open `http://localhost:8050` in your browser.

---

## Dashboard Overview

The Plotly Dash dashboard is the primary deliverable. It presents the business case across 7 sections:

| Section | Question Answered |
|---|---|
| 01 Market Overview | How large is the opportunity and where does Cleo fit? |
| 02 Latin America Demand | Is there real, growing demand from LATAM for Germany pathways? |
| 03 Germany Supply | Does Germany have the capacity and need to absorb international students? |
| 04 Student Profiles | Who exactly is Cleo's student and what do they need? |
| 05 AI Use Cases | Which AI use cases are worth building and in what order? |
| 06 Risks and Compliance | What are the real risks and how does compliance become a moat? |
| 07 Recommendation | Should Cleo invest in AI, and on what terms? |

### Interactive Features

- **Pathway Focus filter** — University / Ausbildung / Work Visa — updates Germany Supply and AI Use Cases sections
- **Priority Market filter** — Colombia / Brazil / Mexico / Chile — updates LATAM Demand and Student Profiles
- **LATAM Countries multi-select** — filters outbound mobility charts
- **Year Range slider** — filters outbound mobility trend lines
- **Investment Scenario toggle** — Solo Operator / Small Team / Full Team — updates ROI cost structure
- **Interactive ROI calculator** — conversion rate and average ticket sliders update the break-even projection in real time
- **Progress step indicator** — always shows which section of the 7-section argument is active

---

## Datasets

| Dataset | Source | Rows | Real/Simulated |
|---|---|---|---|
| International Student Mobility | UNESCO UIS via Kaggle | 134 | Real |
| Share of Students Studying Abroad | UNESCO UIS via Kaggle | 2,407 | Real |
| Enrolled Students in German Universities | Destatis via Kaggle | 9,228 | Real |
| Global Student Migration | Kaggle (synthetic) | 5,000 | ⚠️ Simulated |
| European Job Postings | Kaggle | 39,774 | Real (2018) |
| International Student Demographics | IIE Open Doors via Kaggle | 22,000+ | Real |
| German University Courses (DAAD) | DAAD via Kaggle | 2,215 | Real |
| AI Impact on Students | Kaggle | 50,000 | Real |

**Note on the simulated dataset:** Global Student Migration is a synthetic dataset used for directional analysis only. All findings from it are corroborated against official DAAD and QS sources. Every chart using this dataset is clearly marked.

---

## Key Findings

**The investment case in three data points:**

1. **Demand is structural, not cyclical.** Canada's 50%+ permit drop and Australia's tightening are redirecting LATAM students toward Europe permanently. Germany enrolled a record 420,000+ international students in 2025/26 and is actively expanding capacity.

2. **The supply gap is urgent.** Germany has 617,000 unfilled jobs, Ausbildung positions average 222 days unfilled in nursing, and the 2023 Fachkräfteeinwanderungsgesetz opened non-EU vocational training visas. The regulatory door is open — the Spanish-language advisory infrastructure is not.

3. **No competitor occupies this position.** Every major study abroad AI platform (Leverage Edu, ApplyBoard, Study Metro) is generic and English-first. Zero AI-native Spanish-language advisory services exist for the Germany pathway. The competitive white space is real and currently unclaimed.

**Primary recommendation:** Invest in UC-01 (Germany Readiness Diagnostic Agent) first. Two-week MVP, €3,700, validated before any larger commitment. Break-even at Month 5 on conservative assumptions.

---

## Compliance Notes

Two AI use cases (UC-01 and UC-02) are classified as **High Risk** under EU AI Act Annex III — they profile individuals for educational access and vocational training assignment. Articles 9–15 compliance obligations apply including human oversight gate, DPIA, audit logging, and EU database registration before August 2, 2026.

All student data handling is subject to GDPR. Data Processing Agreements required with all third-party processors (LLM APIs, WhatsApp, CRM) before platform launch.

See `research/opportunities_risks.md` for the full compliance assessment.

---

## Requirements

```
dash==4.2.0
dash-bootstrap-components>=1.6.0
plotly>=5.22.0
pandas>=2.2.2
numpy>=1.26.4
openpyxl>=3.1.2
streamlit>=1.35.0
python-dotenv>=1.0.1
kagglehub[pandas-datasets]
kaggle>=2.2.1
```

Install with:
```bash
pip install -r requirements.txt
```

---

## File Map

| File | Description |
|---|---|
| `research/market_research.md` | Full market analysis with TAM/SAM/SOM, PESTLE, Porter's Five Forces. APA citations throughout. |
| `research/opportunities_risks.md` | Risk register (likelihood × impact), EU AI Act classification per use case, GDPR data flow assessment, Green AI evaluation, Trust Architecture framework. |
| `research/use_case_discovery.md` | 10 AI use cases scored across Business Impact, Differentiation, AI Fit, Feasibility, and Time to Value. Competitive landscape table. Primary and secondary recommendations with justification. |
| `implementation/solution_proposal.md` | Full investment case including build vs buy decisions, end-to-end system flow, two cost scenarios (MVP and scale), ROI analysis, and the strategic window argument. |
| `implementation/implementation_plan.md` | Day-by-day 14-day MVP sprint, complete tech stack with configuration sequence, dependency tree, go-live checklist with 20 items, rollback procedures for 5 failure scenarios. |
| `cost_estimation/cost_analysis.md` | Cost per use case, Scenario A (€3,700 MVP) and Scenario B (€16K–€19K/month scale), revenue model with three tiers, break-even analysis, opportunity cost argument. |
| `cost_estimation/timeline_estimate.md` | 14-day critical path with day-by-day tasks, 12-month milestone roadmap, compliance timeline tied to EU AI Act August 2026 enforcement, dependency and blocker register. |
| `dashboard/dashboard_dash.py` | Plotly Dash dashboard — primary deliverable. 8 datasets, 7 sections, 5 interactive filters, real-time ROI calculator, responsive design. |
| `dashboard/dashboard.py` | Streamlit version — supplementary. Same data and narrative, alternative rendering. |
| `dashboard/dashboard_documentation.md` | Full documentation of dashboard design decisions, chart type rationale, data sources, section-by-section breakdown, and technical architecture. |

---

## Methodology Notes

**Use case scoring framework:** Each of the 10 AI use cases was scored across 5 dimensions (Business Impact, Differentiation, AI Fit, Feasibility, Time to Value) on a 1–5 scale. Maximum score: 25. Priority tiers: Critical (20+), High (15–19), Medium (10–14). Scores reflect market evidence from the research phase, not subjective preference.

**Risk scoring:** Risks scored as Likelihood (1–5) × Impact (1–5). Maximum risk score: 25. High-risk threshold: 15+. Risk register contains 9 identified risks across Regulatory, Legal, Operational, Market, Ethical, Technical, and Reputational categories.

**EU AI Act classification:** Based on Regulation (EU) 2024/1689 and its Annexes. Classification methodology: check for Annex III triggers (education and vocational training systems that profile individuals for access), then assess whether automated processing affects significant decisions about natural persons.

**Market size figures:** Sourced from published commercial market research reports. Treated as directional estimates rather than precise valuations per standard consulting methodology for TAM sizing.

---

*AI Adoption Opportunity Project · Ironhack Berlin AI & Integration Consulting Program · June 2026*
*Lucas Barrios · Kairos Consulting · kairosconsulting.co*