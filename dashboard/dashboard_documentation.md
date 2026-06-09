# Dashboard Documentation
## AI Adoption Market Intelligence Dashboard
### AI Adoption Opportunity Project — Ironhack Berlin
**Author:** Lucas Barrios | **Date:** June 2026 | **Version:** 2.1

---

## 1. Overview

This dashboard presents the market evidence supporting an AI investment decision for Cleo, CEO of a small digital-first education consulting firm targeting Spanish-speaking Latin Americans pursuing German university, Ausbildung, and work visa pathways.

**Tool:** Plotly Dash 4.2 (Python)
**Run command:** `python dashboard/dashboard_dash.py`
**Local URL:** `http://localhost:8050`
**File:** `dashboard/dashboard_dash.py`

The dashboard is organised as a 7-section narrative that builds from market sizing to a specific investment recommendation. Each section answers one question. Together they answer the central question: **should Cleo invest in AI now, and if so, where exactly?**

---

## 2. Design Principles Applied

This dashboard was built following the data visualisation principles from the Ironhack Module 5 lesson. Key decisions:

### Chart Type Selection (Encoding Hierarchy)
- **Horizontal bar charts** used for all category comparisons — position along a common scale (rank 1 in accuracy) rather than angle or area
- **Radar chart replaced** with a grouped horizontal bar for the top 3 use case comparison — radar uses angle (rank 4); grouped bar uses position (rank 1)
- **Line charts** used for all time series data — the connecting line implies continuous change between measurements, which is appropriate for enrollment trends and mobility rates
- **Scatter plot** used for the competitive positioning 2×2 — two quantitative axes (AI capability, LATAM+Germany specialisation) with bubble size as a tertiary variable only
- **Funnel chart** used for TAM/SAM/SOM — appropriate for showing progressive narrowing of a market opportunity
- **Grouped bar** used for all before/after and multi-scenario comparisons — barmode='group' with position encoding

### Color Discipline
- **One signal color:** `#1D4ED8` (professional blue) — used only for the element Cleo must focus on in each chart
- **Everything else:** `#D1D5DB` (gray) for noise, `#9CA3AF` for secondary elements
- **Exception colors:** `#DC2626` (red) for risk/negative, `#D97706` (amber) for warnings, `#059669` (green) for positive outcomes
- No decorative color — every color encodes meaning

### Headline Titles
Every chart title states the conclusion the reader should draw, not a description of the axes. Examples:
- ❌ "International Students by Semester" 
- ✅ "Germany has broken its own enrollment record every year since 2010."

### So What Annotations
Every chart ends with a "So what:" annotation written in plain conversational language explaining the business implication for Cleo. This answers the question a non-technical CEO would ask after seeing the data.

### Data-Ink Ratio
- Y-axis gridlines removed on horizontal bar charts (bars provide their own reference)
- X-axis gridlines kept light (`#F3F4F6`) where they aid reading values
- No chart borders, 3D effects, or decorative backgrounds
- Legend placed horizontally below chart where possible to maximise chart area

---

## 3. Section-by-Section Documentation

### Section 01 — Market Overview
**Question answered:** How large is the opportunity and where does Cleo fit?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| Top 15 student-exporting countries | Horizontal bar | UNESCO UIS via Kaggle (danielarivasu) | LATAM countries appear in global top 15 but receive no targeted advisory |
| Study abroad and AI in education market growth | Dual line | Cognitive Market Research 2024, Grand View Research 2024 | Both markets growing simultaneously — enter before the curve steepens |
| TAM/SAM/SOM | Funnel | Market research synthesis | Cleo's opportunity is specific, defensible and currently uncrowded |

**About the Data card:** Explains real vs simulated data sources upfront so readers don't encounter unexplained warnings mid-dashboard.

---

### Section 02 — Latin America Demand
**Question answered:** Is there real, growing demand from Latin America for Germany pathways?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| Outbound mobility rate by country over time | Multi-line | UNESCO UIS via Kaggle (thedevastator) | Colombia and Brazil lead — both are Germany's top DAAD recipients |
| Outbound rate ranking (latest year) | Horizontal bar | Same | Single-year snapshot for comparison |
| Anglophone destination collapse | Grouped bar | ICEF Monitor 2024/25, ApplyBoard Research | Germany is the only major destination growing |
| Where LATAM students go | Horizontal bar | Global Student Migration dataset (simulated) | Germany already ranks high without any advisory support |
| Scholarship rates by country | Horizontal bar | Global Student Migration dataset (simulated) | Colombia and Brazil have strongest institutional backing |

**Filter interaction:** Country filter and year range both affect this section. Priority Market filter overrides country selection to single-country focus with a contextual stat card.

---

### Section 03 — Germany Supply
**Question answered:** Does Germany have the capacity and the need to absorb international students?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| International student enrollment trend | Area line | German University Enrollment via Kaggle (phoellermann) | Record enrollment every year since 2010 |
| International share of total enrollment | Bar | Same | Rising share — structural integration, not tolerance |
| Ausbildung vacancies by sector | Horizontal bar | BIBB 2024, Bundesagentur 2025, FMC Group 2025 | Nursing and IT have most unfilled positions — both high LATAM fit |
| Average days positions stay unfilled | Horizontal bar | Same | Employers lose months of productivity — they will pay for pre-screened candidates |
| Origin countries of Germany-bound students | Horizontal bar | Global Student Migration (simulated) | LATAM already appears without advisory support |
| German courses by subject | Horizontal bar | DAAD Studiengangsdatenbank via Kaggle (azdurjoy) | Engineering and sciences dominate — match to vacancy sectors |
| German courses by city | Horizontal bar | Same | Berlin leads but options distributed across all major cities |
| Teaching language distribution | Horizontal bar | Same | English-accessible programmes lower the barrier for early-stage students |

**Filter interaction:** Pathway filter adds a contextual info box highlighting the most relevant data for the selected pathway (University/Ausbildung/Work Visa).

---

### Section 04 — Student Profiles
**Question answered:** Who exactly is Cleo's student, and what do they need?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| Field of study — LATAM students | Horizontal bar | Global Student Migration (simulated) | Engineering and healthcare map to Germany's highest-vacancy sectors |
| Enrollment reason | Horizontal bar | Global Student Migration (simulated) | Career advancement is the #1 driver — lead with outcomes |
| Language test distribution | Horizontal bar | Global Student Migration (simulated) | English test dominance signals German language prep gap |
| Global fields of study | Horizontal bar | IIE Open Doors via Kaggle (webdevbadger) | Business and engineering attract most international students globally |

**Filter interaction:** Priority Market filter prepends a one-sentence context box describing that country's specific student profile characteristics.

---

### Section 05 — AI Use Cases
**Question answered:** Which AI use cases are worth building and in what order?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| All 10 use cases priority score | Horizontal bar | Use case scoring framework | 7 of 10 score Critical — genuine market gaps with strong AI fit |
| Top 3 use cases across 5 dimensions | Grouped horizontal bar | Use case scoring framework | UC-01 leads; UC-02 wins on differentiation |
| Competitive positioning 2×2 | Scatter | Public product analysis, June 2026 | Every competitor sits bottom-left. Cleo's position is unclaimed. |
| LATAM interest vs Germany vacancies | Grouped bar | BIBB 2024, DAAD 2024, simulated data | Sector match validates UC-02 data-first |
| Implementation timeline | Gantt | Implementation plan | 14-day MVP, everything else sequenced after validation |
| GenAI hours by major | Horizontal bar | Kaggle — laveshjadon (50,000 students) | STEM students already use AI 7+ hours/week |
| Primary AI use cases | Horizontal bar | Same | Top use cases map to UC-01, UC-04, UC-07 |
| Paid subscription rates | Horizontal bar | Same | Target majors already pay for AI tools |
| GPA delta by AI usage band | Bar | Same | Moderate AI use correlates with academic improvement |

**Filter interaction:** Pathway filter reorders the priority bar so the most relevant use case for the selected pathway appears at top with a contextual badge.

---

### Section 06 — Risks and Compliance
**Question answered:** What are the real risks and how does compliance become a competitive advantage?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| Risk matrix | Scatter (likelihood × impact × size) | Risk register | 3 critical risks share the same mitigation |
| EU AI Act classification list | Card component | Regulation (EU) 2024/1689 | UC-01 and UC-02 are High Risk under Annex III |
| Risk scores ranked | Horizontal bar | Risk register | Only 3 exceed the high-risk threshold |

**Design note:** The EU AI Act classification panel is an HTML component rather than a chart — the data is categorical and a structured list communicates it more clearly than any chart type would.

---

### Section 07 — Recommendation
**Question answered:** Should Cleo invest in AI, and on what terms?

| Chart | Type | Data Source | Message |
|---|---|---|---|
| Decision cards (3 options) | Card component | — | Invest Now is the data-supported answer |
| Interactive ROI calculator | Line chart + sliders | Scenario analysis | Cleo can test her own assumptions in real time |
| Investment comparison | Grouped bar | cost_analysis.md | MVP at €3,700 pays back by Month 5 (conservative) |
| Three forces summary | Card component | Market research synthesis | Three converging forces create a time-sensitive window |

**Interactive elements:**
- **Conversion rate slider** (5–40%): adjusts the monthly client volume assumption
- **Average ticket slider** (€200–€1,500): adjusts revenue per paying client
- **Investment Scenario toggle** (Solo/Small Team/Full Team): switches the cost structure on the ROI chart

---

## 4. Interactive Filters

The dashboard has four interactive filters in the sidebar. All filters are connected to the main navigation callback and update relevant sections in real time.

| Filter | ID | Options | Affects |
|---|---|---|---|
| Pathway Focus | `pathway-filter` | All / University / Ausbildung / Work Visa | Sections 03, 05 |
| Priority Market | `market-filter` | All / Colombia / Brazil / Mexico / Chile | Sections 02, 04 |
| LATAM Countries | `filter-countries` | Multi-select, 20 countries | Section 02 |
| Year Range | `filter-years` | 2000–2022 | Section 02 |
| Investment Scenario | `scenario-filter` | Solo / Small Team / Full Team | Section 07 ROI chart |

---

## 5. Data Sources

| Dataset | Source | Type | Used In |
|---|---|---|---|
| International Student Mobility 2020–2023 | Kaggle — danielarivasu | Real | Sections 01, 02 |
| Share of Students Studying Abroad | Kaggle — thedevastator | Real (UNESCO UIS) | Section 02 |
| Enrolled Students in German Universities | Kaggle — phoellermann | Real | Section 03 |
| Global Student Migration | Kaggle — atharvasoundankar | ⚠️ Simulated | Sections 02, 03, 04 |
| European Job Postings | Kaggle — thedevastator | Real (2018) | Section 03 |
| International Student Demographics | Kaggle — webdevbadger (IIE Open Doors) | Real | Section 04 |
| German University Courses | Kaggle — azdurjoy (DAAD) | Real | Section 03 |
| AI Impact on Students | Kaggle — laveshjadon | Real | Section 05 |
| Market size projections | Cognitive Market Research, Grand View Research | Real (published reports) | Section 01 |
| BIBB vacancy data | BIBB Annual Vocational Training Report 2024 | Real (hardcoded from report) | Section 03 |
| Anglophone displacement index | ICEF Monitor 2024/25, ApplyBoard Research | Real (hardcoded) | Section 02 |

**Note on simulated data:** The Global Student Migration dataset is synthetic. It is used for directional trend analysis only and is explicitly marked throughout the dashboard. All directional findings from this dataset are corroborated by official DAAD country statistics and QS Global Student Flows 2024.

---

## 6. Technical Architecture

```
dashboard_dash.py
├── Imports and color constants
├── Layout helper functions (card, row2, row3, sw, nt, sh, g, CL)
├── Data loading (raw() — cached with functools.lru_cache)
├── Data processing (D() — returns processed dict)
├── Section functions (s_market, s_latam, s_germany, s_profiles,
│                      s_usecases, s_risks, s_reco)
├── CSS (injected via app.index_string)
├── App layout (sidebar + progress bar + main content)
└── Callbacks
    ├── render_page — navigation + all filter inputs → page content
    ├── update_nav — nav buttons → nav store
    ├── style_nav — nav store → button classes
    ├── update_roi — sliders + scenario → ROI chart + summary
    └── update_progress — nav store → progress bar steps
```

**Caching:** `raw()` uses `functools.lru_cache(maxsize=1)` so datasets are loaded from disk once per server session, not on every page render.

**Responsive design:** All `dcc.Graph` components use `responsive=True`. CSS media query at 900px breakpoint stacks sidebar above main content on narrow screens.

---

## 7. Known Limitations

- **Simulated dataset**: Global Student Migration is synthetic. Country-level student flow numbers should be treated as directional only.
- **Job postings dataset**: European job postings data is from 2018. Used for sector distribution analysis only — not for current job volume claims.
- **Market size projections**: Commercial market research reports use different methodologies. The $23.5B TAM figure is a directional estimate, not a precise valuation.
- **Competitive positioning**: The 2×2 quadrant scores are qualitative assessments based on public product analysis as of June 2026. Competitor positions may have shifted.

---

## 8. Running the Dashboard

**Prerequisites:**
```bash
pip install -r requirements.txt
```

**Run from project root:**
```bash
python dashboard/dashboard_dash.py
```

**Access:** `http://localhost:8050`

**Data files required** (must be present in `data/raw/` before running):
```
data/raw/student_mobility/international_student_mobility - data.csv
data/raw/study_abroad_share/Share of Students Studying Abroad.csv
data/raw/german_universities/Enrolled students.xlsx
data/raw/global_migration/global_student_migration.csv
data/raw/europe_jobs/emed_careers_eu.csv
data/raw/student_demographics/field_of_study.csv
data/raw/german_courses/All_Courses_In_Germany.csv
data/raw/ai_impact/ai_student_impact_dataset (1).csv
```

---

*Dashboard Documentation — AI Adoption Opportunity Project · Ironhack Berlin · June 2026*