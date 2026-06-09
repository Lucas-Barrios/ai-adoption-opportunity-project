# Opportunity & Risk Analysis
## AI Adoption Opportunity Project — Ironhack Berlin
**Student:** Lucas Barrios | **Date:** June 2026 | **Version:** 1.0

---

## Executive Summary

This document provides a structured analysis of the opportunities and risks associated with deploying an AI-powered education advisory platform for Spanish-speaking Latin Americans pursuing German university, Ausbildung, and work visa pathways. The analysis is organised across six layers: market opportunity mapping, operational risk register, EU AI Act compliance classification, GDPR data protection assessment, Green AI sustainability evaluation, and algorithmic fairness review. A concluding section reframes compliance not as a legal burden but as a strategic trust architecture — the primary differentiator in a market where students hand over passports, documents, and life decisions to a service provider.

---

## 1. Opportunity Map

Each opportunity is scored across three dimensions on a 1–5 scale:

| Dimension | What It Measures |
|---|---|
| **Market Pull** | Evidence-backed demand signal — how strong is the external case? |
| **Strategic Fit** | Alignment with Cleo's positioning, language capability, and niche |
| **AI Leverage** | How much AI amplifies the value relative to a manual approach |

**Maximum score: 15**

---

### O-01 — Ausbildung Advisory for Latin America
**Signal:** 270,000–617,000 unfilled German vocational positions annually; zero Spanish-language competitors in this niche; BIBB projects shortages intensifying through 2030

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 5 | 5 | 5 | **15 / 15** 🔴 |

**Why now:** The Fachkräfteeinwanderungsgesetz (2023) opened non-EU Ausbildung visas. The market has regulatory access but no advisory infrastructure in Spanish. This is a white space that exists today and will not exist in 36 months.

---

### O-02 — AI-Powered Intake & Personalisation at Scale
**Signal:** Study abroad consulting market growing at 9–10% CAGR; AI in education at 31% CAGR; agentic AI at 43.84% CAGR — the technology window and market window align

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 5 | 5 | 5 | **15 / 15** 🔴 |

**Why now:** Manual intake caps revenue at consultant hours. AI intake removes the ceiling. No Spanish-language Germany advisory platform has deployed this yet.

---

### O-03 — Germany's Active International Student Policy
**Signal:** 420,000+ international students in Germany in 2025/26 (+6% YoY); Germany explicitly pursuing more; English-language caps in Anglophone countries redirecting Latin American students to Europe

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 5 | 4 | 3 | **12 / 15** 🟠 |

**Why now:** Germany's open policy is a structural tailwind — not a trend. Unlike Canada or Australia, Germany is actively investing in international student attraction. Cleo operates from inside Germany — the trust and credibility this provides cannot be replicated by a remote agency.

---

### O-04 — Qualification Recognition as Premium Service
**Signal:** 95,500 recognition procedures in 2024 — record high; 97% success rate when properly navigated; Anabin/ZAB process is opaque and anxiety-inducing

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 4 | 5 | 4 | **13 / 15** 🟠 |

**Why now:** The volume is growing and almost no automated Spanish-language tool helps students pre-assess their eligibility before spending €300+ on formal recognition processes. An AI pre-screening tool here has high perceived value and low development cost.

---

### O-05 — B2B Institutional Partnerships (Universities, NGOs, Foundations)
**Signal:** DAAD runs 86+ scholarship programs across Latin America; Colombian and Brazilian universities actively seek Germany placement partnerships; institutional deals replace hundreds of individual sales

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 4 | 4 | 3 | **11 / 15** 🟠 |

**Why now:** Institutional trust takes 12–24 months to build. Starting these relationships before scaling the B2C platform means the institutional channel is ready when the platform is ready — not after.

---

### O-06 — Compliance as a Premium Brand Signal
**Signal:** EU AI Act fully applicable August 2026; GDPR enforcement intensifying; students sharing sensitive documents with advisory services are becoming more privacy-aware; institutional clients require GDPR compliance from service providers

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 4 | 5 | 3 | **12 / 15** 🟠 |

**Why now:** Most competitors — especially small local LATAM consultants — are not GDPR-compliant, not EU AI Act-ready, and not transparent about how their tools work. Being the first in the niche to publish a compliance posture is a conversion argument, not just a legal requirement.

---

### O-07 — Post-Arrival Integration Market
**Signal:** No competitor currently offers post-visa support; post-arrival dropout and disorientation are documented problems (Anmeldung, Krankenkasse, housing, banking — all in German); lifetime value per client doubles if the relationship continues after arrival

| Market Pull | Strategic Fit | AI Leverage | Total |
|---|---|---|---|
| 4 | 5 | 4 | **13 / 15** 🟠 |

**Why now:** This is an upsell, not a new product. The same student who paid for pre-arrival advisory will pay a smaller recurring fee for post-arrival support. The agent is already built — it just continues past the visa stamp.

---

## 2. Risk Register

**Scoring Matrix:**
- **Likelihood:** 1 (rare) → 5 (almost certain)
- **Impact:** 1 (negligible) → 5 (existential)
- **Risk Score = Likelihood × Impact | Max: 25**

| Priority | Score | Level |
|---|---|---|
| 🔴 Critical | 16–25 | Immediate mitigation required |
| 🟠 High | 10–15 | Mitigation plan required |
| 🟡 Medium | 5–9 | Monitor and manage |
| 🟢 Low | 1–4 | Accept and note |

---

### R-01 — EU AI Act Non-Compliance (High-Risk Classification)
**Category:** Regulatory / Legal
**Description:** UC-01 (Germany Readiness Diagnostic Agent) and UC-02 (Ausbildung Matcher) both profile individual natural persons AND fall under Annex III of the EU AI Act (education and vocational training — "assessing the appropriate level of education that an individual will receive or will be able to access"). Under Article 6, an Annex III system that profiles individuals is **automatically classified as High-Risk**, regardless of the operator's intent. Full Articles 9–15 compliance obligations apply.

| Likelihood | Impact | Score |
|---|---|---|
| 4 | 5 | **20 / 25** 🔴 |

**Mitigation:** See Section 3 (EU AI Act Compliance Assessment) for full remediation plan.

---

### R-02 — GDPR Data Protection Breach
**Category:** Legal / Reputational
**Description:** The platform collects highly sensitive personal data from non-EU citizens (education history, financial information, identity documents, career goals). Processing this data using US-based LLM APIs (OpenAI, Anthropic) constitutes a cross-border data transfer requiring Standard Contractual Clauses (SCCs). A breach or non-compliant data flow could result in fines of up to 4% of global annual turnover under GDPR Article 83.

| Likelihood | Impact | Score |
|---|---|---|
| 3 | 5 | **15 / 25** 🟠 |

**Mitigation:** See Section 4 (GDPR Assessment) for full remediation plan.

---

### R-03 — Algorithmic Bias in Readiness Scoring
**Category:** Ethical / Legal / Reputational
**Description:** The Germany Readiness Score (UC-01) produces a numerical assessment of an individual's probability of success. If the underlying model systematically disadvantages students from lower-income backgrounds, specific nationalities, or lower-tier educational institutions — even unintentionally — this constitutes algorithmic discrimination. Under EU AI Act Article 10 (high-risk systems), data used to train or calibrate the system must be examined for bias. Additionally, GDPR Article 22 grants individuals the right not to be subject to solely automated decisions with significant effects.

| Likelihood | Impact | Score |
|---|---|---|
| 3 | 4 | **12 / 25** 🟠 |

**Mitigation:** See Section 6 (Algorithmic Fairness) for full assessment.

---

### R-04 — Agentic System Giving Incorrect Visa/Legal Advice
**Category:** Operational / Legal
**Description:** Agents operating autonomously (UC-03, UC-05, UC-07) may generate incorrect, outdated, or jurisdiction-specific advice about visa requirements, eligibility, or document validity. A student acting on wrong AI advice and being denied a visa has direct legal exposure for the service provider. This risk is highest when the agent retrieves live regulatory data that has changed without the RAG index being updated.

| Likelihood | Impact | Score |
|---|---|---|
| 3 | 5 | **15 / 25** 🟠 |

**Mitigation:** All agent outputs on visa or legal matters must be flagged as informational only — not professional legal advice. Human consultant review required before any formal submission recommendation. Regulatory RAG index must include versioning and staleness detection.

---

### R-05 — Competitive Entry by Leverage Edu or Similar Scale Players
**Category:** Market / Strategic
**Description:** Leverage Edu (TechCrunch, October 2025) is explicitly expanding into Latin America. ApplyBoard operates globally. Both have significantly more capital, engineering capacity, and institutional relationships than Cleo. If either pivots to include a Germany-specific Spanish-language Ausbildung offering, Cleo's differentiator narrows significantly.

| Likelihood | Impact | Score |
|---|---|---|
| 3 | 4 | **12 / 25** 🟠 |

**Mitigation:** Speed and depth of niche positioning are the primary defences. A 12-month head start with genuine German residency expertise, placed alumni, and a GDPR/EU AI Act-compliant platform creates a switching cost that a generic global platform cannot easily replicate. Institutional B2B relationships further deepen the moat.

---

### R-06 — Student Drop-Off Due to Language Barrier
**Category:** Operational / Revenue
**Description:** German language proficiency is the #1 reason Latin American students abandon Germany pathways (DAAD, 2024). If the platform onboards students who then fail to reach B1 within the required timeframe, refund requests, poor reviews, and reputational damage follow. The platform cannot control the student's effort but will be blamed for the outcome.

| Likelihood | Impact | Score |
|---|---|---|
| 4 | 3 | **12 / 25** 🟠 |

**Mitigation:** Build language readiness assessment into the diagnostic agent (UC-01). Students below A2 should be placed in a language preparation track before the main advisory flow. Success metrics and realistic timelines must be disclosed at intake — not as fine print, but as part of the onboarding experience.

---

### R-07 — Over-Reliance on Single LLM Provider
**Category:** Operational / Technical
**Description:** If the platform is built entirely on one LLM API (e.g., OpenAI GPT-4o or Anthropic Claude) and that provider experiences an outage, changes pricing dramatically, or modifies its terms of service to restrict advisory use cases, the entire platform is exposed.

| Likelihood | Impact | Score |
|---|---|---|
| 2 | 4 | **8 / 25** 🟡 |

**Mitigation:** Design the LLM layer with provider abstraction from day one (LiteLLM or similar routing). Maintain compatibility with at least one European-hosted open model (e.g., Mistral) as a fallback — this also strengthens the GDPR data residency posture.

---

### R-08 — WhatsApp API Dependency
**Category:** Operational / Technical
**Description:** The lead nurturing and student communication strategy (UC-05, UC-08) relies heavily on WhatsApp Business API. Meta's pricing, policy changes, or account restrictions can disrupt the primary communication channel overnight.

| Likelihood | Impact | Score |
|---|---|---|
| 2 | 3 | **6 / 25** 🟡 |

**Mitigation:** Build email as a parallel channel from day one. WhatsApp is the primary channel for conversion; email is the backup channel for continuity. Student consent for both channels collected at intake.

---

### R-09 — Green AI Reputational Risk
**Category:** Reputational / Environmental
**Description:** Running high-volume LLM inference for 10,000+ diagnostic sessions per month has a measurable carbon footprint. As AI sustainability becomes a mainstream concern — particularly among institutional partners in the EU education sector — operating without any sustainability policy creates reputational exposure.

| Likelihood | Impact | Score |
|---|---|---|
| 2 | 3 | **6 / 25** 🟡 |

**Mitigation:** See Section 5 (Green AI Assessment) for the sustainability strategy.

---

## 3. EU AI Act Compliance Assessment

**Applicable from:** August 2, 2026 (full enforcement)
**Cleo's role:** Deployer (uses third-party LLM APIs to build and operate AI systems)
**Relevant obligations:** Transparency (all tiers), High-Risk Articles 9–15 (for classified systems), AI literacy (all systems), GPAI downstream obligations

---

### 3.1 Use Case Risk Classification

| Use Case | Annex III Trigger | Profiling? | Classification | Key Obligations |
|---|---|---|---|---|
| **UC-01 Diagnostic Agent** | ✅ Annex III Point 3(a) — assessing education access level | ✅ Yes — scores individuals | **HIGH RISK** | Articles 9–15: risk management, data governance, transparency, human oversight, accuracy, logging |
| **UC-02 Ausbildung Matcher** | ✅ Annex III Point 3(a) — assigning individuals to vocational training | ✅ Yes — matches and ranks individuals | **HIGH RISK** | Same as UC-01; additionally, Article 14 human oversight before final placement recommendation |
| **UC-03 Application Tracker** | ❌ No Annex III trigger — administrative/procedural | ❌ No individual scoring | **LIMITED RISK** | Transparency: users must be informed they are interacting with an AI agent |
| **UC-04 Document Factory** | ❌ No Annex III trigger — content generation | ❌ No | **LIMITED RISK** | AI-generated content disclosure; no claim that documents were human-authored |
| **UC-05 Lead Nurturing Agent** | ⚠️ Potential trigger if lead scoring affects access to advisory services | ✅ Scores and segments individuals | **LIMITED–HIGH RISK** ⚠️ | Requires legal review; if lead score determines whether a student receives service, HIGH RISK classification may apply |
| **UC-07 Visa Intelligence Agent** | ❌ No direct trigger — informational monitoring | ❌ No | **MINIMAL RISK** | Voluntary code of conduct recommended; AI literacy obligation for operators |
| **UC-08 Integration Concierge** | ❌ No Annex III trigger — post-arrival support | ❌ No | **MINIMAL RISK** | Chatbot disclosure transparency |

---

### 3.2 High-Risk Compliance Obligations (UC-01, UC-02)

Under Articles 9–15 of the EU AI Act, Cleo must implement the following for UC-01 and UC-02:

**Article 9 — Risk Management System**
A documented, continuous risk management process identifying foreseeable misuses, failure modes, and residual risks. Must be updated throughout the system lifecycle — not a one-time exercise.

**Article 10 — Data Governance**
Training data, validation data, and any calibration data used to produce readiness scores must be examined for biases. Data sources must be documented. Personal data used only for defined purposes. This applies even when using third-party LLMs — the deployer inherits documentation obligations.

**Article 13 — Transparency & Provision of Information**
Users (students) must receive clear information that they are interacting with an AI system and that its output is a recommendation, not a binding determination. The scoring logic — at a level a non-technical person can understand — must be disclosed.

**Article 14 — Human Oversight**
High-risk systems must be designed to allow natural persons to monitor, intervene, override, and correct outputs. For UC-01, this means: no readiness score is delivered as a final advisory without a human consultant review step. For UC-02, no Ausbildung position match is formally recommended without human validation.

**Article 15 — Accuracy, Robustness & Cybersecurity**
The system must perform consistently across the full range of users — including students from lower-income backgrounds, less prestigious educational institutions, and countries with non-standard credential systems. Performance testing across demographic subgroups is required.

**Article 49 — Registration**
High-risk AI systems must be registered in the EU database prior to deployment. If Cleo determines UC-01 is not high-risk, this assessment must be documented and retained.

---

### 3.3 Compliance as Competitive Positioning

This is the reframe most competitors will miss: **EU AI Act compliance for UC-01 and UC-02 is not a burden. It is the most credible trust signal Cleo can offer to institutional partners.**

When a Colombian university considers licensing Cleo's diagnostic tool for their students, the first question their legal team will ask is: "Is this GDPR and EU AI Act compliant?" Being able to answer yes — with documentation — closes that deal. A competitor operating a non-compliant scoring system cannot participate in that conversation.

**Recommended action:** Publish a one-page "Responsible AI Commitment" on the platform homepage. No technical jargon. Just: what data we collect, why, how the score works, and who reviews it before it affects your path. This converts compliance effort into brand equity.

---

## 4. GDPR Data Protection Assessment

### 4.1 Data Inventory

| Data Category | Examples | Sensitivity | Legal Basis |
|---|---|---|---|
| Identity data | Name, date of birth, nationality | Standard | Consent (Art. 6(1)(a)) |
| Contact data | Email, phone, WhatsApp | Standard | Contract (Art. 6(1)(b)) |
| Educational history | Degrees, institutions, grades, transcripts | Standard | Contract (Art. 6(1)(b)) |
| Financial data | Budget range, funding source | Sensitive | Consent (Art. 6(1)(a)) |
| Language certificates | Goethe, TestDaF, IELTS scores | Standard | Contract (Art. 6(1)(b)) |
| Career goals | Target sector, Ausbildung preference | Standard | Contract (Art. 6(1)(b)) |
| AI-generated scores | Readiness Score, lead classification | Standard | Legitimate interest (Art. 6(1)(f)) |
| Communication logs | WhatsApp, email history with agents | Standard | Contract (Art. 6(1)(b)) |

**Note:** Health data, ethnic origin, and political opinions are **special categories** under GDPR Article 9 and must not be collected unless explicitly required and separately consented to.

---

### 4.2 Cross-Border Data Transfer Risk

Students are data subjects located in Latin America (non-EU). Cleo processes their data in Germany (EU). However:

- **LLM API calls** (OpenAI, Anthropic) route student data to US-based servers → requires **Standard Contractual Clauses (SCCs)** under GDPR Article 46
- **WhatsApp Business API** routes through Meta's infrastructure → requires SCC + Meta DPA
- **Supabase** — if using EU region (Frankfurt), data stays within EEA — no transfer risk ✅
- **Any US-hosted CRM** (HubSpot free tier) → requires SCC

**Recommended action:** Host all primary data on Supabase EU region. Route LLM calls through EU-hosted proxies where possible. Maintain a Data Processing Agreement (DPA) with every third-party processor before going live.

---

### 4.3 GDPR Article 22 — Automated Decision-Making

Students have the right under GDPR Article 22 not to be subject to **solely automated decisions** that produce legal or similarly significant effects. A Germany Readiness Score that determines whether a student receives advisory service, or which pathway is recommended, may qualify.

**Mitigation:** The score must be presented as a **recommendation input**, not a final decision. A human consultant must be in the loop before the score produces a significant consequence for the student. This aligns with EU AI Act Article 14 human oversight requirements — solving both compliance obligations with one design decision.

---

### 4.4 Key GDPR Action Items

| Requirement | Status for New Platform | Action Required |
|---|---|---|
| Privacy Policy (Art. 13/14) | ❌ Not yet created | Draft before launch |
| Cookie consent banner | ❌ Not yet created | Implement on website |
| Data Processing Agreements | ❌ Not yet signed | Sign with OpenAI, Anthropic, Meta, CRM provider |
| Data Retention Policy | ❌ Not defined | Define: active clients, inactive leads, archived cases |
| Right to Erasure process | ❌ Not yet built | Must delete all data including LLM interaction logs |
| Data Breach Response Plan | ❌ Not yet created | 72-hour notification obligation to supervisory authority |
| DPIA (Data Protection Impact Assessment) | ⚠️ Required for UC-01 (high-risk AI + profiling) | Complete before UC-01 deployment |

---

## 5. Green AI Sustainability Assessment

### 5.1 Why This Matters for Cleo

The EU AI Act explicitly references environmental sustainability as a consideration in AI development and deployment. More practically: institutional partners in the German and European education sector increasingly request environmental impact statements from service providers. Being the only advisory platform in this niche with a published Green AI policy is a differentiator — not a compliance box.

### 5.2 Environmental Impact of the AI Stack

**Current understanding of LLM inference energy costs:**
- A single GPT-4 class inference query consumes approximately 0.001–0.01 kWh (estimates vary significantly by model and context window; Luccioni et al., 2024; Huson et al., 2024)
- At 10,000 diagnostic sessions/month, each generating 3–5 LLM calls, total inference energy is approximately **0.3–5 kWh/month** — modest at this scale
- Water consumption for AI data center cooling is an emerging secondary metric (Li et al., cited in arXiv:2505.09598, 2025)
- Hardware embodied carbon (GPU manufacturing) represents a significant share of total AI lifecycle impact but is largely outside Cleo's control as an API consumer

### 5.3 Green AI Strategy for Cleo's Platform

| Principle | Implementation |
|---|---|
| **Right-size the model** | Use smallest capable model for each task — not GPT-4 for FAQ responses. Reserve frontier models (GPT-4o, Claude Sonnet) for complex, high-value generations only |
| **Cache repeated outputs** | Standard diagnostic responses for common profiles can be cached and served without re-inference. Significant energy and cost reduction at scale |
| **Batch non-urgent processing** | Lead scoring, document drafts, and follow-up sequences do not need real-time inference. Schedule batch processing during low-carbon grid hours where possible |
| **EU data centre preference** | Prefer LLM providers with EU or renewable-powered infrastructure — Mistral (Paris) for European data residency and lower embodied carbon per query |
| **Measure and publish** | Use tools such as CodeCarbon, EcoLogits, or Anthropic's usage dashboards to track inference carbon estimates. Publish an annual AI Sustainability Report — even a brief one. No competitor in this niche will do this |

### 5.4 The Business Case for Green AI

A 2024 study (Luccioni et al.) demonstrated that smaller, specialised models can outperform general-purpose frontier models on specific advisory tasks while consuming 10–100x less energy. For Cleo's use cases — which are highly structured (intake forms → roadmap generation) — a fine-tuned or RAG-augmented smaller model is not only greener but likely more accurate on Germany-specific content than a generic large model.

**Recommendation:** Begin with frontier models for speed to market. By Month 6, evaluate whether a RAG-enhanced smaller model (Mistral 7B or similar) can handle 80% of diagnostic queries at lower cost, lower latency, and lower carbon footprint. This is an architectural decision that compounds in value as volume grows.

---

## 6. Algorithmic Fairness & Bias Assessment

### 6.1 The Risk in Plain Terms

The Germany Readiness Score assigns a number to a human being's probability of success. If that number is systematically lower for students from:
- Lower-income families
- Non-prestigious universities
- Countries with non-standardised credential systems (most of Latin America)
- Students whose profiles don't match historical success data

...then the AI is not neutral. It is replicating and amplifying historical inequalities. Under EU AI Act Article 10, deployers of high-risk AI systems must actively assess and address this.

### 6.2 Bias Sources Specific to This Use Case

| Bias Type | Where It Enters | Impact |
|---|---|---|
| **Training data bias** | If the LLM was trained primarily on English-language academic success data, it may undervalue Latin American credentials and institutions | Systematic underscoring of Latin American applicants |
| **Proxy discrimination** | Budget range as a proxy for socioeconomic status; lower budget → lower score; but lower budget ≠ lower capability | Students from lower-income families receive lower readiness scores |
| **Credential non-equivalence** | German Anabin database does not recognise all Latin American universities equally; AI may penalise students from unrecognised institutions even when their skills are equivalent | Colombian or Bolivian students from regional universities systematically disadvantaged |
| **Language bias** | Students completing the diagnostic in imperfect Spanish may receive lower-quality outputs than fluent writers | Non-native Spanish speakers or bilingual students disadvantaged |

### 6.3 Fairness Mitigation Framework

**Step 1 — Disaggregated performance testing**
Before launch, test UC-01 outputs across a synthetic dataset representing diverse profiles: Colombia, Brazil, Mexico, Peru; public and private universities; low, mid, and high budget ranges. Flag any systematic score differential not explained by genuine eligibility differences.

**Step 2 — Explainable scores**
The readiness score must be accompanied by the specific factors driving it — not just a number. "Your score is 62 because: German language level is below B1 (primary factor), your degree is pending Anabin review (secondary factor), your budget covers 12 months." This enables the student and consultant to understand and challenge the output.

**Step 3 — Human review override**
Any student whose score falls below a threshold (e.g., below 50) should trigger a human consultant review before the score is communicated. Automated low scores without human validation carry the highest fairness and legal risk.

**Step 4 — Feedback loop monitoring**
Track whether students with similar profiles but from different countries or institutions receive different scores over time. Build a quarterly bias audit into operations.

---

## 7. Trust Architecture: Compliance as the Product

The following framework synthesises all compliance obligations into a single positioning principle:

> **"Our AI helps. Our humans decide. You keep control."**

This three-part statement maps directly to every compliance layer:

| Statement | Compliance Layer | Business Benefit |
|---|---|---|
| "Our AI helps" | EU AI Act transparency (Art. 13) — disclose AI involvement | Builds informed consent; reduces abandonment |
| "Our humans decide" | EU AI Act human oversight (Art. 14) + GDPR Art. 22 — no solely automated decisions | Positions consultants as premium value-add; not replaced by AI |
| "You keep control" | GDPR rights (erasure, access, portability) + explainable scoring | Trust signal for privacy-aware students and institutional partners |

### 7.1 Recommended Trust Artefacts

These are concrete deliverables that operationalise the trust architecture and differentiate Cleo from every unregulated competitor:

| Artefact | Description | When to Produce |
|---|---|---|
| **Responsible AI Commitment** | One-page public statement: what AI does, what humans do, how data is protected | Before launch |
| **Score Explainability Card** | Sent with every readiness score: factors, weights, how to improve | With every UC-01 output |
| **GDPR Transparency Notice** | Plain-language data processing disclosure at intake | At signup |
| **Data Protection Impact Assessment (DPIA)** | Formal assessment for UC-01 and UC-02 | Before deployment of high-risk systems |
| **Annual AI Sustainability Report** | One-page carbon and energy estimate for platform AI usage | Annually from Year 1 |
| **AI Literacy Disclosure** | Inform all staff and contractors interacting with AI systems — required under EU AI Act | At onboarding |

---

## 8. Risk Mitigation Roadmap

| Timeline | Action | Priority |
|---|---|---|
| **Pre-launch (Month 0)** | Draft Privacy Policy and GDPR Transparency Notice | 🔴 |
| **Pre-launch (Month 0)** | Sign DPAs with OpenAI/Anthropic, Meta (WhatsApp), CRM provider | 🔴 |
| **Pre-launch (Month 0)** | Classify UC-01 and UC-02 as High Risk under EU AI Act; document classification assessment | 🔴 |
| **Pre-launch (Month 0)** | Implement human review step for all UC-01 readiness scores before delivery | 🔴 |
| **Pre-launch (Month 0)** | Add AI disclosure to all chatbot and agent interactions | 🔴 |
| **Month 1** | Complete DPIA for UC-01 and UC-02 | 🔴 |
| **Month 1** | Publish Responsible AI Commitment on website | 🟠 |
| **Month 2** | Run disaggregated bias testing across synthetic Latin American student profiles | 🟠 |
| **Month 3** | Evaluate Mistral or EU-hosted model for lower-stakes inference tasks | 🟡 |
| **Month 6** | Publish first AI Sustainability Report | 🟡 |
| **Month 6** | Register high-risk AI systems in EU database (mandatory from August 2026) | 🔴 |
| **Ongoing** | Quarterly bias audit; annual DPIA review; LLM provider contract monitoring | 🟠 |

---

## 9. References

*(APA 7th Edition)*

Artificial Intelligence Act (EU) 2024/1689. (2024). *Regulation of the European Parliament and of the Council laying down harmonised rules on artificial intelligence*. Official Journal of the European Union. https://artificialintelligenceact.eu

Artificial Intelligence Act EU. (2024). *Annex III: High-risk AI systems referred to in Article 6(2)*. https://artificialintelligenceact.eu/annex/3/

Artificial Intelligence Act EU. (2024). *Article 6: Classification rules for high-risk AI systems*. https://artificialintelligenceact.eu/article/6/

European Data Protection Board. (2024). *Guidelines on automated individual decision-making and profiling*. https://edpb.europa.eu

FMC Group. (2025). *Germany skilled worker shortage stats: 2026 report*. https://fmcgroup.com/germany-skilled-worker-shortage/

Huson, C., et al. (2024). *The price of prompting: Profiling energy use in large language model inference*. In S. Rince (Ed.), Awesome Green AI. GitHub. https://github.com/samuelrince/awesome-green-ai

Jegham, N., et al. (2025). *How hungry is AI? Benchmarking energy, water, and carbon footprint of LLM inference* (arXiv:2505.09598). https://arxiv.org/abs/2505.09598

Lexology. (2025, June). *High-risk systems according to the EU AI Act*. https://www.lexology.com/library/detail.aspx?g=70b04b24-03f8-483b-ae17-a2f5732a3f01

Lowenstein Sandler LLP. (2024). *The EU Artificial Intelligence Act of 2024: What you need to know (Privacy)*. https://www.lowenstein.com/news-insights/publications/client-alerts/the-eu-artificial-intelligence-act-of-2024-what-you-need-to-know-privacy

Luccioni, A., et al. (2024). *From efficiency gains to rebound effects: The problem of Jevons' paradox in AI's polarized environmental debate*. In S. Rince (Ed.), Awesome Green AI. GitHub. https://github.com/samuelrince/awesome-green-ai

Plan Be Eco. (2026, April). *EU AI Act for the education industry: Guide 2026*. https://planbe.eco/en/blog/eu-ai-act-for-the-education-industry/

Regulation (EU) 2016/679 (General Data Protection Regulation). (2016). *Official Journal of the European Union*. https://gdpr-info.eu

Solovyeva, L., & Castor, F. (2026). *Towards green AI: Decoding the energy of LLM inference in software development* (arXiv:2602.05712). University of Twente. https://arxiv.org/html/2602.05712v1

TechCrunch. (2025, October 1). *Visa crackdowns are blocking students' study-abroad dreams, so India's Leverage Edu is rerouting them*. https://techcrunch.com/2025/10/01/visa-crackdowns-are-blocking-students-study-abroad-dreams

---

*This document was prepared as part of the AI Adoption Opportunity Project — Ironhack Berlin AI & Integration Consulting Program, June 2026. Compliance assessments are for educational and business planning purposes and do not constitute legal advice. A qualified legal professional should review all compliance postures before platform deployment.*
