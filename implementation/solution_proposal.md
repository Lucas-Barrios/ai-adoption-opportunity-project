# Solution Proposal
## AI-Powered Germany Pathway Advisory Platform
### AI Adoption Opportunity Project — Ironhack Berlin
**Student:** Lucas Barrios | **Date:** June 2026 | **Version:** 1.0

---

## Executive Summary

This proposal recommends that Cleo invest in a focused, phased AI adoption strategy built around one primary use case: an **AI Germany Readiness Diagnostic Agent** (UC-01) — an intelligent intake and personalisation system that profiles Spanish-speaking Latin American students, scores their Germany readiness, and delivers a personalised pathway roadmap autonomously, with human consultant review before delivery.

The investment case is straightforward: Cleo's business cannot scale on consultant hours alone. The Latin American → Germany advisory market is growing at 6% annually, Ausbildung vacancies exceed 600,000 unfilled positions, and no Spanish-language competitor has deployed AI in this niche. The window is open. The technology is ready. The risk of waiting exceeds the risk of investing.

The proposed MVP can be validated in **2 weeks at under €5,000** — making this one of the lowest-risk AI adoption decisions a small operator can make. The question Cleo needs to answer before committing to a full team build is not *"should we do this?"* It is *"does this convert students?"* — and that question costs €5,000 to answer, not €150,000.

---

## 1. The Problem Being Solved

### 1.1 Cleo's Operational Constraint

Cleo's current model is time-for-money. Every client requires:
- 2–3 hours of discovery and intake
- 1–2 hours of document review and roadmap preparation
- Ongoing follow-up and application tracking

At 10 clients per month, that is 30–50 hours of non-scalable labour. At 50 clients, it requires a team. At 200 clients — the volume needed to make an international strategy profitable — it requires an operation Cleo cannot fund from early-stage revenue.

**AI adoption is not optional for this business model to work internationally. It is structural.**

### 1.2 The Student's Problem

Spanish-speaking Latin American students face a system that is:
- Documented almost entirely in German
- Structurally complex (Anabin, APS, ZAB, Goethe certificates, Ausbildung applications, visa categories)
- Overwhelming without a trusted guide
- Expensive to navigate through traditional consultants charging €150+/hour

The first moment of value Cleo can deliver — before any paid engagement — is clarity. A student who understands their current position, what their realistic pathway is, and what the next 6 months look like is a student who trusts Cleo. That clarity is what UC-01 delivers, at scale, in under 5 minutes.

---

## 2. Recommended Solution

### 2.1 Primary Recommendation — UC-01: AI Germany Readiness Diagnostic Agent

**What it is:**
An intelligent, conversational intake system that collects student profile data and autonomously generates:
- A **Germany Readiness Score** (0–100) with factor-level explainability
- A **recommended pathway** (university / Ausbildung / work visa / language preparation)
- A **personalised month-by-month roadmap** for the next 6–12 months
- A **next steps summary** with specific actions, resources, and estimated timelines

**What it is not:**
It is not a replacement for the consultant. It is the first 3 hours of every engagement, automated. The consultant enters at the review and strategy stage — the highest-value interaction — not the data collection stage.

**How it works end-to-end:**

```
Student lands on platform
        ↓
Completes diagnostic intake form (10–12 fields, ~4 minutes)
        ↓
LLM processes profile against German eligibility criteria,
Ausbildung sector demand data, visa requirements, language thresholds
        ↓
Generates: Readiness Score + Pathway Recommendation + Roadmap
        ↓
Human consultant reviews output (target: <30 min per student)
EU AI Act Article 14 compliance: no automated delivery without human review
        ↓
Score and roadmap delivered to student via email + WhatsApp
        ↓
Student invited to book paid strategy consultation (Calendly)
        ↓
Lead logged in CRM with score, pathway, and engagement data
```

**Why this use case first:**
Every other use case depends on it. The Ausbildung matcher (UC-02) needs the student profile. The application tracker (UC-03) needs the target programme. The document factory (UC-04) needs the roadmap. UC-01 is the foundation — build it right and every subsequent use case plugs into it.

---

### 2.2 Secondary Recommendation — UC-03: Agentic Application & Deadline Tracker

To be activated in Phase 3 (post-pilot validation). The application tracker extends the value of UC-01 through the full client lifecycle — from roadmap delivery to application submission. It monitors deadlines, chases missing documents via WhatsApp, and updates a shared status dashboard without manual follow-up by the consultant.

This is the use case that allows Cleo to manage 200+ active cases simultaneously without dropping a single deadline.

---

### 2.3 Build vs Buy vs Configure Decision

| Component | Decision | Rationale |
|---|---|---|
| **Frontend (intake form + dashboard)** | Build | Next.js — already in Cleo's tech orbit; full control over UX and data flows |
| **Database & auth** | Configure (Supabase) | Fastest path to production; EU region for GDPR compliance; real-time capabilities |
| **LLM inference** | Configure (Anthropic Claude API) | Best-in-class reasoning for structured advisory output; EU AI Act GPAI transparency requirements met |
| **Workflow automation** | Configure (n8n) | Connects intake → LLM → CRM → WhatsApp without custom code; self-hostable for data residency |
| **WhatsApp delivery** | Configure (WhatsApp Business API via 360dialog or Twilio) | Fastest to market; handles LATAM timezone 24/7 delivery |
| **CRM** | Configure (HubSpot Starter) | Lead scoring, pipeline, and DPA available; integrates with n8n |
| **Scheduling** | Configure (Calendly) | Zero development time; handles payment integration for premium sessions |
| **Hosting** | Configure (Vercel + Supabase EU) | Both already in stack; EU data residency solves GDPR transfer risk |

**Stack summary:** Next.js + Supabase (EU) + Anthropic API + n8n + WhatsApp Business API + HubSpot Starter + Vercel + Calendly

**Total monthly infrastructure cost at MVP scale:** €95–€175/month
**Total monthly infrastructure cost at 1,000+ sessions:** €490–€990/month

---

## 3. Implementation Phases

---

### Phase 0 — Discovery Validation (Days 1–2)
**Objective:** Confirm assumptions before writing a single line of code.

| Task | Owner | Output |
|---|---|---|
| Map 5 realistic Latin American student profiles across different pathways | Consultant | Profile matrix document |
| Validate German eligibility criteria against official sources (BAMF, Anabin, BIBB) | Consultant | Content accuracy checklist |
| Define diagnostic form fields (locked, no scope creep after Day 2) | Consultant | Final form specification |
| Define scoring logic — what inputs map to which pathway and score range | Consultant | Scoring rubric v1 |
| Draft LLM system prompt for diagnostic agent | Consultant | Prompt v1 |
| Set pilot success metrics | Consultant | Measurement framework |

**Exit criteria:** Form fields locked. Scoring logic documented. Content validated. Prompt tested on 5 profiles producing coherent, accurate outputs.

**Risk at this phase:** Scoring logic is under-specified → builds wrong thing → wastes Week 1. Do not skip this phase to save time.

---

### Phase 1 — MVP Build (Days 3–10)

#### Week 1 Sprint (Days 3–7) — Core Platform

| Day | Task | Output |
|---|---|---|
| Day 3 | Supabase schema: students, scores, roadmaps, leads tables | Database live |
| Day 3 | GDPR consent layer at intake: privacy notice, processing disclosure | Compliance foundation |
| Day 4 | Diagnostic intake form (Next.js) — 10–12 fields, mobile-responsive | Form live on staging URL |
| Day 5 | LLM integration: Anthropic API → readiness score + pathway + roadmap generation | Score generation working |
| Day 6 | Admin dashboard: consultant view of submissions, review interface, approve/edit/send | Consultant workflow live |
| Day 7 | EU AI Act compliance layer: AI disclosure on form, human review gate before delivery | Compliance layer live |

#### Week 2 Sprint (Days 8–10) — Automation & Delivery

| Day | Task | Output |
|---|---|---|
| Day 8 | n8n workflow: form submission → LLM → Supabase → consultant notification | Automated pipeline live |
| Day 8 | WhatsApp Business API: score and roadmap delivery after consultant approval | WhatsApp delivery working |
| Day 9 | HubSpot integration: lead logging with score, pathway tag, and engagement status | CRM pipeline live |
| Day 9 | Calendly integration: post-score CTA linking to paid strategy consultation booking | Conversion flow live |
| Day 10 | End-to-end testing across 5 student profiles | QA sign-off |
| Day 10 | Deploy to production (Vercel + Supabase EU) | Platform live |

**Exit criteria:** A student submits the form, receives a score and roadmap via WhatsApp within 5 minutes of consultant approval, and can book a follow-up consultation directly from the message. Zero critical errors on visa or eligibility information.

---

### Phase 2 — Pilot (Days 11–14)
**Objective:** Real students, real feedback, real conversion data.

| Task | Detail |
|---|---|
| Recruit 10–20 beta students | Colombia and Brazil priority; via LinkedIn, university groups, DAAD community channels |
| Consultant reviews every score | No automated delivery without human sign-off during pilot |
| Structured feedback collection | 5-question post-roadmap survey: accuracy, clarity, usefulness, trust, next step intent |
| Track all pilot metrics | Completion rate, time-to-score, review time, conversion to consultation |
| Daily iteration | Fix errors and improve prompt within 24 hours of identification |

**Exit criteria:** Proceed to Phase 3 if:
- Diagnostic completion rate ≥ 60%
- Student satisfaction ≥ 70% find roadmap useful
- Consultant review time ≤ 30 minutes per student
- Conversion to follow-up consultation ≥ 20%

---

### Phase 3 — Evaluate & Scale Decision (Week 3+)
**Objective:** Data-driven go/no-go on full platform investment.

**Three decision paths:**

| Outcome | Signal | Action |
|---|---|---|
| ✅ **Go** | Pilot metrics hit; students converting; consultant time reduced >50% | Activate UC-03 (Application Tracker); begin Scenario B team planning; launch Colombia + Brazil marketing |
| ⚠️ **Iterate** | Product works but conversion below target | Adjust messaging, pricing, or CTA before scaling; re-run pilot with changes |
| ❌ **Pivot** | Fundamental assumption wrong (students don't trust AI scores, wrong pathway focus) | Redesign diagnostic logic; consider manual-first with AI-assist model before full automation |

---

### Phase 4 — Full Platform Rollout (Month 2–6)
**Activated only after Phase 3 Go decision.**

| Month | Milestone |
|---|---|
| Month 2 | UC-03 Agentic Application Tracker live; first 50 paying clients |
| Month 3 | UC-04 Document Factory live (CV, Motivationsschreiben); upsell to existing clients |
| Month 3 | UC-05 Lead Nurturing Agent live; WhatsApp sequences automated end-to-end |
| Month 4 | UC-02 Ausbildung Position Matcher live; BIBB vacancy data integrated via RAG |
| Month 5 | UC-07 Visa & Regulatory Intelligence Agent live; BAMF monitoring active |
| Month 6 | First B2B institutional partnership outreach (Colombian and Brazilian universities) |

---

## 4. Cost Analysis

### 4.1 Scenario A — Solo Operator MVP (2-Week Sprint)

| Item | Type | Cost |
|---|---|---|
| Consultant time (Lucas) — 10 days × €350/day | One-time | €3,500 |
| Anthropic API (testing + 200 pilot sessions) | One-time | €50–€150 |
| Supabase Free tier | Monthly | €0 |
| Vercel Hobby tier | Monthly | €0 |
| WhatsApp Business API (first 1,000 conversations free via Meta) | Monthly | €0 |
| n8n Cloud Starter | Monthly | €20 |
| HubSpot Free CRM | Monthly | €0 |
| Calendly Free tier | Monthly | €0 |
| Domain + professional email (if not existing) | One-time | €30 |
| **Total MVP Investment** | | **€3,600–€3,700** |
| **First month operational cost** | | **€20–€50/month** |

**ROI breakeven:** 4–5 paid consultations at €800 each. The MVP pays for itself before the end of Week 3 if the pilot converts.

---

### 4.2 Scenario B — Small Team Build (Month 3–12, Post-Validation)

#### People Costs

| Role | Engagement Type | Monthly Cost |
|---|---|---|
| AI / Backend Developer | Freelance, part-time (3 days/week) | €3,000–€4,500 |
| Full-Stack Frontend Developer | Freelance, part-time (3 days/week) | €2,500–€4,000 |
| Lucas (Consultant / PM / Strategist) | Full-time equivalent | €4,000–€6,000 |
| **People Subtotal** | | **€9,500–€14,500/month** |

*Note: Freelance rates based on Berlin market for experienced developers. Reduced to part-time because AI-assisted development (Claude Code, Cursor) compresses delivery time significantly — a 3-day/week developer with AI tooling delivers what previously required 5 days.*

#### Infrastructure Costs (At Scale)

| Item | Monthly Cost |
|---|---|
| Supabase Pro (EU region) | €25 |
| Vercel Pro | €20 |
| Anthropic API (1,000–5,000 sessions) | €200–€500 |
| WhatsApp Business API (scaled volume) | €100–€300 |
| n8n Cloud (production) | €50 |
| HubSpot Starter CRM | €45 |
| LangSmith / observability | €50 |
| Domain + email (Google Workspace) | €12 |
| **Infrastructure Subtotal** | | **€502–€1,002/month** |

| **Scenario B Total** | **€10,002–€15,502/month** |
|---|---|

#### Break-Even Analysis (Scenario B)

| Revenue Model | Clients Needed to Break Even |
|---|---|
| Productized service avg €500/client | 20–32 clients/month |
| Subscription avg €99/month | 101–157 active subscribers |
| Mixed (70% productized + 30% subscription) | ~18 clients + 40 subscribers |

**At 50 clients/month (achievable by Month 6 with AI-driven lead nurturing), Scenario B generates €25,000/month revenue against €10,000–€15,500 costs — a sustainable operating margin of 38–60%.**

---

### 4.3 Total Investment Summary

| Phase | Timeframe | Investment | Risk Level |
|---|---|---|---|
| Phase 0–2 (MVP + Pilot) | Weeks 1–2 | €3,600–€3,700 | Very Low |
| Phase 3 (Evaluation) | Week 3 | €0 (analysis only) | None |
| Phase 4 (Full Rollout) | Month 2–6 | €10,000–€15,500/month | Medium |
| Phase 4 (Infrastructure) | Month 2–6 | €500–€1,000/month | Low |

---

## 5. Success Metrics

### Phase 2 Pilot Metrics (Go/No-Go Gates)

| Metric | Target | Measurement Method |
|---|---|---|
| Diagnostic completion rate | ≥ 60% | Supabase analytics: started vs completed forms |
| Score delivery time | < 5 minutes post-approval | n8n workflow timestamp |
| Consultant review time per student | ≤ 30 minutes | Manual consultant log during pilot |
| Student satisfaction (roadmap useful) | ≥ 70% | Post-delivery survey (5 questions) |
| Conversion to paid consultation | ≥ 20% | Calendly bookings / pilot participants |
| Zero critical errors in visa guidance | 100% accuracy | Manual audit of all 20 pilot outputs |

### Phase 4 Scale Metrics (Month 6 Targets)

| Metric | Target |
|---|---|
| Monthly active students on platform | 200+ |
| Paying clients per month | 50+ |
| Monthly recurring revenue | €25,000+ |
| Consultant time per client (hours) | < 1 hour (vs 4–5 hours manual) |
| Lead-to-consultation conversion rate | ≥ 25% |
| Net Promoter Score | ≥ 50 |

---

## 6. Risk & Assumptions

### Key Assumptions

| Assumption | Basis | Validation Method |
|---|---|---|
| Latin American students will trust an AI readiness score | Industry evidence: 92% of students use AI tools (HEPI, 2025); Leverage Edu and ApplyBoard have validated AI intake at scale | Pilot feedback survey |
| WhatsApp is the right delivery channel | WhatsApp penetration in Colombia and Brazil exceeds 95% (Meta, 2024) | Pilot channel preference question |
| Consultant review takes ≤ 30 min per student | Assumption based on structured output format reducing review to validation, not creation | Measured during pilot |
| LLM accuracy on German visa and Ausbildung content is sufficient | Anthropic Claude performs well on structured regulatory content with RAG augmentation | Content accuracy audit during Phase 0 |
| 20% conversion from free diagnostic to paid consultation | Conservative estimate; comparable EdTech platforms report 15–35% free-to-paid conversion | Measured in pilot |

### Key Risks and Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| EU AI Act High-Risk classification requires compliance overhead | High | Human review gate (already planned) + DPIA before launch covers core obligations |
| LLM produces incorrect visa or eligibility information | Medium | RAG index from official BAMF/BIBB sources + human review gate + informational disclaimer on all outputs |
| Students abandon long intake form | Medium | Progressive disclosure UX: show 3 fields at a time, not 12; save progress; estimated completion time shown |
| Leverage Edu enters Spanish-language Germany market | Medium | 12-month head start + authentic German residency expertise + placed alumni network creates switching cost they cannot buy |
| WhatsApp API delays or restrictions | Low | Email as parallel delivery channel; both collected at intake |

---

## 7. Why Invest Now — The Strategic Window Argument

Three forces are converging simultaneously that create a market entry window which will not exist in 36 months:

**Force 1 — Demand redirection:** Canada, Australia, and UK policy tightening is structurally redirecting Latin American students toward Europe. This is not a trend — it is a multi-year shift. Germany is the primary beneficiary. The students are looking for guidance right now.

**Force 2 — German labour policy:** The Fachkräfteeinwanderungsgesetz (2023) opened Ausbildung visas for non-EU applicants at exactly the moment Germany faces 600,000+ unfilled positions. The regulatory infrastructure for this pathway exists. The advisory infrastructure in Spanish does not.

**Force 3 — AI technology readiness:** LLMs are now capable of producing accurate, personalised, multi-step advisory content. Agentic frameworks enable autonomous document tracking and lead nurturing without a large engineering team. The technology that makes this model viable at small-business scale did not exist 24 months ago.

**The window closes when:** A well-funded competitor (Leverage Edu is already moving into LATAM) occupies the Spanish-language Germany niche with AI-native tooling. At that point, Cleo competes on brand and relationships — harder to build than a technical advantage from a standing start.

**The investment case in one sentence:** €3,700 now to validate a market that the data says is real, before a competitor with €10M in venture funding does it for you.

---

## 8. Methodology & Sources

This proposal is grounded in the accompanying market research (`market_research.md`) and opportunity/risk analysis (`opportunities_risks.md`). All market sizing figures are sourced from publicly available reports including DAAD Wissenschaft Weltoffen 2025, QS Global Student Flows Latin America 2024, BIBB Annual Vocational Training Report 2024, Bundesagentur für Arbeit 2025, and multiple third-party market intelligence sources. Cost estimates are based on current published pricing for all named tools and services as of June 2026. Consultant day rates reflect Berlin freelance market benchmarks. All EU AI Act compliance assessments reference Regulation (EU) 2024/1689 and its associated Annexes directly.

This proposal was prepared for educational purposes as part of the Ironhack Berlin AI & Integration Consulting Program, June 2026. It does not constitute legal or financial advice.

---

*Next document: `implementation_plan.md` — detailed phase breakdown with task owners, tool configuration steps, dependencies, and go-live checklist.*
