# Cost Analysis
## AI-Powered Germany Pathway Advisory Platform
### AI Adoption Opportunity Project — Ironhack Berlin
**Student:** Lucas Barrios | **Date:** June 2026 | **Version:** 1.0

---

## Overview

This document provides a full cost breakdown across all proposed use cases, two deployment scenarios (MVP solo operator and small team scale), and a return on investment projection. All figures reflect current market pricing as of June 2026. Tool costs are based on published pricing tiers. Consultant and developer rates reflect Berlin freelance market benchmarks.

---

## 1. Cost Framework

Costs are organised across four categories:

| Category | Description |
|---|---|
| **People** | Consultant, developer, and advisory time |
| **Infrastructure** | Hosting, database, deployment, monitoring |
| **AI & APIs** | LLM inference, WhatsApp, communication tools |
| **Tooling & SaaS** | CRM, scheduling, automation, analytics |

Two scenarios are costed in parallel:

- **Scenario A — MVP (Solo Operator, 2-Week Sprint):** Minimum viable investment to validate the concept
- **Scenario B — Scale (Small Team, Month 3–12):** Post-validation investment for full platform build

---

## 2. Scenario A — MVP Cost Breakdown

### 2.1 People Costs

| Role | Days | Day Rate | Total |
|---|---|---|---|
| AI Consultant / Developer (Lucas) | 10 days | €350 | €3,500 |
| **People Total** | | | **€3,500** |

*Note: €350/day reflects a conservative rate for a Berlin-based AI consultant with full-stack development capability. Market range for this profile is €300–€500/day. Using lower end for MVP given early-stage context.*

---

### 2.2 Infrastructure Costs (Month 1)

| Tool | Tier | Monthly Cost | Notes |
|---|---|---|---|
| Supabase | Free | €0 | 500MB database, 2GB bandwidth — sufficient for pilot |
| Vercel | Hobby | €0 | Unlimited deployments, 100GB bandwidth |
| GitHub | Free | €0 | Private repos included |
| **Infrastructure Total** | | **€0/month** | |

---

### 2.3 AI & API Costs (MVP Period)

| Service | Usage Estimate | Unit Cost | Total |
|---|---|---|---|
| Anthropic Claude API (Sonnet) | 200 assessments × ~2,000 tokens input + ~1,500 tokens output | ~€0.003–€0.015 per assessment | €0.60–€3.00 |
| WhatsApp Business API (360dialog) | First 1,000 conversations (within 24hr window) | Free (Meta policy) | €0 |
| Resend (email) | 3,000 emails/month | Free tier | €0 |
| **AI & API Total** | | | **€0.60–€3.00** |

*Note: Anthropic API costs at pilot scale (200 sessions) are negligible — under €3. This figure becomes significant only above 5,000 monthly sessions.*

---

### 2.4 Tooling & SaaS Costs (Month 1)

| Tool | Tier | Monthly Cost | Notes |
|---|---|---|---|
| n8n Cloud | Starter | €20 | 2,500 workflow executions/month — sufficient for pilot |
| HubSpot CRM | Free | €0 | Contact management, pipeline, basic email |
| Calendly | Free | €0 | 1 event type, unlimited bookings |
| 360dialog (WhatsApp) | Starter | €0 first month | Free trial period; €49/month after |
| Domain + email (if new) | One-time | €30 | .com domain + Namecheap email forwarding |
| **Tooling Total** | | **€20–€50/month** | |

---

### 2.5 Scenario A Total

| Category | One-Time | Monthly (Month 1) |
|---|---|---|
| People | €3,500 | — |
| Infrastructure | — | €0 |
| AI & APIs | €0.60–€3.00 | ~€5–€15 (ongoing) |
| Tooling & SaaS | €30 (domain) | €20–€50 |
| **TOTAL** | **€3,530–€3,533** | **€25–€65/month** |

**All-in MVP investment: €3,555–€3,598**

---

## 3. Scenario B — Small Team Scale Cost Breakdown

*Activated after Phase 3 Go decision. Applies from Month 3 onward.*

### 3.1 People Costs (Monthly)

| Role | Engagement | Days/Week | Day Rate | Monthly Cost |
|---|---|---|---|---|
| AI Consultant / PM (Lucas) | Full-time equivalent | 5 | €350 | €7,000 |
| AI / Backend Developer | Freelance | 3 | €400 | €4,800 |
| Full-Stack Frontend Developer | Freelance | 3 | €350 | €4,200 |
| Student Success Advisor (Month 4+) | Part-time | 3 | €180 | €2,160 |
| **People Total (Month 3)** | | | | **€16,000/month** |
| **People Total (Month 4+)** | | | | **€18,160/month** |

*Note: Developer rates reflect experienced Berlin freelance market. AI-assisted development (Claude Code, Cursor) reduces effective cost by compressing delivery time — a 3-day/week freelancer with AI tooling delivers what previously required 5 days, making part-time engagement viable.*

---

### 3.2 Infrastructure Costs (Monthly, At Scale)

| Tool | Tier | Monthly Cost | Notes |
|---|---|---|---|
| Supabase | Pro (EU Frankfurt) | €25 | 8GB database, 250GB bandwidth, PITR backups |
| Vercel | Pro | €20 | Team features, advanced analytics, SLAs |
| **Infrastructure Total** | | **€45/month** | |

---

### 3.3 AI & API Costs (Monthly, At Scale)

| Service | Usage Estimate | Monthly Cost |
|---|---|---|
| Anthropic Claude API | 2,000–5,000 assessments + agent runs | €200–€500 |
| WhatsApp Business API (360dialog) | 5,000–20,000 conversations | €100–€300 |
| Resend (email) | 50,000 emails/month | €20 |
| LangSmith (observability) | Pro tier | €50 |
| **AI & API Total** | | **€370–€870/month** |

---

### 3.4 Tooling & SaaS Costs (Monthly, At Scale)

| Tool | Tier | Monthly Cost | Notes |
|---|---|---|---|
| n8n Cloud | Pro | €50 | Unlimited executions, custom variables |
| HubSpot | Starter | €45 | Marketing Hub + CRM, 1,000 contacts |
| Calendly | Standard | €12 | Multiple event types, payment integration |
| Google Workspace | Business Starter | €12 | Professional email, Drive, Meet |
| Figma | Professional | €15 | UI design for ongoing feature development |
| **Tooling Total** | | **€134/month** | |

---

### 3.5 Scenario B Total (Monthly, Month 3–6)

| Category | Monthly Cost (Month 3) | Monthly Cost (Month 4+) |
|---|---|---|
| People | €16,000 | €18,160 |
| Infrastructure | €45 | €45 |
| AI & APIs | €370–€870 | €370–€870 |
| Tooling & SaaS | €134 | €134 |
| **TOTAL** | **€16,549–€17,049** | **€18,709–€19,209** |

---

## 4. Cost Per Use Case

### 4.1 UC-01 — AI Germany Readiness Diagnostic Agent

| Cost Element | MVP | At Scale (1,000 sessions/month) |
|---|---|---|
| Development (one-time) | €2,100 (6 days) | — |
| LLM inference per session | €0.003–€0.015 | €3–€15/month total |
| Storage per student record | ~0.001MB | Negligible |
| Human review time | 30 min × consultant rate | €175/month (10 clients) → €875/month (50 clients) |
| **Total UC-01 (MVP)** | **€2,100** | — |
| **Total UC-01 (Scale, 1,000/month)** | — | **€200–€900/month** |

---

### 4.2 UC-03 — Agentic Application & Deadline Tracker

| Cost Element | Development (One-Time) | Monthly Operational |
|---|---|---|
| n8n workflow development | €700 (2 days) | Included in n8n Pro tier |
| Supabase schema extension | €350 (1 day) | Included in Supabase Pro |
| WhatsApp message templates (3 new) | €175 (0.5 day) | €0.05–€0.15 per message |
| QA and testing | €350 (1 day) | — |
| **Total UC-03** | **€1,575** | **€50–€150/month** |

---

### 4.3 UC-04 — AI Document Factory

| Cost Element | Development (One-Time) | Per Document |
|---|---|---|
| Prompt engineering (CV + Motivationsschreiben templates) | €700 (2 days) | — |
| Frontend upload/preview interface | €1,050 (3 days) | — |
| LLM inference per document set | — | €0.05–€0.20 |
| Storage per document | — | ~0.5MB per student |
| **Total UC-04** | **€1,750** | **€0.05–€0.20/document** |

*Revenue model: Document Factory sold as premium add-on at €49–€99 per student. At €0.20 cost per document set and €79 average selling price, gross margin is 99.7%.*

---

### 4.4 UC-02 — Agentic Ausbildung Position Matcher

| Cost Element | Development (One-Time) | Monthly Operational |
|---|---|---|
| RAG pipeline: Bundesagentur vacancy data ingestion | €1,400 (4 days) | €50 (re-indexing) |
| Matching algorithm + scoring | €1,050 (3 days) | Included in API costs |
| Supabase pgvector setup and indexing | €350 (1 day) | Included in Supabase Pro |
| LangSmith trace integration | €350 (1 day) | €50/month |
| Weekly vacancy data refresh automation | €700 (2 days) | €20/month (n8n) |
| **Total UC-02** | **€3,850** | **€120/month** |

*Most technically complex UC. Recommended for Month 4 — after platform stability is confirmed.*

---

### 4.5 UC-05 — Agentic Lead Nurturing System

| Cost Element | Development (One-Time) | Monthly Operational |
|---|---|---|
| HubSpot sequence setup (3 tracks) | €350 (1 day) | Included in HubSpot Starter |
| n8n lead scoring workflow | €350 (1 day) | Included in n8n Pro |
| WhatsApp sequence templates (6 messages) | €350 (1 day) | €0.05/message |
| A/B testing setup | €175 (0.5 day) | — |
| **Total UC-05** | **€1,225** | **€100–€300/month** |

---

### 4.6 Full Use Case Cost Summary

| Use Case | Development Cost | Monthly Operational | Priority |
|---|---|---|---|
| UC-01 Diagnostic Agent | €2,100 | €200–€900 | 🔴 MVP |
| UC-03 Application Tracker | €1,575 | €50–€150 | 🔴 Month 2 |
| UC-04 Document Factory | €1,750 | Negligible | 🟠 Month 3 |
| UC-05 Lead Nurturing Agent | €1,225 | €100–€300 | 🟠 Month 3 |
| UC-02 Ausbildung Matcher | €3,850 | €120 | 🟠 Month 4 |
| UC-07 Visa Intelligence Agent | €2,100 | €50 | 🟡 Month 5 |
| UC-08 Integration Concierge | €1,400 | €30–€100 | 🟡 Month 5 |
| **Platform Total (All UCs)** | **€14,000** | **€550–€1,620/month** | |

*Development costs calculated at €350/day consultant rate. Infrastructure and tooling SaaS costs excluded from per-UC figures (covered in Scenario B total).*

---

## 5. Revenue Projections & ROI

### 5.1 Revenue Model

| Tier | Price | Volume Target (Month 6) | Monthly Revenue |
|---|---|---|---|
| Free diagnostic | €0 | 500 sessions | €0 (lead generation) |
| Consultoría Básica (strategy session) | €99 | 80 clients | €7,920 |
| Programa Estudiar en Alemania | €499 | 30 clients | €14,970 |
| Programa Ausbildung | €699 | 15 clients | €10,485 |
| Programa Premium Integral | €1,500 | 5 clients | €7,500 |
| Document add-on | €79 | 40 clients | €3,160 |
| **Total MRR (Month 6 target)** | | | **€44,035** |

---

### 5.2 ROI Analysis

#### MVP ROI (2-Week Sprint)

| Metric | Figure |
|---|---|
| Total MVP investment | €3,555–€3,598 |
| Revenue to break even | 4 × €99 consultations = **€396** — covers API/tooling |
| Full MVP cost recovery | 5 × €699 Ausbildung programmes = **€3,495** |
| Break-even timeline | **Week 3–4 post-launch** (if pilot converts at 20%) |

#### 12-Month ROI Projection

| Period | Investment | Revenue | Net |
|---|---|---|---|
| Month 1–2 (MVP + Pilot) | €3,600 | €2,000–€5,000 (pilot clients) | -€1,600 to +€1,400 |
| Month 3–6 (Scale) | €66,000–€76,000 | €80,000–€150,000 | **+€14,000–€74,000** |
| Month 7–12 (Optimised) | €90,000–€115,000 | €200,000–€320,000 | **+€110,000–€205,000** |

**Projected 12-month ROI: 180–420%** depending on conversion rate and scale of B2B institutional partnerships.

---

### 5.3 The Opportunity Cost Argument

Without AI adoption, Cleo handles intake manually:

| Metric | Manual Model | AI Model |
|---|---|---|
| Clients per month (solo) | 10–15 max | 100–200+ |
| Hours per client | 4–5 hours | <1 hour (review only) |
| Revenue cap (solo) | €7,000–€10,500/month | €44,000+/month |
| Revenue ceiling | Hard cap at consultant hours | Removed by AI automation |

**The AI investment does not add a feature. It removes the revenue ceiling.**

---

## 6. Assumptions & Methodology

- All developer/consultant rates based on Berlin freelance market, June 2026
- Anthropic Claude API pricing based on published claude-sonnet-4-6 rates (input: €3/MTok, output: €15/MTok)
- WhatsApp Business API pricing based on Meta's published per-conversation rates for European accounts
- SaaS tool pricing based on published pricing pages as of June 2026; subject to change
- Revenue projections assume 20% free-to-paid conversion rate (conservative; EdTech benchmark 15–35%)
- Developer efficiency assumes 40% time compression from AI-assisted development tools
- All figures in EUR; no currency conversion applied

---

*This cost analysis was prepared as part of the AI Adoption Opportunity Project — Ironhack Berlin AI & Integration Consulting Program, June 2026. Figures are estimates for planning purposes and do not constitute a binding financial commitment. Actual costs may vary based on usage, tool pricing changes, and team composition.*
