# Use Case Discovery & AI Adoption Recommendation
## AI Adoption Opportunity Project — Ironhack Berlin
**Student:** Lucas Barrios | **Date:** June 2026

---

## 1. Business Context

**Cleo's Company:** Small digital-first education consulting firm (1–10 employees, fully remote)
**Core Service:** Guiding Spanish-speaking Latin Americans through university admissions, Ausbildung (German vocational training), and skilled work visa pathways into Germany
**Strategic Driver:** Cleo has decided to pursue an international strategy as the primary path to profitability — the domestic market alone is too small to sustain the business

---

## 2. Stakeholder & Problem Framing

**Primary Stakeholder:** Cleo — CEO, non-technical, skeptical of AI hype, focused on ROI and scalability
**End Users:** Spanish-speaking students and young professionals aged 18–32 from Colombia, Brazil, Mexico, Chile, and Peru

**Core Pain Points (Cleo's side):**
- Consulting hours are the bottleneck — revenue caps when time caps
- Lead qualification is manual and inefficient
- Document preparation is repetitive and time-consuming
- No scalable way to serve hundreds of clients simultaneously across time zones
- Ausbildung pathway is virtually unguided in Spanish — massive opportunity with no playbook

**Core Pain Points (Student side):**
- The German system (Anabin, APS, ZAB, Goethe certificates, Ausbildung applications) is opaque and overwhelming in Spanish
- Visa processes are long, document-heavy, and anxiety-inducing
- No trusted, affordable, Spanish-language resource specifically for Germany pathways
- Post-arrival integration (Anmeldung, Krankenkasse, housing, banking) is equally confusing

---

## 3. Competitive Landscape

| Company | What They Do | Gap |
|---|---|---|
| **Livin-France** | Student relocation platform for France (visa, housing, insurance) | Not AI-driven, France only, no Ausbildung |
| **Leverage Edu** | AI-powered study abroad platform, India-focused | No Spanish, no Germany Ausbildung specialization |
| **ApplyBoard / Abbie** | AI advisor for university applications globally | English-first, university only, no vocational |
| **Study Metro** | AI university matchmaker and SOP generator | Generic, no country specialization |
| **Ambitio** | AI study abroad copilot | University-focused, English-first |

**White Space:** No competitor is combining (1) Spanish-language delivery, (2) Germany-specific expertise, (3) Ausbildung as a primary pathway, and (4) agentic AI automation. This is Cleo's moat.

---

## 4. Scoring Framework

Each use case is rated across 5 dimensions on a 1–5 scale:

| Dimension | What It Measures |
|---|---|
| **Business Impact** | Revenue potential, scalability, direct contribution to Cleo's growth |
| **Differentiation** | How unique this is in the market — hard to replicate quickly |
| **AI Fit** | How well agentic, generative, or other AI technologies apply |
| **Feasibility** | Can a small team (1–5 people) realistically execute this |
| **Time to Value** | How quickly this generates measurable results after implementation |

**Maximum score: 25**
**Priority tiers:** 🔴 Critical (20–25) | 🟠 High (15–19) | 🟡 Medium (10–14) | 🟢 Exploratory (below 10)

---

## 5. Use Case Proposals

---

### UC-01 — AI Germany Readiness Diagnostic Agent
**AI Type:** Agentic AI + Generative AI
**Description:**
An intelligent intake agent that collects student profile data (education, language level, budget, goals, timeline) through a conversational interface and autonomously generates a personalized Germany Readiness Score (0–100), a recommended pathway (university / Ausbildung / work visa), and a month-by-month roadmap — without human involvement.

**How it works:** Student completes a structured form or chat-based intake → agent scores profile against admission/visa eligibility criteria → LLM generates a personalized roadmap document → delivered instantly via email/WhatsApp

**Why it matters:** Replaces the first 2–3 hours of manual discovery work per client. Scales to unlimited simultaneous leads. Becomes the lead magnet that drives all other conversions.

| Dimension | Score |
|---|---|
| Business Impact | 5 |
| Differentiation | 4 |
| AI Fit | 5 |
| Feasibility | 5 |
| Time to Value | 5 |
| **TOTAL** | **24 / 25** 🔴 |

---

### UC-02 — Agentic Ausbildung Position Matcher
**AI Type:** Agentic AI + RAG (Retrieval-Augmented Generation)
**Description:**
An autonomous agent that continuously scrapes and indexes live Ausbildung vacancies from German job portals (Bundesagentur für Arbeit, Make it in Germany, Ausbildung.de), matches them against student profiles in the CRM, and proactively notifies students of compatible open positions — including a pre-filled application draft.

**How it works:** Agent monitors job boards on a schedule → cross-references vacancy requirements (sector, language level, location) against student profiles → ranks matches by fit score → sends personalized match alerts with application support

**Why it matters:** No competitor offers this for Spanish-speaking applicants. Ausbildung has 270,000+ unfilled positions annually. This turns a passive advisory service into an active placement engine — a fundamentally different and more valuable product.

| Dimension | Score |
|---|---|
| Business Impact | 5 |
| Differentiation | 5 |
| AI Fit | 5 |
| Feasibility | 3 |
| Time to Value | 4 |
| **TOTAL** | **22 / 25** 🔴 |

---

### UC-03 — Agentic Application & Deadline Tracker
**AI Type:** Agentic AI
**Description:**
An autonomous pipeline agent that manages the entire application lifecycle for each student — tracking submission deadlines, chasing missing documents via WhatsApp/email, updating application status, and escalating to a human consultant only when a decision or exception is required.

**How it works:** Student profile and target programs loaded into agent → agent monitors deadlines via calendar logic → sends automated reminders and document requests → updates a shared status dashboard → flags exceptions for human review

**Why it matters:** A single consultant currently manages this manually for each client. This agent allows one person to manage 200+ active cases simultaneously without dropping the ball on any.

| Dimension | Score |
|---|---|
| Business Impact | 5 |
| Differentiation | 4 |
| AI Fit | 5 |
| Feasibility | 4 |
| Time to Value | 5 |
| **TOTAL** | **23 / 25** 🔴 |

---

### UC-04 — AI German Document Factory
**AI Type:** Generative AI
**Description:**
An automated document generation system that produces German-format professional documents tailored to each student's profile: DIN 5008-compliant CVs, personalized Motivationsschreiben, Ausbildung application letters, university admission essays, and APS preparation checklists — in German and Spanish.

**How it works:** Student inputs profile data → GenAI generates draft documents using German formatting standards and sector-specific language → consultant reviews and approves → delivered to student within minutes

**Why it matters:** Document preparation currently takes 3–5 hours per client. This compresses it to under 30 minutes of review time. High perceived value for students, minimal effort for the business.

| Dimension | Score |
|---|---|
| Business Impact | 4 |
| Differentiation | 3 |
| AI Fit | 5 |
| Feasibility | 5 |
| Time to Value | 5 |
| **TOTAL** | **22 / 25** 🔴 |

---

### UC-05 — Agentic Lead Nurturing & Qualification System
**AI Type:** Agentic AI + Generative AI
**Description:**
An autonomous multi-channel lead nurturing agent that scores inbound leads, segments them by pathway (university / Ausbildung / work), sends personalized follow-up sequences via WhatsApp and email, answers FAQs, and routes only conversion-ready or high-complexity leads to Cleo's calendar — without manual intervention.

**How it works:** Lead submits diagnostic form → agent scores and tags lead → triggers personalized nurture sequence → monitors engagement → escalates to human when lead signals intent to buy or asks a question outside the agent's scope

**Why it matters:** Most small consulting businesses lose 60–70% of leads due to slow follow-up. This agent responds instantly, 24/7, in Spanish — across all time zones in Latin America.

| Dimension | Score |
|---|---|
| Business Impact | 5 |
| Differentiation | 3 |
| AI Fit | 5 |
| Feasibility | 4 |
| Time to Value | 5 |
| **TOTAL** | **22 / 25** 🔴 |

---

### UC-06 — German Language Readiness AI Coach
**AI Type:** Generative AI + Conversational AI
**Description:**
A personalized AI language coach embedded in the platform that prepares students for the specific German language requirements of their chosen pathway — Goethe-Zertifikat (B1/B2) for Ausbildung, TestDaF for university, or basic A1 for work visas — with adaptive exercises, vocabulary sets, and mock exam simulations in Spanish.

**How it works:** Student's target pathway determines required German level → AI coach delivers bite-sized daily lessons, tracks progress, simulates exam conditions, and adjusts difficulty dynamically → integrates with roadmap milestones

**Why it matters:** Language is the #1 dropout reason for international students in Germany according to DAAD. Solving this within the platform creates stickiness, increases completion rates, and adds a recurring subscription revenue layer.

| Dimension | Score |
|---|---|
| Business Impact | 4 |
| Differentiation | 4 |
| AI Fit | 4 |
| Feasibility | 3 |
| Time to Value | 3 |
| **TOTAL** | **18 / 25** 🟠 |

---

### UC-07 — Visa & Regulatory Intelligence Agent
**AI Type:** Agentic AI + RAG
**Description:**
An autonomous monitoring agent that tracks changes to German visa regulations, Ausbildung eligibility requirements, APS procedures, and Fachkräfteeinwanderungsgesetz updates — and proactively notifies affected students and updates their roadmaps in real time.

**How it works:** Agent monitors official sources (BAMF, Bundesagentur, Make it in Germany, German embassy websites) on a scheduled basis → detects regulatory changes → cross-references active student profiles → sends personalized impact alerts → updates affected roadmap steps

**Why it matters:** Visa policy changes have derailed thousands of students internationally (Canada 2024 being the most recent example). Being the first to notify and guide students through changes is a massive trust and retention driver.

| Dimension | Score |
|---|---|
| Business Impact | 4 |
| Differentiation | 5 |
| AI Fit | 5 |
| Feasibility | 3 |
| Time to Value | 3 |
| **TOTAL** | **20 / 25** 🔴 |

---

### UC-08 — Post-Arrival Integration Concierge Agent
**AI Type:** Agentic AI + Generative AI
**Description:**
An autonomous post-arrival support agent that guides students through the German bureaucratic integration process after landing: Anmeldung (city registration), Krankenkasse (health insurance) enrollment, bank account opening, housing search, and local orientation — all in Spanish, step-by-step.

**How it works:** Student triggers the post-arrival flow upon landing → agent delivers city-specific checklists and instructions → sends appointment reminders → answers questions about forms and procedures → connects student to relevant service providers

**Why it matters:** Competitors stop at visa approval. Cleo's service continues after arrival, dramatically increasing lifetime value per client, generating referrals, and creating a natural upsell pathway.

| Dimension | Score |
|---|---|
| Business Impact | 4 |
| Differentiation | 5 |
| AI Fit | 4 |
| Feasibility | 4 |
| Time to Value | 3 |
| **TOTAL** | **20 / 25** 🔴 |

---

### UC-09 — B2B White-Label Platform for Latin American Universities
**AI Type:** Generative AI + Agentic AI (platform layer)
**Description:**
Package the diagnostic agent, roadmap generator, and application tracker as a white-label SaaS product licensed to Latin American universities, NGOs, and career centers — allowing them to offer Germany pathway advisory to their students under their own brand, powered by Cleo's platform and expertise.

**How it works:** Partner institution signs a platform license (€200–€500/month) → their students access the branded diagnostic tool → Cleo's AI handles the advisory layer → complex cases escalate to Cleo's human team for a revenue share

**Why it matters:** One institutional deal replaces hundreds of individual student sales. This is the path from consulting business to scalable SaaS — the highest-ceiling business model in the stack.

| Dimension | Score |
|---|---|
| Business Impact | 5 |
| Differentiation | 5 |
| AI Fit | 4 |
| Feasibility | 2 |
| Time to Value | 2 |
| **TOTAL** | **18 / 25** 🟠 |

---

### UC-10 — Alumni Intelligence & Peer Mentorship Network
**AI Type:** Generative AI + AI Matching
**Description:**
An AI-powered matching system that connects newly onboarded students with alumni who completed the same pathway (same country of origin, same Ausbildung sector or university field, same destination city in Germany) — enabling structured peer mentorship, social proof generation, and community-driven retention.

**How it works:** New student profile created → AI matches against alumni database by pathway, origin, sector, and city → match request sent → structured mentorship flow initiated (first call agenda generated by AI) → alumni share testimonials that feed the marketing engine

**Why it matters:** Peer trust is the most powerful conversion driver in education. A verified alumni network is nearly impossible to replicate quickly and becomes more valuable with every placement — a true compounding moat.

| Dimension | Score |
|---|---|
| Business Impact | 3 |
| Differentiation | 5 |
| AI Fit | 3 |
| Feasibility | 3 |
| Time to Value | 2 |
| **TOTAL** | **16 / 25** 🟠 |

---

## 6. Priority Summary

| Rank | Use Case | Score | Priority | AI Type |
|---|---|---|---|---|
| 1 | UC-01 Germany Readiness Diagnostic Agent | 24/25 | 🔴 Critical | Agentic + GenAI |
| 2 | UC-03 Agentic Application & Deadline Tracker | 23/25 | 🔴 Critical | Agentic AI |
| 3 | UC-02 Agentic Ausbildung Position Matcher | 22/25 | 🔴 Critical | Agentic + RAG |
| 4 | UC-04 AI German Document Factory | 22/25 | 🔴 Critical | Generative AI |
| 5 | UC-05 Agentic Lead Nurturing System | 22/25 | 🔴 Critical | Agentic + GenAI |
| 6 | UC-07 Visa & Regulatory Intelligence Agent | 20/25 | 🔴 Critical | Agentic + RAG |
| 7 | UC-08 Post-Arrival Integration Concierge | 20/25 | 🔴 Critical | Agentic + GenAI |
| 8 | UC-06 German Language Readiness Coach | 18/25 | 🟠 High | GenAI + Conversational |
| 9 | UC-09 B2B White-Label Platform | 18/25 | 🟠 High | Agentic + GenAI |
| 10 | UC-10 Alumni Intelligence Network | 16/25 | 🟠 High | GenAI + AI Matching |

---

## 7. Recommended Primary Use Case for This Project

**UC-01 — AI Germany Readiness Diagnostic Agent** is the recommended primary use case for the following reasons:

- Highest combined score (24/25)
- Directly addresses Cleo's core constraint: scaling advisory without scaling headcount
- Serves as the foundation on which all other use cases are built — no other UC works without knowing the student profile
- Technically achievable for a small operator using current LLM APIs and no-code/low-code tooling
- Generates immediate, measurable business value: reduced intake time, improved lead qualification, faster time-to-first-consultation

**Secondary recommendation:** UC-03 (Agentic Application Tracker) as the first expansion, since it extends the value of UC-01 throughout the client lifecycle.

---

## 8. Sources & References

- DAAD Country Statistics: daad.de/en/the-daad/what-we-do/facts-figures/daad-country-statistics/
- Wissenschaft Weltoffen 2025 Report: wissenschaft-weltoffen.de
- BIBB Annual Vocational Training Report 2024: bibb.de/en
- Destatis Foreign Qualification Recognition 2024: destatis.de
- ICEF Monitor — Germany International Student Statistics 2024/25
- QS Global Student Flows Latin America 2024
- Bundesagentur für Arbeit — Ausbildung Vacancy Statistics 2024
- Fachkräfteeinwanderungsgesetz Amendment 2023 — BAMF
- Leverage Edu / TechCrunch — AI Study Abroad Platform Analysis, October 2025
- ApplyBoard — Abbie AI Advisor Launch, June 2024
- Livin-France — Competitor Reference: livin-france.com/fr
