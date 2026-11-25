"""The AI Growth Stack (book). Convert, Retain, Scale."""

PART2B = [
("Chapter 5 · Convert: from click to customer", """
You can buy traffic. You cannot buy conversion. This layer is where most companies leave the most money on the table, and where AI gives the fastest return, because every improvement multiplies the value of the spend above it.

## The four conversion moments

1. **The first page.** Does the landing page match the promise in the ad or the search query?
2. **The first commitment.** Is the form, booking or trial sign-up as easy as it can be?
3. **The first value.** Does a new lead, patient or trial user get a useful result fast?
4. **The decision.** Does a sales call, follow-up or reminder arrive at the right time with the right message?

## Landing pages in the AI era

- **One page per intent.** "Dermatology clinic Abu Dhabi" and "laser hair removal price Dubai" deserve different pages.
- **Build fast, test fast.** Tools like Lovable, Framer AI, Webflow and Claude can produce a working page in an hour. The bottleneck is now the offer and the proof, not the build.
- **Proof above the fold.** Numbers, reviews, accreditations and faces.
- **Arabic and English** (or German and English) as real versions, not machine translations nobody checked.

## Lead scoring and speed to lead

In healthcare and real estate, the lead that is called back within five minutes is far more likely to convert than the one called back the next day. AI makes instant response possible:

- **WhatsApp and web chat agents** answer common questions, qualify the lead and book a slot 24/7, then hand over to a human.
- **AI lead scoring** reads form answers, page behaviour and source to rank leads, so sales calls the best ones first.
- **Call summaries**: AI transcribes and summarises sales calls into the CRM, so follow-up is consistent.

## Nurture that actually nurtures

For SaaS trials, the nurture sequence is the product's second salesperson. The structure I use:

| Day | Message | Goal |
|---|---|---|
| 0 | Welcome and one quick win | First value within 10 minutes |
| 1 | The feature most paying customers use first | Activation |
| 3 | A customer story in their segment | Proof |
| 5 | Offer of a short demo or setup call | Human touch |
| 7–10 | Trial expiry reminders with a clear next step | Decision |
| After expiry | Win-back with a reason to return | Recovery |

AI personalises each message by segment, role and behaviour, but the structure stays human-designed.

## From my work

At the **B2B analytics SaaS company in Germany**, behavioural email segmentation (activation, demo, support, reminders and trial expiry) worked together with paid search. Trial-to-paid conversion rose 12%.

At the **fintech SaaS scale-up in Germany**, landing page UX work, A/B testing and onboarding improvements lifted onboarding completion by 18%.

At the **networking app in Germany**, landing page and call-to-action work raised landing page conversion by 25% and click-to-install by 35%.

## Prompt to try

> Act as a conversion copywriter. Here is my ad, my landing page copy and the top five objections from sales calls. Rewrite the page so the headline matches the ad promise, each objection is answered with proof, and there is one clear call to action. Give me two versions to A/B test.

## Convert checklist

- Every major intent has its own landing page.
- Leads get a response within five minutes, 24/7.
- Lead scoring sends the best leads to humans first.
- Trial users get a clear first win on day 0.
- At least one conversion test runs every two weeks.
"""),
("Chapter 6 · Retain: grow the customers you already paid for", """
Acquisition costs keep rising. Retention is where margin is made. Yet in most growth teams I join, retention belongs to nobody: product thinks it is marketing's job, marketing thinks it is customer success's job.

## What retention means by business model

| Model | Retention looks like | Key metric |
|---|---|---|
| DTC and eCommerce | Second purchase, subscription, referral | Repeat purchase rate, 90-day LTV |
| SaaS | Activation, expansion, renewal | Net revenue retention, logo churn |
| Healthcare | Follow-up visits, treatment plans, reviews | Return visit rate, review volume |
| Real estate | Referrals, repeat investors, community | Referral share of sales, investor repeat rate |

## Four retention engines

1. **Onboarding.** The first 7–30 days decide most churn. Map the moments where users drop and fix them one by one.
2. **Lifecycle messaging.** Email, WhatsApp, SMS and in-app messages triggered by behaviour, not by calendar.
3. **Community.** A place where customers learn from each other. It lowers support load and raises loyalty.
4. **Churn signals.** Usage drops, support tickets and payment failures, flagged early so a human can step in.

## Where AI helps

- **Churn prediction.** Feed usage and billing data to a simple model (or ask Claude or ChatGPT to analyse an export) to find the behaviours that come before churn.
- **Personalised win-backs.** AI writes messages based on what each customer actually used.
- **Community management.** AI summarises discussions, drafts answers and spots unhappy members for a human to contact.
- **Review generation.** For clinics and local businesses, automated post-visit messages asking for reviews, with replies drafted by AI and approved by staff.

## From my work

At the **fintech SaaS scale-up in Germany**, we built a community from zero to 1,200 active members. Alongside better onboarding, this was a main reason MQL to SQL conversion improved by 16%. People who joined the community understood the product better before they ever spoke to sales.

At the **developer SaaS startup in Germany**, automated email funnels for trial engagement and retention were part of the growth engine that lifted organic sign-ups by 32%.

For a **coach's personal brand in Germany**, consistent content, email outreach and LinkedIn strategy grew the audience by 300+ followers and 500+ profile views a week. That is retention for a personal brand: people coming back.

## Retain checklist

- Someone owns retention, with a number.
- The first 30 days of the customer journey are mapped and measured.
- Lifecycle messages are triggered by behaviour.
- Churn signals are flagged weekly.
- Reviews and referrals are asked for automatically at the right moment.
"""),
("Chapter 7 · Scale: agents, automation and reporting", """
Scale is the top layer. It is where AI agents and automation let a small team do the work of a large one. It comes last for a reason: automation multiplies what is underneath. With strong layers below, it is a superpower. Without them, it is an expensive way to make mistakes faster.

## What to hand to AI, and what to keep

I use a simple test for every marketing task: **volume, rules and risk.**

| | Low risk | High risk |
|---|---|---|
| **High volume, clear rules** | Automate fully (reporting, tagging, ad variations, lead routing) | Automate with human approval (bid changes, budget shifts, outbound messages) |
| **Low volume, unclear rules** | AI assists a human (research, first drafts, analysis) | Keep human (positioning, pricing, crisis comms, partnerships) |

## The 2026 agent layer

AI agents can now browse, use tools, write code and run multi-step tasks. In marketing operations I use them for:

- **Research agents.** Manus, ChatGPT agent mode, Claude and Perplexity can research competitors, pull pricing, read reviews and summarise markets in an hour instead of a week.
- **Build agents.** Claude Code, Cursor and Lovable build landing pages, tracking scripts, dashboards and small internal tools. This book's companion website was built and deployed this way, on Cloudflare.
- **Workflow automation.** n8n, Make and Zapier connect CRM, ad platforms, sheets and messaging, with an LLM step where judgement is needed.
- **Edge automation.** Cloudflare Workers run lightweight scripts at low cost: server-side tracking, form handling, scheduled reports and API glue.
- **Open models.** Hugging Face gives access to open models for classification, translation and image work where you want control over data or cost.

## The weekly CEO memo

The single most valuable automation I recommend: a reporting agent that writes the weekly growth memo.

1. Every Monday at 7am, a scheduled workflow pulls last week's numbers from GA4, Google Ads, Meta, the CRM and billing.
2. An LLM compares them to the previous four weeks and to targets.
3. It writes a one-page memo in plain English: what moved, why it probably moved, what to do next, and what needs a decision.
4. A human reads it, edits it in five minutes and sends it.

That replaces half a day of manual reporting with five minutes of review, and leadership gets a consistent story every week.

## AI staffing: the lean growth team

In 2026, I design growth teams as **humans plus agents**. A typical setup for a company doing $2M–$20M:

| Role | Human | AI support |
|---|---|---|
| Growth lead | 1 (often fractional) | Research agent, reporting agent |
| Performance marketer | 1 | Creative generation, bid monitoring, anomaly alerts |
| Content and brand | 1 | Drafting, repurposing, localisation, video generation |
| Marketing ops | 0.5 | Workflow automation, CRM hygiene, tracking QA |
| Sales or front desk | As needed | WhatsApp and chat agents, call summaries, lead scoring |

Three and a half people with a well-designed agent layer can now out-produce a traditional team of ten. The skill that matters most is no longer doing the task. It is **designing, checking and improving the system that does it**.

## From my work

At the **networking app in Germany**, combining app campaigns, store optimisation and a steady flow of video creative scaled installs by 40% and app users by 60%, with ROAS above 3.2x on app campaigns. Much of that came from producing and testing creative faster than a traditional team could.

Across 50+ projects at a **digital agency serving international clients**, standardising how campaigns were built, reported and improved is what allowed client ROI gains of around 80% via paid search and segmentation. That standardisation is exactly what AI agents now make cheaper.

## Scale checklist

- Every recurring task is scored on volume, rules and risk.
- The weekly growth memo is automated and human-reviewed.
- Every agent or workflow has an owner, a metric and a kill switch.
- Bid and budget changes over a set limit need human approval.
- The team reviews its automation list monthly and switches off what does not earn its place.
"""),
]
