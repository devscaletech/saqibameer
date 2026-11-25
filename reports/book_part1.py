"""The AI Growth Stack (book). Part 1 and Part 2 opening chapters."""

FRONT = [
("A note before we start", """
I have spent more than eight years inside growth teams: as an agency lead running 50+ projects for international clients, as a marketing manager and CMO for SaaS and app companies in Germany, and today leading AI-led growth for healthcare in the UAE and real estate in Saudi Arabia.

Across all of that work, one pattern keeps repeating. The companies that grow are not the ones with the biggest budgets or the most tools. They are the ones that **fix the order of operations**: they measure properly, then acquire, then convert, then keep the customers they paid for, and only then scale with automation. AI makes every one of those steps faster. It also makes every mistake in that order more expensive.

This book is the method I use. I call it **The AI Growth Stack**. It is written for founders, CMOs and growth leads at DTC brands, eCommerce stores and SaaS companies, roughly in the $1M to $50M revenue range, who want to grow faster without simply spending more.

**How to read it.** Part 1 explains why growth broke and what the stack is. Part 2 takes each of the five layers in turn. Part 3 shows how to make it run inside a real team, with scenarios from my own work. Part 4 covers guardrails and where this is heading. Every layer chapter ends with a checklist you can use on Monday morning.

**A word on the examples.** Every result in this book comes from engagements I led. I describe the companies by sector and country rather than by name. Where I describe a scenario and what to aim for, I say so clearly. Results depend on context, and nothing here is a guarantee.

> Growth in 2026 is not a tools problem. It is an order-of-operations problem that AI makes faster to solve, and faster to get wrong.

*Saqib Ameer, Dubai, November 2026*
"""),
]

PART1 = [
("Chapter 1 · The growth squeeze", """
Most growth teams I meet in 2026 are working harder for less. The symptoms are the same whether the company is a German SaaS startup, a Dubai clinic or a Saudi real estate developer.

## Five forces squeezing growth

1. **Paid media got more expensive and less visible.** Auction prices rose while privacy changes (iOS app tracking, cookie loss, consent mode) removed much of the signal ad platforms used to optimise. Platforms filled the gap with modelled conversions and black-box campaign types. If your tracking is weak, the algorithm is optimising on guesses.
2. **Search is splitting.** Buyers now ask ChatGPT, Claude, Gemini and Perplexity before they ever reach Google, and Google itself answers more questions with AI Overviews and AI Mode. Ranking a blog post is no longer enough. You need to be the source those answers cite.
3. **Content became free to produce and expensive to stand out.** Every competitor can now publish 100 articles and 500 ad variations a month. Volume is no longer an advantage. Specific, experience-backed content is.
4. **Teams are smaller.** Many companies cut marketing headcount in 2023–2025 and expected the same output. The gap was meant to be filled by AI, but in most teams AI is used ad hoc, one person and one prompt at a time.
5. **Boards want efficiency, not just growth.** CAC payback, contribution margin and blended ROAS are now the numbers that get budgets approved.

## Why adding AI tools on top makes it worse

The instinct is to buy a stack of AI tools and plug them into the existing funnel. I have seen this fail many times, for one reason: **AI amplifies whatever system it touches.**

- Feed an AI bidding strategy bad conversion data and it will spend faster on the wrong people.
- Ask an AI writer for 50 landing pages without a clear offer and you get 50 forgettable pages.
- Automate follow-up emails without a clean CRM and you email the wrong people, faster.

> AI is a multiplier. Multiply a broken funnel and you get a bigger broken funnel.

## What actually works

In the engagements behind this book, the biggest gains came from fixing things in a specific order:

| Step | What it fixed | Example result from my work |
|---|---|---|
| Measure | Clean conversion data and cohort visibility | Fintech SaaS in Germany: CAC down 22% |
| Acquire | Segmented, intent-based paid and organic | Medical center in Abu Dhabi: Google Ads clicks +60% |
| Convert | Trials, landing pages and nurture | Analytics SaaS in Germany: 1,000+ trials at about €1.40 each |
| Retain | Community, onboarding, lifecycle | Fintech SaaS: community 0 to 1,200, MQL to SQL +16% |
| Scale | Automation and reporting | Networking app in Germany: 3.2x+ ROAS on app campaigns |

That order is the AI Growth Stack.

## Checklist: are you in the squeeze?

- Your blended CAC has risen for three or more quarters.
- You cannot say, with confidence, which channel produced last month's revenue.
- Your team uses AI tools, but nobody owns how they are used.
- Organic traffic is flat or falling while AI search grows.
- Reporting takes more than half a day a week.

If three or more are true, start with Chapter 3.
"""),
("Chapter 2 · The AI Growth Stack in one page", """
The AI Growth Stack is a five-layer model. Each layer depends on the one below it. You can work on several at once, but you cannot skip one.

| Layer | Question it answers | What AI does here | Core metric |
|---|---|---|---|
| 05 · Scale | How do we grow without adding headcount? | Agents, workflow automation, reporting | Output per person, CAC payback |
| 04 · Retain | Do customers stay, buy again and refer? | Lifecycle personalisation, churn signals, community | Retention, LTV, referral rate |
| 03 · Convert | Do visitors become leads, trials and buyers? | Landing page testing, lead scoring, nurture | Conversion rate, trial to paid |
| 02 · Acquire | Are we reaching the right people at the right cost? | Creative generation, bidding, AI search visibility | CAC, CPL, ROAS |
| 01 · Signal | Do we know what is actually working? | Tracking QA, attribution, anomaly detection | Data match rate, reporting confidence |

## The three rules

1. **Signal before scale.** No automation goes live on a metric you do not trust.
2. **Humans set the strategy, AI runs the reps.** Positioning, offer and brand voice stay human. Variations, analysis and routine execution go to AI.
3. **Every AI workflow has an owner and a number.** If nobody owns it and it does not move a number, switch it off.

## How the layers fit together

Think of the stack as a building. Signal is the foundation. Acquire and Convert are the main floors where money is made. Retain is what stops the building leaking. Scale is the lift that lets you add floors without adding stairs.

Most companies I work with have spent heavily on floor two (Acquire) and almost nothing on the foundation (Signal). That is why their acquisition costs keep rising.

## Where to start

Score each layer from 1 (missing) to 5 (excellent) using the scorecard in the appendix. Then:

- **Any layer scores 1 or 2:** fix the lowest one first, starting from the bottom.
- **All layers score 3 or more:** go to Scale and automate the repeated work.
- **Signal scores below 3:** stop new AI automation until it is fixed.

## The 2026 reality check

Every layer now has strong AI tools, and many are cheap or free. The constraint is no longer access. It is **judgement**: knowing which tool to point at which problem, in which order. The rest of this book is about building that judgement.
"""),
]

PART2A = [
("Chapter 3 · Signal: measure before you automate", """
Signal is the layer nobody wants to fund and everybody depends on. It is the system that tells you what is working. When it is weak, every other layer is guessing.

## What good signal looks like in 2026

- **One source of truth** for leads, trials, purchases and revenue, usually your CRM or backend, not the ad platforms.
- **GA4 configured for the business**, with key events that match real outcomes rather than page views.
- **Server-side tracking** sending conversions directly to Google (Enhanced Conversions) and Meta (Conversions API), so ad platforms get the signal browsers now block.
- **Consent mode v2** set up properly, especially for EU and UK audiences.
- **Offline conversions** fed back to the platforms: a qualified lead, a booked appointment, a signed contract, a paid invoice.
- **UTM discipline**, so every link is labelled the same way.

## The Signal method

1. **Map the money.** Write down the 5–8 events that matter, from first visit to revenue. For a clinic that might be: call click, form submit, booking, show-up, treatment paid. For a SaaS company: sign-up, activation, demo, paid, expansion.
2. **Audit what you capture.** For each event, check: is it tracked, is it deduplicated, is it sent to each ad platform, and does it match the CRM within 10%?
3. **Move tracking to the server.** Use Google Tag Manager server-side, a Cloudflare Worker, or a tool like Stape to send events from your own domain.
4. **Close the loop.** Upload qualified and paid outcomes back into Google Ads and Meta, ideally daily and automatically.
5. **Add a watchdog.** An AI agent checks every morning that event volumes are within normal range and alerts you when a tag breaks.

## Where AI helps

- **Tracking QA.** Paste your GTM container export or GA4 event list into Claude or ChatGPT and ask it to find duplicates, missing parameters and naming conflicts.
- **Anomaly detection.** A scheduled script (a Cloudflare Worker, n8n or Make) pulls yesterday's numbers and asks an LLM to flag anything outside normal range in plain English.
- **Attribution sense-checks.** Give the model a month of channel data and your CRM revenue, and ask where the platforms over-claim.

## From my work

At a **developer SaaS startup in Germany**, where I served as CMO, much of the early work was invisible: rebuilding tracking and trial funnels so that marketing and product saw the same numbers. Once the team could see which sources produced active users, rather than just sign-ups, we shifted effort accordingly. Organic sign-ups rose 32% and brand awareness rose 60% in four months.

At a **fintech SaaS scale-up in Germany**, cohort analysis and funnel analytics (CAC, LTV and blended ROAS by cohort) were the basis for every budget decision. That is what made the 22% CAC reduction possible: we could see which spend was producing customers who stayed.

## Prompt to try

> You are a senior marketing analytics engineer. Here is my GA4 event list and my CRM pipeline stages. Map each CRM stage to a GA4 event, list any stage with no event, list any event that is duplicated or badly named, and propose a clean naming scheme. Output a table.

## Signal checklist

- The 5–8 money events are written down and agreed.
- Server-side conversions are live for Google and Meta.
- Offline outcomes (qualified, booked, paid) are uploaded at least weekly.
- Platform conversions match the CRM within 10–15%.
- An automated daily check alerts someone when tracking breaks.
- Consent mode is set correctly for every market you sell into.
"""),
("Chapter 4 · Acquire: paid and organic with AI in the loop", """
Acquisition is where most budgets go and where AI has changed the most. The platforms themselves are now AI systems. Your job has shifted from pulling levers to **feeding the machine the right inputs**: clean signal, strong creative, a clear offer and the right structure.

## Paid media in 2026

**Google.** Performance Max, broad match with Smart Bidding, and newer AI-driven campaign options now handle most of the bidding and placement. What still wins:

- Campaigns split by **intent and market**, not one big campaign for everything.
- Value-based bidding fed by real outcomes from your CRM.
- Search themes, audience signals and brand exclusions set deliberately.
- Landing pages written for the specific query intent.

**Meta.** Advantage+ campaigns do the targeting. Creative is now the targeting. What wins:

- A steady flow of **new creative concepts** every week, not just variations of one ad.
- Clear angles per persona: problem, outcome, proof, offer.
- Lead forms with qualifying questions, synced to the CRM in real time.
- Retargeting built on engaged audiences, not just site visitors.

**LinkedIn** remains the best paid channel for B2B SaaS decision makers, but only with tight audiences and thought-leadership-style creative.

## Creative at AI speed

The biggest change I have made in my own workflow is how creative is produced.

| Task | Tools I use or recommend | What to watch |
|---|---|---|
| Angles, hooks and scripts | Claude, ChatGPT, Moonshot's Kimi | Feed real customer language from reviews and calls |
| Static ad images | Midjourney, ChatGPT image generation, Canva AI, Google's image models | Brand consistency, no fake claims or text errors |
| Video ads and UGC-style clips | Higgsfield, Runway, Google Veo, Kling, HeyGen | Label AI clearly where required; check likeness rights |
| Voiceovers and localisation | ElevenLabs | Arabic and German need a native review |
| Variation at scale | Canva bulk create, Figma plugins, AdCreative-type tools | Test concepts, not just colours |

> The rule: AI generates the options, the market picks the winner, and a human decides what the brand will and will not say.

## Organic and AI search

Search engine optimisation is now **answer engine optimisation** as well. Buyers ask AI assistants which clinic, which CRM, which agency. To be cited:

1. **Publish specific, experience-backed content**: real numbers, real processes, named authors with credentials.
2. **Structure pages for extraction**: clear headings, short answers, FAQ sections, tables and schema markup.
3. **Be mentioned elsewhere**: reviews, directories, podcasts, LinkedIn and industry press. AI models trust what many sources repeat.
4. **Keep the technical basics strong**: speed, crawlability and clean sitemaps. Make sure AI crawlers are allowed if you want to be cited.
5. **Track AI visibility**: ask the major assistants your top 20 buyer questions every month and record who they recommend.

## From my work

At a **multi-specialty medical center in Abu Dhabi**, I owned digital marketing end to end. We rebuilt Google Search around high-intent service-line campaigns and ran Meta lead generation with audience segmentation, retargeting and constant creative testing. Google Ads clicks rose 60%, and Meta leads came in at around AED 15 each in a regulated, trust-sensitive category.

At a **B2B analytics SaaS company in Germany**, I segmented Google Ads by market (UK, Europe, Germany, DACH and the Middle East) and by intent (free trial versus sign-up). Paired with email nurture, this produced over 1,000 trial sign-ups at a blended cost of about €1.40 per trial.

At a **professional networking app in Germany**, Google and Meta app campaigns, combined with app store optimisation and new video creative, drove a 40% rise in paid installs and 3.2x+ ROAS.

## Acquire checklist

- Campaigns are split by market and intent.
- Bidding uses real outcomes (qualified lead, paid), not just form fills.
- At least 3–5 new creative concepts go live every week.
- Every persona has its own angle, proof and offer.
- You track who AI assistants recommend for your top buyer questions.
- Brand and compliance review happens before AI creative goes live.
"""),
]
