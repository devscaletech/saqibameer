"""Builds the static site in ./site from shared partials. Run: python build.py"""
import json, pathlib

OUT = pathlib.Path(__file__).parent / "site"
DOMAIN = "https://saqibameer.com"
LINKEDIN = "https://www.linkedin.com/in/saqibameer"
EMAIL = "hello@saqibameer.com"
TITLE = "AI Growth Leader"

IMG = {
    "hero": "assets/img/saqib-headshot-cut-bw.webp",
    "hero_full": False,          # True when hero is a full-bleed photo (AI portrait)
    "band": "assets/img/ai/ai-workshop.webp",
    "workshop": "assets/img/ai/ai-workshop.webp",
    "about": "assets/img/saqib-lean-cut-bw.webp",
    "about_cut": True,
    "services": "assets/img/saqib-standing-cut-bw.webp",
    "services_cut": True,
    "g1": "assets/img/saqib-marina-bw.webp",
    "g2": "assets/img/saqib-polo-bw.webp",
    "g3": "assets/img/saqib-terrace-bw.webp",
    "lead": "assets/img/saqib-terrace-bw.webp",
}
_ov = pathlib.Path(__file__).parent / "images.json"
if _ov.exists():
    IMG.update(json.loads(_ov.read_text()))

ARR = '<span class="arr">→</span>'
NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("stack.html", "AI Growth Stack"), ("work.html", "Work"), ("insights.html", "Insights")]

PERSON = {
    "@context": "https://schema.org", "@type": "Person", "name": "Saqib Ameer",
    "jobTitle": TITLE, "url": DOMAIN, "email": "mailto:" + EMAIL,
    "image": DOMAIN + "/assets/img/og.jpg",
    "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
    "sameAs": [LINKEDIN, "https://github.com/saqi097"],
    "alumniOf": ["PMAS Arid Agriculture University Rawalpindi", "University of the Punjab"],
    "knowsAbout": ["AI marketing", "Growth leadership", "Performance marketing", "Marketing automation",
                   "Marketing analytics", "eCommerce", "SaaS", "Go-to-market strategy"],
}


def head(title, desc, path):
    canon = DOMAIN + "/" + ("" if path == "index.html" else path.replace(".html", ""))
    full = f"{title} · Saqib Ameer" if title else f"Saqib Ameer · {TITLE}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A0A0A">
<meta name="author" content="Saqib Ameer">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700&family=Inter:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css?v=3">
<script type="application/ld+json">{json.dumps(PERSON)}</script>
</head>
<body>
<div class="loader" aria-hidden="true"><div class="l-top"><span>Saqib Ameer</span><span>{TITLE} · Dubai</span></div><div class="l-name"><span>Saqib Ameer</span></div><div class="l-bot"><span class="dim" style="font-size:13px">Growth, led by data.<br>Multiplied by AI.</span><span class="l-count">000</span></div><div class="l-bar"></div></div>
<div class="noise" aria-hidden="true"></div>
<div class="progress" aria-hidden="true"></div>
<div class="pt" aria-hidden="true"></div>
<div class="cursor" aria-hidden="true"><span></span></div><div class="cursor-dot" aria-hidden="true"></div>
"""


def nav(cur):
    links = "".join(f'<a href="{h}"{" aria-current=page" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="nav"><div class="wrap">
<a class="logo" href="index.html" aria-label="Saqib Ameer home"><span class="logo-mark">SA</span><span>Saqib Ameer<small>{TITLE}</small></span></a>
<nav class="nav-links" id="menu" aria-label="Main">{links}<a class="btn btn-primary btn-sm nav-cta" href="contact.html">Let’s talk {ARR}</a></nav>
<button class="burger" aria-label="Menu" aria-controls="menu" aria-expanded="false"><span></span><span></span></button>
</div></header>
<main>
"""


FOOT = f"""</main>
<footer><div class="wrap">
<div class="foot-cta"><div><span class="kicker rv">Open to new mandates · 2026</span><h2 class="h-l rv" style="margin-top:20px" data-split>Have a growth problem worth solving?</h2></div>
<div class="hero-ctas rv"><a class="btn btn-primary" href="contact.html">Start a conversation {ARR}</a><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a></div></div>
<div class="foot">
<div><a class="logo" href="index.html"><span class="logo-mark">SA</span><span>Saqib Ameer<small>{TITLE}</small></span></a>
<p class="muted" style="margin-top:20px;max-width:36ch;font-size:14px">I lead growth for DTC, eCommerce and SaaS brands — building the data, media, automation and AI systems that make revenue compound.</p></div>
<div><h5>Explore</h5><a href="about.html">About</a><a href="services.html">Services</a><a href="stack.html">AI Growth Stack</a><a href="work.html">Work</a><a href="insights.html">Insights</a></div>
<div><h5>Connect</h5><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a><a href="https://github.com/saqi097" target="_blank" rel="noopener">GitHub ↗</a><a href="mailto:{EMAIL}">Email</a><a href="contact.html">Book a call</a></div>
<div><h5>Dubai, UAE</h5><span class="t">Local time <b class="clock" style="color:var(--text);font-weight:500"></b> (GMT+4)</span><span class="t">Working worldwide</span><span class="t">English · Urdu</span></div>
</div>
<div class="big-name" aria-hidden="true">Saqib Ameer</div>
<div class="foot-bottom"><span>© <span data-year>2026</span> Saqib Ameer. All rights reserved.</span><span>Designed &amp; built in Dubai</span><button class="to-top" aria-label="Back to top">↑</button></div>
</div></footer>
<script src="assets/js/site.js?v=3" defer></script>
</body></html>
"""


def page(path, title, desc, content):
    (OUT / path).write_text(head(title, desc, path) + nav(path) + content + FOOT, encoding="utf-8")


def portrait_html(eager=True):
    full = " full" if IMG["hero_full"] else ""
    return f"""<div class="portrait{full} fade-up d2" data-cursor="Hello">
<img src="{IMG['hero']}" alt="Black and white portrait of Saqib Ameer" width="1000" height="1250" {'fetchpriority="high"' if eager else 'loading="lazy"'}>
<svg class="rot" viewBox="0 0 100 100" aria-hidden="true"><defs><path id="c" d="M50,50 m-38,0 a38,38 0 1,1 76,0 a38,38 0 1,1 -76,0"/></defs><text><textPath href="#c">AI Growth Leader · Dubai · Since 2015 · </textPath></text></svg>
<div class="ptag"><span>Saqib Ameer</span><span>Dubai · UAE</span></div>
</div>"""


def frame(src, alt, cut=False, cap="", extra=""):
    c = " cut" if cut else ""
    cap_html = f'<span class="cap">{cap}</span>' if cap else ""
    return f'<div class="frame reveal-img{c}" {extra}><img src="{src}" alt="{alt}" loading="lazy">{cap_html}</div>'


# ---------------------------------------------------------------- shared blocks
ICONS = {
    "ai": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M18.4 5.6l-2.8 2.8M8.4 15.6l-2.8 2.8"/></svg>',
    "target": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/></svg>',
    "flow": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><path d="M9 6h4a3 3 0 0 1 3 3v6"/></svg>',
    "chart": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
    "people": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17.5" cy="9" r="2.5"/><path d="M16 14.2A5 5 0 0 1 21.5 19"/></svg>',
    "box": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="m12 3 8 4.5v9L12 21l-8-4.5v-9z"/><path d="m4 7.5 8 4.5 8-4.5M12 12v9"/></svg>',
    "cart": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M3 4h2l2.4 11h11L21 7H6.2"/><circle cx="9" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/></svg>',
    "layers": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></svg>',
    "compass": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>',
}

MARQUEE_TOOLS = ["Google Ads", "Meta Ads", "TikTok Ads", "LinkedIn Ads", "GA4", "Google Tag Manager", "HubSpot",
                 "GoHighLevel", "Looker Studio", "Klaviyo", "Mailchimp", "Apollo.io", "Clay", "Zapier", "Make",
                 "SEMrush", "Ahrefs", "ChatGPT", "Claude", "Gemini"]


def marquee(items, big=False, direction="left"):
    spans = "".join(f"<span>{i}</span>" for i in items) * 2
    cls = "big-marquee" if big else "marquee"
    return f'<div class="{cls}" aria-hidden="true"><div class="marquee-track" data-dir="{direction}">{spans}</div></div>'


STACK = [
    ("Signal", "Data & tracking", "Clean data before clever AI. GA4, server-side tagging, consent-aware tracking, attribution and cohort views — so every budget decision runs on numbers the CFO trusts.", ["GA4", "Tag Manager", "Server-side", "Attribution", "Cohorts", "Looker Studio"]),
    ("Acquire", "Performance media", "AI-assisted media buying across Google, Meta, TikTok and LinkedIn. Faster creative testing, tighter audiences and budgets that follow CAC, ROAS and payback — not opinions.", ["Google Ads", "PMax", "Meta Ads", "TikTok", "LinkedIn", "Creative testing"]),
    ("Convert", "CRO & experience", "Landing pages, offers and journeys tested like products. AI speeds up variant creation; disciplined experiments decide what ships.", ["A/B testing", "Landing pages", "Offer design", "UX research", "Heatmaps"]),
    ("Retain", "Automation & lifecycle", "Email, SMS, WhatsApp and CRM flows that onboard, nurture and win back customers on autopilot — so revenue keeps compounding after the first sale.", ["HubSpot", "GoHighLevel", "Klaviyo", "Lead scoring", "Win-back"]),
    ("Scale", "AI operations", "AI agents and workflows that take repetitive marketing work off your team: reporting, research, briefs, content ops, QA and lead handling.", ["AI agents", "Workflows", "Content ops", "Auto-reporting", "Enablement"]),
]


def stack_block(paper=False):
    items = ""
    for i, (n, tag, p, lis) in enumerate(STACK):
        d = " rv-d1" if i else ""
        lis_html = "".join(f"<li>{x}</li>" for x in lis)
        items += f'<div class="layer rv{d}" tabindex="0"><header><span class="idx">0{i+1}</span><h3>{n}</h3><span class="tag">{tag}</span></header><div class="body"><div><p>{p}</p><ul>{lis_html}</ul></div></div></div>'
    slabs = "".join(f'<div class="slab" style="--w:{56 + i*9}%"><span>{n}</span><i>L0{i+1}</i></div>' for i, (n, *_r) in enumerate(STACK))
    return f'<div class="stack"><div class="stack-list">{items}</div><div class="stack-visual rv" aria-hidden="true"><div class="grid-bg"></div>{slabs}</div></div>'


CASES = [
    dict(tag="Healthcare · Abu Dhabi", when="2025 – now", name="House of Nature Medical Center",
         role="Marketing Manager — owns digital growth end to end",
         p="Leading digital growth for a multi-specialty medical center: high-intent Google Search, Meta lead generation with retargeting, website conversion paths, Google Business Profile and local SEO — all reporting into one cost-per-patient view.",
         pills=["Google Ads", "Meta Ads", "Local SEO", "Website CRO"],
         nums=[("+60%", "Google Ads clicks"), ("AED 15", "Meta cost per lead"), ("360°", "Ads · site · content · GBP"), ("Now", "Current leadership role")]),
    dict(tag="AI / Web3 SaaS · Germany", when="2024 – 2026", name="CHAMELAION GmbH",
         role="Marketing Manager, CMO track — owned the marketing P&L",
         p="Owned the marketing P&L for a SaaS product targeting DACH markets. Rebuilt persona targeting and funnel segmentation, introduced cohort-based attribution and built an organic and community engine from zero.",
         pills=["Paid media", "Attribution", "SEO", "Community"],
         nums=[("−22%", "Customer acquisition cost"), ("+45%", "Organic traffic in 4 months"), ("0 → 1,200", "Community members"), ("+16%", "MQL → SQL conversion")]),
    dict(tag="B2B SaaS · Germany", when="2024", name="QMANTIC SaaS GmbH",
         role="Marketing Manager — acquisition and lifecycle",
         p="Paired Google Ads with automated email nurture and behavioural onboarding to turn clicks into trials, and trials into paying users, at a blended CAC most SaaS teams would envy.",
         pills=["Google Ads", "Lifecycle", "Automation", "Onboarding"],
         nums=[("1,000+", "Trial sign-ups"), ("€1.40", "Blended CAC"), ("+12%", "Trial → paid"), ("+38%", "Social engagement")]),
    dict(tag="Mobile app · EU", when="2023 – 2024", name="VANCY GmbH",
         role="Marketing Manager — app growth across EU markets",
         p="Scaled app growth across EU markets with ASO, SEO and Google + Meta app campaigns, backed by landing-page and creative testing that kept ROAS above target as spend grew.",
         pills=["App campaigns", "ASO", "CRO", "Creative testing"],
         nums=[("3.2×+", "ROAS on app campaigns"), ("+60%", "App users"), ("+40%", "App installs"), ("+25%", "Conversion rate")]),
    dict(tag="Developer SaaS · Germany", when="2022 – 2023", name="SQUIDEX.IO GmbH",
         role="CMO / Marketing Consultant — full go-to-market ownership",
         p="Led marketing at CMO level: go-to-market, positioning, performance, content and SEO run as one growth engine, with CEO-level reporting on pipeline and payback.",
         pills=["GTM", "Positioning", "Content", "Email funnels"],
         nums=[("+60%", "Brand awareness in 4 months"), ("+32%", "Organic sign-ups"), ("CMO", "Go-to-market ownership"), ("4 mo", "To measurable brand lift")]),
    dict(tag="Agency · SaaS, fintech, eCommerce", when="2017 – 2022", name="HA-Technologies",
         role="Digital Marketing Manager — led delivery for international clients",
         p="Led 360° marketing delivery for international clients across SaaS, IT, fintech and eCommerce — owning strategy, media, reporting and client relationships across MENA, Europe and South Asia.",
         pills=["Search", "Segmentation", "Reporting", "Client leadership"],
         nums=[("50+", "Growth projects led"), ("+80%", "Client ROI"), ("+200%", "Real-estate leads"), ("3", "Regions: MENA · EU · South Asia")]),
]


def case_html(c, i, total):
    pills = "".join(f'<span class="pill">{p}</span>' for p in c["pills"])
    nums = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in c["nums"])
    return f"""<article class="case rv" style="--i:{i}">
<div><div class="meta"><span class="pill g">{c['tag']}</span><span class="pill">{c['when']}</span></div>
<h3>{c['name']}</h3><p>{c['p']}</p><p class="role">{c['role']}</p>
<div class="meta" style="margin-top:22px;margin-bottom:0">{pills}</div></div>
<div class="nums">{nums}</div><span class="bg-n" aria-hidden="true">{i+1:02d}</span>
</article>"""


FAQ = [
    ("Do you lead strategy, or do you also build?", "Both — that is the point. I set the strategy, own the numbers and lead the people, and I can still open the ad account, the tag manager or the automation builder myself. Nothing gets lost between the deck and the dashboard."),
    ("What kind of companies do you work with?", "Brands with product-market fit that sell online and want to grow more efficiently: DTC, eCommerce and SaaS teams are the best fit, plus healthcare and service businesses with a clear digital funnel."),
    ("Can you lead our team or agencies?", "Yes. As a fractional or full-time growth lead I set priorities, run the experiment roadmap, manage agencies and freelancers, and report to founders and the board in plain numbers."),
    ("Do you work with clients outside the UAE?", "Yes. I have worked remotely with teams in Germany and across Europe since 2022, alongside clients in the GCC, MENA and South Asia. Dubai time (GMT+4) overlaps well with both Europe and Asia."),
    ("Which AI tools do you use?", "Whatever fits the job and your stack: leading LLMs such as ChatGPT, Claude and Gemini, automation platforms like Zapier and Make, enrichment tools like Clay and Apollo, and the AI features already built into Google, Meta and your CRM."),
    ("How quickly will we see results?", "The audit gives you a ranked plan in two weeks. Tracking and quick wins usually land in the first month; compounding gains from automation and AI operations build over the following quarter."),
]


def faq_html(items=FAQ):
    return '<div class="faq">' + "".join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + "</div>"


def cta(title="Let’s make AI pay for itself.", text="Tell me where growth is stuck. In a 30-minute call we’ll map where AI, paid media and automation can move your numbers first — and what it’s worth."):
    return f"""<section><div class="wrap"><div class="cta-box rv"><span class="orbit" aria-hidden="true"></span><span class="orbit o2" aria-hidden="true"></span>
<span class="kicker" style="position:relative">Now booking strategy calls</span>
<h2 class="h-xl" style="position:relative">{title}</h2>
<p class="lede" style="position:relative">{text}</p>
<div class="hero-ctas" style="position:relative"><a class="btn btn-primary" href="contact.html">Book a strategy call {ARR}</a><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">Connect on LinkedIn</a></div>
</div></div></section>
"""


def page_hero(kicker, h1, lede, extra=""):
    return f"""<section class="page-hero"><div class="grid-bg"></div><div class="wrap" style="position:relative">
<div class="crumb fade-up"><a href="index.html">Home</a><span>/</span><span>{kicker}</span></div>
<h1 class="h-xl" data-split>{h1}</h1>
<p class="lede fade-up d2">{lede}</p>{extra}
</div></section>
"""


# ---------------------------------------------------------------- HOME
home = f"""
<section class="hero">
<div class="grid-bg"></div>
<div class="wrap">
<div class="hero-grid">
<div>
<span class="kicker fade-up">{TITLE} · Dubai, UAE</span>
<h1 class="h-xl"><span class="split-l"><span>Leading growth</span></span><span class="split-l"><span>in the age</span></span><span class="split-l"><span><span class="serif">of AI.</span></span></span></h1>
<p class="lede fade-up d1">I’m Saqib Ameer. For 10+ years I’ve led growth for SaaS, eCommerce, app and healthcare brands across the UAE and Europe — owning strategy, budgets and teams, and building the data, media and AI systems that turn marketing spend into compounding revenue.</p>
<div class="hero-ctas fade-up d2"><a class="btn btn-primary" href="contact.html">Book a strategy call {ARR}</a><a class="btn" href="work.html">See the results</a></div>
<div class="hero-meta fade-up d3"><div><b>−22%</b>Customer acquisition cost</div><div><b>3.2×+</b>ROAS on app growth</div><div><b>50+</b>Growth projects led</div></div>
</div>
{portrait_html()}
</div>
<div class="scroll-cue fade-up d4"><i></i>Scroll to explore</div>
</div>
</section>
{marquee(MARQUEE_TOOLS)}

<section><div class="wrap two-col" style="align-items:start">
<div><span class="kicker rv">01 — Point of view</span></div>
<div><p class="statement" data-lit>Most brands bolt AI onto broken funnels. I lead the other way round: fix the data, fix the engine, then let AI multiply what already works.</p>
<div class="hero-ctas rv" style="margin-top:40px"><a class="link" href="about.html">More about how I lead →</a></div></div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="stats rv">
<div class="stat"><div class="num"><span data-to="10">0</span><em>+</em></div><p>Years leading growth across SaaS, eCommerce, fintech, apps and healthcare.</p></div>
<div class="stat"><div class="num"><span data-to="50">0</span><em>+</em></div><p>Full-funnel growth projects led for international clients.</p></div>
<div class="stat"><div class="num"><em>−</em><span data-to="22">0</span><em>%</em></div><p>Lower customer acquisition cost while owning the marketing P&amp;L at CHAMELAION.</p></div>
<div class="stat"><div class="num"><span data-to="3.2">0</span><em>×</em></div><p>ROAS sustained on Google and Meta app campaigns across EU markets.</p></div>
</div>
</div></section>

<section class="paper rounded-top"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">02 — The framework</span><h2 class="h-l" style="margin-top:20px" data-split>The AI Growth Stack</h2></div>
<p class="lede rv" style="max-width:44ch">Five layers I install in every business I lead, in this order. Each layer makes the next one cheaper, faster and more accurate — and stops AI from scaling your mistakes.</p></div>
{stack_block(paper=True)}
<p class="rv" style="margin-top:40px"><a class="link" href="stack.html">How the stack works, layer by layer →</a></p>
</div></section>

<section class="paper" style="padding-top:0"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">03 — What I lead</span><h2 class="h-l" style="margin-top:20px" data-split>Four ways I move your numbers</h2></div>
<a class="btn rv" href="services.html">Services &amp; engagement models {ARR}</a></div>
<div class="svc">
<a class="svc-row rv" href="services.html#ai"><span class="n">01</span><h3>AI transformation</h3><p>Find where AI earns its keep, then build it in: agents, workflows and content ops your team actually uses.</p><span class="go">→</span></a>
<a class="svc-row rv" href="services.html#performance"><span class="n">02</span><h3>Performance marketing</h3><p>Google, Meta, TikTok and LinkedIn run on CAC, ROAS and LTV — with tracking that proves what worked.</p><span class="go">→</span></a>
<a class="svc-row rv" href="services.html#automation"><span class="n">03</span><h3>Automation &amp; CRM</h3><p>Lifecycle flows across email, SMS, WhatsApp and CRM that onboard, nurture and retain without adding headcount.</p><span class="go">→</span></a>
<a class="svc-row rv" href="services.html#leadership"><span class="n">04</span><h3>Fractional growth leadership</h3><p>CMO-level ownership of strategy, budgets, agencies and board reporting — for teams that need a leader, not another vendor.</p><span class="go">→</span></a>
</div>
</div></section>

<section style="padding:clamp(24px,4vw,48px) 0 0"><div class="wrap">
<div class="band side rv" data-cursor="Workshops"><div class="band-img" data-speed=".35"><img src="{IMG['band']}" alt="Saqib Ameer leading a growth strategy workshop at a whiteboard" loading="lazy"></div>
<div class="in"><span class="kicker">Workshops &amp; leadership</span><h2 class="h-l" style="margin-top:18px">I lead the room,<br><span class="serif">not just the account.</span></h2>
<p class="lede" style="margin-top:18px">From funnel teardowns at the whiteboard to AI enablement for whole marketing teams, I help people see where growth comes from — then build the system with them. Based in Dubai, working with teams in the UAE, Germany and beyond.</p>
<div class="hero-ctas" style="margin-top:28px"><a class="btn btn-primary" href="contact.html">Book a team workshop {ARR}</a></div></div></div>
</div></section>

{marquee(["Strategy", "Data", "Media", "Automation", "AI", "Leadership"], big=True)}

<section style="padding-top:0"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">04 — Selected work</span><h2 class="h-l" style="margin-top:20px" data-split>Results, not decks</h2></div>
<a class="btn rv" href="work.html">All case studies {ARR}</a></div>
<div class="cases stacked">{''.join(case_html(c, i, 3) for i, c in enumerate(CASES[:3]))}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">05 — How I lead</span><h2 class="h-l" style="margin-top:20px" data-split>Principles I lead by</h2></div>
<p class="lede rv" style="max-width:42ch">Titles change. These don’t. They’re how I run every team, budget and experiment I’m trusted with.</p></div>
<div class="principles">
<div class="principle rv"><span class="n">/01</span><div><h3>Numbers before narratives</h3><p>CAC, ROAS, LTV and payback decide where money goes. Opinions are welcome; data breaks the tie.</p></div></div>
<div class="principle rv rv-d1"><span class="n">/02</span><div><h3>Systems over heroics</h3><p>One great campaign is luck. A system of tracking, testing and automation is a growth engine.</p></div></div>
<div class="principle rv"><span class="n">/03</span><div><h3>AI as a multiplier, not a strategy</h3><p>AI scales whatever it touches. I make sure it’s touching clean data and a funnel that already converts.</p></div></div>
<div class="principle rv rv-d1"><span class="n">/04</span><div><h3>Lead from inside the work</h3><p>I set direction and still open the dashboards myself. Teams follow leaders who understand the work.</p></div></div>
</div>
</div></section>

<section class="paper rounded-top"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">06 — Who I work with</span><h2 class="h-l" style="margin-top:20px" data-split>Built for brands that sell online</h2></div></div>
<div class="cards">
<div class="card rv" data-tilt><div class="ico">{ICONS['box']}</div><h3>DTC brands</h3><p>Founder-led brands ready to scale beyond the first profitable channel.</p><ul><li>Creative testing at AI speed</li><li>Profitable Meta and TikTok scaling</li><li>Post-purchase flows that lift LTV</li></ul></div>
<div class="card rv rv-d1" data-tilt><div class="ico">{ICONS['cart']}</div><h3>eCommerce</h3><p>Stores where margin, tracking and retention decide who wins.</p><ul><li>Search, Shopping and PMax structure</li><li>Tracking you can trust after iOS changes</li><li>Retention and win-back automation</li></ul></div>
<div class="card rv rv-d2" data-tilt><div class="ico">{ICONS['layers']}</div><h3>SaaS</h3><p>B2B and B2C software teams that need efficient pipeline, not just traffic.</p><ul><li>Trial and demo acquisition at lower CAC</li><li>Onboarding and activation sequences</li><li>Pipeline attribution from click to revenue</li></ul></div>
</div>
</div></section>

<section class="paper" style="padding-top:0"><div class="wrap two-col">
<div><span class="kicker rv">07 — FAQ</span><h2 class="h-l" style="margin-top:20px" data-split>Good questions</h2><p class="lede rv" style="margin-top:20px">Still unsure? <a class="link" href="contact.html">Ask me directly</a> — I reply within two working days.</p></div>
{faq_html(FAQ[:4])}
</div></section>

<section style="padding-top:clamp(88px,12vw,160px)"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">08 — Insights</span><h2 class="h-l" style="margin-top:20px" data-split>Notes from the stack</h2></div>
<a class="btn rv" href="insights.html">All insights {ARR}</a></div>
<a class="post rv" href="insights.html"><span class="mono muted">Playbook</span><div><h3>The AI Growth Stack: why tracking comes before AI</h3><p>The order that stops AI from scaling your mistakes.</p></div><span class="arr">→</span></a>
<a class="post rv" href="insights.html"><span class="mono muted">Paid media</span><div><h3>How I cut CAC by 22% without cutting spend</h3><p>Persona targeting, bid rules and funnel segmentation, step by step.</p></div><span class="arr">→</span></a>
<a class="post rv" href="insights.html"><span class="mono muted">Automation</span><div><h3>€1.40 per trial: pairing Google Ads with email nurture</h3><p>The exact sequence behind 1,000+ SaaS sign-ups.</p></div><span class="arr">→</span></a>
</div></section>
{cta()}
"""

# ---------------------------------------------------------------- ABOUT
about_img = frame(IMG["about"], "Saqib Ameer", cut=IMG["about_cut"], extra='data-cursor="Saqib"')
about = f"""
<section class="page-hero"><div class="grid-bg"></div><div class="wrap split" style="position:relative">
<div><div class="crumb fade-up"><a href="index.html">Home</a><span>/</span><span>About</span></div>
<h1 class="h-xl" data-split>Engineer’s brain. <span class="serif">Leader’s job.</span></h1>
<p class="lede fade-up d2">I’m Saqib Ameer, an {TITLE} based in Dubai. I studied computer science, fell for marketing, and have spent more than a decade connecting the two — leading the data, media, funnels, automation and people that make growth predictable.</p>
<div class="hero-ctas fade-up d3" style="margin-top:36px"><a class="btn btn-primary" href="contact.html">Work with me {ARR}</a><a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a></div></div>
{about_img}
</div></section>

<section style="padding-top:0"><div class="wrap two-col">
<div><span class="kicker rv">My story</span></div>
<div class="prose rv">
<p class="statement" data-lit style="margin-bottom:40px">I’m as comfortable in a tag manager as I am in a boardroom. That’s rare in marketing — and it’s exactly why AI came naturally.</p>
<p>I started in 2015 doing SEO and PPC for real-estate and local businesses in Pakistan. Within two years I was leading digital delivery at HA-Technologies, where I ran <strong>50+ growth projects</strong> for international clients across SaaS, fintech, IT and eCommerce.</p>
<p>From 2022 I moved into leadership roles with German tech companies — first as <strong>CMO and marketing consultant at SQUIDEX.IO</strong>, then leading app growth at VANCY, acquisition and lifecycle at QMANTIC, and owning the <strong>marketing P&amp;L at CHAMELAION</strong>, where we cut CAC by 22%.</p>
<p>Today I’m based in Dubai, leading end-to-end digital growth for House of Nature Medical Center in Abu Dhabi, and advising founders on how to put AI to work across their growth stack.</p>
<p class="signature">Saqib Ameer</p>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="gallery">
{frame(IMG['g1'], 'Saqib Ameer at Dubai Marina', cap='Dubai Marina')}
{frame(IMG['g2'], 'Saqib Ameer in Dubai', cap='Dubai')}
{frame(IMG['g3'], 'Saqib Ameer in Downtown Dubai', cap='Downtown Dubai')}
</div></div></section>

<section style="padding-top:0"><div class="wrap">
<div class="band side rv" data-cursor="Workshops"><div class="band-img" data-speed=".35"><img src="{IMG['workshop']}" alt="Saqib Ameer leading a growth strategy workshop at a whiteboard" loading="lazy"></div>
<div class="in"><span class="kicker">Talks &amp; workshops</span><h2 class="h-l" style="margin-top:18px">Strategy is a team sport.</h2>
<p class="lede" style="margin-top:18px">I run hands-on sessions for founders and marketing teams: the AI Growth Stack, AI for performance marketing, and tracking that survives privacy changes.</p></div></div>
</div></section>

<section class="paper rounded-top"><div class="wrap split" style="align-items:start">
<div style="position:sticky;top:120px"><span class="kicker rv">Career</span><h2 class="h-l" style="margin-top:20px" data-split>From SEO to the C-suite</h2>
<p class="lede rv" style="margin-top:20px">A decade of compounding skills: search, paid media, funnels, lifecycle, leadership — and now AI across all of it.</p></div>
<div class="tl">
<div class="tl-item"><span class="dot"></span><span class="when">2025 – now</span><div><h4>Marketing Manager · House of Nature Medical Center</h4><p>Abu Dhabi. Leading end-to-end digital growth for a multi-specialty medical center.</p><ul><li>Google Ads</li><li>Meta lead gen</li><li>Local SEO</li></ul></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">2024 – 2026</span><div><h4>Marketing Manager, CMO track · CHAMELAION GmbH</h4><p>Germany, remote. Owned the marketing P&amp;L for an AI / Web3 SaaS product.</p><ul><li>−22% CAC</li><li>+45% organic</li><li>Attribution</li></ul></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">2024</span><div><h4>Marketing Manager · QMANTIC SaaS GmbH</h4><p>Germany, remote. Paid acquisition plus lifecycle automation.</p><ul><li>1,000+ trials</li><li>€1.40 CAC</li></ul></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">2023 – 2024</span><div><h4>Marketing Manager · VANCY GmbH</h4><p>Germany, remote. Led app growth across EU markets.</p><ul><li>3.2×+ ROAS</li><li>+60% users</li></ul></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">2022 – 2023</span><div><h4>CMO / Marketing Consultant · SQUIDEX.IO GmbH</h4><p>Germany, remote. Full go-to-market ownership with CEO-level reporting.</p><ul><li>GTM</li><li>+32% sign-ups</li></ul></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">2017 – 2022</span><div><h4>Digital Marketing Manager · HA-Technologies</h4><p>Pakistan. Led 50+ projects for international clients.</p><ul><li>Multi-GEO</li><li>+80% client ROI</li></ul></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">2015 – 2017</span><div><h4>SEO &amp; Digital Marketing · SEO Islamabad, Estate92</h4><p>Where it started: SEO, PPC and content for real estate.</p><ul><li>+200% leads</li></ul></div></div>
</div>
</div></section>

<section class="paper" style="padding-top:0"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">Leadership</span><h2 class="h-l" style="margin-top:20px" data-split>What I bring to a leadership seat</h2></div></div>
<div class="cards">
<div class="card rv" data-tilt><div class="ico">{ICONS['chart']}</div><h3>P&amp;L ownership</h3><p>I’ve owned marketing budgets and been accountable for CAC, payback and pipeline — not just clicks.</p></div>
<div class="card rv rv-d1" data-tilt><div class="ico">{ICONS['people']}</div><h3>Teams &amp; agencies</h3><p>I set priorities, run the experiment roadmap and lead in-house teams, agencies and freelancers to one scoreboard.</p></div>
<div class="card rv rv-d2" data-tilt><div class="ico">{ICONS['compass']}</div><h3>Board-ready clarity</h3><p>Founders and boards get plain-language reporting: what we spent, what it returned, what we do next.</p></div>
</div>
</div></section>

<section><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">Toolkit</span><h2 class="h-l" style="margin-top:20px" data-split>The stack I lead with</h2></div></div>
<div class="tools rv">
<div><h4>Media</h4><p>Google Ads · PMax<br>Meta Ads<br>TikTok Ads<br>LinkedIn Ads</p></div>
<div><h4>Data</h4><p>GA4 · Tag Manager<br>Looker Studio<br>Server-side tracking<br>Attribution &amp; cohorts</p></div>
<div><h4>Lifecycle</h4><p>HubSpot · GoHighLevel<br>Klaviyo · Mailchimp<br>Apollo.io · Clay<br>Zapier · Make</p></div>
<div><h4>AI</h4><p>ChatGPT · Claude<br>Gemini<br>AI agents &amp; workflows<br>AI creative testing</p></div>
</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="cards">
<div class="card rv"><div class="ico">{ICONS['compass']}</div><h3>Education</h3><ul><li>MSc Computer Science — PMAS Arid Agriculture University, Rawalpindi (2018)</li><li>BSc Computer Science — University of the Punjab, Lahore (2016)</li></ul></div>
<div class="card rv rv-d1"><div class="ico">{ICONS['chart']}</div><h3>Industries</h3><ul><li>SaaS and B2B tech</li><li>eCommerce and DTC</li><li>Fintech and mobile apps</li><li>Healthcare and real estate</li></ul></div>
<div class="card rv rv-d2"><div class="ico">{ICONS['ai']}</div><h3>Talks &amp; workshops</h3><p>Available for team workshops and talks on:</p><ul><li>The AI Growth Stack</li><li>AI for performance marketing</li><li>Tracking that survives privacy changes</li></ul></div>
</div>
</div></section>
{cta("Let’s build what’s next.", "Whether you need a growth leader, a fractional CMO or a sharp second opinion, I’m happy to talk.")}
"""

# ---------------------------------------------------------------- SERVICES
svc_img = frame(IMG["services"], "Saqib Ameer", cut=IMG["services_cut"])
services = page_hero("Services", "AI that shows up in your <span class=\"serif\">P&amp;L.</span>",
                     "Strategy, leadership and hands-on execution in one person. I plan it, build it, run it and report on it — so nothing gets lost between the deck and the dashboard.") + f"""
<section style="padding-top:0"><div class="wrap">
<div class="cards two">
<div class="card rv" id="ai" data-tilt><span class="num-tag">01</span><div class="ico">{ICONS['ai']}</div><h3>AI marketing transformation</h3><p>Audit where your team spends time, then replace the repetitive parts with AI agents and workflows that actually get used.</p>
<ul><li>AI opportunity audit across your funnel</li><li>Agents for research, reporting and content ops</li><li>AI-assisted creative and copy testing</li><li>Team enablement, playbooks and guardrails</li></ul></div>
<div class="card rv rv-d1" id="performance" data-tilt><span class="num-tag">02</span><div class="ico">{ICONS['target']}</div><h3>Performance marketing</h3><p>Paid acquisition run on unit economics, not vanity metrics.</p>
<ul><li>Google Search, Shopping, PMax and YouTube</li><li>Meta, TikTok and LinkedIn campaigns</li><li>Budget allocation by CAC, ROAS, LTV and payback</li><li>Creative testing frameworks</li></ul></div>
<div class="card rv" id="automation" data-tilt><span class="num-tag">03</span><div class="ico">{ICONS['flow']}</div><h3>Marketing automation &amp; CRM</h3><p>Lifecycle systems that keep selling after the first click.</p>
<ul><li>HubSpot, GoHighLevel and Klaviyo set-up</li><li>Onboarding, nurture and win-back flows</li><li>Lead scoring, enrichment and routing</li><li>Email, SMS and WhatsApp automation</li></ul></div>
<div class="card rv rv-d1" id="analytics" data-tilt><span class="num-tag">04</span><div class="ico">{ICONS['chart']}</div><h3>Tracking, CRO &amp; analytics</h3><p>The Signal layer: data you can make money decisions on.</p>
<ul><li>GA4, Tag Manager and server-side tracking</li><li>Attribution and cohort reporting</li><li>Landing page and funnel A/B testing</li><li>Looker Studio executive dashboards</li></ul></div>
</div>
</div></section>

<section class="paper rounded-top" id="leadership"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">Engagement models</span><h2 class="h-l" style="margin-top:20px" data-split>Pick your starting point</h2></div>
<p class="lede rv" style="max-width:40ch">Every engagement starts with the numbers. Scope grows only when the results justify it.</p></div>
<div class="cards">
<div class="card rv" data-tilt><span class="mono">01 · 2 weeks</span><h3 style="margin-top:18px">Growth Stack Audit</h3><p>A full review of your tracking, paid media, funnel and automation, with a ranked plan of what to fix first and where AI fits.</p><ul><li>Account and funnel audit</li><li>AI opportunity map</li><li>90-day roadmap with impact estimates</li><li>Leadership read-out</li></ul></div>
<div class="card feature rv rv-d1" data-tilt><span class="mono">02 · 6–8 weeks</span><h3 style="margin-top:18px">Build Sprint</h3><p>We install the highest-impact layers of the stack — tracking, campaigns, flows and AI workflows — built, documented and handed over.</p><ul><li>Hands-on implementation</li><li>Weekly reporting and stand-ups</li><li>Documentation and team training</li><li>Clean handover</li></ul></div>
<div class="card rv rv-d2" data-tilt><span class="mono">03 · Monthly</span><h3 style="margin-top:18px">Fractional growth leader</h3><p>Ongoing CMO-level ownership of growth: strategy, budgets, agencies, experiments and board-ready reporting.</p><ul><li>Strategy and P&amp;L ownership</li><li>Team and agency leadership</li><li>Experiment roadmap</li><li>Monthly board reporting</li></ul></div>
</div>
</div></section>

<section class="paper" style="padding-top:0"><div class="wrap split">
{svc_img}
<div><span class="kicker rv">The process</span><h2 class="h-l" style="margin-top:20px" data-split>Audit. Build. Compound.</h2>
<div class="tl" style="margin-top:40px">
<div class="tl-item"><span class="dot"></span><span class="when">Week 1–2</span><div><h4>Diagnose</h4><p>Numbers first: tracking, CAC, ROAS, funnel drop-offs and team workflows. You get a ranked list of what’s worth fixing.</p></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">Week 3–8</span><div><h4>Build</h4><p>Install the layers that unlock the most revenue, fastest — tracking, campaigns, flows and the first AI workflows.</p></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">Month 3+</span><div><h4>Lead &amp; compound</h4><p>Run the experiment roadmap, hand more repeatable work to AI, and report what it returned.</p></div></div>
</div></div>
</div></section>

<section><div class="wrap two-col">
<div><span class="kicker rv">FAQ</span><h2 class="h-l" style="margin-top:20px" data-split>Good questions</h2></div>
{faq_html()}
</div></section>
{cta()}
"""

# ---------------------------------------------------------------- STACK
stack = page_hero("AI Growth Stack", "The AI Growth <span class=\"serif\">Stack.</span>",
                  "A five-layer system for turning AI from a buzzword into a growth engine — built from 10+ years of leading paid media, funnels and automation for SaaS, eCommerce, apps and healthcare.") + f"""
<section style="padding-top:0"><div class="wrap">{stack_block()}</div></section>
<section style="padding-top:0"><div class="wrap two-col">
<div><span class="kicker rv">Why the order matters</span></div>
<p class="statement" data-lit>AI amplifies whatever it touches. Point it at bad data and broken funnels and you scale waste. Point it at a clean stack and you scale profit.</p>
</div></section>
{marquee(["Signal", "Acquire", "Convert", "Retain", "Scale"], big=True, direction="right")}
<section class="paper rounded-top"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">Principles</span><h2 class="h-l" style="margin-top:20px" data-split>Rules the stack runs on</h2></div></div>
<div class="principles">
<div class="principle rv"><span class="n">/01</span><div><h3>Bottom up</h3><p>Signal before Acquire, Acquire before Scale. Skipping layers is how budgets disappear.</p></div></div>
<div class="principle rv rv-d1"><span class="n">/02</span><div><h3>Unit economics decide</h3><p>CAC, ROAS, LTV and payback period — not impressions — decide what gets more budget.</p></div></div>
<div class="principle rv"><span class="n">/03</span><div><h3>Automate the repeatable</h3><p>People own strategy and taste. AI and workflows own the repetitive work.</p></div></div>
<div class="principle rv rv-d1"><span class="n">/04</span><div><h3>Measure the multiplier</h3><p>Every AI workflow gets a baseline and a before/after. If it doesn’t move a number, it goes.</p></div></div>
</div>
</div></section>
<section class="paper" style="padding-top:0"><div class="wrap">
<div class="sec-head"><div><span class="kicker rv">Diagnostic</span><h2 class="h-l" style="margin-top:20px" data-split>Signs a layer is broken</h2></div></div>
<div class="cards">
<div class="card rv"><span class="mono">Signal</span><h3 style="margin-top:14px">Platforms disagree</h3><p>Google, Meta and your CRM report different revenue, and nobody trusts any of them.</p></div>
<div class="card rv rv-d1"><span class="mono">Acquire · Convert</span><h3 style="margin-top:14px">CAC keeps creeping</h3><p>Spend goes up, results flatten, and the answer is always “more creative”.</p></div>
<div class="card rv rv-d2"><span class="mono">Retain · Scale</span><h3 style="margin-top:14px">Team is buried</h3><p>Reporting, briefs and lead follow-up eat the hours that should go into strategy.</p></div>
</div>
</div></section>
{cta("Where does your stack break?", "Book a call and we’ll find the weakest layer in your growth stack — and what fixing it is worth.")}
"""

# ---------------------------------------------------------------- WORK
work = page_hero("Work", "Numbers I’ve <span class=\"serif\">moved.</span>",
                 "Selected results from leadership, in-house and consulting roles across healthcare, SaaS, apps, fintech and eCommerce. Every figure below comes from work I led.") + f"""
<section style="padding-top:0"><div class="wrap">
<div class="stats rv" style="margin-bottom:clamp(56px,8vw,96px)">
<div class="stat"><div class="num"><span data-to="6">0</span></div><p>Companies where I led growth since 2017.</p></div>
<div class="stat"><div class="num"><span data-to="50">0</span><em>+</em></div><p>Growth projects delivered.</p></div>
<div class="stat"><div class="num"><span data-to="4">0</span></div><p>Markets: UAE, Germany / DACH, EU and South Asia.</p></div>
<div class="stat"><div class="num"><span data-to="10">0</span><em>+</em></div><p>Years in growth and digital marketing.</p></div>
</div>
<div class="cases stacked">{''.join(case_html(c, i, len(CASES)) for i, c in enumerate(CASES))}</div>
</div></section>
{cta("Want numbers like these?", "Tell me what you’re working toward and I’ll show you which layer of the stack moves it first.")}
"""

# ---------------------------------------------------------------- INSIGHTS
POSTS = [("Playbook", "The AI Growth Stack: why tracking comes before AI", "The order that stops AI from scaling your mistakes."),
         ("Paid media", "How I cut CAC by 22% without cutting spend", "Persona targeting, bid rules and funnel segmentation, step by step."),
         ("Automation", "€1.40 per trial: pairing Google Ads with email nurture", "The exact sequence behind 1,000+ SaaS sign-ups."),
         ("AI ops", "5 marketing tasks I hand to AI agents every week", "Reporting, research, briefs, QA and lead handling."),
         ("eCommerce", "Tracking after iOS: a practical GA4 + server-side setup", "What to measure, and what to stop trusting."),
         ("Healthcare", "Lead gen for clinics: Google Search vs Meta lead forms", "What worked in a regulated, high-intent category."),
         ("Leadership", "What a fractional growth leader should own in month one", "The first 30 days, from audit to first wins."),
         ("AI ops", "Building an AI reporting agent your CEO will actually read", "From raw platform data to a one-page Monday memo.")]
posts = "".join(f'<a class="post rv" href="contact.html"><span class="mono muted">{k}</span><div><h3>{t}</h3><p>{d} <span class="dim">· Coming soon</span></p></div><span class="arr">→</span></a>' for k, t, d in POSTS)
insights = page_hero("Insights", "Practical AI for <span class=\"serif\">growth leaders.</span>",
                     "Playbooks, teardowns and experiments from the AI Growth Stack. No hype — just what’s working in real accounts.") + f"""
<section style="padding-top:0"><div class="wrap">
<div class="card rv" style="display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center;padding:clamp(28px,4vw,56px)">
<div><span class="kicker">Newsletter</span><h2 class="h-l" style="margin-top:16px">The AI Growth Memo</h2><p style="margin-top:14px">One practical AI + growth idea, every other week. Written for founders and marketing leaders. Launching soon.</p></div>
<form class="form" onsubmit="event.preventDefault();location.href='mailto:{EMAIL}?subject=Add%20me%20to%20The%20AI%20Growth%20Memo'"><div class="field"><label for="nl">Email</label><input id="nl" type="email" placeholder="you@company.com" required></div><button class="btn btn-primary" type="submit" style="justify-self:start">Join the waitlist {ARR}</button></form>
</div>
<div style="margin-top:64px">{posts}</div>
</div></section>
<section style="padding-top:0"><div class="wrap"><div class="tag-cloud rv">
<span>AI agents</span><span>Performance marketing</span><span>GA4</span><span>Attribution</span><span>Lifecycle</span><span>CRO</span><span>Growth leadership</span><span>SaaS</span><span>eCommerce</span><span>Healthcare marketing</span><span>Automation</span><span>Creative testing</span>
</div></div></section>
{cta()}
"""

# ---------------------------------------------------------------- CONTACT
focus = ["AI transformation", "Performance marketing", "Automation & CRM", "Tracking & analytics", "Fractional growth leader", "Something else"]
chips = "".join(f'<label><input type="checkbox" name="focus" value="{f}"><span>{f.replace("&", "&amp;")}</span></label>' for f in focus)
budgets = ["Under $5k / month", "$5k – $20k / month", "$20k – $50k / month", "$50k+ / month", "Not sure yet"]
bopts = "".join(f"<option>{b}</option>" for b in budgets)
contact = f"""
<section class="page-hero"><div class="grid-bg"></div><div class="wrap split" style="position:relative;align-items:start">
<div><div class="crumb fade-up"><a href="index.html">Home</a><span>/</span><span>Contact</span></div>
<h1 class="h-xl" data-split>Let’s find your next <span class="serif">growth lever.</span></h1>
<p class="lede fade-up d2">Share a little about your business and where growth feels stuck. I reply to every message within two working days.</p>
<div class="contact-tiles fade-up d3" style="margin-top:40px" id="book">
<a class="tile" href="mailto:{EMAIL}"><div><small>Email</small><b>{EMAIL}</b></div><span class="arr">→</span></a>
<a class="tile" href="{LINKEDIN}" target="_blank" rel="noopener"><div><small>LinkedIn</small><b>linkedin.com/in/saqibameer</b></div><span class="arr">→</span></a>
<a class="tile" href="https://github.com/saqi097" target="_blank" rel="noopener"><div><small>GitHub</small><b>github.com/saqi097</b></div><span class="arr">→</span></a>
<div class="tile"><div><small>Location</small><b>Dubai, UAE · <span class="clock"></span> local time</b></div></div>
</div></div>
<form class="form card fade-up d2" id="contact-form" style="padding:clamp(24px,3.4vw,44px);gap:28px">
<div class="row"><div class="field"><label for="name">Name</label><input id="name" name="name" autocomplete="name" required></div>
<div class="field"><label for="company">Company</label><input id="company" name="company" autocomplete="organization"></div></div>
<div class="row"><div class="field"><label for="site">Website</label><input id="site" name="site" placeholder="https://"></div>
<div class="field"><label for="budget">Monthly marketing budget</label><select id="budget" name="budget">{bopts}</select></div></div>
<div class="field"><label>What can I help with?</label><div class="chips">{chips}</div></div>
<div class="field"><label for="msg">What are you working toward?</label><textarea id="msg" name="msg" required></textarea></div>
<button class="btn btn-primary" type="submit" style="justify-self:start">Send message {ARR}</button>
<p class="dim" style="font-size:13px">This opens your email app with the details filled in.</p>
</form>
</div></section>
<section style="padding-top:0"><div class="wrap two-col">
<div><span class="kicker rv">Before we talk</span><h2 class="h-l" style="margin-top:20px" data-split>What happens next</h2></div>
<div class="tl">
<div class="tl-item"><span class="dot"></span><span class="when">Day 1–2</span><div><h4>I reply personally</h4><p>No auto-responders or sales teams — you hear from me.</p></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">Call · 30 min</span><div><h4>We map the problem</h4><p>Where growth is stuck, what the numbers say, and which layer of the stack moves first.</p></div></div>
<div class="tl-item"><span class="dot"></span><span class="when">Within a week</span><div><h4>You get a clear proposal</h4><p>Scope, timeline and expected impact — or an honest “you don’t need me yet”.</p></div></div>
</div>
</div></section>
"""

# ---------------------------------------------------------------- 404
notfound = f"""
<section class="page-hero" style="min-height:80vh;display:flex;align-items:center"><div class="grid-bg"></div><div class="wrap" style="position:relative">
<span class="kicker fade-up">Error 404</span>
<h1 class="h-xxl" style="margin-top:24px" data-split>Wrong <span class="serif">turn.</span></h1>
<p class="lede fade-up d2" style="margin-top:28px">This page doesn’t exist — but the growth stack does.</p>
<div class="hero-ctas fade-up d3" style="margin-top:36px"><a class="btn btn-primary" href="index.html">Back home {ARR}</a><a class="btn" href="work.html">See the work</a></div>
</div></section>
"""

PAGES = [
    ("index.html", "", "Saqib Ameer is an AI Growth Leader in Dubai who leads growth for DTC, eCommerce and SaaS brands with AI, performance marketing and marketing automation. Creator of The AI Growth Stack.", home),
    ("about.html", "About", "Saqib Ameer is an AI Growth Leader in Dubai with 10+ years leading growth across SaaS, eCommerce, fintech, apps and healthcare, and an MSc in Computer Science.", about),
    ("services.html", "Services", "AI marketing transformation, performance marketing, automation and fractional growth leadership from Saqib Ameer, AI Growth Leader in Dubai.", services),
    ("stack.html", "The AI Growth Stack", "The AI Growth Stack: a five-layer framework by Saqib Ameer for turning AI into a measurable growth engine.", stack),
    ("work.html", "Work", "Case studies and results from Saqib Ameer: −22% CAC, 3.2×+ ROAS, €1.40 blended CAC and 50+ growth projects led.", work),
    ("insights.html", "Insights", "Practical AI and growth playbooks from Saqib Ameer, AI Growth Leader in Dubai.", insights),
    ("contact.html", "Contact", f"Contact Saqib Ameer, AI Growth Leader in Dubai. Email {EMAIL} or book a strategy call.", contact),
    ("404.html", "Not found", "Page not found.", notfound),
]

if __name__ == "__main__":
    for p in PAGES:
        page(*p)
    (OUT / "_headers").write_text("/assets/*\n  Cache-Control: public, max-age=604800\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    urls = "".join(f"<url><loc>{DOMAIN}/{'' if p[0]=='index.html' else p[0].replace('.html','')}</loc></url>" for p in PAGES if p[0] != "404.html")
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
    print("built", len(PAGES), "pages")
