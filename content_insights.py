"""Long-form insights for saqibameer.com.

Every figure quoted here comes from Saqib Ameer's own case studies, resume and
portfolio (Google Drive "SA - My Portfolio"). Anything illustrative is labelled
as an example. Articles are written in a tiny markdown dialect, see md() below.
"""
import html as _h
import re

AUTHOR = "Saqib Ameer"
PUBLISHED = "November 2026"


def _inline(s):
    s = _h.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a class="link" href="\2">\1</a>', s)
    return s


def md(text):
    """## h2, ### h3, - bullets, 1. numbered, > pull quote, | table rows, blank line = paragraph."""
    out, buf, lst, tbl = [], [], None, []

    def flush():
        nonlocal buf, lst, tbl
        if buf:
            out.append("<p>" + _inline(" ".join(buf)) + "</p>")
            buf = []
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{_inline(i)}</li>" for i in items) + f"</{tag}>")
            lst = None
        if tbl:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in tbl if not set(r.replace("|", "").strip()) <= set("-: ")]
            head, body = rows[0], rows[1:]
            out.append('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{_inline(c)}</th>" for c in head) +
                       "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in body) +
                       "</tbody></table></div>")
            tbl = []

    for raw in text.strip().splitlines():
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush(); continue
        if s.startswith("## "):
            flush(); out.append(f"<h2>{_inline(s[3:])}</h2>"); continue
        if s.startswith("### "):
            flush(); out.append(f"<h3>{_inline(s[4:])}</h3>"); continue
        if s.startswith("> "):
            flush(); out.append(f"<blockquote>{_inline(s[2:])}</blockquote>"); continue
        if s.startswith("|"):
            if buf or lst:
                b, l = buf, lst; buf, lst = [], None
                if b: out.append("<p>" + _inline(" ".join(b)) + "</p>")
                if l: out.append(f"<{l[0]}>" + "".join(f"<li>{_inline(i)}</li>" for i in l[1]) + f"</{l[0]}>")
            tbl.append(s); continue
        m = re.match(r"^(\d+)\.\s+(.*)", s)
        if s.startswith("- ") or m:
            tag = "ol" if m else "ul"
            item = m.group(2) if m else s[2:]
            if buf:
                out.append("<p>" + _inline(" ".join(buf)) + "</p>"); buf = []
            if lst and lst[0] == tag:
                lst[1].append(item)
            else:
                if lst: flush()
                lst = (tag, [item])
            continue
        if lst or tbl:
            flush()
        buf.append(s)
    flush()
    return "\n".join(out)


ARTICLES = [
{
"slug": "ai-growth-stack-tracking-before-ai",
"kicker": "Framework",
"title": "The AI Growth Stack: why tracking comes before AI",
"dek": "AI amplifies whatever it touches. Point it at broken data and you scale waste. Here is the order I install growth systems in, and why Signal always comes first.",
"read": 9,
"body": """
Every marketing team I talk to in 2026 has the same tools. ChatGPT and Claude for copy. Meta Advantage+ and Google Performance Max for buying. An AI feature in every CRM. And yet results across those teams are wildly different.

The difference is not the tools. It is the *order* in which the tools are put to work. After more than a decade running paid media, funnels and lifecycle programs for SaaS, eCommerce, app and healthcare brands, I have settled on a five-layer model I call **The AI Growth Stack**. This article explains the model and, more importantly, why the first layer is the one most teams skip.

## The five layers

| Layer | Job | Typical failure when skipped |
|---|---|---|
| 01 Signal | Data, tracking, attribution | AI optimises toward the wrong conversion |
| 02 Acquire | Paid and organic demand | Spend scales before unit economics are known |
| 03 Convert | Pages, offers, journeys | Traffic arrives at a leaky funnel |
| 04 Retain | Lifecycle and CRM automation | Every customer is bought twice |
| 05 Scale | AI agents and workflows | Automation multiplies the problems above |

The layers are built bottom-up. Each one makes the next cheaper, faster and more accurate. Skipping a layer does not save time. It moves the cost somewhere harder to see.

## Why Signal comes first

Modern ad platforms are machine-learning systems. When you choose a "Maximise conversions" strategy, you hand the algorithm a target and a budget and let it search. That is powerful, but it means the definition of "conversion" is now the most important strategic decision in the account.

If the conversion event fires twice, the algorithm learns that the cheapest way to win is to find people who trigger duplicate events. If it fires on a page view instead of a completed sign-up, the algorithm buys page views. If offline revenue never flows back, the algorithm cannot tell a €10 customer from a €10,000 one.

> AI does not fix bad tracking. It scales it, faster and with more confidence than any human media buyer ever could.

At Qmantic, a B2B SaaS analytics company, the Google Ads account was structured around clearly separated conversion objectives: free trials and sign-ups, split by market (UK, Europe, Germany, DACH and Middle East). Over the period from July 2023 to July 2024 the account recorded **6.78K clicks, 105K impressions and 1.35K conversions on €3.8K of recorded spend**. Those numbers were only meaningful, and only optimisable, because each campaign bid toward a specific, correctly measured action.

## What "Signal" actually includes

When I audit the Signal layer, I check five things:

1. **One source of truth for conversions.** GA4 or the CRM decides what counts. Ad platforms receive that definition, they do not invent their own.
2. **Event hygiene.** No duplicates, consistent naming, and a documented event map that a new hire can read.
3. **Value, not just volume.** Trials, demos and purchases carry a value so bidding can prefer better customers.
4. **Cohort views.** CAC and LTV by acquisition month and channel, not blended across the whole history.
5. **Technical foundations.** Sitemap, robots.txt, analytics coverage and page speed. At Qmantic the on-page audit documented exactly these items before any scale-up.

## What changes when Signal is fixed

At CHAMELAION, a SaaS company selling into the DACH region, building cohort-based attribution was the step that unlocked the rest. Once we could see CAC, LTV and blended ROAS by channel and persona, the media plan changed: budget moved toward the segments that actually paid back. The result was a **22% reduction in customer acquisition cost** and a **16% lift in MQL-to-SQL conversion**, alongside **45% organic traffic growth in four months**.

None of that came from a new AI tool. It came from giving the existing tools, including the platforms' own AI, a correct target.

## How to start this week

- List every conversion event you send to ad platforms. Delete or demote anything that is not a real business outcome.
- Pick one primary conversion per funnel stage and give it a value.
- Build a simple monthly cohort table: new customers, spend, CAC, 90-day revenue.
- Only then ask where AI can help. You will find the answer is "almost everywhere", and now it will help in the right direction.

The rest of the stack, Acquire, Convert, Retain and Scale, is where the visible wins come from. But they all stand on Signal. Build it first.

*Download the full framework as a PDF: [The AI Growth Stack whitepaper](assets/pdf/ai-growth-stack-whitepaper.pdf).*
"""
},
{
"slug": "cut-cac-22-percent-without-cutting-spend",
"kicker": "Paid media",
"title": "How I cut CAC by 22% without cutting spend",
"dek": "Persona targeting, bid discipline and funnel segmentation. A step-by-step breakdown of the work behind a 22% CAC reduction for a SaaS company in the DACH market.",
"read": 8,
"body": """
The fastest way to lower customer acquisition cost is to spend less. It is also the fastest way to stop growing. When I joined CHAMELAION, a SaaS company targeting regulated DACH markets, the brief was the opposite: keep investing across Google, Meta, LinkedIn and programmatic, but make each euro work harder.

Over the following months we reduced CAC by **22%**, improved MQL-to-SQL conversion by **16%** and grew organic traffic by **45% in four months**. This is how.

## Step 1: Replace one audience with several personas

The account had been targeting one broad "decision maker" audience. In practice, three or four different people were buying, each with different triggers, objections and channels. We rebuilt targeting around those personas.

- Each persona got its own ad groups, creative angle and landing page variant.
- LinkedIn handled job-title precision; Google captured active search intent; Meta and programmatic re-engaged people who had already shown interest.
- Messaging spoke to the persona's job, not to the product's feature list.

Precision targeting raises CPMs a little and lowers wasted clicks a lot. The net effect on CAC was strongly positive.

## Step 2: Bid toward the right event

Platforms optimise toward whatever you tell them is a conversion. We separated soft actions (content downloads, newsletter sign-ups) from hard ones (demo requests, qualified sign-ups) and bid on the hard ones wherever volume allowed. Soft actions were kept for audience building, not for bidding.

## Step 3: Segment the funnel, then fix the leaks

With cohort-based attribution in place, we could see where each persona dropped. That turned a vague "conversion rate is low" into a list of specific fixes:

1. Landing pages rewritten per persona, with one clear call to action.
2. Forms shortened to the fields sales genuinely used.
3. A/B tests on headlines, proof points and page layout, run one variable at a time.

UX and A/B testing on these pages is what drove the **16% improvement in MQL-to-SQL conversion**. Better leads in, better leads out.

## Step 4: Build an organic engine to carry part of the load

Paid acquisition gets more expensive the harder you push it. In parallel we invested in technical SEO, content syndication and backlinks. Within four months organic traffic was up **45%**, which reduced dependency on paid channels and lowered blended CAC further.

## Step 5: Give the community a job

We grew the product community from **zero to 1,200 active members**, and improved onboarding completion by **18%**. Community members converted better, churned less and referred others. A community is the cheapest acquisition channel most SaaS companies never build.

## What made the difference

> The 22% did not come from one clever trick. It came from making every layer a little more accurate: who we targeted, what we bid on, where people landed and what happened next.

If you want to try this on your own account, start with the persona exercise. Write down every distinct buyer, what they search for and what they fear. Most accounts I audit are one persona short, or three personas too broad.

*See all results in the [case study compendium (PDF)](assets/pdf/saqib-ameer-case-study-compendium.pdf).*
"""
},
{
"slug": "google-ads-plus-email-nurture-saas-trials",
"kicker": "Automation",
"title": "From click to customer: pairing Google Ads with email nurture",
"dek": "How a B2B SaaS analytics company turned paid search into a full lifecycle system, with market-segmented campaigns and behaviour-based email follow-up.",
"read": 8,
"body": """
Most SaaS ad accounts stop at the sign-up. The campaign reports a conversion, the dashboard turns green, and then the new trial user receives one generic welcome email and silence. At Qmantic, a B2B SaaS company offering AI-powered data analysis and cloud BI, we treated the sign-up as the start of the job, not the end.

## The acquisition side

We started with demand, not budget. Keyword research connected Qmantic's value proposition to the language prospects were already searching: AI data analysis, cloud BI, dashboards, reporting. The working sheet combined search volumes, CPC estimates and draft ad copy so research flowed straight into campaign build.

The account was then segmented on two axes:

- **Market:** separate campaigns for the UK, Europe, Germany, DACH and the Middle East, each with its own budget and language.
- **Intent:** free-trial campaigns for high-intent searchers and sign-up campaigns for earlier-stage interest, both using Maximise Conversions bidding.

From July 2023 to July 2024 the account recorded **6.78K clicks, 105K impressions and 1.35K conversions on €3.8K of spend**. Across the role, integrated paid acquisition and email nurture produced **1,000+ SaaS trial sign-ups**.

## The lifecycle side

A trial is a promise, not a customer. The lifecycle system had one goal: get each new user to their first meaningful result in the product as quickly as possible.

| Trigger | Message | Goal |
|---|---|---|
| Sign-up | Confirmation and quick-start | Log in within 24 hours |
| No activation after signup | Guided setup and a demo invitation | First dashboard created |
| Activated user | Feature education and use cases | Habit and depth of use |
| Support interaction | Follow-up and resources | Remove the blocker |
| Trial ending | Reminder with value recap | Upgrade |

Contacts were segmented and tagged by behaviour: registered, activated, non-activated, support contact, influencer contact. Each segment received different templates. This automated onboarding, activation and trigger-based email work improved **trial-to-paid conversion by 12%**.

## The supporting layers

Two less glamorous workstreams made the system hold together:

- **SEO foundation.** An on-page audit documented gaps in titles, meta descriptions, alt text and mobile speed, and confirmed the sitemap, robots.txt and analytics set-up.
- **Social content.** A consistent creative system explained AI analytics, BI Cloud, dashboards, integrations and data security in plain language, as static posts, reels and video, with social engagement up **38%**.

## The lesson

> Paid search buys attention. Lifecycle automation turns it into revenue. Budget for both, or you are paying for half a funnel.

If you run SaaS acquisition, audit what happens in the first 72 hours after a sign-up. Map every email, every in-app prompt and every gap. In my experience that gap is where most of the margin is hiding.
"""
},
{
"slug": "marketing-tasks-for-ai-agents",
"kicker": "AI ops",
"title": "5 marketing tasks to hand to AI agents first",
"dek": "Not every task is ready for AI. These five are repetitive, rule-based and measurable, which makes them the right place to start building a marketing team with an AI shift.",
"read": 7,
"body": """
The question I hear most from founders and CMOs is "where do we start with AI?" The honest answer is: not with the most impressive demo. Start with work that is repetitive, rule-based and easy to check. Those tasks give a fast return and teach the team how to supervise AI before it touches anything customer-facing.

Here are the five I recommend first, roughly in the order I build them.

## 1. Weekly performance reporting

Pulling numbers from Google Ads, Meta, GA4 and the CRM into one view is pure assembly work. An agent can collect the data, compare it with the previous period, flag anomalies and draft a one-page summary in plain language.

- **Human role:** check the flagged anomalies and add the "so what".
- **Guardrail:** the agent never changes budgets on its own.

## 2. Competitor and market research

Monitoring competitor ads, landing pages, pricing and content is valuable and tedious. An agent can collect it weekly and summarise what changed.

- **Human role:** decide whether any change matters.
- **Guardrail:** sources are always cited so claims can be checked.

## 3. Creative briefs and variant drafts

AI is excellent at producing first drafts of ad variants from your best performers: new headlines, new hooks, new angles. The creative team then edits and approves.

- **Human role:** brand voice, taste and final approval.
- **Guardrail:** variants are tested against a control, never shipped blind.

## 4. Campaign QA

Broken links, missing UTM parameters, disapproved ads, budget pacing errors and tracking tags that stopped firing. An agent can check these daily and raise a ticket.

- **Human role:** fix the issue, or approve the agent's fix.
- **Guardrail:** checks are logged so you can see what was caught.

## 5. Lead handling and routing

New leads can be enriched, scored and routed to the right person or nurture sequence in minutes instead of hours. Speed-to-lead is one of the most reliable conversion levers in B2B and service businesses.

- **Human role:** define the scoring rules and review edge cases.
- **Guardrail:** sensitive data is handled inside your CRM, not pasted into public tools.

## What these five have in common

| Task | Repetitive | Rule-based | Easy to verify |
|---|---|---|---|
| Reporting | Yes | Yes | Yes |
| Research | Yes | Mostly | With sources |
| Creative drafts | Yes | Partly | Through testing |
| QA | Yes | Yes | Yes |
| Lead routing | Yes | Yes | Yes |

> Give AI the work your team is bored of, not the decisions your business depends on. Then move up the ladder as trust is earned.

This is the **Scale** layer of the AI Growth Stack. It only works when the layers beneath it are sound: a reporting agent fed by broken tracking will write very confident, very wrong summaries.

*For the full operating model, roles and 90-day rollout, download [The AI Marketing Operations Playbook (PDF)](assets/pdf/ai-marketing-ops-playbook.pdf).*
"""
},
{
"slug": "ga4-tracking-after-ios",
"kicker": "eCommerce",
"title": "Tracking after iOS: a practical GA4 measurement plan",
"dek": "Privacy changes broke a lot of attribution. Here is a practical way to rebuild measurement you can make money decisions on, and what to stop trusting.",
"read": 8,
"body": """
Since Apple's App Tracking Transparency and the wider move away from third-party cookies, every marketer has seen the same symptoms: platform-reported conversions that don't match the shop, ROAS that swings for no reason, and audiences that shrink every quarter. The response should not be panic. It should be a measurement plan.

This is the approach I use for eCommerce and app brands. It is deliberately practical.

## Principle 1: Decide what is true before you decide what to optimise

Your store or CRM knows how many orders and how much revenue came in. That is the truth. GA4 and the ad platforms are *models* of that truth. Every report should be reconciled back to it.

## Principle 2: Measure fewer things, properly

Most accounts I audit track dozens of events and trust none of them. A strong plan has a short list:

| Stage | Event | Notes |
|---|---|---|
| Interest | view_item, add_to_cart | For audiences and diagnostics |
| Intent | begin_checkout | Key leading indicator |
| Outcome | purchase with value | The only event most campaigns should bid on |
| Retention | repeat purchase | Feeds LTV and lifecycle |

## Principle 3: Send first-party data back to the platforms

Server-side tagging and conversion APIs send conversion data from your server rather than relying only on the visitor's browser. Combined with consented first-party data, this restores much of the signal the platforms need to optimise. Set-up details vary by platform, but the principle is the same: the most reliable data you own should be the data the algorithms learn from.

## Principle 4: Use more than one lens

No single attribution model is "right". I use three views side by side:

1. **Platform view** for in-platform optimisation decisions.
2. **GA4 / analytics view** for cross-channel comparison.
3. **Business view**: blended CAC and MER (total revenue divided by total marketing spend) by month and by cohort.

When the three disagree, the business view wins budget decisions.

## Principle 5: Test incrementality when the money is big

If a channel claims a large share of revenue, test it. Geographic holdouts, budget pauses and on/off tests are imperfect but honest. They tell you what would have happened without the spend.

## What to stop trusting

- View-through conversions reported as if they were clicks.
- ROAS from a single platform used to justify total budget.
- Any dashboard nobody can explain the source of.

## A worked example from app growth

At VANCY, a professional networking app in Germany, app growth was measured on installs and active users, not clicks. With ASO, SEO and Google and Meta app campaigns aligned to those outcomes, app users grew **60%**, installs **40%**, and app campaigns delivered **ROAS above 3.2×**. The measurement plan came first; the growth followed.

> Good measurement doesn't make marketing look better. It makes marketing decisions better.
"""
},
{
"slug": "clinic-lead-generation-google-vs-meta",
"kicker": "Healthcare",
"title": "Lead generation for clinics: Google Search vs Meta lead forms",
"dek": "What worked in a regulated, high-intent category: lessons from running end-to-end digital growth for a medical center in Abu Dhabi.",
"read": 7,
"body": """
Healthcare marketing in the UAE is different from selling software or sneakers. Patients search when they have a need, trust is everything, and advertising rules are strict. At House of Nature Medical Center in Abu Dhabi I own end-to-end digital growth: Google Ads, Meta lead generation, website conversion paths, content and local SEO.

Two channels do most of the work, and they do very different jobs.

## Google Search: capture the intent that already exists

People search for a treatment or a clinic when they are ready to act. Search campaigns built around high-intent healthcare keywords put the clinic in front of them at that moment.

- Campaigns are organised by service line, so ads and landing pages match what the patient searched.
- Call and appointment actions are tracked as the primary conversions.
- Negative keywords remove research-only and job-seeker queries.

Over the engagement, this work increased Google Ads clicks by **60%**.

## Meta lead forms: create demand and stay top of mind

Meta does not capture existing intent as well as Search, but it is excellent at reaching the right local audience and bringing them back.

- Lead form campaigns, segmented by service and audience.
- Retargeting for website visitors and engaged social audiences.
- Continuous creative testing: offers, formats and messages.

Lead generation on Meta has been maintained at a cost per lead of around **AED 15**.

## Side by side

| | Google Search | Meta lead forms |
|---|---|---|
| Best at | Capturing ready-to-book intent | Reaching and re-engaging local audiences |
| Typical lead quality | Higher | Varies, needs fast follow-up |
| Main lever | Keyword and landing page match | Creative and audience testing |
| Watch out for | Rising CPCs on competitive terms | Low-intent form fills |

## The part nobody talks about: follow-up

The biggest gains in clinic lead generation usually happen after the lead arrives. Response time, the script on the first call and reminder messages decide whether a lead becomes a patient. Website CTAs, inquiry funnels and Google Business Profile optimisation complete the picture.

> In healthcare, the ad gets the inquiry. The experience after the inquiry gets the patient.

## What I would tell any clinic starting out

1. Start with Search for the services with the clearest demand.
2. Add Meta lead forms once you can answer every lead within minutes.
3. Track booked appointments, not just form fills.
4. Treat your Google Business Profile as a second website.
"""
},
{
"slug": "fractional-growth-leader-first-30-days",
"kicker": "Leadership",
"title": "What a fractional growth leader should own in month one",
"dek": "The first 30 days decide whether a fractional or interim growth lead creates momentum or just more meetings. This is the plan I follow.",
"read": 7,
"body": """
More companies now hire senior growth leadership part-time: a fractional CMO or growth lead who owns strategy and results without a full-time salary. I have worked this way with SaaS and app companies in Germany, including C-level marketing ownership at SQUIDEX.IO, where I built and ran the full go-to-market across brand, performance, content and SEO.

The model works when the first month is structured. Here is how I run it.

## Week 1: Listen and measure

- Interviews with the founder, sales, product and anyone touching customers.
- Access to every ad account, analytics property and CRM.
- A first-pass audit of the Signal layer: what is tracked, what is trusted, what is missing.

**Output:** a one-page "state of growth" with the three biggest problems in plain language.

## Week 2: Pick the bets

Not everything can be fixed at once. I rank opportunities by impact, confidence and effort, and agree on two or three bets for the next 60 days with the leadership team.

**Output:** a 90-day plan with owners, budgets and the metric each bet should move.

## Week 3: Ship the first win

Momentum matters. The first win is usually something fast and visible: fixing conversion tracking, relaunching the best-performing campaign with tighter targeting, or turning on an onboarding email that should have existed already.

**Output:** one shipped improvement with before-and-after numbers.

## Week 4: Build the operating rhythm

- A weekly growth meeting with a fixed agenda: numbers, experiments, decisions.
- A shared dashboard everyone reads from.
- Clear agency and freelancer briefs, with reporting that gives the CEO visibility into ROI.

**Output:** a team that can keep the work going between my sessions.

## What month one is not

> Month one is not the time for a rebrand, a new website or a 60-slide strategy deck. It is the time to understand the numbers, earn trust and prove the approach with one real result.

## Results this approach has supported

At SQUIDEX.IO, running brand, performance, content and SEO as one engine grew brand awareness by **60% in four months** and organic sign-ups by **32%**, with automated email funnels improving trial engagement and retention.

If you are considering fractional growth leadership, ask any candidate one question: "What will be different at the end of week four?" The answer tells you most of what you need to know.
"""
},
{
"slug": "ai-reporting-agent-ceo-memo",
"kicker": "AI ops",
"title": "Building an AI reporting agent your CEO will actually read",
"dek": "From raw platform data to a one-page Monday memo. A practical design for an AI reporting workflow, including the guardrails that keep it honest.",
"read": 8,
"body": """
Most marketing reports are too long, arrive too late and answer questions nobody asked. Leadership wants three things on Monday morning: what happened, why, and what we are doing about it. That is exactly the kind of structured summarising AI is good at, if you design the workflow properly.

## The output first

Start by designing the memo, not the pipeline. A good memo fits on one page:

1. **Headline:** one sentence on the week, for example "Revenue on target; paid social efficiency slipped; fix in progress."
2. **Scoreboard:** five to eight numbers against target and last period (spend, revenue, CAC, ROAS or MER, leads, conversion rate).
3. **What changed and why:** three bullets at most.
4. **Actions:** what the team is doing, who owns it, and what needs a decision.

## The pipeline

| Step | What happens | Who or what does it |
|---|---|---|
| Collect | Pull data from ad platforms, GA4, CRM and store | Scheduled connectors |
| Reconcile | Compare platform numbers with the business source of truth | Rules plus agent checks |
| Diagnose | Flag movements beyond normal ranges and look for likely causes | AI agent |
| Draft | Write the memo in the agreed format | AI agent |
| Review | Check facts, add context, approve actions | Human growth lead |
| Send | Deliver to leadership at a fixed time | Automation |

## Guardrails that keep it honest

- **Every number has a source.** The memo links each figure to where it came from.
- **The agent proposes; people decide.** It can suggest a budget shift but cannot make one.
- **Anomalies need evidence.** "CPA rose because of creative fatigue" must point to the creatives and their trend.
- **Same format every week.** Consistency makes changes visible.

## An illustrative weekly run

*Example with sample data, not a client report:* the agent syncs four sources, notices that prospecting CPA on Meta rose sharply week on week while three ads have run for more than a month, drafts six new variants based on the best performers, proposes moving part of the budget to brand search, queues a win-back flow for lapsed buyers and sends the memo at 09:00, waiting for a human to approve three actions.

## Why it works

> Leaders don't need more data. They need a reliable judgement on the data, delivered at the same time every week.

The reporting agent is often the first AI workflow I build in a business, because it immediately frees hours and it exposes every weakness in tracking. If the memo looks wrong, the Signal layer needs work, and now everyone can see it.

*The full playbook, including a 90-day rollout plan, is available as a [PDF download](assets/pdf/ai-marketing-ops-playbook.pdf).*
"""
},
]

REPORTS = [
    ("the-ai-growth-stack-book.pdf", "Book", "The AI Growth Stack: the book",
     "The full method in 13 chapters: why growth broke, the five layers in depth, cutting CAC without cutting spend, real 2026 scenarios from healthcare in the UAE and real estate in Saudi Arabia, the AI tool stack I use, a 90-day rollout, a scorecard and a prompt library."),
    ("ai-growth-stack-whitepaper.pdf", "Whitepaper", "The AI Growth Stack",
     "The five-layer framework for turning AI into a measurable growth engine: Signal, Acquire, Convert, Retain and Scale, with audit checklists, failure signs and a 90-day sequence."),
    ("saqib-ameer-case-study-compendium.pdf", "Case studies", "Growth Case Study Compendium 2017–2026",
     "Seven engagements across healthcare, SaaS, apps and personal branding: the challenge, what was done and the results, from House of Nature, CHAMELAION, Qmantic, VANCY, SQUIDEX and more."),
    ("ai-marketing-ops-playbook.pdf", "Playbook", "The AI Marketing Operations Playbook",
     "How to give your marketing team an AI shift: which tasks to automate first, roles, guardrails, tooling choices and a practical 90-day rollout."),
]
