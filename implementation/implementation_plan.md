# Implementation Plan
## AI-Powered Germany Pathway Advisory Platform
### AI Adoption Opportunity Project — Ironhack Berlin
**Student:** Lucas Barrios | **Date:** June 2026 | **Version:** 1.0

---

## Overview

This document provides the granular execution plan for delivering the AI Germany Readiness Diagnostic Agent (UC-01) from zero to a live, validated MVP in 14 days, followed by a structured scale path through Month 6. It covers task ownership, tool configuration sequence, dependencies, go-live checklist, and rollback procedures.

---

## 1. Team & Roles

### MVP Phase (Weeks 1–2) — Solo Operator Model

| Role | Owner | Responsibility |
|---|---|---|
| **Consultant / Strategist** | Lucas | Architecture decisions, prompt engineering, content accuracy, compliance layer, stakeholder communication |
| **Full-Stack Developer** | Lucas (AI-assisted via Claude Code / Cursor) | Next.js frontend, Supabase schema, API integrations, n8n workflows |
| **QA / Content Reviewer** | Lucas | Test all student profiles, validate visa and Ausbildung content accuracy |
| **Human Review Consultant** | Lucas (or designated advisor) | Review and approve all diagnostic outputs before delivery during pilot |

### Scale Phase (Month 3+) — Small Team Model

| Role | Type | Responsibility |
|---|---|---|
| **AI Consultant / PM** | Lucas (full-time) | Strategy, client relationships, product decisions, compliance oversight |
| **AI / Backend Developer** | Freelance (3 days/week) | Agent development, RAG pipeline, API integrations, LLM prompt optimisation |
| **Full-Stack Developer** | Freelance (3 days/week) | Frontend features, admin dashboard, B2B portal, performance |
| **Student Success Advisor** | Part-time (Month 4+) | Human review queue, complex case handling, client onboarding |

---

## 2. Technology Stack & Configuration Sequence

### 2.1 Full Stack

| Layer | Tool | Purpose | Configuration Priority |
|---|---|---|---|
| **Frontend** | Next.js 14 (App Router) | Intake form, admin dashboard, student portal | Day 3 |
| **Database** | Supabase (Frankfurt EU region) | Student profiles, scores, roadmaps, leads, audit logs | Day 3 |
| **Authentication** | Supabase Auth | Consultant admin login; optional student account creation | Day 3 |
| **LLM Inference** | Anthropic Claude API (claude-sonnet-4-6) | Readiness score generation, roadmap creation, FAQ responses | Day 5 |
| **RAG / Knowledge Base** | Supabase pgvector + LangChain | German regulatory content: BAMF visa rules, BIBB Ausbildung sectors, Anabin database | Month 2 |
| **Workflow Automation** | n8n Cloud | Intake → LLM → CRM → WhatsApp pipeline | Day 8 |
| **CRM** | HubSpot Free / Starter | Lead management, pipeline tracking, email sequences | Day 9 |
| **Messaging** | WhatsApp Business API (via 360dialog) | Score and roadmap delivery, follow-up sequences | Day 8 |
| **Scheduling** | Calendly | Post-score consultation booking with payment | Day 9 |
| **Hosting** | Vercel | Frontend deployment, serverless API routes | Day 10 |
| **Observability** | LangSmith (Month 2+) | LLM trace logging, prompt performance monitoring, EU AI Act audit trail | Month 2 |
| **Email** | Resend | Transactional emails: score delivery, welcome, follow-up | Day 9 |

### 2.2 Configuration Dependencies

```
Supabase (EU region) must be live BEFORE:
  └── Next.js frontend (needs DB connection string)
  └── n8n workflows (needs Supabase credentials)
  └── Auth setup (needs project reference)

Anthropic API key must be set BEFORE:
  └── LLM integration in Next.js API routes
  └── n8n LLM workflow nodes

WhatsApp Business API account must be approved BEFORE:
  └── Score delivery workflow in n8n
  └── Lead nurturing sequences
  NOTE: Meta approval can take 24–72 hours — apply on Day 1

n8n workflows must be live BEFORE:
  └── End-to-end testing (Day 10)
  └── Pilot launch (Day 11)

HubSpot integration must be live BEFORE:
  └── Pilot launch (Day 11)
  └── Lead scoring and pipeline tracking
```

---

## 3. Phase-by-Phase Execution Plan

---

### Phase 0 — Discovery Validation (Days 1–2)

**Goal:** Lock all inputs before building. No ambiguity enters Week 1.

#### Day 1 Tasks

| Task | Detail | Output | Owner |
|---|---|---|---|
| Apply for WhatsApp Business API | Submit via 360dialog — 24–72hr approval window | API application submitted | Lucas |
| Create 5 synthetic student profiles | Cover: Colombia university, Brazil Ausbildung (IT), Mexico work visa, Chile nursing Ausbildung, Peru language prep | Profile matrix document | Lucas |
| Validate German pathway eligibility criteria | Cross-reference BAMF, Anabin, BIBB, Make it in Germany | Content accuracy checklist | Lucas |
| Draft scoring rubric v1 | Define: which inputs map to which score range and pathway recommendation | Scoring rubric document | Lucas |

#### Day 2 Tasks

| Task | Detail | Output | Owner |
|---|---|---|---|
| Lock diagnostic form fields | Maximum 12 fields: name, email, WhatsApp, country, age, education level, German level, target pathway, target sector (Ausbildung only), budget range, timeline, motivation priority | Final form specification | Lucas |
| Engineer LLM system prompt v1 | Write and test diagnostic prompt against all 5 synthetic profiles | Prompt v1 producing coherent outputs | Lucas |
| Define pilot success metrics | Completion rate, satisfaction, conversion, review time targets | Measurement framework document | Lucas |
| Set up project repository | GitHub repo with folder structure matching brief requirements | Repo live | Lucas |

**Exit gate:** All 5 synthetic profiles produce accurate, pathway-appropriate outputs from Prompt v1. Form fields locked. No scope additions after Day 2.

---

### Phase 1 — MVP Build (Days 3–10)

#### Week 1: Core Platform (Days 3–7)

**Day 3 — Infrastructure Foundation**

| Task | Tool | Detail |
|---|---|---|
| Initialise Supabase project (Frankfurt region) | Supabase | Enable pgvector extension; set up Row Level Security policies |
| Design database schema | Supabase | Tables: `students`, `assessments`, `scores`, `roadmaps`, `leads`, `audit_log` |
| Set up environment variables | Vercel + local `.env` | Supabase URL/key, Anthropic API key, WhatsApp credentials |
| Scaffold Next.js project | Next.js 14 | App Router; Tailwind CSS; Supabase client library; TypeScript |
| GDPR consent layer | Next.js | Privacy notice modal at form start; consent stored in `students` table with timestamp |

**Day 4 — Diagnostic Intake Form**

| Task | Tool | Detail |
|---|---|---|
| Build multi-step intake form | Next.js | 3 steps, 4 fields each; progress indicator; save-and-resume via localStorage |
| Form validation | Next.js (react-hook-form + zod) | Client-side validation before submission |
| Form submission API route | Next.js API + Supabase | POST `/api/assessment` → writes to `students` + `assessments` tables |
| EU AI Act disclosure | Next.js | Clear statement before submission: "This assessment is generated by AI and reviewed by a human consultant before delivery" |
| Mobile-responsive design | Tailwind CSS | Test on 375px (iPhone SE) and 390px (iPhone 14) — primary student device sizes in LATAM |

**Day 5 — LLM Integration**

| Task | Tool | Detail |
|---|---|---|
| Anthropic API integration | Next.js API route | POST `/api/generate-score` → sends structured profile to Claude → returns JSON score object |
| Prompt engineering v2 | Anthropic Claude | Refine system prompt with German regulatory content injected as context; structured JSON output schema |
| Score generation | Claude API | Output: `{ readiness_score: number, pathway: string, score_factors: array, roadmap: array, next_steps: array }` |
| Store score in Supabase | Supabase | Write assessment result to `scores` + `roadmaps` tables |
| Prompt version logging | Supabase `audit_log` | Log prompt version, model used, timestamp per assessment — EU AI Act documentation requirement |

**Day 6 — Admin Dashboard**

| Task | Tool | Detail |
|---|---|---|
| Consultant login | Supabase Auth | Email/password auth; protected dashboard route |
| Submissions queue | Next.js dashboard | List of pending assessments awaiting consultant review |
| Review interface | Next.js | Show student profile + AI-generated score + roadmap; edit fields inline; approve or reject |
| Human oversight gate | Next.js + Supabase | Status field: `pending_review` → `approved` → `delivered`; no WhatsApp send until status = `approved` |
| Basic analytics | Next.js | Count: total submissions, pending review, approved, delivered |

**Day 7 — Compliance Layer & Buffer**

| Task | Tool | Detail |
|---|---|---|
| AI disclosure on all output pages | Next.js | Persistent label: "Generated by AI · Reviewed by a human consultant" |
| GDPR data retention policy implementation | Supabase | Soft delete on student records; 24-month retention default; right to erasure endpoint |
| Explainability card template | Next.js | Score delivery page and WhatsApp message include: top 3 score factors with plain-language explanation |
| Day 7 buffer | — | Fix any blockers from Days 3–6; do not start Day 8 tasks early |

---

#### Week 2: Automation & Delivery (Days 8–10)

**Day 8 — Workflow Automation**

| Task | Tool | Detail |
|---|---|---|
| n8n workflow: intake → LLM trigger | n8n Cloud | Webhook trigger on new Supabase `assessments` row → calls `/api/generate-score` → writes result |
| n8n workflow: approval → WhatsApp delivery | n8n Cloud | Trigger on `status = approved` in Supabase → format message → send via WhatsApp Business API |
| WhatsApp message template | WhatsApp Business API | Template must be pre-approved by Meta; submit on Day 1; format: score summary + 3 key factors + roadmap link + Calendly CTA |
| Error handling | n8n | Failed LLM calls → consultant email alert; failed WhatsApp delivery → fallback to email via Resend |

**Day 9 — CRM & Conversion Flow**

| Task | Tool | Detail |
|---|---|---|
| HubSpot integration | n8n → HubSpot API | On assessment approval: create/update HubSpot contact with score, pathway tag, country, lead status |
| Lead scoring in HubSpot | HubSpot | Score ≥ 70 = Hot lead; 40–69 = Warm; < 40 = Nurture track |
| Calendly integration | Calendly embed + WhatsApp | Post-score WhatsApp message includes Calendly link for paid 60-min strategy consultation |
| Resend transactional email | Resend API | Backup delivery: score summary email sent simultaneously with WhatsApp |
| Email sequence setup | HubSpot / n8n | 3-email nurture sequence for non-converting leads: Day 1 (score reminder), Day 4 (Ausbildung story), Day 10 (deadline urgency) |

**Day 10 — Testing, QA & Deployment**

| Task | Detail | Pass Criteria |
|---|---|---|
| End-to-end test: all 5 synthetic profiles | Run each profile through full flow: form → score → admin review → WhatsApp delivery → CRM log | All 5 complete without errors |
| Content accuracy audit | Expert review of all 5 roadmaps against official German sources | Zero critical errors in visa or eligibility guidance |
| Mobile UX test | Test intake form on Android (Samsung Galaxy A series — most common LATAM device) and iOS | Form completes without layout breaks |
| Load test | Simulate 20 concurrent submissions | No timeout errors |
| GDPR compliance check | Verify: consent stored, audit log writing, deletion endpoint working | All three pass |
| Deploy to production | Vercel deployment; Supabase production project; environment variables set | Platform live on production URL |

---

### Phase 2 — Pilot (Days 11–14)

**Goal:** 10–20 real students. Real feedback. Conversion data.

#### Pilot Recruitment

| Channel | Target | Detail |
|---|---|---|
| LinkedIn outreach | Colombia + Brazil focus | Post in DAAD alumni groups, German-LATAM student communities |
| WhatsApp groups | Brazil and Colombia student networks | Direct outreach via personal and professional network |
| Reddit | r/germany, r/AskAGerman, r/brasil | Post offering free AI Germany assessment for Latin American students |
| Personal network | Lucas's contacts | 5 guaranteed beta testers from consulting and Ironhack network |

#### Pilot Operations

| Day | Task |
|---|---|
| Day 11 | Onboard first 5 beta students; consultant reviews each score personally |
| Day 12 | Onboard next 5–10 students; identify any prompt or UX issues |
| Day 13 | Fix critical issues identified in Days 11–12; send post-assessment surveys |
| Day 14 | Final 5 students; compile all feedback; calculate pilot metrics |

#### Pilot Measurement Framework

| Metric | Target | Measurement |
|---|---|---|
| Form completion rate | ≥ 60% | Started vs completed in Supabase |
| Score delivery time | < 5 min post-approval | n8n timestamp delta |
| Consultant review time | ≤ 30 min/student | Manual log |
| Student satisfaction | ≥ 70% useful | Post-delivery 5-question survey |
| Consultation conversion | ≥ 20% | Calendly bookings / pilot participants |
| Critical content errors | 0 | Manual content audit |

---

### Phase 3 — Evaluate & Decide (Week 3)

**Go decision:** All 6 pilot metrics hit → proceed to Phase 4 scale plan
**Iterate decision:** 4–5 metrics hit → identify root cause, fix, re-run 10-student mini-pilot
**Pivot decision:** Fewer than 4 metrics hit → return to Phase 0 with revised assumptions

---

### Phase 4 — Scale Rollout (Month 2–6)

| Month | Use Case Activated | Key Milestone |
|---|---|---|
| Month 2 | UC-03 Agentic Application Tracker | 50 paying clients; LangSmith observability live |
| Month 2 | RAG pipeline for regulatory content | BAMF + BIBB + Anabin knowledge base indexed |
| Month 3 | UC-04 Document Factory (CV + Motivationsschreiben) | First German-format documents generated and delivered |
| Month 3 | UC-05 Lead Nurturing Agent (full automation) | WhatsApp sequences running without human involvement |
| Month 4 | UC-02 Ausbildung Position Matcher | Live vacancy data from Bundesagentur für Arbeit integrated |
| Month 5 | UC-07 Visa & Regulatory Intelligence Agent | BAMF monitoring active; student alerts on regulation changes |
| Month 5 | EU AI Act formal registration | High-risk systems registered in EU database (mandatory August 2026) |
| Month 6 | B2B institutional outreach begins | First partnership proposals to Colombian and Brazilian universities |
| Month 6 | LangSmith audit trail reviewed | Quarterly bias audit completed; first AI Sustainability Report published |

---

## 4. Go-Live Checklist

Before the platform accepts real student data, every item below must be confirmed:

### Legal & Compliance
- [ ] Privacy Policy published on website (GDPR Art. 13/14)
- [ ] GDPR consent captured and stored at intake with timestamp
- [ ] AI disclosure present on form and all output pages (EU AI Act transparency)
- [ ] Human review gate active — no automated delivery without `status = approved`
- [ ] Data Processing Agreements signed: Anthropic, 360dialog (WhatsApp), HubSpot
- [ ] Supabase project confirmed on Frankfurt (EU) region
- [ ] Right-to-erasure endpoint tested and working
- [ ] EU AI Act risk classification documented (UC-01 = High Risk)

### Technical
- [ ] All environment variables set in Vercel production
- [ ] Supabase Row Level Security policies active
- [ ] End-to-end flow tested on production URL (not staging)
- [ ] WhatsApp message template approved by Meta
- [ ] n8n error handling active (failed LLM → consultant alert)
- [ ] Backup email delivery (Resend) confirmed working
- [ ] Database backups enabled in Supabase

### Content
- [ ] All visa and Ausbildung content validated against official sources
- [ ] Scoring rubric reviewed by consultant familiar with German admissions
- [ ] Prompt v2 tested on minimum 5 diverse student profiles
- [ ] Disclaimer on all outputs: "Informational only — not legal or immigration advice"
- [ ] Calendly consultation page live with clear service description and pricing

### Operational
- [ ] Consultant review queue monitored at least twice daily during pilot
- [ ] Pilot feedback survey ready (Typeform or Google Forms)
- [ ] Error logging monitored (Vercel logs + n8n execution history)
- [ ] Rollback plan documented (see Section 5)

---

## 5. Rollback & Contingency Plan

| Scenario | Trigger | Response |
|---|---|---|
| LLM produces critically incorrect visa information | Content error identified in pilot review | Suspend automated generation; revert to manual consultant drafting with AI assist only; audit and fix prompt before re-enabling |
| WhatsApp API delivery fails | >20% delivery failure rate | Switch to email-only delivery via Resend; maintain WhatsApp as secondary channel |
| Supabase outage | Platform unavailable >30 min | Redirect form to a Typeform backup; consultant processes manually; restore from last backup |
| GDPR complaint received | Student requests erasure or data access | Execute right-to-erasure endpoint within 72 hours; document response; notify DPA if breach confirmed |
| Pilot conversion rate <10% | Below go-no-go threshold | Pause paid advertising; iterate on score presentation and CTA copy; re-run 10-student mini-pilot before Phase 4 |

---

## 6. Dependencies & External Blockers

| Dependency | Risk Level | Mitigation |
|---|---|---|
| WhatsApp Business API approval (24–72hr) | 🟠 High — blocks Day 8 delivery workflow | Apply Day 1; have email-only delivery as fallback for Days 11–14 if not approved |
| Meta WhatsApp message template approval | 🟠 High — template must be approved before sending | Submit template on Day 1 alongside API application; prepare 2 template variants |
| Anthropic API rate limits | 🟡 Medium — low risk at pilot volume | Monitor usage in Anthropic dashboard; upgrade tier if needed |
| German regulatory content accuracy | 🟡 Medium — content errors damage trust | Validate all content before Day 5 LLM integration; link to official sources in roadmap |
| Beta student recruitment (10–20 in 4 days) | 🟡 Medium — pilot requires real users | Begin recruitment outreach on Day 10 (before pilot launch); use personal network as guaranteed baseline |

---

## 7. Methodology & Assumptions

**Development methodology:** Agile sprint model compressed to daily cycles. No formal sprint ceremonies — daily 15-minute self-review against task list. Scope locked after Phase 0 to prevent feature creep.

**AI-assisted development:** Claude Code, Cursor, and GitHub Copilot are used throughout development. These tools are estimated to reduce solo development time by 40–60% on boilerplate tasks (schema generation, form validation, API routes), freeing Lucas to focus on prompt engineering, compliance architecture, and content accuracy — the tasks where human judgment is irreplaceable.

**Scope boundary:** MVP scope is intentionally minimal. Features not in the Day 3–10 build list — language coaching, Ausbildung vacancy matching, document generation, alumni network — are explicitly out of scope for the MVP. They are Phase 4 items. Scope additions after Day 2 are not permitted without adding days to the timeline.

---

*This implementation plan was prepared as part of the AI Adoption Opportunity Project — Ironhack Berlin AI & Integration Consulting Program, June 2026. It does not constitute legal or financial advice. All tool pricing and API specifications are accurate as of June 2026 and subject to change.*
