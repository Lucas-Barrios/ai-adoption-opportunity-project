# Timeline Estimate
## AI-Powered Germany Pathway Advisory Platform
### AI Adoption Opportunity Project — Ironhack Berlin
**Student:** Lucas Barrios | **Date:** June 2026 | **Version:** 1.0

---

## Overview

This document provides timeline estimates across two horizons:

- **Horizon 1 — MVP Sprint (14 Days):** Day-by-day delivery plan for the solo operator build
- **Horizon 2 — Platform Roadmap (12 Months):** Milestone-based scale plan from validated MVP to full platform

All timelines account for a 1–10 person small business context, AI-assisted development tooling, and the EU AI Act compliance requirements embedded in the build.

---

## 1. Timeline Assumptions

| Assumption | Detail |
|---|---|
| **Development model** | Solo operator (Lucas) using AI-assisted tooling (Claude Code, Cursor, GitHub Copilot) — estimated 40% time compression on boilerplate tasks vs manual development |
| **Working hours** | 8–9 productive hours/day during 2-week sprint |
| **Scope discipline** | Feature scope locked after Day 2 Phase 0 — no additions accepted until Phase 4 |
| **External dependencies** | WhatsApp Business API approval (24–72hr) applied for on Day 1; does not block frontend/backend build but blocks delivery workflow on Day 8 |
| **Buffer allocation** | Day 7 and Day 14 designated as explicit buffer days — not filled with new tasks |
| **Scale phase** | Assumes Go decision from Phase 3 evaluation; timelines activate from Month 2 post-pilot |

---

## 2. Horizon 1 — MVP Sprint (14 Days)

```
WEEK 1                                          WEEK 2
──────────────────────────────────────────────────────────────────────────
Day 1    Day 2    Day 3    Day 4    Day 5    Day 6    Day 7
PHASE 0           PHASE 1 — CORE BUILD
Discovery Validation    │ Infrastructure │  Form  │  LLM  │ Admin │ Buffer/
                        │ + Schema       │        │       │ Dash  │ Compliance
──────────────────────────────────────────────────────────────────────────
Day 8    Day 9    Day 10   Day 11   Day 12   Day 13   Day 14
PHASE 1 — AUTOMATION    │ PHASE 2 — PILOT              │ Buffer/
n8n + WhatsApp│CRM+Conv. │ QA + Deploy│ Beta 1–5│Beta 6–15│ Fix   │ Compile
──────────────────────────────────────────────────────────────────────────
```

### Day-by-Day Timeline

| Day | Phase | Primary Deliverable | Completed When |
|---|---|---|---|
| **Day 1** | Phase 0 | WhatsApp API applied; 5 synthetic profiles created; eligibility criteria validated | API application submitted; profiles documented |
| **Day 2** | Phase 0 | Form fields locked; scoring rubric v1; LLM prompt v1 tested on all 5 profiles | All 5 profiles produce coherent, accurate outputs |
| **Day 3** | Phase 1 | Supabase schema live (EU); Next.js scaffolded; GDPR consent layer built | Database accepting test writes; form renders in browser |
| **Day 4** | Phase 1 | Multi-step intake form live on staging; validation working; mobile-responsive | Form submits without errors on mobile and desktop |
| **Day 5** | Phase 1 | Anthropic API integrated; score + roadmap generated from form submission | JSON score object returned correctly for all 5 test profiles |
| **Day 6** | Phase 1 | Admin dashboard live; consultant review queue; approve/reject workflow | Consultant can log in, view submissions, approve scores |
| **Day 7** | Phase 1 | EU AI Act disclosures live; GDPR data retention implemented; buffer for blockers | All compliance elements present; no critical blockers carry into Week 2 |
| **Day 8** | Phase 1 | n8n pipeline live: intake → LLM → Supabase → consultant alert | Full automated pipeline runs end-to-end in test environment |
| **Day 8** | Phase 1 | WhatsApp delivery workflow live (if API approved) or email fallback | Score delivered via WhatsApp or email post-consultant-approval |
| **Day 9** | Phase 1 | HubSpot integration live; Calendly embedded; email nurture sequence set up | Lead created in HubSpot on every approval; Calendly link in delivery message |
| **Day 10** | Phase 1 | End-to-end QA on all 5 profiles; production deploy; go-live checklist signed off | Platform live on production URL; all checklist items confirmed |
| **Day 11** | Phase 2 | First 5 beta students onboarded; consultant reviews each score personally | 5 students receive roadmaps; no critical errors |
| **Day 12** | Phase 2 | Next 5–10 beta students; identify and fix any UX or content issues | Running error log; fixes deployed same day |
| **Day 13** | Phase 2 | Post-assessment surveys sent to Day 11–12 cohort; fixes from Day 12 verified | Survey responses beginning to arrive |
| **Day 14** | Phase 2 | Final 5 students; pilot metrics compiled; Go/Iterate/Pivot decision documented | All 6 pilot metrics calculated; Phase 3 recommendation written |

---

### Critical Path

The following tasks are on the critical path — a delay in any of them delays the final go-live:

```
Day 1: WhatsApp API application
   ↓
Day 2: Scoring logic + prompt locked (nothing builds correctly without this)
   ↓
Day 3: Supabase schema (everything reads/writes from here)
   ↓
Day 5: LLM integration (score generation is the core product)
   ↓
Day 6: Admin dashboard (human review gate — required for EU AI Act compliance)
   ↓
Day 8: n8n pipeline (connects all components)
   ↓
Day 10: Production deploy
   ↓
Day 11: Pilot launch
```

---

### Risk Buffer Analysis

| Risk | Probability | Days Lost | Mitigation |
|---|---|---|---|
| WhatsApp API not approved by Day 8 | Medium | 0 (email fallback covers pilot) | Apply Day 1; use Resend email delivery during pilot if needed |
| LLM prompt produces inaccurate outputs on Day 5 | Low | 1–2 days | Day 7 buffer absorbs this; content audit built into Day 2 |
| Supabase schema redesign required mid-build | Low | 1 day | Schema validated with all use cases before Day 3 — not just UC-01 |
| WhatsApp template rejected by Meta | Medium | 1–2 days | Submit 2 template variants on Day 1; email covers gap |

**Conclusion:** The 14-day timeline is achievable with current assumptions. The two buffer days (Day 7, Day 14) absorb the most likely blockers. The only scenario that breaks the timeline is a fundamental error in the scoring logic not caught until Day 5 or later — which is why Day 2 (Phase 0 exit gate) is the most important day in the sprint.

---

## 3. Horizon 2 — Platform Roadmap (12 Months)

### 3.1 Monthly Milestone Overview

| Month | Phase | Key Deliverables | Team Size |
|---|---|---|---|
| **Month 1** | MVP + Pilot | UC-01 live; 20 beta students; Go decision | 1 (Lucas) |
| **Month 2** | Early Scale | UC-03 live; 50 paying clients; LangSmith observability; RAG pipeline started | 1–2 |
| **Month 3** | Product Expansion | UC-04 Document Factory; UC-05 Lead Nurturing Agent; HubSpot Starter; 100 clients | 2–3 |
| **Month 4** | AI Depth | UC-02 Ausbildung Matcher (RAG + live vacancy data); Student Success Advisor hired | 3–4 |
| **Month 5** | Compliance + Intelligence | UC-07 Visa Intelligence Agent; EU AI Act formal registration; DPIA completed | 3–4 |
| **Month 6** | B2B + Sustainability | First institutional partnership outreach; AI Sustainability Report published; 200 clients | 3–4 |
| **Month 7–9** | Optimisation | Bias audit completed; prompt optimisation; smaller model evaluation; B2B pilots | 4–5 |
| **Month 10–12** | Platform Maturity | UC-08 Integration Concierge; PWA capability; institutional contracts signed; 400+ clients | 4–5 |

---

### 3.2 Detailed Quarterly Breakdown

#### Q1 (Months 1–3) — Validate, Launch, Expand

```
Month 1: VALIDATE
├── Week 1–2: MVP Build (see Horizon 1)
├── Week 3: Pilot evaluation + Go/Iterate/Pivot decision
└── Week 4: Marketing launch (Colombia + Brazil) — LinkedIn, WhatsApp groups, DAAD communities

Month 2: LAUNCH
├── UC-03 Agentic Application Tracker development (2 weeks)
├── RAG pipeline architecture designed (BAMF + BIBB content indexed)
├── LangSmith integration for EU AI Act audit trail
├── Target: 50 paying clients by end of Month 2
└── Freelance backend developer onboarded (part-time, 3 days/week)

Month 3: EXPAND
├── UC-04 Document Factory development (2 weeks)
├── UC-05 Lead Nurturing Agent (WhatsApp sequences automated)
├── HubSpot Starter upgrade (contact limit reached on free tier)
├── Target: 100 paying clients
└── First revenue milestone: €15,000–€25,000 MRR
```

---

#### Q2 (Months 4–6) — Deepen, Comply, Partner

```
Month 4: AI DEPTH
├── UC-02 Ausbildung Position Matcher (most complex UC — 4 weeks)
│   ├── Week 1–2: Bundesagentur für Arbeit API integration
│   ├── Week 3: Matching algorithm + student profile cross-reference
│   └── Week 4: QA + bias testing across 5 country profiles
├── Student Success Advisor hired (handles review queue + complex cases)
└── Target: 150 paying clients

Month 5: COMPLIANCE
├── UC-07 Visa & Regulatory Intelligence Agent
│   ├── BAMF + German embassy monitoring setup
│   └── Student alert workflow via WhatsApp + email
├── EU AI Act: High-risk system registration in EU database (mandatory August 2026)
├── DPIA completion for UC-01 and UC-02
├── Quarterly bias audit (first formal run)
└── Target: 175 paying clients

Month 6: PARTNER
├── UC-09 B2B institutional partnership outreach begins
│   ├── Prospect list: 10 Colombian universities + 5 Brazilian universities
│   └── Partnership proposal deck prepared
├── AI Sustainability Report v1 published
├── Full-stack frontend developer onboarded (part-time, 3 days/week)
└── Target: 200 paying clients; €35,000–€45,000 MRR
```

---

#### Q3–Q4 (Months 7–12) — Optimise, Partner, Scale

```
Month 7–9: OPTIMISATION
├── LLM cost optimisation: evaluate Mistral/smaller model for standard queries
├── Prompt performance analysis via LangSmith (identify lowest-accuracy query types)
├── A/B test: score presentation formats (numerical vs descriptive vs visual)
├── First B2B institutional pilots activated
└── Target: 250–300 paying clients

Month 10–12: PLATFORM MATURITY
├── UC-08 Post-Arrival Integration Concierge (Anmeldung, Krankenkasse, housing)
├── PWA capability added to Next.js platform (app-like mobile experience)
├── Alumni network module launched (AI matching for peer mentorship)
├── First institutional contracts signed (B2B revenue stream activated)
├── Second annual bias audit
└── Target: 400+ paying clients; €60,000–€80,000 MRR
```

---

### 3.3 Visual Timeline Summary

```
MONTH:  1      2      3      4      5      6      7-9    10-12
        ───────────────────────────────────────────────────────
UC-01   ██████ ─────────────────────────────────────────────── Live
UC-03          ██████ ──────────────────────────────────────── Live
UC-04                 ██████ ─────────────────────────────────  Live
UC-05                 ██████ ─────────────────────────────────  Live
UC-02                        ████████ ────────────────────────  Live
UC-07                               ██████ ──────────────────── Live
UC-08                                             ████████────  Live
PWA                                               ████████────  Live
B2B                                      ─────────────────────  Ongoing

TEAM:   1      2      3      4      4      4      5      5
CLIENTS: 20   50     100    150    175    200  250-300  400+
MRR:    <5K  15-25K 25-35K 30-40K 35-45K 45K+ 55-65K  70-80K
        (€)
```

---

## 4. Compliance Timeline

Given that the EU AI Act reaches full enforcement on **August 2, 2026**, the following compliance milestones are non-negotiable:

| Deadline | Requirement | Status |
|---|---|---|
| **Before launch (Month 1)** | AI disclosure on all interfaces | To do |
| **Before launch (Month 1)** | GDPR consent layer + Privacy Policy | To do |
| **Before launch (Month 1)** | DPAs signed with all processors | To do |
| **Before launch (Month 1)** | UC-01 High-Risk classification documented | To do |
| **Month 2** | DPIA initiated for UC-01 and UC-02 | To do |
| **Month 5** | DPIA completed | To do |
| **Before August 2, 2026** | High-risk systems registered in EU database | To do |
| **Month 6** | First AI Sustainability Report published | To do |
| **Quarterly** | Bias audit and LLM performance review | Recurring |
| **Annual** | DPIA review and update | Recurring |

---

## 5. Dependencies & External Constraints

| Dependency | Impact on Timeline | Owner |
|---|---|---|
| WhatsApp API approval (24–72hr) | Delays Day 8 delivery workflow if not approved | Apply Day 1 |
| EU AI Act enforcement (August 2, 2026) | Platform must be compliant before this date regardless of development stage | Lucas (compliance lead) |
| Bundesagentur für Arbeit API access (UC-02) | Required for Ausbildung Matcher — apply in Month 3 | Backend developer |
| Beta student recruitment | Pilot cannot start without 10+ students committed | Begin outreach Day 10 |
| Freelance developer onboarding | Month 2 delivery depends on developer available at Month 2 start | Begin recruitment during pilot phase |
| B2B institutional sales cycle | 12–24 months typical for university partnerships | Begin outreach Month 6; first deals expected Month 12–18 |

---

*This timeline was prepared as part of the AI Adoption Opportunity Project — Ironhack Berlin AI & Integration Consulting Program, June 2026. All estimates are based on current assumptions and subject to revision following Phase 3 pilot evaluation. The 14-day MVP timeline is the highest-confidence estimate in this document; the 12-month roadmap is directional and contingent on Phase 3 Go decision.*
