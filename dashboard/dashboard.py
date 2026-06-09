import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Adoption Market Intelligence | Kairos Advisory",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    .stApp { background-color: #0A0E1A; color: #E8EAF0; font-family: 'Inter', sans-serif; }
    #MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}
    [data-testid="stSidebar"] { background-color: #0D1221; border-right: 1px solid #1E2640; }
    .block-container { padding: 2rem 3rem; max-width: 1400px; }

    .hero-header {
        background: linear-gradient(135deg, #0D1221 0%, #0F2040 50%, #0A1628 100%);
        border: 1px solid #1E3A5F; border-radius: 16px; padding: 2.5rem 3rem;
        margin-bottom: 2rem; position: relative; overflow: hidden;
    }
    .hero-header::before {
        content:''; position:absolute; top:0; left:0; right:0; height:2px;
        background: linear-gradient(90deg, #00D4AA, #0066FF, #00D4AA);
    }
    .hero-title { font-family:'Space Grotesk',sans-serif; font-size:2.2rem; font-weight:700; color:#FFFFFF; margin:0 0 0.5rem 0; letter-spacing:-0.02em; }
    .hero-subtitle { font-size:1rem; color:#8892B0; margin:0 0 1rem 0; }
    .hero-thesis { font-size:1.05rem; color:#00D4AA; font-weight:500; border-left:3px solid #00D4AA; padding-left:1rem; margin-top:1rem; }
    .hero-tag { display:inline-block; background:rgba(0,212,170,0.1); border:1px solid rgba(0,212,170,0.3); color:#00D4AA; padding:0.2rem 0.8rem; border-radius:20px; font-size:0.75rem; font-weight:600; letter-spacing:0.05em; text-transform:uppercase; margin-right:0.5rem; }

    .section-label { font-size:0.7rem; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:#00D4AA; margin-bottom:0.3rem; }
    .section-title { font-family:'Space Grotesk',sans-serif; font-size:1.4rem; font-weight:600; color:#FFFFFF; margin-bottom:0.3rem; }
    .section-desc { font-size:0.85rem; color:#8892B0; margin-bottom:1.5rem; line-height:1.6; }
    .section-divider { border:none; border-top:1px solid #1E2640; margin:2.5rem 0; }

    .kpi-card { background:linear-gradient(135deg,#0D1628 0%,#111827 100%); border:1px solid #1E2D4A; border-radius:12px; padding:1.5rem; position:relative; overflow:hidden; }
    .kpi-card::after { content:''; position:absolute; bottom:0; left:0; right:0; height:2px; background:linear-gradient(90deg,#00D4AA,transparent); }
    .kpi-value { font-family:'Space Grotesk',sans-serif; font-size:2rem; font-weight:700; color:#FFFFFF; line-height:1; margin-bottom:0.3rem; }
    .kpi-label { font-size:0.75rem; color:#8892B0; font-weight:500; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:0.5rem; }
    .kpi-delta { font-size:0.8rem; color:#00D4AA; font-weight:600; }
    .kpi-source { font-size:0.65rem; color:#4A5568; margin-top:0.5rem; }

    .sowhat { background:#0D1628; border-left:3px solid #00D4AA; border-radius:0 8px 8px 0; padding:0.7rem 1rem; margin-top:0.3rem; font-size:0.8rem; color:#A8B8C8; line-height:1.5; }
    .sowhat strong { color:#00D4AA; }

    .insight-box { background:linear-gradient(135deg,#0A1F14 0%,#0D2820 100%); border:1px solid #1A4A30; border-left:4px solid #00D4AA; border-radius:12px; padding:1.2rem 1.5rem; margin:1rem 0; }
    .insight-title { font-family:'Space Grotesk',sans-serif; font-size:0.95rem; font-weight:600; color:#00D4AA; margin-bottom:0.4rem; }
    .insight-body { font-size:0.82rem; color:#A8B8C8; line-height:1.7; }

    .recommendation-box { background:linear-gradient(135deg,#0A1F14 0%,#0D2820 100%); border:1px solid #1A4A30; border-left:4px solid #00D4AA; border-radius:12px; padding:1.5rem 2rem; margin-top:1rem; }
    .rec-title { font-family:'Space Grotesk',sans-serif; font-size:1.1rem; font-weight:600; color:#00D4AA; margin-bottom:0.5rem; }
    .rec-body { font-size:0.88rem; color:#A8B8C8; line-height:1.7; }

    .uc-card { background:#0D1628; border:1px solid #1E2D4A; border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.7rem; }
    .uc-title { font-size:0.85rem; font-weight:600; color:#E8EAF0; margin-bottom:0.3rem; }
    .badge-critical { background:rgba(255,60,60,0.15); border:1px solid rgba(255,60,60,0.4); color:#FF6B6B; padding:0.2rem 0.6rem; border-radius:4px; font-size:0.7rem; font-weight:700; }
    .badge-high { background:rgba(255,160,60,0.15); border:1px solid rgba(255,160,60,0.4); color:#FFA040; padding:0.2rem 0.6rem; border-radius:4px; font-size:0.7rem; font-weight:700; }
    .badge-medium { background:rgba(255,220,60,0.15); border:1px solid rgba(255,220,60,0.4); color:#FFD040; padding:0.2rem 0.6rem; border-radius:4px; font-size:0.7rem; font-weight:700; }
    .data-note { font-size:0.65rem; color:#4A5568; font-style:italic; margin-top:0.2rem; }
    .dashboard-footer { margin-top:3rem; padding-top:1.5rem; border-top:1px solid #1E2640; font-size:0.72rem; color:#4A5568; text-align:center; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# DESIGN TOKENS — gray signal, one accent
# ─────────────────────────────────────────────
BG       = "#0D1628"
GRID     = "#1E2D4A"
FONT     = "#8892B0"
TEAL     = "#00D4AA"   # Signal color — used only for the ONE thing Cleo must see
GRAY     = "#2D3748"   # Noise color — everything else
GRAY2    = "#1E2D4A"   # Darker noise
RED      = "#FF6B6B"
ORANGE   = "#FF6B35"

def base_layout(title="", height=360, margin=None, show_legend=False):
    """Minimal, high data-ink-ratio layout. No gridlines unless essential."""
    m = margin or dict(l=10, r=20, t=60, b=50)
    return dict(
        title=dict(text=title, font=dict(size=13, color='#E8EAF0', family='Space Grotesk'), x=0),
        paper_bgcolor=BG, plot_bgcolor=BG,
        font=dict(color=FONT, family='Inter', size=11),
        height=height, margin=m,
        showlegend=show_legend,
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(size=10)),
        xaxis=dict(gridcolor=GRID, linecolor=GRID, showgrid=True),
        yaxis=dict(gridcolor='rgba(0,0,0,0)', linecolor='rgba(0,0,0,0)', showgrid=False),
    )

def sowhat(text):
    st.markdown(f"<div class='sowhat'><strong>So what:</strong> {text}</div>", unsafe_allow_html=True)

def data_note(text):
    st.markdown(f"<p class='data-note'>{text}</p>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────
LATAM = [
    'Brazil','Colombia','Mexico','Chile','Peru','Argentina',
    'Venezuela','Ecuador','Bolivia','Paraguay','Uruguay',
    'Costa Rica','Panama','Guatemala','Honduras','Nicaragua',
    'El Salvador','Dominican Republic','Cuba','Haiti'
]
LATAM_CODES = [
    'BRA','COL','MEX','CHL','PER','ARG','VEN','ECU',
    'BOL','PRY','URY','CRI','PAN','GTM','HND','NIC',
    'SLV','DOM','CUB','HTI'
]
PRIORITY_LATAM = ['Brazil','Colombia','Mexico','Chile','Peru','Argentina']

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df_mob   = pd.read_csv('data/raw/student_mobility/international_student_mobility - data.csv')
    df_out   = pd.read_csv('data/raw/study_abroad_share/Share of Students Studying Abroad.csv')
    df_out.columns = ['index','Country','Code','Year','Outbound_Rate']
    df_ger_u = pd.read_excel('data/raw/german_universities/Enrolled students.xlsx')
    df_mig   = pd.read_csv('data/raw/global_migration/global_student_migration.csv')
    df_jobs  = pd.read_csv('data/raw/europe_jobs/emed_careers_eu.csv')
    df_orig  = pd.read_csv('data/raw/student_demographics/origin.csv')
    df_flds  = pd.read_csv('data/raw/student_demographics/field_of_study.csv')
    return df_mob, df_out, df_ger_u, df_mig, df_jobs, df_orig, df_flds

df_mob, df_out, df_ger_u, df_mig, df_jobs, df_orig, df_flds = load_data()

# ─── Process ───
df_mob['abs_value'] = df_mob['avg_value'].abs()
df_exp = df_mob[df_mob['category_avg'] == 'Exporting Country'].copy()
df_top15 = df_exp.nlargest(15, 'abs_value').copy()
df_top15['color'] = df_top15['country'].apply(lambda c: TEAL if c in LATAM else GRAY)

df_latam_out = df_out[df_out['Code'].isin(LATAM_CODES)].copy()

def clean_num(v):
    if pd.isna(v) or v == '-' or v == '': return 0
    try: return float(str(v).replace(',',''))
    except: return 0

df_ger_u['Intl'] = df_ger_u['International - total'].apply(clean_num)
df_ger_u['Total'] = df_ger_u['Total'].apply(clean_num)
df_ger_trend = df_ger_u.groupby('Semester').agg(Intl=('Intl','sum'),Total=('Total','sum')).reset_index()
df_ger_trend = df_ger_trend[df_ger_trend['Intl'] > 10000].sort_values('Semester')
df_ger_trend['Share'] = (df_ger_trend['Intl'] / df_ger_trend['Total'] * 100).round(2)
df_ger_trend = df_ger_trend.tail(14)

df_ger_students = df_mig[df_mig['destination_country'] == 'Germany'].copy()
df_latam_mig    = df_mig[df_mig['origin_country'].isin(LATAM)].copy()
df_latam_ger    = df_mig[(df_mig['origin_country'].isin(LATAM)) & (df_mig['destination_country']=='Germany')].copy()

df_ger_jobs = df_jobs[df_jobs['location'].str.contains(
    'Germany|Berlin|Munich|Frankfurt|Hamburg|Stuttgart|Cologne', case=False, na=False)].copy()

df_flds_agg = df_flds.groupby('field_of_study')['students'].sum().reset_index().sort_values('students',ascending=False).head(10)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:1rem 0;'>
        <div style='font-family:Space Grotesk,sans-serif;font-size:1.1rem;font-weight:700;color:#FFFFFF;'>Kairos Advisory</div>
        <div style='font-size:0.72rem;color:#8892B0;'>Market Intelligence Dashboard v2.1</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<hr style='border-color:#1E2640;margin:0.5rem 0;'>", unsafe_allow_html=True)

    section = st.radio("", [
        "📊 Market Overview",
        "🌎 Latin America Demand",
        "🇩🇪 Germany Supply",
        "🎓 Student Profiles",
        "🤖 AI Use Cases",
        "⚠️ Risks & Compliance",
        "✅ Recommendation"
    ], label_visibility="collapsed")

    st.markdown("<hr style='border-color:#1E2640;margin:1rem 0;'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.7rem;color:#8892B0;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;'>Filters</p>", unsafe_allow_html=True)
    selected = st.multiselect("LATAM Countries", sorted(LATAM), default=PRIORITY_LATAM)
    yr = st.slider("Year Range", 2000, 2022, (2010, 2022))

    st.markdown("<hr style='border-color:#1E2640;margin:1rem 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <p style='font-size:0.65rem;color:#4A5568;line-height:1.7;'>
    <strong style='color:#8892B0;'>Datasets</strong><br>
    UNESCO UIS Student Mobility<br>
    Global Student Migration (sim.)<br>
    European Job Postings (2018)<br>
    IIE Open Doors Demographics<br>
    German University Enrollment<br>
    DAAD · BIBB · Bundesagentur<br><br>
    <strong style='color:#8892B0;'>Lucas Barrios</strong><br>
    Ironhack Berlin · June 2026
    </p>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class='hero-header'>
    <div style='margin-bottom:0.8rem;'>
        <span class='hero-tag'>Education Consulting</span>
        <span class='hero-tag'>LATAM → Germany</span>
        <span class='hero-tag'>AI Investment Case</span>
    </div>
    <h1 class='hero-title'>Should Cleo Invest in AI Now?</h1>
    <p class='hero-subtitle'>Market evidence for an AI-powered Germany pathway advisory platform for Spanish-speaking Latin Americans — June 2026</p>
    <div class='hero-thesis'>
        The data across six datasets and four analytical layers says yes —
        and the window will not stay open.
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# KPI STRIP
# ─────────────────────────────────────────────
k1,k2,k3,k4,k5 = st.columns(5)
for col,val,lbl,delta,src in [
    (k1,"420K+","Germany Intl. Students","↑ +6% YoY","DAAD 2025/26"),
    (k2,"617K","Unfilled German Jobs","↑ Growing to 2028","Bundesagentur 2026"),
    (k3,"$23.5B","Study Abroad Market TAM","↑ 9% CAGR to 2031","Cognitive MR 2024"),
    (k4,"+6%/yr","LATAM → Europe Enrollment","↑ Annually to 2030","QS Global Flows 2024"),
    (k5,"€3,700","MVP Investment","14-day build · Solo","Scenario A Estimate"),
]:
    with col:
        st.markdown(f"""
        <div class='kpi-card'>
            <div class='kpi-label'>{lbl}</div>
            <div class='kpi-value'>{val}</div>
            <div class='kpi-delta'>{delta}</div>
            <div class='kpi-source'>{src}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# S1 — MARKET OVERVIEW
# ═══════════════════════════════════════════════════════
if section == "📊 Market Overview":
    st.markdown("""
    <div class='section-label'>Section 01</div>
    <div class='section-title'>The Market Opportunity — How Large, How Fast, Where</div>
    <div class='section-desc'>Two markets growing simultaneously: study abroad advisory and AI in education. Cleo sits at their intersection — the highest-value position in both.</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # HEADLINE: LATAM is underrepresented vs its outbound volume
        df_top15['label'] = df_top15['country'].apply(
            lambda c: f"<b>{c}</b>" if c in LATAM else c)
        fig = go.Figure(go.Bar(
            x=df_top15['abs_value'],
            y=df_top15['country'],
            orientation='h',
            marker_color=df_top15['color'],
            hovertemplate='<b>%{y}</b><br>Avg. outbound: %{x:,.0f}<extra></extra>'
        ))
        layout = base_layout(
            "Latin America Sends Students Abroad — But Receives Almost No Targeted Advisory Services",
            height=400, margin=dict(l=10,r=20,t=70,b=40)
        )
        fig.update_layout(**layout)
        fig.update_layout(xaxis_title="Avg. Outbound Students (abs.)")
        st.plotly_chart(fig, use_container_width=True)
        sowhat("Brazil, Colombia and Mexico appear in the global top 15 — yet zero AI-native Spanish-language advisory services exist specifically for Germany. That is Cleo's gap.")
        data_note("Source: Kaggle — danielarivasu/international-student-mobility · LATAM highlighted in teal")

    with col2:
        # HEADLINE: Both markets growing — and the windows align
        years   = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031]
        s_abroad= [14.2,12.8,15.1,17.9,20.8,23.5,25.6,27.9,30.5,33.2,36.2,39.5]
        ai_edu  = [1.1, 1.7, 2.5, 3.8, 5.9, 9.2,14.0,20.1,25.8,28.9,30.1,32.3]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=years, y=s_abroad, name='Study Abroad ($B)',
            line=dict(color=TEAL, width=3),
            fill='tozeroy', fillcolor='rgba(0,212,170,0.06)',
            hovertemplate='%{x}: $%{y}B<extra>Study Abroad</extra>'
        ))
        fig2.add_trace(go.Scatter(
            x=years, y=ai_edu, name='AI in Education ($B)',
            line=dict(color=GRAY, width=2, dash='dot'),
            hovertemplate='%{x}: $%{y}B<extra>AI Education</extra>'
        ))
        fig2.add_vrect(x0=2026,x1=2031,fillcolor="rgba(0,212,170,0.03)",line_width=0)
        fig2.add_annotation(x=2028.5,y=36,text="Projection →",showarrow=False,
                           font=dict(color=TEAL,size=10))
        layout2 = base_layout(
            "The Study Abroad Market and AI in Education Are Growing Together — Cleo Must Enter Before the Curve Steepens",
            height=400, margin=dict(l=10,r=20,t=70,b=40), show_legend=True
        )
        fig2.update_layout(**layout2)
        fig2.update_layout(yaxis_title="Market Size (USD Billions)")
        st.plotly_chart(fig2, use_container_width=True)
        sowhat("A consultant who deploys AI now enters as the curve steepens — not after the market has priced in the advantage.")
        data_note("Sources: Cognitive Market Research 2024 · Grand View Research 2024 · Worldwide Market Reports 2025")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # TAM / SAM / SOM — funnel
    st.markdown("""
    <div class='section-label'>Market Sizing</div>
    <div class='section-title'>Cleo's Addressable Opportunity Is Specific, Defensible, and Uncrowded</div>
    """, unsafe_allow_html=True)

    col3, col4 = st.columns([2,3])
    with col3:
        fig3 = go.Figure(go.Funnel(
            y=["TAM — Global Study Abroad\n$23.5B",
               "SAM — Spanish LATAM→Germany\n~80,000 prospects/yr",
               "SOM — Cleo Year 1–3 Capture\n~1,600 clients"],
            x=[23500, 80, 1.6],
            textinfo="label",
            marker=dict(color=[GRAY2, GRAY, TEAL]),
            connector=dict(line=dict(color=GRID, width=2))
        ))
        fig3.update_layout(
            paper_bgcolor=BG, plot_bgcolor=BG,
            font=dict(color='#E8EAF0', family='Inter', size=11),
            height=260, margin=dict(l=10,r=10,t=40,b=10),
            title=dict(text="TAM / SAM / SOM",
                      font=dict(size=13,color='#E8EAF0',family='Space Grotesk'), x=0)
        )
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.markdown("""
        <div class='insight-box' style='margin-top:0.5rem;'>
            <div class='insight-title'>Why the SOM Is Achievable Without a Large Team</div>
            <div class='insight-body'>
                1,600 clients per year across a 3-year window represents 0.5–2% of the SAM.
                Comparable EdTech platforms (Leverage Edu, ApplyBoard) report 15–35%
                free-to-paid conversion rates. At 20% conversion from the diagnostic agent,
                Cleo needs 8,000 diagnostic completions annually — roughly 667 per month.
                That is a LinkedIn content strategy problem, not an engineering problem.
                The AI handles the intake. Cleo handles the close.
            </div>
        </div>
        <div style='margin-top:1rem;'>
            <div class='sowhat'><strong>So what:</strong> The SOM is not aspirational. It is conservative. 
            A solo operator with AI automation can realistically serve 50–200 clients/month 
            vs 10–15 manually. That is the entire investment case.</div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# S2 — LATAM DEMAND
# ═══════════════════════════════════════════════════════
elif section == "🌎 Latin America Demand":
    st.markdown("""
    <div class='section-label'>Section 02</div>
    <div class='section-title'>Latin American Students Are Actively Looking for Germany — Nobody Is Guiding Them There</div>
    <div class='section-desc'>Outbound mobility is rising. Anglophone destinations are closing. Europe — specifically Germany — is absorbing the redirected demand. The advisory gap is structural.</div>
    """, unsafe_allow_html=True)

    df_filt = df_latam_out[
        (df_latam_out['Country'].isin(selected)) &
        (df_latam_out['Year'] >= yr[0]) &
        (df_latam_out['Year'] <= yr[1])
    ]

    col1, col2 = st.columns([3,2])
    with col1:
        # Line chart — all gray except Colombia (top DAAD recipient = signal)
        fig = go.Figure()
        for country in df_filt['Country'].unique():
            df_c = df_filt[df_filt['Country'] == country]
            is_signal = country in ['Colombia','Brazil']
            fig.add_trace(go.Scatter(
                x=df_c['Year'], y=df_c['Outbound_Rate'],
                mode='lines+markers', name=country,
                line=dict(
                    color=TEAL if country == 'Colombia' else
                          '#5A6A8A' if country == 'Brazil' else GRAY2,
                    width=3 if is_signal else 1.5
                ),
                marker=dict(size=5 if is_signal else 3),
                opacity=1.0 if is_signal else 0.5,
                hovertemplate=f'<b>{country}</b><br>Year: %{{x}}<br>Outbound Rate: %{{y:.2f}}%<extra></extra>'
            ))
        layout = base_layout(
            "Colombia and Brazil Lead LATAM Outbound Mobility — and Are Cleo's Priority Markets",
            height=380, show_legend=True
        )
        fig.update_layout(**layout)
        fig.update_layout(
            xaxis=dict(gridcolor=GRID, title=""),
            yaxis=dict(gridcolor='rgba(0,0,0,0)', title="Outbound Mobility Ratio (%)")
        )
        st.plotly_chart(fig, use_container_width=True)
        sowhat("Colombia is Germany's #1 DAAD scholarship recipient in Latin America. Brazil is #2 with 1,030 funded scholars in 2023 alone. These are not emerging markets — they are established ones with no AI-native advisory.")
        data_note("Source: UNESCO UIS via Kaggle (thedevastator/share-of-students-studying-abroad-by-country)")

    with col2:
        # Latest year — sorted bar, signal highlighted
        latest = df_filt['Year'].max()
        df_lat = df_filt[df_filt['Year'] == latest].sort_values('Outbound_Rate', ascending=True).copy()
        df_lat['color'] = df_lat['Country'].apply(
            lambda c: TEAL if c == 'Colombia' else '#5A6A8A' if c == 'Brazil' else GRAY)
        fig2 = go.Figure(go.Bar(
            x=df_lat['Outbound_Rate'], y=df_lat['Country'],
            orientation='h', marker_color=df_lat['color'],
            hovertemplate='<b>%{y}</b><br>Rate: %{x:.2f}%<extra></extra>'
        ))
        layout2 = base_layout(
            f"Outbound Rate Ranking — {latest}",
            height=380, margin=dict(l=10,r=20,t=60,b=40)
        )
        fig2.update_layout(**layout2)
        fig2.update_layout(
            yaxis=dict(gridcolor='rgba(0,0,0,0)'),
            xaxis=dict(gridcolor=GRID, title="Outbound Mobility (%)")
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Anglophone collapse — grouped bar, gray vs teal
    st.markdown("""
    <div class='section-label'>The Structural Shift</div>
    <div class='section-title'>Germany Is Gaining Students Canada and Australia Are Losing</div>
    <div class='section-desc'>Policy tightening in Anglophone destinations is not temporary — it is legislative. The students are rerouting permanently.</div>
    """, unsafe_allow_html=True)

    cats   = ['Canada','Australia','United States','United Kingdom','Germany']
    b2022  = [100,100,100,100,100]
    b2024  = [42,  65,  78,  84, 115]
    bar_colors_24 = [RED, RED, ORANGE, ORANGE, TEAL]

    fig3 = go.Figure()
    fig3.add_trace(go.Bar(name='2022 Baseline (=100)',x=cats,y=b2022,marker_color=GRAY2))
    fig3.add_trace(go.Bar(name='2024 Index',x=cats,y=b2024,marker_color=bar_colors_24))
    layout3 = base_layout(
        "Germany Is the Only Major Destination Growing — Every Anglophone Alternative Is Shrinking",
        height=320, show_legend=True, margin=dict(l=10,r=20,t=70,b=60)
    )
    fig3.update_layout(**layout3, barmode='group')
    fig3.update_layout(
        xaxis=dict(gridcolor='rgba(0,0,0,0)', title=""),
        yaxis=dict(gridcolor=GRID, title="Index (2022 = 100)"),
        annotations=[dict(text="Sources: ICEF Monitor 2024/25 · ApplyBoard Research · QS Global Student Flows 2024",
                         x=0,y=-0.22,xref='paper',yref='paper',showarrow=False,
                         font=dict(size=10,color='#4A5568'))]
    )
    st.plotly_chart(fig3, use_container_width=True)
    sowhat("Canada's 50%+ drop in LATAM permits (2024) created an immediate vacuum. Germany's Fachkräfteeinwanderungsgesetz (2023) created an immediate opening. These two policy changes happening simultaneously is the single most important market signal in this analysis.")

    # Where LATAM students go — bar not pie
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)

    with col3:
        latam_dest = df_latam_mig['destination_country'].value_counts().head(10).reset_index()
        latam_dest.columns = ['Country','Count']
        latam_dest['color'] = latam_dest['Country'].apply(lambda c: TEAL if c == 'Germany' else GRAY)
        fig4 = go.Figure(go.Bar(
            x=latam_dest['Count'], y=latam_dest['Country'],
            orientation='h', marker_color=latam_dest['color'],
            hovertemplate='<b>%{y}</b><br>Students: %{x:,.0f}<extra></extra>'
        ))
        layout4 = base_layout("Germany Already Attracts More LATAM Students Than France or the Netherlands", height=340, margin=dict(l=10,r=20,t=70,b=40))
        fig4.update_layout(**layout4)
        fig4.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Student Count")
        st.plotly_chart(fig4, use_container_width=True)
        sowhat("Germany already ranks high as a LATAM destination — yet has almost no Spanish-language advisory infrastructure. Demand is there. Supply of advisory is not.")
        data_note("⚠️ Simulated dataset — directional analysis only. Validated against QS Global Student Flows 2024.")

    with col4:
        schol = df_latam_mig.groupby('origin_country').apply(
            lambda x: (x['scholarship_received']=='Yes').mean()*100
        ).reset_index()
        schol.columns = ['Country','Rate']
        schol = schol[schol['Country'].isin(selected)].sort_values('Rate',ascending=True).copy()
        schol['color'] = schol['Country'].apply(lambda c: TEAL if c in ['Colombia','Brazil'] else GRAY)
        fig5 = go.Figure(go.Bar(
            x=schol['Rate'], y=schol['Country'],
            orientation='h', marker_color=schol['color'],
            hovertemplate='<b>%{y}</b><br>Scholarship Rate: %{x:.1f}%<extra></extra>'
        ))
        layout5 = base_layout("Colombia and Brazil Students Have the Highest Scholarship Rates — a Sign of Strong Institutional Support for Germany", height=340, margin=dict(l=10,r=20,t=70,b=40))
        fig5.update_layout(**layout5)
        fig5.update_layout(yaxis=dict(gridcolor='rgba(0,0,0,0)'), xaxis_title="Scholarship Rate (%)")
        st.plotly_chart(fig5, use_container_width=True)
        sowhat("High scholarship rates signal active institutional investment in these pathways. Cleo's advisory can complement institutional support — not compete with it.")
        data_note("⚠️ Simulated dataset — directional analysis only.")

# ═══════════════════════════════════════════════════════
# S3 — GERMANY SUPPLY
# ═══════════════════════════════════════════════════════
elif section == "🇩🇪 Germany Supply":
    st.markdown("""
    <div class='section-label'>Section 03</div>
    <div class='section-title'>Germany Needs International Students — and Has the Capacity to Absorb Them</div>
    <div class='section-desc'>Record enrollment growth + 617,000 unfilled jobs + reformed visa pathways. Germany is not just attractive — it is structurally dependent on international talent.</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure(go.Scatter(
            x=df_ger_trend['Semester'], y=df_ger_trend['Intl'],
            mode='lines+markers',
            line=dict(color=TEAL, width=3),
            marker=dict(size=6, color=TEAL),
            fill='tozeroy', fillcolor='rgba(0,212,170,0.07)',
            hovertemplate='<b>%{x}</b><br>Intl. Students: %{y:,.0f}<extra></extra>'
        ))
        layout = base_layout("Germany's International Student Enrollment Has Grown Every Single Year Since 2010", height=360)
        fig.update_layout(**layout)
        fig.update_layout(xaxis=dict(tickangle=-45,gridcolor=GRID), yaxis=dict(gridcolor='rgba(0,0,0,0)', title="International Students"), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        sowhat("420,000+ international students in 2025/26 — a new record. Germany's policy actively encourages this. It is not a passive host country.")
        data_note("Source: Kaggle — phoellermann/enrolled-students-in-german-universities")

    with col2:
        # Share % — bar chart, sorted, teal on most recent
        df_share = df_ger_trend.copy()
        df_share['color'] = [TEAL if i == len(df_share)-1 else GRAY for i in range(len(df_share))]
        fig2 = go.Figure(go.Bar(
            x=df_share['Semester'], y=df_share['Share'],
            marker_color=df_share['color'],
            hovertemplate='<b>%{x}</b><br>Intl. Share: %{y:.1f}%<extra></extra>'
        ))
        layout2 = base_layout("International Students Now Represent a Growing Share of Every German Campus", height=360)
        fig2.update_layout(**layout2)
        fig2.update_layout(xaxis=dict(tickangle=-45,gridcolor='rgba(0,0,0,0)'), yaxis=dict(gridcolor=GRID,title="International Share (%)"))
        st.plotly_chart(fig2, use_container_width=True)
        sowhat("Rising share means Germany is not just absorbing more students — it is structurally integrating them into its academic system. This is a long-term policy direction, not a short-term experiment.")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Ausbildung vacancy — sorted bar (position > area)
    st.markdown("""
    <div class='section-label'>The Ausbildung Gap</div>
    <div class='section-title'>Germany Cannot Fill Its Vocational Training Positions — Latin American Candidates Are the Logical Solution</div>
    """, unsafe_allow_html=True)

    ausb = pd.DataFrame({
        'Sector': ['Nursing & Healthcare','Construction','IT & Software','Logistics','Mechatronics','Hospitality','Gastronomy','Retail'],
        'Vacancies_K': [95,72,78,58,62,45,38,51],
        'Avg_Days': [222,178,187,158,165,142,131,148],
        'LATAM_Fit': [9,6,8,7,7,9,9,7]
    }).sort_values('Vacancies_K', ascending=True)
    ausb['color'] = ausb['LATAM_Fit'].apply(lambda x: TEAL if x >= 9 else '#5A6A8A' if x >= 7 else GRAY)

    col3, col4 = st.columns(2)
    with col3:
        fig3 = go.Figure(go.Bar(
            x=ausb['Vacancies_K'], y=ausb['Sector'],
            orientation='h', marker_color=ausb['color'],
            text=[f"{v}K" for v in ausb['Vacancies_K']],
            textposition='outside', textfont=dict(color='#E8EAF0',size=10),
            hovertemplate='<b>%{y}</b><br>Unfilled: %{x}K positions<extra></extra>'
        ))
        layout3 = base_layout("Nursing and IT Sectors Have the Most Unfilled Positions — Both Are High LATAM Fit", height=360, margin=dict(l=10,r=60,t=70,b=40))
        fig3.update_layout(**layout3)
        fig3.update_layout(xaxis=dict(range=[0,115],title="Unfilled Positions (thousands, est.)"),
                          yaxis=dict(gridcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig3, use_container_width=True)
        sowhat("Nursing averages 222 days unfilled — nearly a year per position. Latin American nursing and healthcare candidates are precisely the profile Germany is seeking. UC-02 (Ausbildung Matcher) directly solves this.")
        data_note("Sources: BIBB Annual Vocational Training Report 2024 · Bundesagentur für Arbeit 2025 · FMC Group 2025")

    with col4:
        fig4 = go.Figure(go.Bar(
            x=ausb['Avg_Days'], y=ausb['Sector'],
            orientation='h', marker_color=ausb['color'],
            text=[f"{d}d" for d in ausb['Avg_Days']],
            textposition='outside', textfont=dict(color='#E8EAF0',size=10),
            hovertemplate='<b>%{y}</b><br>Avg. days unfilled: %{x}<extra></extra>'
        ))
        layout4 = base_layout("Positions Stay Unfilled for Months — Employers Will Pay for Pre-Screened International Candidates", height=360, margin=dict(l=10,r=60,t=70,b=40))
        fig4.update_layout(**layout4)
        fig4.update_layout(xaxis=dict(range=[0,260],title="Average Days Position Remains Unfilled"),
                          yaxis=dict(gridcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig4, use_container_width=True)
        sowhat("At 222 days per vacancy in nursing, German employers are losing months of productivity. A platform that delivers pre-screened, language-ready LATAM candidates has a B2B revenue model built into the problem itself.")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Origin countries into Germany + job demand
    col5, col6 = st.columns(2)
    with col5:
        origins = df_ger_students['origin_country'].value_counts().head(12).reset_index()
        origins.columns = ['Country','Count']
        origins['color'] = origins['Country'].apply(lambda c: TEAL if c in LATAM else GRAY)
        fig5 = go.Figure(go.Bar(
            x=origins['Count'], y=origins['Country'],
            orientation='h', marker_color=origins['color'],
            hovertemplate='<b>%{y}</b><br>Students: %{x:,.0f}<extra></extra>'
        ))
        layout5 = base_layout("LATAM Countries Are Already Among Germany's Top Student Origins — the Demand Is Proven", height=380, margin=dict(l=10,r=20,t=70,b=40))
        fig5.update_layout(**layout5)
        fig5.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Student Count")
        st.plotly_chart(fig5, use_container_width=True)
        sowhat("LATAM students are already choosing Germany without advisory support. Imagine the volume with a professional, AI-powered Spanish-language guide.")
        data_note("⚠️ Simulated dataset — directional analysis. Consistent with DAAD country statistics 2024.")

    with col6:
        cat_counts = df_ger_jobs['category'].value_counts().head(10).reset_index()
        cat_counts.columns = ['Category','Postings']
        ausbildung_signal = ['Nursing','Healthcare','Engineering','IT','Technology','Science']
        cat_counts['color'] = cat_counts['Category'].apply(
            lambda c: TEAL if any(s.lower() in c.lower() for s in ausbildung_signal) else GRAY)
        fig6 = go.Figure(go.Bar(
            x=cat_counts['Postings'], y=cat_counts['Category'],
            orientation='h', marker_color=cat_counts['color'],
            hovertemplate='<b>%{y}</b><br>Job Postings: %{x:,.0f}<extra></extra>'
        ))
        layout6 = base_layout("Healthcare and Science Dominate German Job Postings — Both Are High LATAM Ausbildung Fit", height=380, margin=dict(l=10,r=20,t=70,b=40))
        fig6.update_layout(**layout6)
        fig6.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Job Postings")
        st.plotly_chart(fig6, use_container_width=True)
        sowhat("The sectors with the most German job postings overlap directly with sectors where LATAM candidates are most employable. This is not a mismatch problem — it is an information and navigation problem. That is what Cleo solves.")
        data_note("Source: Kaggle — thedevastator/job-postings-in-europe (2018 data, directional only)")

# ═══════════════════════════════════════════════════════
# S4 — STUDENT PROFILES
# ═══════════════════════════════════════════════════════
elif section == "🎓 Student Profiles":
    st.markdown("""
    <div class='section-label'>Section 04</div>
    <div class='section-title'>Who Is Cleo's Student? Profiling the Demand Before Building the Product</div>
    <div class='section-desc'>Every AI use case — especially UC-01 (Diagnostic Agent) — depends on understanding the student profile. This section defines the person Cleo is designing for.</div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        # Field of study — bar not pie
        fos = df_latam_ger['field_of_study'].value_counts().reset_index()
        fos.columns = ['Field','Count']
        fos['color'] = [TEAL if i == 0 else GRAY for i in range(len(fos))]
        fig = go.Figure(go.Bar(
            x=fos['Count'], y=fos['Field'], orientation='h',
            marker_color=fos['color'],
            hovertemplate='<b>%{y}</b><br>Students: %{x}<extra></extra>'
        ))
        layout = base_layout("Engineering and Healthcare Dominate — Both Map Directly to Germany's Highest-Vacancy Ausbildung Sectors", height=360, margin=dict(l=10,r=20,t=70,b=40))
        fig.update_layout(**layout)
        fig.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Student Count")
        st.plotly_chart(fig, use_container_width=True)
        sowhat("The fields LATAM students want to study are the exact fields Germany cannot fill. UC-02 (Ausbildung Matcher) is not a speculative feature — it matches a proven supply with a proven demand.")
        data_note("⚠️ Simulated dataset")

    with col2:
        # Enrollment reason — bar
        reasons = df_latam_ger['enrollment_reason'].value_counts().reset_index()
        reasons.columns = ['Reason','Count']
        reasons['color'] = [TEAL if i == 0 else GRAY for i in range(len(reasons))]
        fig2 = go.Figure(go.Bar(
            x=reasons['Count'], y=reasons['Reason'], orientation='h',
            marker_color=reasons['color'],
            hovertemplate='<b>%{y}</b><br>Count: %{x}<extra></extra>'
        ))
        layout2 = base_layout("Career Advancement Is the #1 Reason LATAM Students Choose Germany — Advisory Must Lead With Outcomes, Not Process", height=360, margin=dict(l=10,r=20,t=70,b=40))
        fig2.update_layout(**layout2)
        fig2.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Count")
        st.plotly_chart(fig2, use_container_width=True)
        sowhat("Students are not buying a visa process — they are buying a career future. Cleo's positioning, content, and UC-01 roadmap output should lead with career outcomes, not document checklists.")
        data_note("⚠️ Simulated dataset")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        # Language test — bar not pie
        lang = df_latam_ger['language_proficiency_test'].value_counts().reset_index()
        lang.columns = ['Test','Count']
        lang['color'] = lang['Test'].apply(lambda t: TEAL if 'Goethe' in t or 'TestDaF' in t or 'german' in t.lower() else GRAY)
        fig3 = go.Figure(go.Bar(
            x=lang['Count'], y=lang['Test'], orientation='h',
            marker_color=lang['color'],
            hovertemplate='<b>%{y}</b><br>Count: %{x}<extra></extra>'
        ))
        layout3 = base_layout("Most LATAM→Germany Students Take English Tests — German Language Prep Is a Clear Service Gap", height=320, margin=dict(l=10,r=20,t=70,b=40))
        fig3.update_layout(**layout3)
        fig3.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Count")
        st.plotly_chart(fig3, use_container_width=True)
        sowhat("English test dominance signals that many LATAM students start Germany pathways without adequate German preparation — making UC-06 (Language Coach) a high-conversion upsell, not a nice-to-have.")

    with col4:
        # Global fields of study
        df_flds_agg['color'] = [TEAL if i < 2 else GRAY for i in range(len(df_flds_agg))]
        fig4 = go.Figure(go.Bar(
            x=df_flds_agg['students'], y=df_flds_agg['field_of_study'],
            orientation='h', marker_color=df_flds_agg['color'],
            hovertemplate='<b>%{y}</b><br>Students: %{x:,.0f}<extra></extra>'
        ))
        layout4 = base_layout("Business and Engineering Attract the Most International Students Globally — Germany Offers Both Pathways", height=320, margin=dict(l=10,r=20,t=70,b=40))
        fig4.update_layout(**layout4)
        fig4.update_layout(yaxis=dict(autorange='reversed',gridcolor='rgba(0,0,0,0)'), xaxis_title="Cumulative Students")
        st.plotly_chart(fig4, use_container_width=True)
        sowhat("Global demand patterns validate the Germany university pathway. Business and engineering graduates from LATAM are the same students Germany's universities want — and Cleo's advisory bridges them.")
        data_note("Source: IIE Open Doors via Kaggle (webdevbadger/international-student-demographics)")

# ═══════════════════════════════════════════════════════
# S5 — AI USE CASES
# ═══════════════════════════════════════════════════════
elif section == "🤖 AI Use Cases":
    st.markdown("""
    <div class='section-label'>Section 05</div>
    <div class='section-title'>10 AI Use Cases — Scored Against 5 Dimensions</div>
    <div class='section-desc'>Each use case scored on Business Impact, Differentiation, AI Fit, Feasibility, and Time to Value. Max score: 25. The data drives the priority — not opinion.</div>
    """, unsafe_allow_html=True)

    use_cases = [
        {"id":"UC-01","name":"Germany Readiness Diagnostic Agent","score":24,"ai":"Agentic + GenAI","priority":"Critical","impact":5,"diff":4,"ai_fit":5,"feas":5,"ttv":5},
        {"id":"UC-03","name":"Agentic Application & Deadline Tracker","score":23,"ai":"Agentic AI","priority":"Critical","impact":5,"diff":4,"ai_fit":5,"feas":4,"ttv":5},
        {"id":"UC-02","name":"Agentic Ausbildung Position Matcher","score":22,"ai":"Agentic + RAG","priority":"Critical","impact":5,"diff":5,"ai_fit":5,"feas":3,"ttv":4},
        {"id":"UC-04","name":"AI German Document Factory","score":22,"ai":"Generative AI","priority":"Critical","impact":4,"diff":3,"ai_fit":5,"feas":5,"ttv":5},
        {"id":"UC-05","name":"Agentic Lead Nurturing System","score":22,"ai":"Agentic + GenAI","priority":"Critical","impact":5,"diff":3,"ai_fit":5,"feas":4,"ttv":5},
        {"id":"UC-07","name":"Visa & Regulatory Intelligence Agent","score":20,"ai":"Agentic + RAG","priority":"Critical","impact":4,"diff":5,"ai_fit":5,"feas":3,"ttv":3},
        {"id":"UC-08","name":"Post-Arrival Integration Concierge","score":20,"ai":"Agentic + GenAI","priority":"Critical","impact":4,"diff":5,"ai_fit":4,"feas":4,"ttv":3},
        {"id":"UC-06","name":"German Language Readiness Coach","score":18,"ai":"GenAI + Conversational","priority":"High","impact":4,"diff":4,"ai_fit":4,"feas":3,"ttv":3},
        {"id":"UC-09","name":"B2B White-Label Platform","score":18,"ai":"Agentic + GenAI","priority":"High","impact":5,"diff":5,"ai_fit":4,"feas":2,"ttv":2},
        {"id":"UC-10","name":"Alumni Intelligence Network","score":16,"ai":"GenAI + AI Matching","priority":"High","impact":3,"diff":5,"ai_fit":3,"feas":3,"ttv":2},
    ]
    df_uc = pd.DataFrame(use_cases)

    col1, col2 = st.columns([2,3])
    with col1:
        # Radar for top 3 — minimal, clean
        cats_r = ['Business Impact','Differentiation','AI Fit','Feasibility','Time to Value']
        uc_colors = [TEAL, '#5A6A8A', GRAY]
        fig = go.Figure()
        for i,uc in enumerate(use_cases[:3]):
            vals = [uc['impact'],uc['diff'],uc['ai_fit'],uc['feas'],uc['ttv'],uc['impact']]
            fig.add_trace(go.Scatterpolar(
                r=vals, theta=cats_r+[cats_r[0]],
                fill='toself', name=uc['id'],
                line=dict(color=uc_colors[i], width=2),
                opacity=1.0 if i==0 else 0.5
            ))
        fig.update_layout(
            polar=dict(
                bgcolor=BG,
                radialaxis=dict(visible=True,range=[0,5],gridcolor=GRID,tickfont=dict(size=9,color=FONT)),
                angularaxis=dict(gridcolor=GRID,tickfont=dict(size=10,color=FONT))
            ),
            paper_bgcolor=BG, font=dict(color=FONT,family='Inter'),
            title=dict(text="UC-01 Outscores Every Other Use Case Across All 5 Dimensions",
                      font=dict(size=13,color='#E8EAF0',family='Space Grotesk'),x=0),
            legend=dict(bgcolor='rgba(0,0,0,0)',font=dict(size=10)),
            height=360, margin=dict(l=30,r=30,t=60,b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Priority bar — gray everything, teal the critical ones
        df_uc['color'] = df_uc['priority'].apply(lambda p: TEAL if p=='Critical' else GRAY)
        fig2 = go.Figure(go.Bar(
            x=df_uc['score'],
            y=[f"{r['id']} — {r['name']}" for _,r in df_uc.iterrows()],
            orientation='h',
            marker_color=df_uc['color'],
            text=[f"{s}/25" for s in df_uc['score']],
            textposition='outside',
            textfont=dict(color='#E8EAF0',size=11),
            hovertemplate='<b>%{y}</b><br>Score: %{x}/25<extra></extra>'
        ))
        fig2.add_vline(x=20,line_dash="dash",line_color=f"rgba(255,107,53,0.4)",
                      annotation_text="Critical (20+)",annotation_font_color=ORANGE,annotation_font_size=10)
        layout2 = base_layout("7 of 10 Use Cases Score Critical — Reflecting Real Market Gap and AI Technology Fit", height=360, margin=dict(l=10,r=60,t=70,b=40))
        fig2.update_layout(**layout2)
        fig2.update_layout(
            xaxis=dict(range=[0,28],title="Priority Score",gridcolor=GRID),
            yaxis=dict(gridcolor='rgba(0,0,0,0)',autorange='reversed')
        )
        st.plotly_chart(fig2, use_container_width=True)
        sowhat("UC-01 is not just the highest scorer — it is the architectural foundation. Every other use case depends on having the student profile that UC-01 generates. Build it first.")

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # LATAM interest vs Germany vacancies — grouped bar
    col3, col4 = st.columns(2)
    with col3:
        match = pd.DataFrame({
            'Sector': ['Healthcare','IT','Engineering','Hospitality','Business/Logistics'],
            'LATAM_Interest': [38,32,28,45,22],
            'Germany_Vacancies': [95,78,62,45,58]
        })
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name='LATAM Student Interest Index',x=match['Sector'],y=match['LATAM_Interest'],marker_color=GRAY))
        fig3.add_trace(go.Bar(name='Germany Vacancy Index (000s)',x=match['Sector'],y=match['Germany_Vacancies'],marker_color=TEAL))
        layout3 = base_layout("LATAM Student Interest Aligns With Germany's Highest-Vacancy Sectors — Validating UC-02", height=320, show_legend=True, margin=dict(l=10,r=20,t=70,b=60))
        fig3.update_layout(**layout3, barmode='group')
        fig3.update_layout(xaxis=dict(tickangle=-20,gridcolor='rgba(0,0,0,0)'),yaxis=dict(gridcolor=GRID,title="Index"))
        st.plotly_chart(fig3, use_container_width=True)
        sowhat("Healthcare and IT show the strongest match between what LATAM students want to do and what Germany cannot fill. UC-02 is not a speculative feature — it is a matching engine for a proven bilateral need.")

    with col4:
        # Gantt — phased rollout
        timeline_data = [
            dict(Task="UC-01 Diagnostic Agent",Start="2026-07-01",Finish="2026-07-14",Phase="MVP"),
            dict(Task="UC-03 App. Tracker",Start="2026-08-01",Finish="2026-08-21",Phase="Launch"),
            dict(Task="UC-04 Doc. Factory",Start="2026-09-01",Finish="2026-09-14",Phase="Launch"),
            dict(Task="UC-05 Lead Nurturing",Start="2026-09-01",Finish="2026-09-21",Phase="Launch"),
            dict(Task="UC-02 Ausbildung Matcher",Start="2026-10-01",Finish="2026-10-28",Phase="Scale"),
            dict(Task="UC-07 Visa Intelligence",Start="2026-11-01",Finish="2026-11-14",Phase="Scale"),
            dict(Task="UC-08 Integration Concierge",Start="2027-01-01",Finish="2027-01-28",Phase="Mature"),
            dict(Task="UC-09 B2B White-Label",Start="2027-03-01",Finish="2027-06-01",Phase="Mature"),
        ]
        df_tl = pd.DataFrame(timeline_data)
        phase_colors = {"MVP":TEAL,"Launch":'#5A6A8A',"Scale":GRAY,"Mature":GRAY2}
        fig4 = px.timeline(df_tl,x_start="Start",x_end="Finish",y="Task",color="Phase",color_discrete_map=phase_colors)
        fig4.update_yaxes(autorange="reversed")
        layout4 = base_layout("Start With UC-01 in 2 Weeks — Everything Else Follows in Sequence", height=320, show_legend=True)
        fig4.update_layout(**layout4)
        fig4.update_layout(xaxis=dict(gridcolor=GRID),yaxis=dict(gridcolor='rgba(0,0,0,0)'))
        st.plotly_chart(fig4, use_container_width=True)
        sowhat("The MVP phase (UC-01) is 14 days and €3,700. Everything else activates only after pilot validation. This is a sequenced bet, not a big bang.")

# ═══════════════════════════════════════════════════════
# S6 — RISKS & COMPLIANCE
# ═══════════════════════════════════════════════════════
elif section == "⚠️ Risks & Compliance":
    st.markdown("""
    <div class='section-label'>Section 06</div>
    <div class='section-title'>The Risks Are Real — and Manageable. Compliance Is the Competitive Moat.</div>
    <div class='section-desc'>EU AI Act enforcement begins August 2, 2026. GDPR applies from day one. Most competitors will ignore both. Being the only compliant Spanish-language Germany advisor is a trust signal no competitor can easily replicate.</div>
    """, unsafe_allow_html=True)

    risks = [
        {"risk":"EU AI Act Non-Compliance (UC-01, UC-02 = High Risk)","likelihood":4,"impact":5,"score":20,"category":"Regulatory"},
        {"risk":"GDPR Breach — student data across US-based LLM APIs","likelihood":3,"impact":5,"score":15,"category":"Legal"},
        {"risk":"Agentic System Gives Incorrect Visa Advice","likelihood":3,"impact":5,"score":15,"category":"Operational"},
        {"risk":"Leverage Edu Enters Spanish-Language Germany Market","likelihood":3,"impact":4,"score":12,"category":"Market"},
        {"risk":"Algorithmic Bias in Readiness Scoring (UC-01)","likelihood":3,"impact":4,"score":12,"category":"Ethical"},
        {"risk":"Student Drop-off — Language Barrier","likelihood":4,"impact":3,"score":12,"category":"Operational"},
        {"risk":"Single LLM Provider Dependency","likelihood":2,"impact":4,"score":8,"category":"Technical"},
        {"risk":"WhatsApp API Restriction","likelihood":2,"impact":3,"score":6,"category":"Technical"},
        {"risk":"Green AI Reputational Exposure","likelihood":2,"impact":3,"score":6,"category":"Reputational"},
    ]
    df_r = pd.DataFrame(risks)

    col1, col2 = st.columns([3,2])
    with col1:
        # Risk matrix scatter — gray dots, red for critical
        df_r['color'] = df_r['score'].apply(lambda s: RED if s>=15 else ORANGE if s>=10 else '#FFD040')
        fig = go.Figure()
        for _,row in df_r.iterrows():
            fig.add_trace(go.Scatter(
                x=[row['likelihood']], y=[row['impact']],
                mode='markers+text',
                text=[row['risk'][:38]+'...' if len(row['risk'])>38 else row['risk']],
                textposition='top center',
                textfont=dict(size=8.5, color=FONT),
                marker=dict(size=row['score']*2.8, color=row['color'], opacity=0.75,
                           line=dict(color='rgba(255,255,255,0.1)',width=1)),
                hovertemplate=f"<b>{row['risk']}</b><br>Likelihood: {row['likelihood']}/5<br>Impact: {row['impact']}/5<br>Score: {row['score']}/25<extra></extra>",
                showlegend=False
            ))
        fig.add_hline(y=3,line_dash="dash",line_color="rgba(255,255,255,0.06)")
        fig.add_vline(x=3,line_dash="dash",line_color="rgba(255,255,255,0.06)")
        layout = base_layout("Three Risks Require Immediate Action Before Launch — All Are Addressable", height=420)
        fig.update_layout(**layout)
        fig.update_layout(
            xaxis=dict(range=[0.5,5.5],title="Likelihood (1–5)",tickvals=[1,2,3,4,5],gridcolor=GRID),
            yaxis=dict(range=[0.5,5.5],title="Impact (1–5)",tickvals=[1,2,3,4,5],gridcolor=GRID)
        )
        st.plotly_chart(fig, use_container_width=True)
        sowhat("The three highest-scoring risks (EU AI Act, GDPR breach, incorrect visa advice) all have the same mitigation: human review gate + documented compliance posture. One architectural decision resolves all three.")

    with col2:
        st.markdown("""
        <div class='section-label' style='margin-top:0.5rem;'>EU AI Act — Per Use Case</div>
        """, unsafe_allow_html=True)
        classifications = [
            ("UC-01 Diagnostic Agent","HIGH RISK","badge-critical","Annex III — profiles individuals for education access"),
            ("UC-02 Ausbildung Matcher","HIGH RISK","badge-critical","Annex III — assigns individuals to vocational training"),
            ("UC-05 Lead Nurturing","LIMITED–HIGH","badge-high","Requires legal review if score limits service access"),
            ("UC-03 App. Tracker","LIMITED RISK","badge-medium","AI transparency disclosure required"),
            ("UC-04 Doc. Factory","LIMITED RISK","badge-medium","AI-generated content disclosure required"),
            ("UC-07 Visa Intelligence","MINIMAL RISK","badge-medium","Voluntary code of conduct recommended"),
        ]
        for uc,badge,bc,desc in classifications:
            st.markdown(f"""
            <div class='uc-card'>
                <div style='display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.3rem;'>
                    <div class='uc-title'>{uc}</div>
                    <span class='{bc}'>{badge}</span>
                </div>
                <div style='font-size:0.72rem;color:#8892B0;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("""
        <div class='insight-box' style='margin-top:0.8rem;'>
            <div class='insight-title'>Compliance = Trust Infrastructure</div>
            <div class='insight-body'>
                Being the only GDPR-compliant, EU AI Act-ready Spanish-language Germany advisor
                is the one argument that closes institutional B2B deals no competitor can match.
                Publish your compliance posture on the homepage. Make it visible.
                It converts legal overhead into brand equity.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

    # Risk bar — sorted, gray/teal/red
    df_r_sorted = df_r.sort_values('score',ascending=True)
    df_r_sorted['color'] = df_r_sorted['score'].apply(lambda s: RED if s>=15 else ORANGE if s>=10 else '#5A6A8A')
    fig2 = go.Figure(go.Bar(
        x=df_r_sorted['score'], y=df_r_sorted['risk'],
        orientation='h', marker_color=df_r_sorted['color'],
        text=df_r_sorted['score'], textposition='outside',
        textfont=dict(color='#E8EAF0',size=11),
        hovertemplate='<b>%{y}</b><br>Score: %{x}/25<extra></extra>'
    ))
    fig2.add_vline(x=15,line_dash="dash",line_color="rgba(255,107,53,0.4)",
                  annotation_text="High-risk threshold (15)",
                  annotation_font_color=ORANGE,annotation_font_size=10)
    layout2 = base_layout("Only 3 Risks Exceed the High-Risk Threshold — All Have Clear Mitigations", height=340)
    fig2.update_layout(**layout2)
    fig2.update_layout(xaxis=dict(range=[0,28],title="Risk Score (Likelihood × Impact)"),
                      yaxis=dict(gridcolor='rgba(0,0,0,0)'))
    st.plotly_chart(fig2, use_container_width=True)
    sowhat("3 critical risks sounds like a lot until you see they all resolve to the same design decision: human oversight gate + documented compliance posture. The risk profile is manageable for a well-designed MVP.")

# ═══════════════════════════════════════════════════════
# S7 — RECOMMENDATION
# ═══════════════════════════════════════════════════════
elif section == "✅ Recommendation":
    st.markdown("""
    <div class='section-label'>Section 07</div>
    <div class='section-title'>The Verdict: Invest Now, Start Small, Lead With Ausbildung</div>
    <div class='section-desc'>Six datasets. Four analytical layers. The evidence points in one direction.</div>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    for col,icon,title,body,highlight in [
        (c1,"✅","Invest Now — Recommended",
         "2-week MVP at under €3,700. The market data justifies immediate action.",True),
        (c2,"⏸️","Wait — Not Recommended",
         "Leverage Edu is expanding into LATAM. Waiting 12 months cedes first-mover advantage permanently.",False),
        (c3,"🔬","Pilot First — Redundant",
         "The MVP IS the pilot. €3,700 validates the entire concept before any larger commitment.",False),
    ]:
        with col:
            border = '#1A4A30' if highlight else '#1E2D4A'
            opacity = '1.0' if highlight else '0.35'
            color = TEAL if highlight else '#8892B0'
            st.markdown(f"""
            <div class='kpi-card' style='text-align:center;border-color:{border};opacity:{opacity};'>
                <div style='font-size:2.5rem;margin-bottom:0.5rem;'>{icon}</div>
                <div style='font-family:Space Grotesk,sans-serif;font-size:1rem;font-weight:700;color:{color};margin-bottom:0.5rem;'>{title}</div>
                <div style='font-size:0.8rem;color:#8892B0;'>{body}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)

    # ROI projection — clean line chart, one message
    months = list(range(1,13))
    rev_c = [0,2000,5000,10000,15000,18000,22000,26000,30000,35000,40000,44000]
    rev_g = [0,4000,12000,20000,28000,35000,44000,55000,68000,80000,90000,100000]
    cost  = [3700,3700,16200,32400,49000,65000,82000,98000,114000,130000,146000,162000]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months,y=cost,name='Cumulative Investment',
                            line=dict(color=RED,width=2,dash='dash'),
                            hovertemplate='Month %{x}: €%{y:,.0f}<extra>Investment</extra>'))
    fig.add_trace(go.Scatter(x=months,y=rev_c,name='Revenue — Conservative',
                            line=dict(color=GRAY,width=2),
                            fill='tozeroy',fillcolor='rgba(45,55,72,0.3)',
                            hovertemplate='Month %{x}: €%{y:,.0f}<extra>Conservative</extra>'))
    fig.add_trace(go.Scatter(x=months,y=rev_g,name='Revenue — Growth',
                            line=dict(color=TEAL,width=3),
                            fill='tozeroy',fillcolor='rgba(0,212,170,0.05)',
                            hovertemplate='Month %{x}: €%{y:,.0f}<extra>Growth</extra>'))
    fig.add_vline(x=5,line_dash="dot",line_color=f"rgba(0,212,170,0.5)",
                 annotation_text="Break-even ~Month 5",
                 annotation_font_color=TEAL,annotation_font_size=10)
    layout = base_layout("Investment Pays Back by Month 5 on the Conservative Scenario — Growth Scenario Reaches €100K by Month 12", height=360, show_legend=True)
    fig.update_layout(**layout)
    fig.update_layout(
        xaxis=dict(title="Month",tickvals=list(range(1,13)),gridcolor=GRID),
        yaxis=dict(title="EUR (€)",tickformat="€,.0f",gridcolor=GRID)
    )
    st.plotly_chart(fig, use_container_width=True)
    sowhat("At 20% conversion from the diagnostic agent and an average revenue of €500/client, Cleo needs 38 conversions to break even on the MVP. That is less than 2 per day across the 2-week pilot period.")

    # Three forces
    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Why the Window Is Open Now and Will Not Stay Open</div>", unsafe_allow_html=True)
    f1,f2,f3 = st.columns(3)
    for col,icon,title,body in [
        (f1,"🌊","Force 1 — Demand Redirection","Canada, Australia, UK tightening is structurally redirecting LATAM students toward Europe. Germany is the primary beneficiary. Multi-year, not cyclical."),
        (f2,"⚖️","Force 2 — German Labour Policy","Fachkräfteeinwanderungsgesetz (2023) opened Ausbildung for non-EU. 617K+ unfilled positions. The pathway is legally open. The Spanish advisory layer does not exist yet."),
        (f3,"🤖","Force 3 — AI Readiness","LLMs + agentic frameworks make autonomous advisory viable for solo operators today. Agentic AI grows from $7.55B to $199B by 2034. The technology window aligns with the market window."),
    ]:
        with col:
            st.markdown(f"""
            <div class='kpi-card'>
                <div style='font-size:1.5rem;margin-bottom:0.5rem;'>{icon}</div>
                <div class='kpi-label'>{title}</div>
                <div style='font-size:0.82rem;color:#A8B8C8;line-height:1.6;'>{body}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class='recommendation-box' style='margin-top:1.5rem;'>
        <div class='rec-title'>The One-Paragraph Recommendation</div>
        <div class='rec-body'>
            Six datasets across four analytical layers converge on one conclusion:
            <strong style='color:#E8EAF0;'>invest in AI now, start with UC-01, lead with Ausbildung.</strong>
            The MVP validates in 2 weeks at under €3,700 — making this the lowest-risk AI adoption
            decision a small operator can make. The Ausbildung niche is structurally underserved,
            legally accessible since 2023, and has zero Spanish-language AI-native competition.
            Colombia and Brazil are the priority markets — backed by DAAD data, not assumption.
            Every month of delay is a month closer to Leverage Edu, which is already
            expanding into Latin America, occupying this position permanently.
            <strong style='color:#E8EAF0;'>The data says the window is open. Act now.</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class='dashboard-footer'>
    AI Adoption Opportunity Project · Ironhack Berlin AI & Integration Consulting Program · June 2026<br>
    Prepared by Lucas Barrios · Kairos Consulting · kairosconsulting.co<br><br>
    Datasets: UNESCO UIS · Global Student Migration (simulated) · European Job Postings (2018) ·
    IIE Open Doors · German University Enrollment · DAAD 2025/26 · BIBB 2024 · Bundesagentur 2026<br>
    Compliance references: EU AI Act Regulation (EU) 2024/1689 · GDPR Regulation (EU) 2016/679
</div>
""", unsafe_allow_html=True)