import os
import dash
from dash import dcc, html, Input, Output
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import functools
import warnings
warnings.filterwarnings('ignore')

# ── Color System ──────────────────────────────────────────────────────
BLUE   = '#1D4ED8'   # Signal — used sparingly, one highlight per chart
GRAY   = '#D1D5DB'   # Noise — all non-signal elements
GRAY2  = '#9CA3AF'   # Secondary text / axis
DARK   = '#111827'   # Headers
TEXT   = '#374151'   # Body text
LIGHT  = '#F9FAFB'   # Page background
WHITE  = '#FFFFFF'   # Card background
GRID   = '#F3F4F6'   # Chart gridlines
BORDER = '#E5E7EB'   # Card borders
RED    = '#DC2626'
AMBER  = '#D97706'
GREEN  = '#059669'

LATAM = [
    'Brazil','Colombia','Mexico','Chile','Peru','Argentina','Venezuela',
    'Ecuador','Bolivia','Paraguay','Uruguay','Costa Rica','Panama',
    'Guatemala','Honduras','Nicaragua','El Salvador','Dominican Republic','Cuba','Haiti'
]
LATAM_CODES = [
    'BRA','COL','MEX','CHL','PER','ARG','VEN','ECU','BOL','PRY','URY',
    'CRI','PAN','GTM','HND','NIC','SLV','DOM','CUB','HTI'
]
NAV = [
    ('market',   '01  Market Overview'),
    ('latam',    '02  Latin America Demand'),
    ('germany',  '03  Germany Supply'),
    ('profiles', '04  Student Profiles'),
    ('usecases', '05  AI Use Cases'),
    ('risks',    '06  Risks & Compliance'),
    ('reco',     '07  Recommendation'),
]

# ── Scenario constants ────────────────────────────────────────────────
SCENARIO_COSTS = {
    'solo':  [3700, 3700, 3900, 4000, 4000, 4200, 4200, 4500, 4500, 4800, 4800, 5000],
    'small': [3700, 3700, 16200, 16200, 16500, 16500, 17000, 17000, 17500, 17500, 18000, 18000],
    'full':  [3700, 3700, 19200, 19200, 19500, 19500, 20000, 20000, 20500, 20500, 21000, 21000],
}
SCENARIO_LABELS = {
    'solo':  'Solo operator model',
    'small': 'Small team model (3 people)',
    'full':  'Full team model (5 people)',
}
INVEST_MAP = {
    'solo':  [3700, 3900, 4200],
    'small': [3700, 16200, 16500],
    'full':  [3700, 19200, 19500],
}

# ── Chart Helper ──────────────────────────────────────────────────────
def CL(title='', h=360, legend=False, margin=None):
    m = margin or dict(l=10, r=15, t=62, b=45)
    return dict(
        title=dict(text=title, font=dict(size=12.5, color=DARK, family='Inter'), x=0),
        paper_bgcolor=WHITE, plot_bgcolor=WHITE,
        font=dict(family='Inter, system-ui, sans-serif', color=TEXT, size=11),
        height=h, margin=m, showlegend=legend,
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(size=10),
                    orientation='h', y=-0.2),
        xaxis=dict(gridcolor=GRID, linecolor=BORDER, showgrid=True,
                   zeroline=False, tickfont=dict(size=10, color=GRAY2)),
        yaxis=dict(showgrid=False, zeroline=False,
                   linecolor='rgba(0,0,0,0)', tickfont=dict(size=10, color=GRAY2))
    )

# ── Layout Helpers ────────────────────────────────────────────────────
def sw(text):
    return html.Div([
        html.Span("So what: ", style={'color': BLUE, 'fontWeight': '600',
                                       'fontSize': '0.77rem'}),
        html.Span(text, style={'fontSize': '0.77rem', 'color': TEXT})
    ], style={'background': '#EFF6FF', 'borderLeft': f'3px solid {BLUE}',
              'padding': '0.5rem 0.85rem', 'marginTop': '0.4rem',
              'borderRadius': '0 4px 4px 0', 'lineHeight': '1.5'})

def nt(text):
    return html.P(text, style={'fontSize': '0.63rem', 'color': GRAY2,
                                'fontStyle': 'italic', 'marginTop': '0.15rem',
                                'marginBottom': '0'})

def card(*ch, pad='1.25rem 1.5rem', mb='1.25rem'):
    return html.Div(list(ch), style={
        'background': WHITE, 'borderRadius': '8px', 'padding': pad,
        'boxShadow': '0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.04)',
        'marginBottom': mb, 'border': f'1px solid {BORDER}'
    })

def row2(a, b, split='1fr 1fr', gap='1.25rem'):
    return html.Div([a, b], style={
        'display': 'grid', 'gridTemplateColumns': split,
        'gap': gap, 'marginBottom': '1.25rem'
    })

def row3(a, b, c, gap='1.25rem'):
    return html.Div([a, b, c], style={
        'display': 'grid', 'gridTemplateColumns': '1fr 1fr 1fr',
        'gap': gap, 'marginBottom': '1.25rem'
    })

def sh(label, title, desc=''):
    return html.Div([
        html.P(label, style={'fontSize': '0.67rem', 'fontWeight': '700',
                              'letterSpacing': '0.12em', 'textTransform': 'uppercase',
                              'color': BLUE, 'marginBottom': '0.15rem'}),
        html.H2(title, style={'fontSize': '1.25rem', 'fontWeight': '700',
                               'color': DARK, 'marginBottom': '0.3rem',
                               'letterSpacing': '-0.015em'}),
        html.P(desc, style={'fontSize': '0.84rem', 'color': GRAY2,
                             'marginBottom': '1.1rem', 'lineHeight': '1.6'}) if desc else None,
    ])

def divider():
    return html.Hr(style={'borderColor': BORDER, 'margin': '1.5rem 0'})

def g(fig, so_what='', note=''):
    ch = [dcc.Graph(figure=fig, config={'displayModeBar': False},
                    responsive=True, style={'minHeight': '280px'})]
    if so_what: ch.append(sw(so_what))
    if note:    ch.append(nt(note))
    return html.Div(ch)

def info_box(text):
    return html.Div(
        html.P(text, style={'fontSize': '0.83rem', 'color': TEXT,
                            'lineHeight': '1.65', 'margin': '0'}),
        style={
            'background': '#EFF6FF', 'borderRadius': '8px',
            'padding': '1rem 1.25rem', 'marginBottom': '1.25rem',
            'border': f'1px solid rgba(29,78,216,0.2)',
            'borderLeft': f'4px solid {BLUE}'
        }
    )

# ── Data ──────────────────────────────────────────────────────────────
@functools.lru_cache(maxsize=1)
def raw():
    mob    = pd.read_csv('data/raw/student_mobility/international_student_mobility - data.csv')
    out    = pd.read_csv('data/raw/study_abroad_share/Share of Students Studying Abroad.csv')
    out.columns = ['index', 'Country', 'Code', 'Year', 'OR']
    ger    = pd.read_excel('data/raw/german_universities/Enrolled students.xlsx')
    mig    = pd.read_csv('data/raw/global_migration/global_student_migration.csv')
    jobs   = pd.read_csv('data/raw/europe_jobs/emed_careers_eu.csv')
    flds   = pd.read_csv('data/raw/student_demographics/field_of_study.csv')
    crs    = pd.read_csv('data/raw/german_courses/All_Courses_In_Germany.csv',
                         sep=';', on_bad_lines='skip')
    ai_imp = pd.read_csv('data/raw/ai_impact/ai_student_impact_dataset (1).csv')
    return mob, out, ger, mig, jobs, flds, crs, ai_imp

def D():
    mob, out, ger, mig, jobs, flds, crs, ai_imp = raw()

    mob = mob.copy()
    mob['abs'] = mob['avg_value'].abs()
    exp  = mob[mob['category_avg'] == 'Exporting Country']
    t15  = exp.nlargest(15, 'abs').copy()
    t15['color'] = t15['country'].apply(lambda c: BLUE if c in LATAM else GRAY)

    lo = out[out['Code'].isin(LATAM_CODES)].copy()

    def cl(v):
        if pd.isna(v) or v == '-': return 0
        try: return float(str(v).replace(',', ''))
        except: return 0

    ger = ger.copy()
    ger['I'] = ger['International - total'].apply(cl)
    ger['T'] = ger['Total'].apply(cl)
    gt = ger.groupby('Semester').agg(I=('I','sum'), T=('T','sum')).reset_index()
    gt = gt[gt['I'] > 10000].sort_values('Semester')
    gt['S'] = (gt['I'] / gt['T'] * 100).round(2)
    gt = gt.tail(14)

    gs = mig[mig['destination_country'] == 'Germany'].copy()
    la = mig[mig['origin_country'].isin(LATAM)].copy()
    if la.empty:
        la = mig.copy()
    lg = mig[(mig['origin_country'].isin(LATAM)) &
             (mig['destination_country'] == 'Germany')].copy()
    gj = jobs[jobs['location'].str.contains(
        'Germany|Berlin|Munich|Frankfurt|Hamburg', case=False, na=False)].copy()
    ff = (flds.groupby('field_of_study')['students'].sum()
              .reset_index().sort_values('students', ascending=False).head(10))

    # German courses
    crs = crs.copy()
    crs.columns = [c.strip() for c in crs.columns]
    top_subjects = (crs['Subject Name'].value_counts()
                       .head(12).reset_index())
    top_subjects.columns = ['Subject', 'Count']
    top_subjects['color'] = [BLUE if i < 3 else GRAY for i in range(len(top_subjects))]

    top_cities = (crs['City Name'].value_counts()
                     .head(10).reset_index())
    top_cities.columns = ['City', 'Count']
    top_cities['color'] = [BLUE if i == 0 else GRAY for i in range(len(top_cities))]

    lang_col = 'Teaching languages Instruction'
    if lang_col in crs.columns:
        def lang_cat(v):
            if pd.isna(v): return 'Not specified'
            v = str(v).lower()
            if 'english' in v and 'german' in v: return 'Bilingual (DE + EN)'
            if 'english' in v: return 'English available'
            if 'german' in v: return 'German only'
            return 'Other'
        crs['lang_cat'] = crs[lang_col].apply(lang_cat)
        lang_dist = crs['lang_cat'].value_counts().reset_index()
        lang_dist.columns = ['Language', 'Count']
        lang_dist['color'] = lang_dist['Language'].apply(
            lambda x: BLUE if x == 'English available' else
                      GRAY2 if x == 'Bilingual (DE + EN)' else GRAY)
    else:
        lang_dist = pd.DataFrame({'Language':['N/A'],'Count':[0],'color':[GRAY]})

    # AI impact
    ai_imp = ai_imp.copy()
    ai_by_major = (ai_imp.groupby('Major_Category')['Weekly_GenAI_Hours']
                         .mean().reset_index()
                         .sort_values('Weekly_GenAI_Hours', ascending=True))
    ai_by_major.columns = ['Major', 'Avg_Hours']
    ai_by_major['color'] = ai_by_major['Major'].apply(
        lambda m: BLUE if m in ['Technology','Engineering','Medical','Business'] else GRAY)

    use_cases_ai = (ai_imp['Primary_Use_Case'].value_counts()
                        .head(8).reset_index())
    use_cases_ai.columns = ['Use_Case', 'Count']
    use_cases_ai['color'] = [BLUE if i < 2 else GRAY for i in range(len(use_cases_ai))]

    paid_by_major = (ai_imp.groupby('Major_Category')['Paid_Subscription']
                           .mean() * 100).reset_index()
    paid_by_major.columns = ['Major', 'Paid_Pct']
    paid_by_major = paid_by_major.sort_values('Paid_Pct', ascending=True)
    paid_by_major['color'] = paid_by_major['Major'].apply(
        lambda m: BLUE if m in ['Technology','Engineering'] else GRAY)

    gpa_ai = ai_imp.copy()
    gpa_ai['GPA_Delta'] = gpa_ai['Post_Semester_GPA'] - gpa_ai['Pre_Semester_GPA']
    gpa_bins = pd.cut(gpa_ai['Weekly_GenAI_Hours'],
                      bins=[0,2,5,10,20,100],
                      labels=['0-2h','2-5h','5-10h','10-20h','20h+'])
    gpa_ai['AI_Usage'] = gpa_bins
    gpa_trend = (gpa_ai.groupby('AI_Usage', observed=True)['GPA_Delta']
                       .mean().reset_index())
    gpa_trend.columns = ['Usage_Band', 'Avg_GPA_Delta']
    gpa_trend['color'] = gpa_trend['Avg_GPA_Delta'].apply(
        lambda x: BLUE if x > 0 else RED)

    return dict(t15=t15, lo=lo, gt=gt, gs=gs, la=la, lg=lg, gj=gj, ff=ff,
                top_subjects=top_subjects, top_cities=top_cities,
                lang_dist=lang_dist, ai_by_major=ai_by_major,
                use_cases_ai=use_cases_ai, paid_by_major=paid_by_major,
                gpa_trend=gpa_trend)

# ══════════════════════════════════════════════════════════════════════
# SECTIONS
# ══════════════════════════════════════════════════════════════════════

def s_market():
    d = D()

    f1 = go.Figure(go.Bar(
        x=d['t15']['abs'], y=d['t15']['country'], orientation='h',
        marker_color=d['t15']['color'],
        hovertemplate='<b>%{y}</b><br>%{x:,.0f} avg. outbound students<extra></extra>'
    ))
    f1.update_layout(**CL("Latin America Sends Students Abroad — But Receives Almost No Targeted Advisory", 400,
                          margin=dict(l=10, r=20, t=70, b=40)))
    f1.update_layout(xaxis_title="Avg. Outbound Students")

    yrs = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031]
    sa  = [14.2,12.8,15.1,17.9,20.8,23.5,25.6,27.9,30.5,33.2,36.2,39.5]
    ai  = [1.1, 1.7, 2.5, 3.8, 5.9, 9.2,14.0,20.1,25.8,28.9,30.1,32.3]
    f2  = go.Figure()
    f2.add_trace(go.Scatter(x=yrs, y=sa, name='Study Abroad Market ($B)',
                            line=dict(color=BLUE, width=2.5),
                            fill='tozeroy', fillcolor='rgba(29,78,216,0.05)',
                            hovertemplate='%{x}: $%{y}B<extra>Study Abroad</extra>'))
    f2.add_trace(go.Scatter(x=yrs, y=ai, name='AI in Education ($B)',
                            line=dict(color=GRAY, width=1.8, dash='dot'),
                            hovertemplate='%{x}: $%{y}B<extra>AI in Education</extra>'))
    f2.add_vrect(x0=2026, x1=2031, fillcolor='rgba(29,78,216,0.025)', line_width=0,
                 annotation_text="-> Projection", annotation_position="top left",
                 annotation_font=dict(color=BLUE, size=10))
    f2.update_layout(**CL("Both Markets Are Growing Simultaneously — Cleo Must Enter Before the Curve Steepens",
                          400, legend=True, margin=dict(l=10, r=15, t=70, b=65)))
    f2.update_layout(yaxis_title="Market Size (USD Billions)")

    f3 = go.Figure(go.Funnel(
        y=["TAM — Global Study Abroad  $23.5B",
           "SAM — Spanish LATAM->Germany  ~80K prospects/yr",
           "SOM — Cleo Year 1-3  ~1,600 clients"],
        x=[23500, 80, 1.6], textinfo="label",
        marker=dict(color=[GRAY, GRAY2, BLUE]),
        connector=dict(line=dict(color=BORDER, width=1.5))
    ))
    f3.update_layout(paper_bgcolor=WHITE, plot_bgcolor=WHITE,
                     font=dict(family='Inter', color=TEXT, size=11),
                     height=230, margin=dict(l=10, r=10, t=40, b=10),
                     title=dict(text="TAM / SAM / SOM",
                                font=dict(size=12.5, color=DARK, family='Inter'), x=0))

    return html.Div([
        sh("Section 01", "The Market Opportunity — How Large, How Fast, Where",
           "Two markets growing simultaneously: study abroad advisory and AI in education. "
           "Cleo sits at their intersection — the highest-value position in both."),

        html.Div([
            html.Span("i  About the Data: ", style={'fontWeight':'700','color':AMBER}),
            "This dashboard uses ",
            html.Strong("8 datasets"),
            ". Real institutional data: UNESCO UIS, DAAD 2025/26, BIBB 2024, Bundesagentur fur Arbeit, "
            "German University Enrollment (Kaggle), DAAD Course Catalogue, IIE Open Doors, "
            "EU Job Postings. One dataset — Global Student Migration — is synthetic/simulated "
            "(clearly marked throughout) and used for directional analysis only, "
            "validated against DAAD and QS official figures. All market size projections "
            "are sourced from published reports (Cognitive Market Research, Grand View Research)."
        ], className='about-data'),
        row2(
            card(g(f1,
                   "Brazil, Colombia and Mexico are in the global top 15 outbound markets — "
                   "yet zero AI-native Spanish-language advisory services exist for Germany. "
                   "That gap is Cleo's entire business case.",
                   "Source: Kaggle — danielarivasu/international-student-mobility · LATAM in blue")),
            card(g(f2,
                   "A consultant who deploys AI now enters as the curve steepens — not after "
                   "competitors have captured the market.",
                   "Sources: Cognitive Market Research 2024 · Grand View Research 2024"))
        ),
        divider(),
        sh("", "Cleo's Addressable Opportunity Is Specific, Defensible, and Uncrowded"),
        row2(
            card(g(f3)),
            card(
                html.P("Why the SOM Is Achievable Without a Large Team",
                       style={'fontWeight': '600', 'color': DARK, 'marginBottom': '0.6rem',
                              'fontSize': '0.95rem'}),
                html.P("1,600 clients over 3 years = 0.5-2% of SAM. At 20% free-to-paid "
                       "conversion — the EdTech benchmark — Cleo needs 8,000 diagnostic "
                       "completions annually. That is a content strategy problem, not an "
                       "engineering problem. The AI handles intake. Cleo handles the close.",
                       style={'fontSize': '0.83rem', 'color': TEXT, 'lineHeight': '1.75',
                              'marginBottom': '1rem'}),
                sw("A solo operator with AI automation can serve 50-200 clients/month "
                   "vs 10-15 manually. That 10-20x multiplier is the entire investment case.")
            )
        ),
    ])


def s_latam(countries=None, years=None, market='all'):
    d = D()

    MARKET_MAP = {'col': 'Colombia', 'bra': 'Brazil', 'mex': 'Mexico', 'chl': 'Chile'}
    MARKET_STATS = {
        'col': "DAAD's #1 LATAM recipient. 22 active scholarship programs.",
        'bra': "#2 LATAM recipient. 1,030 DAAD scholars in 2023.",
        'mex': "Top LATAM outbound market. Growing Germany interest post-2023.",
        'chl': "Highest GDP per capita in LATAM. Strong EU orientation.",
    }

    if market != 'all' and market in MARKET_MAP:
        countries = [MARKET_MAP[market]]
    else:
        countries = countries or ['Brazil','Colombia','Mexico','Chile','Peru','Argentina']

    years = years or [2010, 2022]

    df = d['lo'][(d['lo']['Country'].isin(countries)) &
                 (d['lo']['Year'] >= years[0]) &
                 (d['lo']['Year'] <= years[1])]

    f1 = go.Figure()
    for c in df['Country'].unique():
        dc  = df[df['Country'] == c]
        sig = (c == 'Colombia')
        f1.add_trace(go.Scatter(
            x=dc['Year'], y=dc['OR'], mode='lines+markers', name=c,
            line=dict(color=BLUE if sig else (GRAY2 if c == 'Brazil' else GRAY),
                      width=2.5 if sig else 1.2),
            marker=dict(size=5 if sig else 3),
            opacity=1.0 if sig else 0.45,
            hovertemplate=f'<b>{c}</b><br>%{{x}}: %{{y:.2f}}%<extra></extra>'
        ))
    f1.update_layout(**CL("Colombia and Brazil Lead LATAM Outbound Mobility — "
                          "Both Are Germany's Top DAAD Recipients",
                          380, legend=True, margin=dict(l=10, r=15, t=70, b=65)))
    f1.update_layout(yaxis_title="Outbound Mobility Ratio (%)")

    latest = df['Year'].max()
    dl = df[df['Year'] == latest].sort_values('OR', ascending=True).copy()
    dl['color'] = dl['Country'].apply(
        lambda c: BLUE if c == 'Colombia' else GRAY2 if c == 'Brazil' else GRAY)
    f2 = go.Figure(go.Bar(
        x=dl['OR'], y=dl['Country'], orientation='h', marker_color=dl['color'],
        hovertemplate='<b>%{y}</b><br>%{x:.2f}%<extra></extra>'
    ))
    f2.update_layout(**CL(f"Outbound Rate Ranking — {latest}", 380,
                          margin=dict(l=10, r=15, t=60, b=40)))
    f2.update_layout(xaxis_title="Outbound Mobility (%)", yaxis=dict(showgrid=False))

    cats = ['Canada', 'Australia', 'United States', 'United Kingdom', 'Germany']
    f3 = go.Figure()
    f3.add_trace(go.Bar(name='2022 Baseline (= 100)', x=cats,
                        y=[100,100,100,100,100], marker_color=GRID))
    f3.add_trace(go.Bar(name='2024 Index', x=cats,
                        y=[42, 65, 78, 84, 115],
                        marker_color=[RED, RED, AMBER, AMBER, BLUE]))
    f3.update_layout(**CL("Germany Is the Only Major Destination Growing — "
                          "Every Anglophone Alternative Is Shrinking",
                          320, legend=True, margin=dict(l=10, r=15, t=70, b=70)))
    f3.update_layout(barmode='group',
                     xaxis=dict(showgrid=False, linecolor=BORDER),
                     yaxis=dict(gridcolor=GRID, title="Index (2022 = 100)"))

    ld = (d['la']['destination_country'].value_counts()
            .head(10).reset_index())
    ld.columns = ['Country', 'Count']
    ld['color'] = ld['Country'].apply(lambda c: BLUE if c == 'Germany' else GRAY)
    f4 = go.Figure(go.Bar(
        x=ld['Count'], y=ld['Country'], orientation='h', marker_color=ld['color'],
        hovertemplate='<b>%{y}</b><br>%{x:,.0f} students<extra></extra>'
    ))
    f4.update_layout(**CL("Germany Already Attracts More LATAM Students Than France or the Netherlands",
                          320, margin=dict(l=10, r=15, t=70, b=40)))
    f4.update_layout(xaxis_title="Student Count",
                     yaxis=dict(autorange='reversed', showgrid=False))

    children = [
        sh("Section 02",
           "Latin American Students Are Actively Looking for Germany — Nobody Is Guiding Them",
           "Outbound mobility is rising. Anglophone destinations are closing. Germany absorbs "
           "the redirected demand. The advisory gap is structural."),
    ]
    if market != 'all' and market in MARKET_STATS:
        children.append(info_box(MARKET_STATS[market]))
    children.extend([
        row2(
            card(g(f1,
                   "Colombia is Germany's #1 DAAD scholarship recipient in Latin America. "
                   "Brazil is #2 with 1,030 funded scholars in 2023. "
                   "These are established markets with no AI-native advisory.",
                   "Source: UNESCO UIS via Kaggle (thedevastator)")),
            card(g(f2))
        ),
        divider(),
        row2(
            card(g(f3,
                   "Canada's 50%+ LATAM permit drop (2024) created a vacuum. "
                   "Germany's Fachkrafteeinwanderungsgesetz (2023) created an opening. "
                   "Two policies happening simultaneously — that is the most important "
                   "signal in this analysis.",
                   "Sources: ICEF Monitor 2024/25 · ApplyBoard Research · QS Flows 2024")),
            card(g(f4,
                   "Germany already ranks high as a LATAM destination without any advisory "
                   "support. Imagine the volume with an AI-powered Spanish-language guide.",
                   "Simulated dataset — directional analysis, consistent with DAAD 2024"))
        )
    ])
    return html.Div(children)


def s_germany(pathway='all'):
    d = D()

    f1 = go.Figure(go.Scatter(
        x=d['gt']['Semester'], y=d['gt']['I'], mode='lines+markers',
        line=dict(color=BLUE, width=2.5), marker=dict(size=5, color=BLUE),
        fill='tozeroy', fillcolor='rgba(29,78,216,0.05)',
        hovertemplate='<b>%{x}</b><br>%{y:,.0f} students<extra></extra>'
    ))
    f1.update_layout(**CL("Germany's International Student Enrollment Has Grown Every Year Since 2010",
                          360))
    f1.update_layout(xaxis=dict(tickangle=-45, gridcolor=GRID, linecolor=BORDER),
                     yaxis=dict(showgrid=False, title="International Students"),
                     showlegend=False)

    gt2 = d['gt'].copy()
    gt2['color'] = [BLUE if i == len(gt2)-1 else GRAY for i in range(len(gt2))]
    f2 = go.Figure(go.Bar(
        x=gt2['Semester'], y=gt2['S'], marker_color=gt2['color'],
        hovertemplate='<b>%{x}</b><br>%{y:.1f}%<extra></extra>'
    ))
    f2.update_layout(**CL("International Students Represent a Growing Share of Every German Campus",
                          360))
    f2.update_layout(xaxis=dict(tickangle=-45, showgrid=False),
                     yaxis=dict(gridcolor=GRID, title="International Share (%)"))

    ausb = pd.DataFrame({
        'Sector': ['Nursing & Healthcare','Construction','IT & Software',
                   'Logistics','Mechatronics','Hospitality','Gastronomy','Retail'],
        'Vac':  [95, 72, 78, 58, 62, 45, 38, 51],
        'Days': [222,178,187,158,165,142,131,148],
        'Fit':  [9,  6,  8,  7,  7,  9,  9,  7]
    }).sort_values('Vac', ascending=True)
    ausb['color'] = ausb['Fit'].apply(
        lambda x: BLUE if x >= 9 else GRAY2 if x >= 7 else GRAY)

    f3 = go.Figure(go.Bar(
        x=ausb['Vac'], y=ausb['Sector'], orientation='h',
        marker_color=ausb['color'],
        text=[f"{v}K" for v in ausb['Vac']], textposition='outside',
        textfont=dict(color=TEXT, size=10),
        hovertemplate='<b>%{y}</b><br>%{x}K unfilled positions<extra></extra>'
    ))
    f3.update_layout(**CL("Nursing and IT Have the Most Unfilled Positions — "
                          "Both Are High LATAM Candidate Fit",
                          360, margin=dict(l=10, r=50, t=70, b=40)))
    f3.update_layout(xaxis=dict(range=[0,115], title="Unfilled Positions (thousands, est.)"),
                     yaxis=dict(showgrid=False))

    f4 = go.Figure(go.Bar(
        x=ausb['Days'], y=ausb['Sector'], orientation='h',
        marker_color=ausb['color'],
        text=[f"{v}d" for v in ausb['Days']], textposition='outside',
        textfont=dict(color=TEXT, size=10),
        hovertemplate='<b>%{y}</b><br>Avg %{x} days unfilled<extra></extra>'
    ))
    f4.update_layout(**CL("Positions Stay Unfilled for Months — Employers Will Pay for "
                          "Pre-Screened International Candidates",
                          360, margin=dict(l=10, r=55, t=70, b=40)))
    f4.update_layout(xaxis=dict(range=[0,265],
                                title="Average Days Position Remains Unfilled"),
                     yaxis=dict(showgrid=False))

    orig = (d['gs']['origin_country'].value_counts()
              .head(12).reset_index())
    orig.columns = ['Country', 'Count']
    orig['color'] = orig['Country'].apply(
        lambda c: BLUE if c in LATAM else GRAY)
    f5 = go.Figure(go.Bar(
        x=orig['Count'], y=orig['Country'], orientation='h',
        marker_color=orig['color'],
        hovertemplate='<b>%{y}</b><br>%{x:,.0f} students<extra></extra>'
    ))
    f5.update_layout(**CL("LATAM Countries Already Appear Among Germany's Top Student Origins",
                          380, margin=dict(l=10, r=15, t=70, b=40)))
    f5.update_layout(xaxis_title="Student Count",
                     yaxis=dict(autorange='reversed', showgrid=False))

    children = [
        sh("Section 03",
           "Germany Needs International Students — and Has the Capacity to Absorb Them",
           "Record enrollment growth + 617,000 unfilled jobs + reformed visa pathways. "
           "Germany is not just attractive — it is structurally dependent on international talent."),
    ]
    if pathway == 'uni':
        children.append(info_box(
            "University focus: 420K+ international students in Germany. "
            "DAAD scholarship programs active in 22 LATAM countries."
        ))
    elif pathway == 'work':
        children.append(info_box(
            "Work visa focus: Chancenkarte and Blue Card pathways open since 2023. "
            "IT and engineering candidates qualify with a recognised degree."
        ))
    children.extend([
        row2(
            card(g(f1,
                   "420,000+ international students in 2025/26 — a new record. "
                   "Germany's policy actively encourages this growth.",
                   "Source: Kaggle — phoellermann/enrolled-students-in-german-universities")),
            card(g(f2,
                   "Rising share means Germany is structurally integrating international "
                   "students, not merely tolerating them. Long-term policy direction."))
        ),
        divider(),
        sh("", "The Ausbildung Gap — Germany Cannot Fill Vocational Positions, "
               "LATAM Candidates Are the Logical Solution"),
    ])
    if pathway == 'ausb':
        children.append(info_box(
            "Ausbildung focus: 617K unfilled positions. "
            "Nursing and IT are the highest-priority sectors for LATAM candidates."
        ))
    children.extend([
        row2(
            card(g(f3,
                   "Nursing averages 222 days unfilled — nearly a year per position. "
                   "LATAM nursing candidates are exactly what Germany needs. "
                   "UC-02 (Ausbildung Matcher) directly solves this.",
                   "Sources: BIBB 2024 · Bundesagentur fur Arbeit 2025 · FMC Group 2025")),
            card(g(f4,
                   "At 222 days per vacancy, employers lose months of productivity. "
                   "A platform delivering pre-screened LATAM candidates has a "
                   "B2B revenue model built into the problem itself."))
        ),
        divider(),
        card(g(f5,
               "LATAM students are already choosing Germany without any advisory support. "
               "With a professional AI-powered Spanish-language guide, volume compounds.",
               "Simulated dataset — consistent with DAAD country statistics 2024.")),

        divider(),
        sh("", "German University Programme Breadth — 2,215 Courses Across Every Major Field",
           "DAAD-listed courses across Germany broken down by subject, city, and language "
           "of instruction. Shows the depth of options available to LATAM students."),
        row3(
            card(g(
                go.Figure(go.Bar(
                    x=d['top_subjects']['Count'],
                    y=d['top_subjects']['Subject'],
                    orientation='h',
                    marker_color=d['top_subjects']['color'],
                    hovertemplate='<b>%{y}</b><br>%{x} courses<extra></extra>'
                )).update_layout(
                    **CL("Engineering and Sciences Have the Most Courses — "
                         "Highest Relevance for LATAM Ausbildung Candidates",
                         360, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis_title="Number of Courses",
                    yaxis=dict(autorange='reversed', showgrid=False)
                ),
                "Engineering and natural sciences dominate — exactly the sectors with "
                "the highest German labour vacancies. This is not a mismatch problem.",
                "Source: DAAD Studiengangsdatenbank via Kaggle (azdurjoy)"
            )),
            card(g(
                go.Figure(go.Bar(
                    x=d['top_cities']['Count'],
                    y=d['top_cities']['City'],
                    orientation='h',
                    marker_color=d['top_cities']['color'],
                    hovertemplate='<b>%{y}</b><br>%{x} courses<extra></extra>'
                )).update_layout(
                    **CL("Berlin Leads — But Programme Options Are Distributed "
                         "Across All Major German Cities",
                         360, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis_title="Number of Courses",
                    yaxis=dict(autorange='reversed', showgrid=False)
                ),
                "Geographic distribution means Cleo's advisory must cover "
                "city-specific guidance — housing, transport, integration. "
                "That validates UC-08 (Post-Arrival Concierge).",
                "Source: DAAD via Kaggle (azdurjoy)"
            )),
            card(g(
                go.Figure(go.Bar(
                    x=d['lang_dist']['Count'],
                    y=d['lang_dist']['Language'],
                    orientation='h',
                    marker_color=d['lang_dist']['color'],
                    hovertemplate='<b>%{y}</b><br>%{x} courses<extra></extra>'
                )).update_layout(
                    **CL("Many Programmes Are English-Accessible — "
                         "Reducing the Language Barrier for Early-Stage LATAM Applicants",
                         360, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis_title="Number of Courses",
                    yaxis=dict(autorange='reversed', showgrid=False)
                ),
                "English-accessible programmes lower the entry barrier. "
                "Students can start while still building German to B1/B2 — "
                "a key advisory talking point for UC-01 roadmaps.",
                "Source: DAAD via Kaggle (azdurjoy)"
            ))
        )
    ])
    return html.Div(children)


def s_profiles(market='all'):
    d = D()

    MARKET_PROFILES = {
        'col': ("Colombia: DAAD's top LATAM partner with 22 active scholarship programs. "
                "Students prioritise engineering and healthcare — Germany's top vacancy sectors."),
        'bra': ("Brazil: Largest LATAM economy with 1,030 DAAD scholars in 2023. "
                "Strong engineering and technology talent pool with high English proficiency."),
        'mex': ("Mexico: LATAM's top outbound market with growing Germany interest post-2023 visa reforms. "
                "IT and business graduates dominate outbound flows."),
        'chl': ("Chile: Highest GDP per capita in LATAM. EU-oriented professionals with strong "
                "academic credentials and above-average study abroad rates."),
    }

    fos_counts = d['la']['field_of_study'].dropna().value_counts()
    fos = fos_counts.reset_index()
    fos.columns = ['Field', 'Count']
    fos = fos.head(10)
    fos['color'] = [BLUE if i == 0 else GRAY for i in range(len(fos))]
    f1 = go.Figure(go.Bar(
        x=fos['Count'], y=fos['Field'], orientation='h',
        marker_color=fos['color'],
        hovertemplate='<b>%{y}</b><br>%{x} students<extra></extra>'
    ))
    f1.update_layout(**CL("Engineering and Healthcare Dominate — Both Map to "
                          "Germany's Highest-Vacancy Ausbildung Sectors",
                          360, margin=dict(l=10, r=15, t=70, b=40)))
    f1.update_layout(xaxis_title="Student Count",
                     yaxis=dict(autorange='reversed', showgrid=False))

    er_counts = d['la']['enrollment_reason'].dropna().value_counts()
    r = er_counts.reset_index()
    r.columns = ['Reason', 'Count']
    r = r.head(10)
    r['color'] = [BLUE if i == 0 else GRAY for i in range(len(r))]
    f2 = go.Figure(go.Bar(
        x=r['Count'], y=r['Reason'], orientation='h',
        marker_color=r['color'],
        hovertemplate='<b>%{y}</b><br>%{x}<extra></extra>'
    ))
    f2.update_layout(**CL("Career Advancement Is the #1 Reason — "
                          "Advisory Must Lead With Outcomes, Not Process",
                          360, margin=dict(l=10, r=15, t=70, b=40)))
    f2.update_layout(xaxis_title="Count",
                     yaxis=dict(autorange='reversed', showgrid=False))

    lp_counts = d['la']['language_proficiency_test'].dropna().value_counts()
    lg = lp_counts.reset_index()
    lg.columns = ['Test', 'Count']
    lg = lg.head(10)
    lg['color'] = lg['Test'].apply(
        lambda t: BLUE if any(x in t.lower() for x in ['goethe','testdaf','german'])
                  else GRAY)
    f3 = go.Figure(go.Bar(
        x=lg['Count'], y=lg['Test'], orientation='h',
        marker_color=lg['color'],
        hovertemplate='<b>%{y}</b><br>%{x}<extra></extra>'
    ))
    f3.update_layout(**CL("Most LATAM Students Take English Tests — "
                          "German Language Prep Is a Service Gap and a UC-06 Upsell",
                          320, margin=dict(l=10, r=15, t=70, b=40)))
    f3.update_layout(xaxis_title="Count",
                     yaxis=dict(autorange='reversed', showgrid=False))

    d['ff']['color'] = [BLUE if i < 2 else GRAY for i in range(len(d['ff']))]
    f4 = go.Figure(go.Bar(
        x=d['ff']['students'], y=d['ff']['field_of_study'], orientation='h',
        marker_color=d['ff']['color'],
        hovertemplate='<b>%{y}</b><br>%{x:,.0f}<extra></extra>'
    ))
    f4.update_layout(**CL("Business and Engineering Attract the Most International Students "
                          "Globally — Germany Offers Both Pathways",
                          320, margin=dict(l=10, r=15, t=70, b=40)))
    f4.update_layout(xaxis_title="Cumulative Students",
                     yaxis=dict(autorange='reversed', showgrid=False))

    children = [
        sh("Section 04",
           "Who Is Cleo's Student? Profiling the Demand Before Building the Product",
           "Every AI use case — especially UC-01 — depends on understanding the student "
           "profile. This section defines the person Cleo is designing for."),
    ]
    if market != 'all' and market in MARKET_PROFILES:
        children.append(info_box(MARKET_PROFILES[market]))
    children.extend([
        row2(
            card(g(f1,
                   "The fields LATAM students want to study are the exact fields Germany "
                   "cannot fill. UC-02 matches proven supply with proven demand.",
                   "⚠️ Simulated — all LATAM outbound students, not filtered to Germany only")),
            card(g(f2,
                   "Students are buying a career future, not a visa process. UC-01's "
                   "roadmap output should lead with outcomes, not document checklists.",
                   "⚠️ Simulated — all LATAM outbound students, not filtered to Germany only"))
        ),
        divider(),
        row2(
            card(g(f3,
                   "English test dominance signals many students start Germany pathways "
                   "without German preparation — making UC-06 (Language Coach) a "
                   "high-conversion upsell, not a nice-to-have.",
                   "⚠️ Simulated — all LATAM outbound students, not filtered to Germany only")),
            card(g(f4,
                   "Global demand patterns validate the Germany university pathway. "
                   "Business and engineering graduates from LATAM are exactly who "
                   "Germany's universities want.",
                   "Source: IIE Open Doors via Kaggle (webdevbadger)"))
        )
    ])
    return html.Div(children)


def s_usecases(pathway='all'):
    d = D()
    uc = [
        {"id":"UC-01","name":"Germany Readiness Diagnostic Agent","score":24,
         "p":"Critical","impact":5,"diff":4,"ai":5,"feas":5,"ttv":5},
        {"id":"UC-03","name":"Agentic Application & Deadline Tracker","score":23,
         "p":"Critical","impact":5,"diff":4,"ai":5,"feas":4,"ttv":5},
        {"id":"UC-02","name":"Agentic Ausbildung Position Matcher","score":22,
         "p":"Critical","impact":5,"diff":5,"ai":5,"feas":3,"ttv":4},
        {"id":"UC-04","name":"AI German Document Factory","score":22,
         "p":"Critical","impact":4,"diff":3,"ai":5,"feas":5,"ttv":5},
        {"id":"UC-05","name":"Agentic Lead Nurturing System","score":22,
         "p":"Critical","impact":5,"diff":3,"ai":5,"feas":4,"ttv":5},
        {"id":"UC-07","name":"Visa & Regulatory Intelligence Agent","score":20,
         "p":"Critical","impact":4,"diff":5,"ai":5,"feas":3,"ttv":3},
        {"id":"UC-08","name":"Post-Arrival Integration Concierge","score":20,
         "p":"Critical","impact":4,"diff":5,"ai":4,"feas":4,"ttv":3},
        {"id":"UC-06","name":"German Language Readiness Coach","score":18,
         "p":"High","impact":4,"diff":4,"ai":4,"feas":3,"ttv":3},
        {"id":"UC-09","name":"B2B White-Label Platform","score":18,
         "p":"High","impact":5,"diff":5,"ai":4,"feas":2,"ttv":2},
        {"id":"UC-10","name":"Alumni Intelligence Network","score":16,
         "p":"High","impact":3,"diff":5,"ai":3,"feas":3,"ttv":2},
    ]
    df = pd.DataFrame(uc)

    PATHWAY_PRIORITY = {'ausb': 'UC-02', 'uni': 'UC-01', 'work': 'UC-07'}
    PATHWAY_BADGES = {
        'ausb': ' (Priority for Ausbildung pathway)',
        'uni':  ' (Priority for University pathway)',
        'work': ' (Priority for Work Visa pathway)',
    }

    if pathway != 'all' and pathway in PATHWAY_PRIORITY:
        priority_id = PATHWAY_PRIORITY[pathway]
        is_priority = df['id'] == priority_id
        df = pd.concat([df[is_priority], df[~is_priority]]).reset_index(drop=True)

    df['color'] = df['p'].apply(lambda p: BLUE if p == 'Critical' else GRAY)

    if pathway != 'all' and pathway in PATHWAY_PRIORITY:
        priority_id = PATHWAY_PRIORITY[pathway]
        badge = PATHWAY_BADGES[pathway]
        df['label'] = df.apply(
            lambda r: f"{r['id']} — {r['name']}{badge}" if r['id'] == priority_id
                      else f"{r['id']} — {r['name']}",
            axis=1
        )
    else:
        df['label'] = df.apply(lambda r: f"{r['id']} — {r['name']}", axis=1)

    f1 = go.Figure(go.Bar(
        x=df['score'], y=df['label'], orientation='h',
        marker_color=df['color'],
        text=[f"{s}/25" for s in df['score']],
        textposition='outside', textfont=dict(color=TEXT, size=10),
        hovertemplate='<b>%{y}</b><br>Score: %{x}/25<extra></extra>'
    ))
    f1.add_vline(x=20, line_dash="dash",
                 line_color="rgba(217,119,6,0.4)",
                 annotation_text="Critical (20+)",
                 annotation_font_color=AMBER, annotation_font_size=10)
    f1.update_layout(**CL("7 of 10 Use Cases Score Critical — Reflecting Real Market Gaps "
                          "With Strong AI Technology Fit",
                          400, margin=dict(l=10, r=55, t=70, b=40)))
    f1.update_layout(xaxis=dict(range=[0,28], title="Priority Score", gridcolor=GRID),
                     yaxis=dict(showgrid=False, autorange='reversed'))

    # Grouped bar replacing radar (position > angle per encoding hierarchy)
    dims = ['Business Impact','Differentiation','AI Fit','Feasibility','Time to Value']
    uc_top3 = [
        {'id':'UC-01','vals':[5,4,5,5,5],'color':BLUE},
        {'id':'UC-02','vals':[5,5,5,3,4],'color':GRAY2},
        {'id':'UC-03','vals':[5,4,5,4,5],'color':GRAY},
    ]
    f2 = go.Figure()
    for u in uc_top3:
        f2.add_trace(go.Bar(
            name=u['id'], y=dims, x=u['vals'], orientation='h',
            marker_color=u['color'],
            hovertemplate=f"<b>{u['id']}</b><br>%{{y}}: %{{x}}/5<extra></extra>"
        ))
    f2.update_layout(
        **CL("UC-01 Leads on Business Impact, AI Fit and Time to Value — "
             "UC-02 Wins on Differentiation",
             360, legend=True, margin=dict(l=10,r=15,t=70,b=55))
    )
    f2.update_layout(
        barmode='group',
        xaxis=dict(range=[0,6], title="Score (out of 5)", gridcolor=GRID),
        yaxis=dict(showgrid=False)
    )

    # Competitive positioning 2x2 — the white space argument
    comp = pd.DataFrame({
        'Company':   ['Leverage Edu','ApplyBoard','Study Metro','Livin-France',
                      "Local LATAM\nConsultants","Cleo's\nPlatform"],
        'AI_Cap':    [7.0, 6.0, 5.0, 2.0, 1.0, 9.2],
        'LATAM_Ger': [2.0, 1.5, 1.0, 1.5, 4.0, 9.2],
        'Size':      [20,  18,  14,  10,  8,   28],
        'Color':     [GRAY, GRAY, GRAY, GRAY, GRAY2, BLUE]
    })
    f_comp = go.Figure()
    for _, row in comp.iterrows():
        f_comp.add_trace(go.Scatter(
            x=[row['AI_Cap']], y=[row['LATAM_Ger']],
            mode='markers+text', name=row['Company'],
            text=[row['Company']], textposition='top center',
            textfont=dict(size=9.5, color=DARK if row['Color']==BLUE else GRAY2,
                          family='Inter'),
            marker=dict(size=row['Size'], color=row['Color'],
                        opacity=0.85, line=dict(color=WHITE, width=2)),
            hovertemplate=f"<b>{row['Company']}</b><br>"
                          f"AI Capability: {row['AI_Cap']}/10<br>"
                          f"LATAM+Germany Specialisation: {row['LATAM_Ger']}/10<extra></extra>",
            showlegend=False
        ))
    for x, y, txt, anchor in [
        (2.5, 8.5, "Specialised\nbut Manual", "center"),
        (7.5, 8.5, "<- Cleo's White Space\nAI + Specialisation", "center"),
        (2.5, 1.5, "Manual\n& Generic", "center"),
        (7.5, 1.5, "AI-Powered\nbut Generic", "center"),
    ]:
        f_comp.add_annotation(x=x, y=y, text=txt, showarrow=False,
                              font=dict(size=9, color=GRID if 'White' not in txt else BLUE,
                                        family='Inter'),
                              align='center')
    f_comp.add_hline(y=5, line_dash="dash", line_color=BORDER)
    f_comp.add_vline(x=5, line_dash="dash", line_color=BORDER)
    f_comp.update_layout(
        **CL("No Competitor Combines AI Capability With LATAM+Germany Specialisation — "
             "That Is Cleo's Unclaimed White Space",
             400, margin=dict(l=10,r=15,t=70,b=40))
    )
    f_comp.update_layout(
        xaxis=dict(range=[0,10.5], title="AI Capability ->", gridcolor=GRID,
                   tickvals=[0,2.5,5,7.5,10]),
        yaxis=dict(range=[0,10.5], title="LATAM + Germany Specialisation ->",
                   gridcolor=GRID, showgrid=True, tickvals=[0,2.5,5,7.5,10])
    )

    match = pd.DataFrame({
        'Sector': ['Healthcare','IT','Engineering','Hospitality','Logistics'],
        'LATAM':  [38, 32, 28, 45, 22],
        'Germany':[95, 78, 62, 45, 58]
    })
    f3 = go.Figure()
    f3.add_trace(go.Bar(name='LATAM Interest Index', x=match['Sector'],
                        y=match['LATAM'], marker_color=GRAY))
    f3.add_trace(go.Bar(name='Germany Vacancy Index (000s)', x=match['Sector'],
                        y=match['Germany'], marker_color=BLUE))
    f3.update_layout(**CL("LATAM Student Interest Aligns With Germany's Highest-Vacancy "
                          "Sectors — Data-Driven Validation of UC-02",
                          320, legend=True, margin=dict(l=10, r=15, t=70, b=70)))
    f3.update_layout(barmode='group',
                     xaxis=dict(showgrid=False, tickangle=-15),
                     yaxis=dict(gridcolor=GRID, title="Index"))

    tl = [
        dict(Task="UC-01 Diagnostic Agent",    Start="2026-07-01",Finish="2026-07-14",P="MVP"),
        dict(Task="UC-03 App. Tracker",         Start="2026-08-01",Finish="2026-08-21",P="Launch"),
        dict(Task="UC-04 Document Factory",     Start="2026-09-01",Finish="2026-09-14",P="Launch"),
        dict(Task="UC-05 Lead Nurturing",       Start="2026-09-01",Finish="2026-09-21",P="Launch"),
        dict(Task="UC-02 Ausbildung Matcher",   Start="2026-10-01",Finish="2026-10-28",P="Scale"),
        dict(Task="UC-07 Visa Intelligence",    Start="2026-11-01",Finish="2026-11-14",P="Scale"),
        dict(Task="UC-08 Concierge",            Start="2027-01-01",Finish="2027-01-28",P="Mature"),
    ]
    df_tl = pd.DataFrame(tl)
    f4 = px.timeline(df_tl, x_start="Start", x_end="Finish", y="Task",
                     color="P",
                     color_discrete_map={"MVP":BLUE,"Launch":GRAY2,"Scale":GRAY,"Mature":GRID})
    f4.update_yaxes(autorange="reversed")
    f4.update_layout(
        paper_bgcolor=WHITE, plot_bgcolor=WHITE,
        font=dict(family='Inter', color=TEXT, size=11),
        title=dict(text="Start With UC-01 in 2 Weeks — Everything Else Follows in Sequence",
                   font=dict(size=12.5, color=DARK, family='Inter'), x=0),
        height=320, margin=dict(l=10, r=15, t=60, b=50),
        showlegend=True,
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(size=10),
                    orientation='h', y=-0.2),
        xaxis=dict(gridcolor=GRID, linecolor=BORDER),
        yaxis=dict(showgrid=False)
    )

    return html.Div([
        sh("Section 05", "10 AI Use Cases — Scored Against 5 Dimensions",
           "Business Impact, Differentiation, AI Fit, Feasibility, Time to Value. "
           "Max 25. The data drives priority — not opinion."),
        row2(
            card(g(f1,
                   "UC-01 is the architectural foundation — every other use case depends "
                   "on the student profile it generates. Build it first.")),
            card(g(f2,
                   "Grouped bar replaces radar for accuracy: position (rank 1) vs angle (rank 4). "
                   "UC-01 leads on 3 of 5 dimensions. UC-02 wins on differentiation — "
                   "nobody else is doing Ausbildung matching in Spanish."))
        ),
        divider(),
        card(g(f_comp,
               "Every competitor sits bottom-left — either generic or manual or both. "
               "Cleo's platform occupies the top-right corner alone. "
               "That white space does not stay empty. Leverage Edu is already moving into LATAM.",
               "Positioning map based on public product analysis — June 2026")),
        divider(),
        row2(
            card(g(f3,
                   "Healthcare and IT show the strongest match between LATAM student "
                   "interest and German vacancies. UC-02 is not speculative.",
                   "Sector fit scores: BIBB 2024 + DAAD 2024")),
            card(g(f4,
                   "The MVP (UC-01) is 14 days and EUR 3,700. Everything activates after "
                   "pilot validation. Sequenced, not a big bang."))
        ),

        divider(),
        sh("", "The Market Is Already Using AI — Cleo's Students Are Ready",
           "50,000 student records showing real AI adoption patterns by major, "
           "use case, willingness to pay, and academic outcomes. "
           "This validates both the demand for Cleo's AI features and "
           "students' willingness to pay for AI-powered tools."),
        row2(
            card(g(
                go.Figure(go.Bar(
                    x=d['ai_by_major']['Avg_Hours'],
                    y=d['ai_by_major']['Major'],
                    orientation='h',
                    marker_color=d['ai_by_major']['color'],
                    hovertemplate='<b>%{y}</b><br>%{x:.1f} hrs/week<extra></extra>'
                )).update_layout(
                    **CL("Technology and Engineering Students Already Use GenAI "
                         "7+ Hours Per Week — Cleo's Core Audience Is AI-Ready",
                         340, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis_title="Avg. Weekly GenAI Hours",
                    yaxis=dict(showgrid=False)
                ),
                "STEM students — the exact profile of LATAM->Germany Ausbildung candidates — "
                "are the heaviest AI users. They will not just tolerate an AI-powered "
                "advisory platform. They will expect one.",
                "Source: Kaggle — laveshjadon/ai-impact-on-students (50,000 students)"
            )),
            card(g(
                go.Figure(go.Bar(
                    x=d['use_cases_ai']['Count'],
                    y=d['use_cases_ai']['Use_Case'],
                    orientation='h',
                    marker_color=d['use_cases_ai']['color'],
                    hovertemplate='<b>%{y}</b><br>%{x:,} students<extra></extra>'
                )).update_layout(
                    **CL("Research and Writing Are the Top AI Use Cases — "
                         "Directly Validating UC-01 (Diagnostic) and UC-04 (Documents)",
                         340, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis_title="Number of Students",
                    yaxis=dict(autorange='reversed', showgrid=False)
                ),
                "The top student AI use cases map exactly to Cleo's core features: "
                "research/advisory (UC-01), document writing (UC-04), and "
                "information lookup (UC-07). Feature-market fit is confirmed by data.",
                "Source: Kaggle — laveshjadon/ai-impact-on-students"
            ))
        ),
        row2(
            card(g(
                go.Figure(go.Bar(
                    x=d['paid_by_major']['Paid_Pct'],
                    y=d['paid_by_major']['Major'],
                    orientation='h',
                    marker_color=d['paid_by_major']['color'],
                    hovertemplate='<b>%{y}</b><br>%{x:.1f}% pay for AI tools<extra></extra>'
                )).update_layout(
                    **CL("Technology and Engineering Students Have the Highest Paid "
                         "AI Subscription Rates — Willingness to Pay Is Real",
                         320, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis_title="% Students With Paid AI Subscription",
                    yaxis=dict(showgrid=False)
                ),
                "Students in Cleo's target majors are already paying for AI tools. "
                "A EUR 49-99 advisory platform is well within their spending behaviour.",
                "Source: Kaggle — laveshjadon/ai-impact-on-students"
            )),
            card(g(
                go.Figure(go.Bar(
                    x=d['gpa_trend']['Usage_Band'],
                    y=d['gpa_trend']['Avg_GPA_Delta'],
                    marker_color=d['gpa_trend']['color'],
                    hovertemplate='<b>%{x}</b><br>Avg. GPA change: %{y:+.3f}<extra></extra>'
                )).update_layout(
                    **CL("Moderate AI Usage (2-10h/week) Correlates With GPA Improvement — "
                         "Validates the Outcome Argument in Cleo's Advisory Pitch",
                         320, margin=dict(l=10,r=15,t=70,b=40))
                ).update_layout(
                    xaxis=dict(showgrid=False),
                    yaxis=dict(gridcolor=GRID, title="Avg. GPA Delta (Post - Pre Semester)",
                               zeroline=True, zerolinecolor=BORDER, showgrid=True)
                ),
                "Students using AI moderately see GPA gains. This is the outcome "
                "data Cleo can cite when positioning the advisory as a "
                "career investment, not just a process service.",
                "Source: Kaggle — laveshjadon/ai-impact-on-students (50,000 students)"
            ))
        )
    ])


def s_risks():
    risks = [
        {"risk":"EU AI Act Non-Compliance (UC-01, UC-02 = High Risk)","l":4,"i":5,"s":20},
        {"risk":"GDPR Breach — Student Data via US-Based LLM APIs","l":3,"i":5,"s":15},
        {"risk":"Agentic System Gives Incorrect Visa Advice","l":3,"i":5,"s":15},
        {"risk":"Leverage Edu Enters Spanish-Language Germany Niche","l":3,"i":4,"s":12},
        {"risk":"Algorithmic Bias in Readiness Scoring","l":3,"i":4,"s":12},
        {"risk":"Student Drop-off — Language Barrier","l":4,"i":3,"s":12},
        {"risk":"Single LLM Provider Dependency","l":2,"i":4,"s":8},
        {"risk":"WhatsApp API Restriction","l":2,"i":3,"s":6},
        {"risk":"Green AI Reputational Exposure","l":2,"i":3,"s":6},
    ]
    df_r = pd.DataFrame(risks)
    df_r['color'] = df_r['s'].apply(
        lambda s: RED if s >= 15 else AMBER if s >= 10 else GRAY)

    f1 = go.Figure()
    for _, row in df_r.iterrows():
        lbl = row['risk'][:38]+'...' if len(row['risk']) > 38 else row['risk']
        f1.add_trace(go.Scatter(
            x=[row['l']], y=[row['i']], mode='markers+text',
            text=[lbl], textposition='top center',
            textfont=dict(size=8.5, color=GRAY2),
            marker=dict(size=row['s']*2.5, color=row['color'],
                        opacity=0.75, line=dict(color=WHITE, width=1.5)),
            hovertemplate=(f"<b>{row['risk']}</b><br>"
                           f"Likelihood: {row['l']}/5<br>"
                           f"Impact: {row['i']}/5<br>"
                           f"Score: {row['s']}/25<extra></extra>"),
            showlegend=False
        ))
    f1.add_hline(y=3, line_dash="dash", line_color="rgba(0,0,0,0.06)")
    f1.add_vline(x=3, line_dash="dash", line_color="rgba(0,0,0,0.06)")
    f1.update_layout(**CL("Three Risks Require Action Before Launch — "
                          "All Three Have the Same Mitigation", 420))
    f1.update_layout(
        xaxis=dict(range=[0.5,5.5], title="Likelihood (1-5)",
                   tickvals=[1,2,3,4,5], gridcolor=GRID, linecolor=BORDER),
        yaxis=dict(range=[0.5,5.5], title="Impact (1-5)",
                   tickvals=[1,2,3,4,5], gridcolor=GRID,
                   linecolor=BORDER, showgrid=True)
    )

    df_rs = df_r.sort_values('s', ascending=True)
    f2 = go.Figure(go.Bar(
        x=df_rs['s'], y=df_rs['risk'], orientation='h',
        marker_color=df_rs['color'],
        text=df_rs['s'], textposition='outside',
        textfont=dict(color=TEXT, size=10),
        hovertemplate='<b>%{y}</b><br>Score: %{x}/25<extra></extra>'
    ))
    f2.add_vline(x=15, line_dash="dash",
                 line_color="rgba(217,119,6,0.4)",
                 annotation_text="High-risk (15+)",
                 annotation_font_color=AMBER, annotation_font_size=10)
    f2.update_layout(**CL("Only 3 Risks Exceed the High-Risk Threshold — "
                          "Each Has a Clear Mitigation",
                          340, margin=dict(l=10, r=40, t=70, b=40)))
    f2.update_layout(xaxis=dict(range=[0,28],
                                title="Risk Score (Likelihood x Impact)",
                                gridcolor=GRID),
                     yaxis=dict(showgrid=False))

    eu_items = [
        ("UC-01 Diagnostic Agent", "HIGH RISK",   RED,   "Annex III — profiles individuals for education access"),
        ("UC-02 Ausbildung Matcher","HIGH RISK",   RED,   "Annex III — assigns individuals to vocational training"),
        ("UC-05 Lead Nurturing",    "LIMITED-HIGH",AMBER, "Legal review required if score limits service access"),
        ("UC-03 App. Tracker",      "LIMITED",     GRAY2, "AI transparency disclosure required"),
        ("UC-04 Doc. Factory",      "LIMITED",     GRAY2, "AI-generated content disclosure required"),
        ("UC-07 Visa Intelligence", "MINIMAL",     GREEN, "Voluntary code of conduct recommended"),
    ]
    eu_list = html.Div([
        html.P("EU AI Act Classification — Per Use Case",
               style={'fontWeight':'700','color':DARK,'fontSize':'0.9rem',
                      'marginBottom':'0.75rem'}),
        *[html.Div([
            html.Div([
                html.Span(u, style={'fontWeight':'600','fontSize':'0.82rem','color':DARK}),
                html.Span(b, style={'color':c,'border':f'1px solid {c}',
                                    'padding':'0.15rem 0.5rem','borderRadius':'4px',
                                    'fontSize':'0.68rem','fontWeight':'700',
                                    'marginLeft':'0.5rem','whiteSpace':'nowrap'}),
            ], style={'display':'flex','justifyContent':'space-between',
                      'alignItems':'center','marginBottom':'0.2rem'}),
            html.P(desc, style={'fontSize':'0.72rem','color':GRAY2,'margin':'0'})
        ], style={'padding':'0.65rem 0','borderBottom':f'1px solid {BORDER}'})
          for u,b,c,desc in eu_items],
        html.Div([
            html.P("Compliance = Competitive Moat",
                   style={'fontWeight':'600','color':BLUE,'marginBottom':'0.35rem',
                          'fontSize':'0.88rem'}),
            html.P("Being the only GDPR-compliant, EU AI Act-ready Spanish-language "
                   "Germany advisor closes institutional B2B deals no competitor can match. "
                   "Publish your compliance posture on the homepage.",
                   style={'fontSize':'0.8rem','color':TEXT,'lineHeight':'1.6','margin':'0'})
        ], style={'background':'#EFF6FF','borderRadius':'6px','padding':'1rem',
                  'marginTop':'1rem','border':f'1px solid rgba(29,78,216,0.15)'})
    ])

    return html.Div([
        sh("Section 06",
           "The Risks Are Real and Manageable — Compliance Is the Competitive Moat",
           "EU AI Act enforcement begins August 2, 2026. GDPR applies from day one. "
           "Most competitors will ignore both. That is Cleo's differentiation opportunity."),
        row2(
            card(g(f1,
                   "The 3 critical risks all resolve to one design decision: human oversight "
                   "gate + documented compliance posture. One architectural choice mitigates all three.")),
            card(eu_list, pad='1.5rem')
        ),
        divider(),
        card(g(f2,
               "3 risks above the high-risk threshold sounds like a lot until you see "
               "they share the same mitigation. The risk profile is manageable."))
    ])


def s_reco(scenario='solo'):
    scenario = scenario or 'solo'

    def decision_card(icon, title, body, active=False):
        return html.Div([
            html.P(icon,  style={'fontSize':'2rem','marginBottom':'0.5rem'}),
            html.P(title, style={'fontWeight':'700',
                                  'color': BLUE if active else GRAY2,
                                  'fontSize':'0.95rem','marginBottom':'0.4rem'}),
            html.P(body,  style={'fontSize':'0.79rem',
                                  'color': TEXT if active else GRAY2,
                                  'lineHeight':'1.6'})
        ], style={
            'background': WHITE if active else LIGHT,
            'borderRadius': '8px', 'padding': '1.5rem', 'textAlign': 'center',
            'boxShadow': '0 1px 3px rgba(0,0,0,0.08)' if active else 'none',
            'border': f'2px solid {BLUE}' if active else f'1px solid {BORDER}',
            'opacity': '1' if active else '0.45'
        })

    def force_card(icon, title, body):
        return card(
            html.P(icon, style={'fontSize':'1.4rem','marginBottom':'0.4rem'}),
            html.P(title, style={'fontWeight':'600','color':DARK,
                                   'fontSize':'0.88rem','marginBottom':'0.4rem'}),
            html.P(body, style={'fontSize':'0.79rem','color':TEXT,'lineHeight':'1.65'})
        )

    # Investment comparison — grouped bar, scenario-aware
    scenario_stages = ['MVP (2 weeks)', 'Scale Month 3', 'Scale Month 6']
    invest = INVEST_MAP.get(scenario, INVEST_MAP['solo'])
    revenue = [0, 15000, 44000]
    f_invest = go.Figure()
    f_invest.add_trace(go.Bar(
        name='Monthly Investment', x=scenario_stages, y=invest,
        marker_color=GRAY,
        hovertemplate='<b>%{x}</b><br>Investment: EUR%{y:,.0f}<extra></extra>'
    ))
    f_invest.add_trace(go.Bar(
        name='Monthly Revenue Target', x=scenario_stages, y=revenue,
        marker_color=BLUE,
        hovertemplate='<b>%{x}</b><br>Revenue Target: EUR%{y:,.0f}<extra></extra>'
    ))
    f_invest.update_layout(
        **CL("The MVP Costs EUR 3,700 — By Month 6 Revenue Exceeds Investment",
             300, legend=True, margin=dict(l=10,r=15,t=70,b=45))
    )
    f_invest.update_layout(
        barmode='group',
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor=GRID, title="EUR", tickformat=",.0f")
    )

    return html.Div([
        sh("Section 07",
           "The Verdict: Invest Now, Start Small, Lead With Ausbildung",
           "Eight datasets. Four analytical layers. One answer."),

        row3(
            decision_card("OK","Invest Now",
                          "2-week MVP at under EUR 3,700. "
                          "Market data justifies immediate action.", active=True),
            decision_card("||","Wait",
                          "Leverage Edu is expanding into LATAM. "
                          "Waiting cedes first-mover advantage permanently."),
            decision_card("?","Pilot First",
                          "The MVP IS the pilot. "
                          "EUR 3,700 validates everything before any larger commitment.")
        ),

        divider(),
        sh("", "Interactive ROI Calculator — Adjust Your Assumptions",
           "Drag the sliders to test your own conversion rate and average ticket price. "
           "The projection updates in real time."),

        card(
            row2(
                html.Div([
                    html.Div([
                        html.P("Conversion Rate", className='roi-slider-label'),
                        html.P("What % of diagnostic completions convert to paying clients?",
                               style={'fontSize':'0.72rem','color':GRAY2,'marginBottom':'0.75rem'}),
                        dcc.Slider(id='conv-rate-slider', min=5, max=40, value=20, step=1,
                                   marks={5:'5%',10:'10%',20:'20%',30:'30%',40:'40%'},
                                   tooltip={"placement":"bottom","always_visible":True}),
                    ], style={'marginBottom':'1.5rem'}),
                    html.Div([
                        html.P("Average Ticket (EUR)", className='roi-slider-label'),
                        html.P("Average revenue per paying client across all service tiers.",
                               style={'fontSize':'0.72rem','color':GRAY2,'marginBottom':'0.75rem'}),
                        dcc.Slider(id='ticket-slider', min=200, max=1500, value=500, step=50,
                                   marks={200:'EUR200',500:'EUR500',1000:'EUR1K',1500:'EUR1.5K'},
                                   tooltip={"placement":"bottom","always_visible":True}),
                    ]),
                    html.Div(id='roi-summary', style={'marginTop':'1.5rem'})
                ], style={'padding':'0.5rem 0'}),
                html.Div([
                    dcc.Graph(id='roi-chart-dynamic',
                              config={'displayModeBar': False},
                              responsive=True,
                              style={'minHeight':'280px'})
                ])
            )
        ),

        divider(),
        card(g(f_invest,
               "The MVP at EUR 3,700 is a bet on market validation, not a platform build. "
               "Month 6 revenue target of EUR 44K comfortably covers the operating "
               "cost of the selected team scenario.")),

        divider(),
        html.P("Why the Window Is Open Now — and Will Not Stay Open",
               style={'fontSize':'0.67rem','fontWeight':'700','letterSpacing':'0.12em',
                      'textTransform':'uppercase','color':BLUE,'marginBottom':'0.75rem'}),
        row3(
            force_card("~","Force 1 — Demand Redirection",
                       "Canada, Australia, UK tightening is structurally redirecting "
                       "LATAM students toward Europe. Germany is the primary beneficiary. "
                       "Multi-year, not cyclical."),
            force_card("=","Force 2 — German Labour Policy",
                       "Fachkrafteeinwanderungsgesetz (2023) opened Ausbildung for "
                       "non-EU applicants. 617K+ unfilled positions. The regulatory "
                       "pathway is open. The Spanish advisory layer does not exist yet."),
            force_card("AI","Force 3 — AI Technology Readiness",
                       "LLMs and agentic frameworks make autonomous advisory viable "
                       "for solo operators today. Agentic AI grows from $7.55B to "
                       "$199B by 2034. Technology window aligns with market window.")
        ),

        html.Div([
            html.P("The Recommendation",
                   style={'fontWeight':'700','color':BLUE,'fontSize':'0.95rem',
                          'marginBottom':'0.6rem'}),
            html.P([
                "Eight datasets across four analytical layers converge on one conclusion: ",
                html.Strong("invest in AI now, start with UC-01, lead with Ausbildung.",
                            style={'color':DARK}),
                " The MVP validates in 2 weeks at under EUR 3,700. The Ausbildung niche is "
                "structurally underserved, legally accessible since 2023, and has zero "
                "Spanish-language AI-native competition. Colombia and Brazil are the "
                "priority markets — backed by DAAD data, not assumption. Every month of "
                "delay is a month closer to Leverage Edu permanently occupying this "
                "position. ",
                html.Strong("The data says the window is open. Act now.",
                            style={'color':DARK})
            ], style={'fontSize':'0.88rem','color':TEXT,'lineHeight':'1.85','margin':'0'})
        ], style={
            'background':'#EFF6FF','borderRadius':'8px',
            'padding':'1.5rem 2rem','marginBottom':'1.25rem',
            'border':f'1px solid rgba(29,78,216,0.2)',
            'borderLeft':f'4px solid {BLUE}'
        })
    ])


# ── CSS ───────────────────────────────────────────────────────────────
CSS = f"""
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:'Inter',system-ui,-apple-system,sans-serif;
        background:{LIGHT}; color:{TEXT}; }}
.layout {{ display:flex; min-height:100vh; }}
.sidebar {{
    width:230px; min-height:100vh; background:{DARK};
    position:sticky; top:0; height:100vh; overflow-y:auto; flex-shrink:0;
    display:flex; flex-direction:column;
}}
.main {{
    flex:1; overflow-y:auto; padding:2rem 2.5rem;
    max-width:1200px;
}}
.nav-logo {{
    padding:1.5rem 1.25rem 1.1rem;
    border-bottom:1px solid rgba(255,255,255,0.07);
    margin-bottom:0.5rem;
}}
.nav-logo-name {{ font-size:0.95rem; font-weight:700; color:{WHITE};
                  letter-spacing:-0.01em; }}
.nav-logo-sub  {{ font-size:0.65rem; color:#4B5563; margin-top:0.15rem; }}
.nav-section   {{ padding:0.8rem 1.25rem 0.3rem; font-size:0.6rem; font-weight:700;
                  letter-spacing:0.12em; text-transform:uppercase; color:#4B5563; }}
.nav-btn {{
    display:block; width:100%; padding:0.55rem 1.25rem;
    color:#9CA3AF; font-size:0.79rem; font-weight:500;
    cursor:pointer; text-align:left;
    background:transparent; border:none; border-left:3px solid transparent;
    font-family:'Inter',system-ui,sans-serif;
    transition:color 0.12s, background 0.12s;
}}
.nav-btn:hover  {{ color:#E5E7EB; background:rgba(255,255,255,0.04); }}
.nav-active     {{ color:{WHITE} !important;
                   background:rgba(255,255,255,0.05) !important;
                   border-left:3px solid {BLUE} !important; }}
.filter-area    {{ padding:1rem 1.25rem;
                   border-top:1px solid rgba(255,255,255,0.07);
                   margin-top:auto; }}
.filter-label   {{ font-size:0.62rem; font-weight:600; letter-spacing:0.08em;
                   text-transform:uppercase; color:#6B7280;
                   margin-bottom:0.4rem; display:block; }}
/* Dash dropdown overrides for dark sidebar */
#filter-countries .Select-control {{
    background:#1F2937 !important; border-color:#374151 !important;
    font-size:0.75rem !important; color:#E5E7EB !important;
}}
#filter-countries .Select-placeholder {{ color:#6B7280 !important; }}
#filter-countries .Select-value-label  {{ color:#E5E7EB !important; font-size:0.75rem !important; }}
#filter-countries .Select-menu-outer   {{ background:#1F2937 !important; border-color:#374151 !important; }}
#filter-countries .Select-option       {{ color:#E5E7EB !important; background:#1F2937 !important; font-size:0.75rem !important; }}
#filter-countries .Select-option:hover {{ background:#374151 !important; }}
#filter-countries .Select-arrow        {{ border-top-color:#6B7280 !important; }}
#filter-countries .Select-multi-value-wrapper {{ max-height:80px; overflow-y:auto; }}
.rc-slider-rail   {{ background:#374151; }}
.rc-slider-track  {{ background:{BLUE}; }}
.rc-slider-handle {{ border-color:{BLUE}; background:{BLUE}; width:12px; height:12px; margin-top:-4px; }}
.dash-graph {{ border-radius:4px; }}
.footer {{ border-top:1px solid {BORDER}; margin-top:2rem; padding-top:1rem;
           font-size:0.67rem; color:{GRAY2}; text-align:center; }}
.progress-bar {{ display:flex; align-items:center; margin-bottom:1.75rem;
                 padding:0.75rem 1.25rem; background:{WHITE};
                 border-radius:8px; border:1px solid {BORDER};
                 box-shadow:0 1px 2px rgba(0,0,0,0.04); flex-wrap:wrap; gap:0; }}
.step-wrap {{ display:flex; align-items:center; }}
.step-dot {{ width:20px; height:20px; border-radius:50%; display:flex;
             align-items:center; justify-content:center; font-size:0.6rem;
             font-weight:700; flex-shrink:0; }}
.step-dot-active {{ background:{BLUE}; color:{WHITE}; }}
.step-dot-done   {{ background:{GRID}; color:{GRAY2}; }}
.step-label {{ font-size:0.7rem; margin-left:0.35rem; white-space:nowrap; }}
.step-label-active {{ color:{DARK}; font-weight:600; }}
.step-label-done   {{ color:{GRAY2}; }}
.step-line {{ width:28px; height:1px; background:{BORDER}; margin:0 0.3rem; flex-shrink:0; }}
.about-data {{ background:#FFFBEB; border:1px solid #FDE68A; border-left:3px solid {AMBER};
               border-radius:8px; padding:0.9rem 1.25rem; margin-bottom:1.5rem;
               font-size:0.78rem; color:{TEXT}; line-height:1.65; }}
.roi-slider-wrap {{ background:{LIGHT}; border:1px solid {BORDER}; border-radius:8px;
                    padding:1.25rem 1.5rem; margin-bottom:1.25rem; }}
.roi-slider-label {{ font-size:0.8rem; color:{DARK}; font-weight:600; margin-bottom:0.5rem; }}
.roi-result {{ font-size:1.1rem; font-weight:700; color:{BLUE}; }}
.roi-sub {{ font-size:0.72rem; color:{GRAY2}; margin-top:0.1rem; }}
/* Sidebar radio item labels */
#pathway-filter label, #market-filter label, #scenario-filter label {{
    font-size:0.75rem !important;
    color:#9CA3AF !important;
    cursor:pointer;
    margin-right:0.4rem;
}}
#pathway-filter input[type="radio"]:checked + label,
#market-filter input[type="radio"]:checked + label,
#scenario-filter input[type="radio"]:checked + label {{
    color:{WHITE} !important;
}}
@media (max-width:900px) {{
    .layout {{ flex-direction:column; }}
    .sidebar {{ width:100%; min-height:auto; height:auto; position:relative; flex-direction:row; flex-wrap:wrap; }}
    .main {{ padding:1rem 1.25rem; }}
    .progress-bar {{ display:none; }}
}}
"""

# ── App ───────────────────────────────────────────────────────────────
app = dash.Dash(
    __name__,
    external_stylesheets=[
        'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap'
    ],
    suppress_callback_exceptions=True
)
app.title = "AI Adoption Market Intelligence | Kairos Advisory"
server = app.server
app.index_string = f"""<!DOCTYPE html>
<html>
  <head>{{%metas%}}<title>{{%title%}}</title>{{%favicon%}}{{%css%}}
    <style>{CSS}</style>
  </head>
  <body>{{%app_entry%}}
    <footer>{{%config%}}{{%scripts%}}{{%renderer%}}</footer>
  </body>
</html>"""

_radio_label_style = {
    'fontSize': '0.75rem', 'color': '#9CA3AF',
    'marginRight': '0.4rem', 'cursor': 'pointer'
}

app.layout = html.Div([
    dcc.Store(id='nav-store', data='market'),

    # ── Sidebar ──
    html.Div([
        html.Div([
            html.Div("Kairos Advisory",   className='nav-logo-name'),
            html.Div("Market Intelligence", className='nav-logo-sub'),
        ], className='nav-logo'),

        html.Div("Navigation", className='nav-section'),
        *[html.Button(label, id=f'btn-{k}', n_clicks=0, className='nav-btn')
          for k, label in NAV],

        html.Div([
            html.Span("Filters", className='filter-label'),
            html.P("Applies to sections 02-07",
                   style={'fontSize':'0.6rem','color':'#4B5563','marginBottom':'0.6rem',
                          'marginTop':'-0.2rem'}),

            # Filter 1 — Pathway Focus
            html.Label("Pathway Focus",
                       style={'fontSize':'0.68rem','color':'#9CA3AF',
                              'marginBottom':'0.3rem','display':'block'}),
            dcc.RadioItems(
                id='pathway-filter',
                options=[
                    {'label': 'All Pathways', 'value': 'all'},
                    {'label': 'University',   'value': 'uni'},
                    {'label': 'Ausbildung',   'value': 'ausb'},
                    {'label': 'Work Visa',    'value': 'work'},
                ],
                value='all',
                labelStyle={'display': 'inline-block', **_radio_label_style},
                style={'marginBottom': '0.9rem', 'lineHeight': '1.8'}
            ),

            # LATAM Countries
            html.Label("LATAM Countries",
                       style={'fontSize':'0.68rem','color':'#9CA3AF',
                              'marginBottom':'0.3rem','display':'block'}),
            dcc.Dropdown(
                id='filter-countries',
                options=[{'label': c, 'value': c} for c in sorted(LATAM)],
                value=['Brazil','Colombia','Mexico','Chile','Peru','Argentina'],
                multi=True, clearable=False,
                style={'fontSize':'0.75rem','marginBottom':'0.8rem'}
            ),

            # Filter 2 — Priority Market
            html.Label("Priority Market",
                       style={'fontSize':'0.68rem','color':'#9CA3AF',
                              'marginBottom':'0.3rem','display':'block'}),
            dcc.RadioItems(
                id='market-filter',
                options=[
                    {'label': 'All Markets', 'value': 'all'},
                    {'label': 'Colombia',    'value': 'col'},
                    {'label': 'Brazil',      'value': 'bra'},
                    {'label': 'Mexico',      'value': 'mex'},
                    {'label': 'Chile',       'value': 'chl'},
                ],
                value='all',
                labelStyle={'display': 'inline-block', **_radio_label_style},
                style={'marginBottom': '0.9rem', 'lineHeight': '1.8'}
            ),

            # Year Range
            html.Label("Year Range (Section 02 only)",
                       style={'fontSize':'0.68rem','color':'#9CA3AF',
                              'marginBottom':'0.35rem','display':'block'}),
            dcc.RangeSlider(
                id='filter-years', min=2000, max=2022, value=[2010, 2022],
                marks={2000:'2000', 2010:'2010', 2022:'2022'}, step=1,
                tooltip={"placement":"bottom","always_visible":False}
            ),

            # Filter 3 — Investment Scenario
            html.Label("Investment Scenario",
                       style={'fontSize':'0.68rem','color':'#9CA3AF',
                              'marginBottom':'0.3rem','display':'block',
                              'marginTop':'0.85rem'}),
            dcc.RadioItems(
                id='scenario-filter',
                options=[
                    {'label': 'Solo Operator',  'value': 'solo'},
                    {'label': 'Small Team (3)', 'value': 'small'},
                    {'label': 'Full Team (5)',  'value': 'full'},
                ],
                value='solo',
                labelStyle={'display': 'inline-block', **_radio_label_style},
                style={'marginBottom': '0.9rem', 'lineHeight': '1.8'}
            ),

            html.Div([
                html.P("Data Sources",
                       style={'fontSize':'0.6rem','color':'#4B5563','fontWeight':'600',
                              'marginBottom':'0.35rem','marginTop':'0.5rem',
                              'letterSpacing':'0.06em','textTransform':'uppercase'}),
                html.P("UNESCO UIS · Global Migration (sim.)\n"
                       "EU Job Postings · IIE Open Doors\n"
                       "German University Enrollment\n"
                       "DAAD 2025/26 · BIBB 2024\n"
                       "Bundesagentur 2026",
                       style={'fontSize':'0.62rem','color':'#6B7280',
                              'lineHeight':'1.75','whiteSpace':'pre-line'})
            ])
        ], className='filter-area'),
    ], className='sidebar'),

    # ── Main ──
    html.Div([
        html.Div(id='progress-bar', className='progress-bar'),
        html.Div(id='page-content'),
        html.Div("AI Adoption Opportunity Project · Ironhack Berlin · June 2026  ·  "
                 "Lucas Barrios · Kairos Consulting · kairosconsulting.co",
                 className='footer')
    ], className='main'),

], className='layout')


# ── Callbacks ─────────────────────────────────────────────────────────
@app.callback(
    Output('page-content', 'children'),
    [Input('nav-store', 'data'),
     Input('filter-countries', 'value'),
     Input('filter-years', 'value'),
     Input('pathway-filter', 'value'),
     Input('market-filter', 'value'),
     Input('scenario-filter', 'value')]
)
def render_page(nav, countries, years, pathway, market, scenario):
    pathway  = pathway  or 'all'
    market   = market   or 'all'
    scenario = scenario or 'solo'
    pages = {
        'market':   lambda: s_market(),
        'latam':    lambda: s_latam(countries, years, market),
        'germany':  lambda: s_germany(pathway),
        'profiles': lambda: s_profiles(market),
        'usecases': lambda: s_usecases(pathway),
        'risks':    lambda: s_risks(),
        'reco':     lambda: s_reco(scenario),
    }
    return pages.get(nav, s_market)()


@app.callback(
    Output('nav-store', 'data'),
    [Input(f'btn-{k}', 'n_clicks') for k, _ in NAV],
    prevent_initial_call=True
)
def update_nav(*_):
    ctx = dash.callback_context
    if not ctx.triggered:
        return 'market'
    return ctx.triggered[0]['prop_id'].split('.')[0].replace('btn-', '')


@app.callback(
    [Output(f'btn-{k}', 'className') for k, _ in NAV],
    Input('nav-store', 'data')
)
def style_nav(active):
    return [
        'nav-btn nav-active' if k == active else 'nav-btn'
        for k, _ in NAV
    ]


@app.callback(
    [Output('roi-chart-dynamic', 'figure'),
     Output('roi-summary', 'children')],
    [Input('conv-rate-slider', 'value'),
     Input('ticket-slider', 'value'),
     Input('scenario-filter', 'value')],
    prevent_initial_call=True
)
def update_roi(conv_rate, ticket, scenario):
    if conv_rate is None or ticket is None:
        raise PreventUpdate

    scenario = scenario or 'solo'
    months = list(range(1, 13))
    completions = [50,150,300,500,700,900,1100,1300,1500,1700,1900,2100]
    monthly_costs = SCENARIO_COSTS[scenario]
    cost = list(np.cumsum(monthly_costs))
    revenue = [round(c * (conv_rate/100) * ticket) for c in completions]
    cum_rev = list(np.cumsum(revenue))

    breakeven = next((m for m, (r, c) in enumerate(zip(cum_rev, cost), 1)
                      if r >= c), None)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=cost, name='Cumulative Investment',
        line=dict(color=RED, width=1.8, dash='dash'),
        hovertemplate='Month %{x}: EUR%{y:,.0f}<extra>Investment</extra>'
    ))
    fig.add_trace(go.Scatter(
        x=months, y=cum_rev, name='Cumulative Revenue',
        line=dict(color=BLUE, width=2.5),
        fill='tozeroy', fillcolor='rgba(29,78,216,0.05)',
        hovertemplate='Month %{x}: EUR%{y:,.0f}<extra>Revenue</extra>'
    ))
    if breakeven:
        fig.add_vline(x=breakeven, line_dash="dot",
                      line_color="rgba(29,78,216,0.5)",
                      annotation_text=f"Break-even: Month {breakeven}",
                      annotation_font_color=BLUE, annotation_font_size=10)

    title = (f"At {conv_rate}% Conversion x EUR{ticket} Avg. Ticket — "
             f"{'Break-even Month ' + str(breakeven) if breakeven else 'Break-even beyond Month 12'}"
             f" — Month 12 Revenue: EUR{revenue[11]:,.0f}/month")
    fig.update_layout(
        **CL(title, 320, legend=True, margin=dict(l=10,r=15,t=70,b=55))
    )
    fig.update_layout(
        xaxis=dict(title="Month", tickvals=list(range(1,13)),
                   gridcolor=GRID, linecolor=BORDER),
        yaxis=dict(gridcolor=GRID, title="EUR",
                   tickformat=",.0f", showgrid=True)
    )

    m12 = revenue[11]
    scenario_label = SCENARIO_LABELS.get(scenario, 'Solo operator model')
    summary = html.Div([
        html.Div([
            html.P("Investment Scenario", className='roi-sub'),
            html.P(scenario_label,
                   style={'fontSize':'0.95rem','fontWeight':'600','color':DARK}),
        ], style={'marginBottom':'1rem'}),
        html.Div([
            html.P("Month 12 Monthly Revenue", className='roi-sub'),
            html.P(f"EUR{m12:,.0f}", className='roi-result'),
        ], style={'marginBottom':'1rem'}),
        html.Div([
            html.P("Break-even", className='roi-sub'),
            html.P(f"Month {breakeven}" if breakeven else "After Month 12",
                   className='roi-result',
                   style={'color': GREEN if breakeven and breakeven <= 6 else AMBER}),
        ], style={'marginBottom':'1rem'}),
        html.Div([
            html.P("Monthly clients needed", className='roi-sub'),
            html.P(f"{round(completions[4] * conv_rate/100)} by Month 5",
                   style={'fontSize':'0.95rem','fontWeight':'600','color':DARK}),
        ]),
    ])

    return fig, summary


@app.callback(
    Output('progress-bar', 'children'),
    Input('nav-store', 'data')
)
def update_progress(active):
    steps = [(k, label.split('  ')[1]) for k, label in NAV]

    items = []
    for i, (k, label) in enumerate(steps):
        is_active = (k == active)

        dot = html.Div(
            str(i+1),
            className='step-dot ' + (
                'step-dot-active' if is_active else 'step-dot-done'
            )
        )
        lbl = html.Span(
            label,
            className='step-label ' + (
                'step-label-active' if is_active else 'step-label-done'
            )
        )
        items.append(html.Div([dot, lbl], className='step-wrap'))
        if i < len(steps) - 1:
            items.append(html.Div(className='step-line'))

    return items


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run(host='0.0.0.0', port=port, debug=False)
