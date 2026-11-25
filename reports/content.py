"""Text of the downloadable PDF reports. Figures come only from Saqib Ameer's own
resume, portfolio deck and case-study PDFs (Drive: SA - My Portfolio)."""

WHITEPAPER = {
"file": "ai-growth-stack-whitepaper.pdf",
"kind": "Whitepaper",
"title": "The AI Growth Stack",
"subtitle": "A five-layer framework for turning AI into a measurable growth engine for DTC, eCommerce and SaaS brands",
"sections": [
("Executive summary", """
Artificial intelligence is now built into every major marketing platform. Ad networks bid with machine learning, CRMs score leads automatically and large language models write copy in seconds. Access to AI is no longer a competitive advantage. Every competitor has the same tools.

What separates the brands that grow from those that simply spend more is the **system** the tools sit inside. This paper sets out that system as five layers, built in order:

1. **Signal:** data, tracking and attribution you can trust.
2. **Acquire:** paid and organic demand, run on unit economics.
3. **Convert:** pages, offers and journeys tested like products.
4. **Retain:** lifecycle automation that keeps revenue compounding.
5. **Scale:** AI agents and workflows that take repetitive work off the team.

Each layer makes the next one cheaper, faster and more accurate. Skipping a layer does not save time; it moves the cost somewhere harder to see. The framework draws on more than a decade of leading growth across SaaS, eCommerce, mobile apps, fintech and healthcare in the UAE, Germany and wider Europe.
"""),
("Why a framework, and why now", """
Three shifts have changed the economics of marketing since 2021:

- **Privacy changes reduced signal.** App Tracking Transparency and the decline of third-party cookies made platform attribution less complete. Brands with strong first-party data recovered; others lost visibility.
- **Platforms automated buying.** Performance Max, Advantage+ and similar products moved control from manual bids to algorithms. The quality of the inputs (conversion definitions, values, creative) now matters more than manual optimisation.
- **Generative AI made content cheap.** Producing ad variants, emails and landing pages is no longer the bottleneck. Choosing, testing and connecting them is.

> When execution becomes cheap, the advantage moves to the system that decides what gets executed.

Teams that bolt AI onto a broken funnel scale the broken parts. The AI Growth Stack is a way to make sure that what AI scales is worth scaling.
"""),
("Layer 01 — Signal", """
**Purpose:** give every person and every algorithm the same, correct picture of what is working.

**What it includes**

- A single source of truth for conversions (CRM, store or GA4), shared with ad platforms.
- A documented event map with consistent naming and no duplicates.
- Conversion values, so bidding can prefer better customers.
- Cohort reporting: CAC, LTV and payback by acquisition month and channel.
- Technical foundations: sitemap, robots.txt, analytics coverage and page speed.
- Server-side tagging and conversion APIs where volumes justify them.

**Signs this layer is broken**

- Platform-reported conversions differ widely from the CRM or store.
- Nobody can explain how ROAS on the dashboard is calculated.
- Budget decisions are made from a single platform's view.

**In practice.** At CHAMELAION, a SaaS business targeting DACH markets, cohort analysis and funnel analytics made CAC, LTV and blended ROAS visible by channel. That visibility drove the budget changes behind a **22% reduction in CAC**. At Qmantic, campaigns bid toward clearly separated sign-up and free-trial conversions, and an on-page audit confirmed sitemap, robots.txt and analytics readiness before scale.
"""),
("Layer 02 — Acquire", """
**Purpose:** create and capture demand at a cost the business can sustain.

**What it includes**

- Channel strategy across Google, Meta, TikTok, LinkedIn and programmatic, chosen by where the buyer is.
- Persona-based targeting and messaging.
- Account structure segmented by market and intent.
- Bidding toward real outcomes, with soft actions used for audiences, not optimisation.
- AI-speed creative testing against a control.
- Organic engines (SEO, content, community) to reduce paid dependency over time.

**Signs this layer is broken**

- Spend rises faster than revenue.
- One broad audience and one creative angle carry the whole account.
- Paid search is the only channel that "works".

**In practice.** Qmantic's Google Ads account was segmented by region (UK, Europe, Germany, DACH, Middle East) and intent (free trial vs sign-up). Between July 2023 and July 2024 it recorded **6.78K clicks, 105K impressions and 1.35K conversions on €3.8K** of spend. At VANCY, Google and Meta app campaigns delivered **ROAS above 3.2×**, with installs up **40%**.
"""),
("Layer 03 — Convert", """
**Purpose:** turn more of the traffic you already pay for into customers.

**What it includes**

- Landing pages matched to persona and search intent, each with one call to action.
- Offer design: trials, demos, guarantees and pricing presentation.
- Structured A/B testing of headlines, proof, layout and forms.
- Journey mapping from first click to first value.
- Speed-to-lead processes for sales-led and service businesses.

**Signs this layer is broken**

- Every campaign lands on the home page.
- Tests are run without a hypothesis or stopped early.
- Leads wait hours or days for a reply.

**In practice.** UX and A/B testing improved MQL-to-SQL conversion by **16%** at CHAMELAION; A/B-tested landing pages and journey mapping lifted conversion rates by **25%** at VANCY.
"""),
("Layer 04 — Retain", """
**Purpose:** make each customer worth more, so acquisition can afford to grow.

**What it includes**

- Onboarding and activation sequences triggered by behaviour.
- Nurture for leads not yet ready to buy.
- Trial-expiry, renewal and win-back flows.
- Contact segmentation and tagging (registered, activated, non-activated, support).
- Community programmes where the product suits them.
- CRM set-up in tools such as HubSpot, GoHighLevel, Mailchimp or Brevo.

**Signs this layer is broken**

- New users receive one welcome email and then nothing.
- Retention and LTV are not reported.
- Every repeat sale is bought again through ads.

**In practice.** At Qmantic, lifecycle templates covered confirmation, activation, demo prompts, reminders and trial expiry, and trigger-based onboarding improved **trial-to-paid conversion by 12%**. At CHAMELAION, the community grew from **0 to 1,200 active members**, with onboarding completion up **18%**.
"""),
("Layer 05 — Scale", """
**Purpose:** let AI and automation take repetitive work off the team, so people spend time on strategy and taste.

**What it includes**

- Reporting agents that assemble, reconcile and summarise performance.
- Research agents that track competitors and markets with cited sources.
- Creative assistants that draft variants from top performers.
- QA agents that check links, tracking, pacing and disapprovals.
- Lead enrichment, scoring and routing.

**Rules for this layer**

1. The agent proposes; people decide on budgets and anything customer-facing.
2. Every figure carries its source.
3. Automations are logged and reviewable.
4. Sensitive data stays inside your own systems.

**Signs this layer is premature**

- AI summaries contradict the finance numbers.
- Automations trigger on events nobody trusts.

> Scale is the last layer, not the first. AI multiplies the quality of everything underneath it.
"""),
("A 90-day sequence", """
| Weeks | Focus | Outputs |
|---|---|---|
| 1–2 | Signal audit | Event map, conversion definitions, cohort baseline |
| 3–4 | Signal fixes | Clean tracking, values, server-side where needed |
| 5–6 | Acquire | Persona structure, intent segmentation, creative test plan |
| 7–8 | Convert | Persona landing pages, first A/B tests, speed-to-lead |
| 9–10 | Retain | Onboarding, nurture and win-back flows live |
| 11–12 | Scale | Reporting agent and QA agent in production |

The sequence is deliberately conservative. Teams that already have strong tracking move faster through the first month; teams with weak data should not rush it.
"""),
("Self-assessment", """
Score each statement from 0 (not true) to 2 (fully true). A score below 5 in any layer marks the place to start.

| Layer | Statement |
|---|---|
| Signal | Platform, analytics and finance numbers reconcile within an agreed tolerance. |
| Signal | We can see CAC and payback by channel and by monthly cohort. |
| Acquire | Campaigns are segmented by persona, market and intent. |
| Acquire | We bid on outcomes that have a value attached. |
| Convert | Each major campaign has a matching landing page. |
| Convert | We run at least two structured tests a month. |
| Retain | New customers enter a behaviour-based onboarding flow. |
| Retain | Retention and LTV appear in the monthly report. |
| Scale | Weekly reporting takes under an hour of human time. |
| Scale | Every automation has an owner and a log. |
"""),
("About the author", """
**Saqib Ameer** is an AI Growth Leader based in Dubai. Over more than ten years he has led growth for SaaS, eCommerce, mobile app, fintech and healthcare brands across the UAE, Germany and Europe, including C-level marketing ownership and P&L responsibility. He holds an MSc in Computer Science, which shapes his systems-first approach to marketing, data and automation.

Selected results: **22% lower CAC** (SaaS, DACH), **1,000+ trial sign-ups** through paid search and email nurture (B2B SaaS), **3.2×+ ROAS** on app campaigns (EU), **+60% Google Ads clicks** and around **AED 15 cost per lead** on Meta (healthcare, Abu Dhabi), and **50+ growth projects** delivered for international clients.

Contact: hello@saqibameer.com · saqibameer.com
"""),
]}

COMPENDIUM = {
"file": "saqib-ameer-case-study-compendium.pdf",
"kind": "Case studies",
"title": "Growth Case Study Compendium",
"subtitle": "Selected engagements 2017–2026 across healthcare, SaaS, mobile apps and personal branding",
"sections": [
("Introduction", """
This compendium collects selected engagements from in-house, consulting and C-level roles. Each case follows the same structure: the context, what was done, and the results. Figures are taken from the original case-study documents, platform screenshots and role records; where a figure covers a specific period, the period is stated.

| Organisation | Sector | Period | Role |
|---|---|---|---|
| House of Nature Medical Center | Healthcare, Abu Dhabi | 2025 – present | Marketing Manager / Performance Marketer |
| CHAMELAION GmbH | Web3 / fintech SaaS, Germany | Dec 2024 – Jan 2026 | Marketing Manager, CMO track |
| QMANTIC SaaS GmbH | B2B SaaS, Germany | Apr – Dec 2024 | Marketing Manager |
| VANCY GmbH | Mobile app, Germany | Dec 2023 – Mar 2024 | Marketing Manager |
| SQUIDEX.IO GmbH | Developer SaaS, Germany | Dec 2022 – Oct 2023 | CMO / Marketing Consultant |
| Eftelya Erbasli / Gelassenerwachsen | Personal brand, Germany | 2023 – 2024 | Consultant |
| HA-Technologies | Agency, Pakistan | 2017 – 2022 | Digital Marketing Manager |
"""),
("House of Nature Medical Center", """
**Context.** A medical center in Abu Dhabi needed a steady flow of patient inquiries in a regulated, trust-sensitive category.

**What was done**

- High-intent Google Search campaigns organised by service line.
- Meta lead generation with audience segmentation, retargeting and creative testing.
- Website calls to action and inquiry funnels.
- Content, local SEO and Google Business Profile optimisation.

**Results**

| Metric | Result |
|---|---|
| Google Ads clicks | +60% |
| Meta cost per lead | around AED 15 |
| Scope | End-to-end digital marketing ownership |
"""),
("CHAMELAION GmbH", """
**Context.** A Web3 and fintech SaaS company selling into regulated DACH markets. Full marketing P&L ownership across Google, Meta, LinkedIn and programmatic.

**What was done**

- Persona-based targeting, bid optimisation and funnel segmentation.
- Performance attribution using cohort analysis and funnel analytics (CAC, LTV, blended ROAS).
- Technical SEO, content syndication and backlink strategy.
- Community building and onboarding improvements.
- Landing page UX and A/B testing.

**Results**

| Metric | Result |
|---|---|
| Customer acquisition cost | −22% |
| Organic traffic | +45% in 4 months |
| Community | 0 → 1,200 active members |
| Onboarding completion | +18% |
| MQL → SQL conversion | +16% |
"""),
("QMANTIC SaaS GmbH", """
**Context.** A B2B SaaS company offering AI-powered data analysis and cloud BI. The role covered the full funnel, from market discovery and paid acquisition to lifecycle follow-up, SEO and social content.

**What was done**

- Keyword research linking search demand, CPC estimates and ad copy.
- Google Ads segmented by market (UK, Europe, Germany, DACH, Middle East) and intent (free trial, sign-up), using Maximise Conversions bidding.
- Lifecycle email templates and behavioural segmentation: activation, demos, support, reminders, trial expiry.
- On-page SEO audit: titles, descriptions, alt text, speed, robots.txt, sitemap, analytics.
- A consistent social content system with static posts, reels and video.

**Results**

| Metric | Result |
|---|---|
| Google Ads clicks (Jul 2023 – Jul 2024) | 6.78K |
| Impressions (same period) | 105K |
| Conversions (same period) | 1.35K |
| Recorded spend (same period) | €3.8K |
| Trial sign-ups via paid + email nurture | 1,000+ |
| Trial → paid conversion | +12% |
| Social engagement | +38% |
"""),
("VANCY GmbH", """
**Context.** A professional networking mobile app in Germany. Objective: increase app users and installs through digital marketing.

**What was done**

- A holistic digital strategy aligned with the German audience.
- Social media creatives in line with brand guidelines.
- Targeted ad campaigns and media buying research for business audiences.
- Video content, graphic design and personalised email templates.
- ASO and SEO, plus Google and Meta app campaigns.

**Results**

| Metric | Result |
|---|---|
| App users (EU) | +60% |
| App installs via paid campaigns | +40% |
| ROAS on app campaigns | 3.2×+ |
| Conversion rate (landing pages) | +25% |
| CTA to app install | +35% |
| Brand visibility | +30% |
| Video engagement | +40% |
| Qualified leads | +30% |
"""),
("SQUIDEX.IO GmbH", """
**Context.** A developer-focused SaaS company in Germany. C-level marketing ownership as CMO / marketing consultant.

**What was done**

- Built and executed the full go-to-market strategy.
- Ran brand, performance, content and SEO as one growth engine.
- Designed automated email funnels for trial engagement and retention.
- Managed agencies, creative briefs and CEO-level reporting on marketing ROI.

**Results**

| Metric | Result |
|---|---|
| Brand awareness | +60% in 4 months |
| Organic sign-ups | +32% |
"""),
("Eftelya Erbasli — personal brand", """
**Context.** A coach and founder of Gelassenerwachsen wanted a strong personal brand and online presence.

**What was done**

- Branding guidelines, logos and brand kits for the person and the company.
- Creative design, theme selection and a social media planner with reels.
- Content and marketing for the High-NRG online course.
- Video production and editing, email outreach (Mailchimp, Brevo).
- LinkedIn automation strategy, Google and YouTube ads, WordPress landing pages and funnel integration.

**Results**

| Metric | Result |
|---|---|
| LinkedIn followers gained | 300+ |
| LinkedIn profile views | 500+ per week |
"""),
("HA-Technologies and earlier work", """
**Context.** Five years leading 360° marketing projects for international clients across SaaS, IT, fintech and eCommerce, preceded by SEO and digital marketing roles at SEO Islamabad and Estate92.

**Results**

| Metric | Result |
|---|---|
| Growth projects delivered | 50+ |
| Client ROI via paid search and segmentation | +80% |
| Real-estate lead generation (earlier work) | +200% |
"""),
("Patterns across the work", """
Looking across these engagements, the same principles recur:

1. **Measure first.** The biggest gains followed better tracking and cohort visibility.
2. **Segment everything.** Market, intent and persona segmentation beat broad targeting in every account.
3. **Own the follow-up.** Lifecycle automation turned acquisition into revenue at Qmantic, SQUIDEX and CHAMELAION.
4. **Build organic alongside paid.** SEO and community reduced dependency on rising ad costs.
5. **Report in business terms.** CAC, LTV, ROAS and payback, not impressions.

These principles became the five layers of **The AI Growth Stack**, published separately as a whitepaper.

Contact: hello@saqibameer.com · saqibameer.com
"""),
]}

PLAYBOOK = {
"file": "ai-marketing-ops-playbook.pdf",
"kind": "Playbook",
"title": "The AI Marketing Operations Playbook",
"subtitle": "How to give your marketing team an AI shift: what to automate first, who owns what, and a 90-day rollout",
"sections": [
("Who this is for", """
Founders, CMOs and growth leads at DTC, eCommerce and SaaS companies who want AI to save real hours and improve decisions, without risking the brand or the budget.

This playbook covers the **Scale** layer of The AI Growth Stack. It assumes your tracking is reasonably sound. If it is not, start with the Signal layer; AI built on unreliable data produces confident, wrong answers.
"""),
("The operating model", """
Think of AI as a new shift on your team: fast, tireless and literal. It needs clear instructions, a supervisor and limits.

| Role | Responsibility |
|---|---|
| Growth lead (owner) | Decides which workflows exist, sets guardrails, approves actions |
| Workflow builder | Designs prompts, connectors and logic; maintains them |
| Reviewer | Checks outputs daily or weekly; flags errors |
| AI agent | Collects, compares, drafts and proposes; never decides alone |

**The golden rule:** agents propose, people decide. Budget changes, publishing and customer messages require a human approval step until a workflow has a long, clean track record.
"""),
("Choosing what to automate", """
Score candidate tasks on four questions. Start with tasks that score high on the first three and low on the fourth.

1. Is it **repetitive** (weekly or more)?
2. Is it **rule-based** (a good junior could follow a checklist)?
3. Is it **easy to verify** (a human can check the output quickly)?
4. Is it **high-risk** if wrong (money, brand, compliance)?

**Recommended first five**

| Workflow | Time it typically replaces | Human checkpoint |
|---|---|---|
| Weekly performance memo | Manual exports and slide-building | Review before sending |
| Competitor and market watch | Ad-hoc browsing | Decide what matters |
| Creative variant drafts | Blank-page writing | Edit and approve |
| Campaign QA | Spot checks | Fix or approve fix |
| Lead enrichment and routing | Manual triage | Rules and edge cases |
"""),
("Workflow design template", """
Document every workflow on one page before you build it:

- **Name and owner.**
- **Trigger:** schedule or event that starts it.
- **Inputs:** systems and fields it reads, with access level.
- **Steps:** collect, reconcile, analyse, draft, propose.
- **Output:** format, destination and timing.
- **Guardrails:** what it may never do.
- **Checkpoint:** who reviews, and how quickly.
- **Success metric:** hours saved, errors caught, speed-to-lead, or test velocity.
- **Kill switch:** how to pause it.
"""),
("Guardrails", """
1. **Source every number.** Outputs link figures to where they came from.
2. **No silent spending.** Agents cannot change budgets, bids or live campaigns without approval.
3. **Protect data.** Customer and patient data stays in your CRM or approved tools, never pasted into public chat tools.
4. **Brand review.** Anything customer-facing passes a human edit.
5. **Log everything.** Each run is recorded with inputs, outputs and approvals.
6. **Review monthly.** Retire workflows that no longer earn their keep.

> Trust is earned per workflow, not granted to "AI" in general.
"""),
("A 90-day rollout", """
| Phase | Weeks | Actions | Exit criteria |
|---|---|---|---|
| Prepare | 1–3 | Signal check, task inventory, scoring, guardrails agreed | Top 5 workflows chosen with owners |
| Pilot | 4–7 | Build reporting memo and campaign QA; run in parallel with the manual process | Outputs match manual work for 3 weeks |
| Expand | 8–10 | Add research, creative drafts and lead routing | Each has a reviewer and a metric |
| Embed | 11–13 | Retire the manual versions, document, train the team | Hours saved measured; monthly review set |
"""),
("Measuring the return", """
Track a small set of numbers from day one:

- **Hours saved** per week, per workflow.
- **Errors caught** by QA workflows before they cost money.
- **Speed-to-lead:** time from inquiry to first response.
- **Test velocity:** number of creative and landing page tests launched per month.
- **Decision speed:** time from data to action on key issues.

Hours saved are only valuable if they are reinvested. Decide in advance what the team will do with the time: more experiments, deeper customer research, better creative.
"""),
("Common mistakes", """
- Starting with a customer-facing chatbot before internal workflows are proven.
- Automating a process nobody has written down.
- Letting AI optimise toward a conversion that is not trusted.
- No named owner, so the workflow quietly breaks.
- Measuring "AI usage" instead of business outcomes.
"""),
("About the author", """
**Saqib Ameer** is an AI Growth Leader based in Dubai and the creator of The AI Growth Stack. He has led growth for SaaS, eCommerce, app, fintech and healthcare brands in the UAE, Germany and Europe for more than ten years, combining hands-on work in ad platforms, analytics and CRM with an MSc in Computer Science.

He helps companies design and install AI marketing workflows, run performance marketing on unit economics and build lifecycle automation.

Contact: hello@saqibameer.com · saqibameer.com
"""),
]}

REPORTS = [WHITEPAPER, COMPENDIUM, PLAYBOOK]
