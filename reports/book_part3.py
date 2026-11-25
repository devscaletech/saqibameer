"""The AI Growth Stack (book). Parts 3-4 and appendix."""

PART3 = [
("Chapter 8 · Cutting CAC without cutting spend", """
The most common request I get from founders is: "Our CAC is too high. Should we cut the budget?" Usually the answer is no. Cutting budget lowers volume. Fixing the system lowers cost.

Here is the full playbook behind a 22% CAC reduction at a **fintech SaaS scale-up in Germany**, selling into regulated DACH markets, where I owned the marketing P&L across Google, Meta, LinkedIn and programmatic.

## Step 1: Find where the money leaks

We rebuilt reporting around cohorts: for each month's new customers, what did they cost, by channel and campaign, and how much were they worth over time? The answer surprised the team. Some of the cheapest leads were the most expensive customers, because they rarely converted or churned quickly.

## Step 2: Re-segment by persona and intent

We split broad campaigns into persona-based ones with their own messaging, landing pages and bids. Budget moved from "cheap clicks" to "valuable customers".

## Step 3: Fix the funnel in the middle

Landing page UX work and A/B tests, plus onboarding improvements, lifted onboarding completion by 18% and MQL to SQL conversion by 16%. The same spend produced more customers.

## Step 4: Build the organic engine in parallel

Technical SEO, content syndication and a backlink plan grew organic traffic by 45% in four months. Every organic customer lowers blended CAC.

## Step 5: Turn customers into a community

We grew a community from zero to 1,200 active members. It produced referrals, warmer leads and faster sales cycles.

## The result

| Metric | Result |
|---|---|
| Customer acquisition cost | −22% |
| Organic traffic | +45% in 4 months |
| Onboarding completion | +18% |
| MQL to SQL conversion | +16% |
| Community | 0 to 1,200 active members |

## How I would run the same playbook with 2026 AI tools

- **Cohort analysis**: export CRM and billing data and have Claude or ChatGPT build the cohort tables and charts in minutes.
- **Persona messaging**: generate angles from real sales-call transcripts, then test them with AI-produced creative.
- **Landing pages**: build test variants with Lovable or Claude in hours, not weeks.
- **SEO**: research agents map the question space, writers add real experience, schema makes it citable by AI assistants.
- **Community**: AI summarises discussions and flags members who need a human reply.

> The lesson: CAC is not a media number. It is a system number. Fix the system and the media gets cheaper.
"""),
("Chapter 9 · Scenarios: what I would do in 2026", """
This chapter takes four situations I see often and shows how I approach them today. Two come straight from my current work. Where I give numbers, they are either real results from my past engagements (marked **Result**) or the targets I set at the start of this kind of project (marked **Target**). Targets are goals, not promises.

## Scenario 1: Scaling a real estate company in Saudi Arabia from scratch

**Situation.** This is my current work: building growth for real estate businesses in Saudi Arabia, in many cases starting with no brand, no data and no marketing team. The market is moving fast under Vision 2030, buyers research on mobile and WhatsApp, and trust is everything.

**What I do**

1. **Signal first.** Before any ads: a CRM, WhatsApp Business API, call tracking and server-side conversions. Every lead is tagged by project, unit type and source from day one.
2. **Brand and proof.** Project pages in Arabic and English, real progress photos and video, developer credentials and clear payment plans. AI video tools (Higgsfield, Runway, Veo) produce walkthrough and lifestyle content from renders, always labelled as visualisations.
3. **Acquire.** Meta and Snapchat for awareness and lead forms, Google Search for high-intent queries, TikTok for reach in younger segments, and property portals where they perform.
4. **Convert.** An Arabic and English WhatsApp agent answers questions 24/7, qualifies budget and timing, and books a site visit or call for the sales team.
5. **Retain and refer.** Buyers and investors get progress updates and referral offers. Investors are the most valuable repeat customers in this market.
6. **Scale.** A weekly AI memo to leadership: leads, cost per qualified lead, visits, reservations and pipeline value by project.

**Target in the first 90 days:** tracking live for every lead, response time under five minutes, and a cost per qualified lead the sales team agrees is sustainable. From earlier real estate work: **Result:** lead generation up 200%.

## Scenario 2: A clinic in Dubai or Abu Dhabi that needs more patients

**Situation.** Also current work: healthcare marketing in the UAE. Patients compare clinics on Google, Instagram and increasingly AI assistants. Advertising rules for healthcare are strict.

**What I do**

1. Service-line campaigns on Google Search, each with its own landing page.
2. Meta lead generation with qualifying questions and instant WhatsApp follow-up.
3. Google Business Profile, reviews and local SEO for every branch.
4. FAQ-rich, doctor-authored content so AI assistants cite the clinic.
5. Compliance review on every ad and page before it goes live.

**Result** (multi-specialty medical center, Abu Dhabi): Google Ads clicks +60%, Meta leads at around AED 15 each.

## Scenario 3: A DTC or eCommerce brand with rising ad costs

**Situation.** A store spending most of its budget on Meta and Google, with ROAS slipping and no clear retention program.

**What I do**

1. Server-side tracking and value-based bidding fed with real margin data.
2. Weekly creative sprints: 5–10 new concepts using AI image and video tools, with UGC-style content.
3. Product feed optimisation for Shopping and Performance Max.
4. Email and WhatsApp flows: welcome, browse and cart abandonment, post-purchase, win-back.
5. Product pages written to be cited by AI shopping assistants.

**Target:** blended ROAS and contribution margin stable or rising while spend grows. **Result** from app campaigns at a networking app in Germany: ROAS above 3.2x.

## Scenario 4: A SaaS company with plenty of trials and too few customers

**Situation.** Paid search and content bring in sign-ups, but trial-to-paid is low and sales cannot keep up.

**What I do**

1. Define the activation moment and track it.
2. Behavioural nurture by segment, with a demo offer at the right moment.
3. AI lead scoring so sales calls the users most likely to buy.
4. Market and intent split in Google Ads, with bidding on activated trials, not sign-ups.

**Result** (B2B analytics SaaS in Germany): 1,000+ trials at about €1.40 each, trial-to-paid +12%.
"""),
("Chapter 10 · The 2026 AI growth tool stack", """
Tools change every month. This is the stack I use and recommend as of late 2026, grouped by job. Treat it as a starting point: pick one tool per job, learn it well, and review the list every quarter.

## Thinking, writing and analysis

| Tool | What I use it for |
|---|---|
| **Claude** (Anthropic) | Strategy drafts, long documents, analysis of exports, writing in a consistent brand voice, building with Claude Code |
| **ChatGPT** (OpenAI) | Research, agent tasks, image generation, quick analysis |
| **Moonshot AI's Kimi** | Long-context reading, research and a strong second opinion at low cost |
| **Gemini** (Google) | Working inside Google Workspace, YouTube and search research |
| **Perplexity** | Fast, cited research on markets and competitors |

## Agents and automation

| Tool | What I use it for |
|---|---|
| **Manus** | Autonomous multi-step research and execution tasks |
| **Claude Code, Cursor** | Building landing pages, tracking scripts, dashboards and internal tools |
| **Lovable** | Rapid web app and landing page prototypes |
| **n8n, Make, Zapier** | Connecting CRM, ad platforms, sheets and messaging with AI steps in between |
| **Cloudflare (Pages, Workers)** | Hosting fast sites, server-side tracking, form handling and scheduled automations at the edge |

## Creative: image, video and voice

| Tool | What I use it for |
|---|---|
| **Higgsfield** | Cinematic AI video and motion for ads and social content |
| **Runway, Google Veo, Kling** | Text-to-video and image-to-video production |
| **Midjourney, ChatGPT images, Canva AI** | Ad visuals, concepts and on-brand layouts |
| **HeyGen** | Avatar and presenter video, translation and lip-sync |
| **ElevenLabs** | Voiceovers and multilingual audio |

## Models and data

| Tool | What I use it for |
|---|---|
| **Hugging Face** | Open models for classification, translation, embeddings and image tasks where data control or cost matters |
| **GA4, BigQuery, Looker Studio** | Analytics backbone and reporting |
| **HubSpot or another CRM with AI features** | Single source of truth for leads and revenue |

## How I choose

1. **Start from the job, not the tool.** Which task, in which layer, moves which number?
2. **Test with real work.** Run a two-week trial on a live task before rolling a tool out.
3. **Check the data terms.** Know where customer data goes, especially for healthcare and EU audiences.
4. **Keep the stack small.** Ten tools used well beat forty tools used badly.
5. **Review quarterly.** The best tool for a job in January may not be the best in June.
"""),
("Chapter 11 · The 90-day rollout", """
Here is how I roll the AI Growth Stack out in a new company or a new role. It works for a full-time leader or a fractional one.

## Days 1–30: Signal and quick wins

| Week | Focus | Output |
|---|---|---|
| 1 | Listen and map | Interviews with leadership, sales and customers; the money-events map |
| 2 | Audit | Tracking, campaigns, funnel and tools scored with the stack scorecard |
| 3 | Fix signal | Server-side conversions, offline uploads, UTM rules |
| 4 | Quick wins | Wasted spend cut, broken pages fixed, speed-to-lead improved |

## Days 31–60: Acquire and convert

| Week | Focus | Output |
|---|---|---|
| 5 | Restructure | Campaigns split by market and intent |
| 6 | Creative engine | Weekly AI-assisted creative sprint running |
| 7 | Landing pages | One page per major intent, first A/B tests live |
| 8 | Nurture | Lead scoring and lifecycle flows live |

## Days 61–90: Retain and scale

| Week | Focus | Output |
|---|---|---|
| 9 | Retention | Onboarding map, churn signals, review and referral asks |
| 10 | Automate | Weekly CEO memo and anomaly alerts automated |
| 11 | Team | Roles, owners and agent responsibilities written down |
| 12 | Review | Results against baseline, the next 90-day plan agreed |

## What to report at day 90

- CAC, CPL or cost per trial, against the day-1 baseline.
- Conversion rate at each main funnel step.
- Hours of manual work removed by automation.
- The three biggest problems still open, and the plan for each.

> A good first 90 days does not fix everything. It makes the numbers trustworthy, removes the obvious waste and builds the engine for the next 90.
"""),
]

PART4 = [
("Chapter 12 · Guardrails", """
AI makes it easy to move fast. Guardrails make sure you do not move fast in the wrong direction, or into legal trouble.

## Brand and truth

- **No invented claims.** Every number, testimonial and result in an ad must be real and provable. AI will happily invent them.
- **Label AI visuals** where rules or common sense require it, especially for property renders and medical imagery.
- **A brand voice guide** that every AI tool is given, with words you use and words you never use.

## Data and privacy

- **GDPR** for EU audiences, the **UAE PDPL** and Saudi Arabia's **PDPL** in the Gulf. Know what data you collect, why, and where it goes.
- **Never paste patient data or personal customer data** into a tool whose data terms you have not checked. Use business plans with no training on your data, or anonymise first.
- **Consent first.** Consent mode, clear opt-ins for WhatsApp and email.

## Regulated sectors

- **Healthcare**: medical advertising rules in the UAE are strict. Avoid before-and-after claims and guaranteed outcomes, and get approvals where required.
- **Real estate**: payment plans, completion dates and returns must match official project information. Follow the local regulator's advertising rules in each market.
- **Finance and fintech**: performance claims need care, especially in the EU.

## Humans in the loop

| Decision | Who decides |
|---|---|
| Positioning, pricing, offers | Human |
| Budget changes above a set limit | Human approves AI recommendation |
| Ad creative and copy | AI drafts, human approves |
| Routine reporting and alerts | AI, human reviews weekly |
| Customer complaints and sensitive cases | Human, AI assists with summary |
"""),
("Chapter 13 · The next three years", """
Nobody can predict AI precisely, but some directions are already clear from the work I see every day.

## 1. Agents will run most campaign operations

Setting up campaigns, writing variations, adjusting bids, pulling reports: these are becoming agent jobs. The marketer's job becomes setting goals, guardrails and strategy, and checking the work.

## 2. AI assistants become a main buying channel

People will increasingly ask an assistant to find, compare and even buy. Brands need to be the trusted, cited source in those answers, and their products need to be easy for agents to read and transact with.

## 3. Creative becomes infinite, so taste becomes the edge

Anyone can generate a thousand ads. The winners will be the brands with a clear point of view, real proof and the judgement to choose.

## 4. First-party data becomes the moat

As tracking gets harder and AI gets better, the companies with clean, consented, connected first-party data will out-learn everyone else.

## 5. Growth teams get smaller and more senior

Fewer people, more leverage. The most valuable growth people will be those who can design systems of humans and agents, not just run channels.

## How to stay ahead

- Spend one hour a week testing a new tool on a real task.
- Keep a shared prompt and workflow library for your team.
- Rebuild your stack scorecard every quarter.
- Invest in signal and first-party data before anything else.
- Build your own authority: publish what you learn.

> The companies that win the next three years will not be the ones that used AI first. They will be the ones that used it in the right order.
"""),
]

APPENDIX = [
("Appendix A · AI Growth Stack scorecard", """
Score each statement from 1 (not true) to 5 (fully true). Average each layer.

| Layer | Statement |
|---|---|
| Signal | We have agreed, written definitions of our 5–8 money events |
| Signal | Platform conversions match our CRM within 15% |
| Signal | Server-side conversions are live for Google and Meta |
| Signal | Offline outcomes are fed back to ad platforms at least weekly |
| Signal | We are alerted automatically when tracking breaks |
| Acquire | Campaigns are split by market and intent |
| Acquire | Bidding is based on real business outcomes |
| Acquire | We launch new creative concepts every week |
| Acquire | We know who AI assistants recommend in our category |
| Acquire | Organic search brings a growing share of leads |
| Convert | Each major intent has its own landing page |
| Convert | New leads get a response within five minutes |
| Convert | Leads are scored and prioritised |
| Convert | We run at least one conversion test every two weeks |
| Convert | Trial users or new leads get value on day 0 |
| Retain | Someone owns retention, with a target |
| Retain | Lifecycle messages are triggered by behaviour |
| Retain | We track churn or repeat-purchase signals weekly |
| Retain | Reviews and referrals are requested automatically |
| Retain | We have a community or customer program |
| Scale | Recurring tasks are scored for automation |
| Scale | Weekly reporting is automated and reviewed |
| Scale | Every AI workflow has an owner and a metric |
| Scale | Budget changes above a limit need approval |
| Scale | We review our tools and automations monthly |

**Reading the score.** Below 2.5 in any layer means fix that layer next. Signal below 3 means stop new automation until it is fixed.
"""),
("Appendix B · Prompt library", """
Twelve prompts I use often. Replace the brackets with your details.

1. **Tracking audit.** "You are a marketing analytics engineer. Here is my GA4 event list and CRM stages: [paste]. Map each stage to an event, flag gaps and duplicates, and propose clean names in a table."
2. **Persona angles.** "Here are 20 customer reviews and 5 sales-call notes: [paste]. Find the top 5 pains, the words customers use, and write 3 ad angles per pain."
3. **Ad variations.** "Write 10 Meta ad primary texts under 125 characters for [offer] aimed at [persona]. Each must use one proof point from: [list]. No invented claims."
4. **Search ad structure.** "Group these keywords into tightly themed ad groups by intent and market, and suggest 3 headlines per group: [paste keywords]."
5. **Landing page rewrite.** "Rewrite this page so the headline matches this ad: [ad]. Answer these objections with proof: [list]. One call to action. Give two test versions."
6. **Nurture sequence.** "Design a 10-day trial nurture for [product] for [segment]. Day 0 must deliver a quick win. Include subject lines and one CTA per email."
7. **WhatsApp qualifier.** "Write a WhatsApp conversation flow in Arabic and English that qualifies a property lead on budget, timing and unit type, then offers a site visit."
8. **Churn analysis.** "Here is a usage and billing export: [paste]. Find behaviours common in the 30 days before churn and suggest 3 interventions."
9. **AI search check.** "Answer as a buyer would ask: who are the best [category] providers in [city]? List who you recommend and why." Run monthly in each major assistant.
10. **CEO memo.** "Here are this week's and the last four weeks' numbers: [paste]. Write a one-page memo: what moved, likely why, what to do next, and decisions needed."
11. **Competitor scan.** "Research [competitors]. For each: offer, pricing, main ad angles, review themes and weak spots. Output a table and three opportunities for us."
12. **Brand voice check.** "Here is our voice guide: [paste]. Review this copy: [paste]. Flag anything off-voice, unprovable or non-compliant and suggest fixes."
"""),
("About the author", """
**Saqib Ameer** is an AI Growth Leader who helps DTC, eCommerce, SaaS, healthcare and real estate companies grow faster with AI, performance marketing and automation.

He has more than eight years of experience across in-house, consulting and C-level roles, including CMO and marketing leadership for SaaS and app companies in Germany, healthcare marketing in the UAE, and current work scaling real estate growth in Saudi Arabia. Earlier, he led 50+ growth projects for international clients at a digital agency.

Selected results from his work include a 22% reduction in customer acquisition cost, 1,000+ SaaS trials at about €1.40 each, ROAS above 3.2x on app campaigns, and a 60% rise in Google Ads clicks for a medical center.

He holds an MSc and a BSc in Computer Science and is based in Dubai.

**Work with Saqib:** AI growth strategy, fractional growth leadership, AI marketing operations, and speaking.

saqibameer.com · hello@saqibameer.com
"""),
]
