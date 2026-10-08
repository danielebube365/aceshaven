"""
Builds the Aces Haven static site.

All content (contact details, properties, reviews, guide) lives in this file.
Edit it, then run from the project root:

    python tools/build.py

The output is plain HTML in the project root, ready for GitHub Pages or any host.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"

# ---------------------------------------------------------------- business
BRAND = "Aces Haven"
TAGLINE = "Another place like home"
EMAIL = "hello@aceshaven.co"
PHONES = [
    {"label": "Mobile", "display": "07787 800913", "tel": "+447787800913"},
    {"label": "Landline", "display": "020 7164 6834", "tel": "+442071646834"},
]
SOCIALS = {
    "instagram": "https://www.instagram.com/AceHaven/",
    "facebook": "https://www.facebook.com/AceHaven/",
}
YEAR = 2026

# ---------------------------------------------------------------- properties
EVERY_HAVEN = [
    "Self-contained and completely private",
    "Fully equipped kitchen and appliances",
    "Fast Wi-Fi",
    "TV",
    "Laundry machine",
]

PROPERTIES = [
    {
        "slug": "george-street",
        "name": "George Street Haven",
        "area": "Staines-upon-Thames",
        "beds": 3,
        "kind": "House",
        "cover": "george-1", "hover": "george-4",
        "imgs": ["george-2", "george-1", "george-4", "george-3", "george-5"],
        "short": "Five minutes' walk to Staines station and the high street, with Thorpe Park just down the road.",
        "about": "Nestled in Staines, this Haven is just a five-minute walk from the station and the high street, with its restaurants, shops and bars. Thorpe Park is ten minutes away, Legoland twenty, and the M25 a five-minute drive.",
        "highlights": ["Walk to the station and high street", "Restaurants, shops and bars nearby", "Quick access to the M25", "Ideal for theme-park trips"],
        "nearby": [("Staines station", "5 min walk"), ("High street", "5 min walk"), ("M25", "5 min drive"), ("Thorpe Park", "10 min"), ("Legoland Windsor", "20 min")],
        "airbnb": "https://www.airbnb.co.uk/rooms/50060759",
        "booking": "https://www.booking.com/hotel/gb/newly-refurbished-3-bed-2-5-bath-house-in-staines.en-gb.html",
    },
    {
        "slug": "hillingdon",
        "name": "Hillingdon Haven",
        "area": "Stanwell",
        "beds": 4,
        "kind": "House",
        "cover": "hill-1", "hover": "hill-2",
        "imgs": ["hill-1", "hill-2", "hill-3", "hill-4", "hill-5"],
        "short": "A modern four-bedroom home in a quiet village, close to Heathrow and the big theme parks.",
        "about": "A modern and ideally located four-bedroom home in the quiet village of Stanwell. It is close to Heathrow, Legoland, Chessington and Thorpe Park, and within easy reach of Central London.",
        "highlights": ["Four bedrooms, room for the whole family", "Modern, ideally located home", "Quiet residential village", "Easy run into Central London"],
        "nearby": [("Heathrow Airport", "Nearby"), ("Thorpe Park", "Nearby"), ("Legoland Windsor", "Nearby"), ("Chessington World of Adventures", "Nearby"), ("Central London", "Close proximity")],
        "airbnb": "https://www.airbnb.co.uk/rooms/39593529",
        "booking": "https://www.booking.com/hotel/gb/ra-3-bedroom-apartment-close-to-heathrow.en-gb.html",
    },
    {
        "slug": "pavilion",
        "name": "Pavilion Haven",
        "area": "Staines-upon-Thames",
        "beds": 3,
        "kind": "House",
        "cover": "pav-1", "hover": "pav-4",
        "imgs": ["pav-1", "pav-4", "pav-2", "pav-3", "pav-5"],
        "short": "A three-bedroom house with spacious rooms and a big garden for slow evenings.",
        "about": "Our nicely decorated three-bedroom house in Staines has spacious rooms, unlimited high-speed internet and a big garden, the ideal place to relax and unwind after a long day.",
        "highlights": ["Big garden", "Spacious rooms throughout", "Unlimited high-speed internet", "Three bedrooms"],
        "nearby": [("Staines town centre", "Nearby"), ("Thorpe Park", "Nearby"), ("Heathrow Airport", "Nearby")],
        "airbnb": "https://www.airbnb.co.uk/rooms/40722454",
        "booking": "https://www.booking.com/hotel/gb/nicely-decorated-3-bedroom-house-near-heathrow-london.en-gb.html",
    },
    {
        "slug": "padcroft",
        "name": "Padcroft Haven",
        "area": "West Drayton",
        "beds": 2,
        "kind": "Apartment",
        "cover": "pad-4", "hover": "pad-1",
        "imgs": ["pad-4", "pad-1", "pad-3", "pad-2"],
        "short": "A tastefully decorated two-bedroom apartment in the heart of West Drayton, with private parking.",
        "about": "Lodge in this tastefully decorated two-bedroom apartment in the heart of West Drayton. It has a spacious living room with a large Smart TV, high-speed Wi-Fi and private parking.",
        "highlights": ["Private parking", "Large Smart TV", "Spacious living room", "High-speed Wi-Fi"],
        "nearby": [("West Drayton centre", "On the doorstep"), ("Heathrow Airport", "Nearby")],
        "airbnb": "https://www.airbnb.co.uk/rooms/47964560",
        "booking": "https://www.booking.com/hotel/gb/stunning-spacious-contemporary-2-bedroom-flat-near-heathrow.en-gb.html",
    },
    {
        "slug": "west-end",
        "name": "West End Haven",
        "area": "Harlington",
        "beds": 2,
        "kind": "House",
        "cover": "west-4", "hover": "west-5",
        "imgs": ["west-4", "west-5", "west-3", "west-2", "west-1"],
        "short": "A beautiful two-bedroom home in Harlington Village, moments from Heathrow.",
        "about": "Step into the comfort of this beautiful two-bedroom home in Harlington Village. It is well connected and close to Heathrow Airport, so getting around is the least of your worries.",
        "highlights": ["Moments from Heathrow", "Well-connected village location", "Two comfortable bedrooms", "Excellent facilities"],
        "nearby": [("Heathrow Airport", "Close by"), ("Harlington Village", "On the doorstep")],
        "airbnb": "https://www.airbnb.co.uk/rooms/46038968",
        "booking": "https://www.booking.com/hotel/gb/exquisite-and-modern-2-bed-apartment.en-gb.html",
    },
    {
        "slug": "benen-stock",
        "name": "Benen Stock Haven",
        "area": "Thames Valley, near Windsor",
        "beds": 2,
        "kind": "House",
        "cover": "benen-1", "hover": "benen-4",
        "imgs": ["benen-1", "benen-4", "benen-2", "benen-3", "benen-5"],
        "short": "A two-bedroom house in a picturesque Thames village, close to Windsor and Runnymede.",
        "about": "An exquisite two-bedroom house in one of the most picturesque villages on the Thames. It is a homely, well-connected base near Windsor Castle, the River Thames and Runnymede.",
        "highlights": ["Picturesque riverside village", "Homely, well-connected base", "Close to Windsor", "Two bedrooms"],
        "nearby": [("Windsor Castle", "Nearby"), ("River Thames", "Nearby"), ("Runnymede", "Nearby")],
        "airbnb": "https://www.airbnb.co.uk/rooms/49085233",
        "booking": "https://www.booking.com/hotel/gb/private-comfortable-2-bedroom-home-away-from-home.en-gb.html",
    },
]

# Quoted exactly as guests wrote them.
REVIEWS = [
    ("Tinia", "Guest review", "The house is very comfortable and homely. It has a real English charm. You will find everything you need for a short or extended stay. Perfect for a family."),
    ("Martin", "Guest review", "Stayed for work, close to Heathrow airport and close to Staines town centre. TV with Netflix and heating. Perfect for work stay."),
    ("Tanya", "Guest review", "We had a great stay. Quick to respond and very accommodating. The Christmas tree was a lovely touch. Perfect for a family & child friendly."),
    ("Will", "Guest review", "Top place to stay. Very friendly & helpful people."),
]

# ---------------------------------------------------------------- icons
ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "bed": '<path d="M3 19V6M3 15h18v4M21 15v-3a3 3 0 0 0-3-3h-7v6"/><circle cx="7" cy="11.5" r="1.6"/>',
    "home": '<path d="M3 11 12 4l9 7M5 9.5V20h14V9.5"/><path d="M10 20v-5h4v5"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "plane": '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
    "kitchen": '<path d="M3 2v7a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2V2M7 2v20M21 15V2a5 5 0 0 0-5 5v6a2 2 0 0 0 2 2h3zm0 0v7"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/>',
    "images": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "close": '<path d="M18 6 6 18M6 6l12 12"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".8" fill="currentColor"/>',
    "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
}


def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- helpers
def img_w(name):
    """Real pixel width of a generated image (for honest srcset values)."""
    try:
        from PIL import Image
        with Image.open(IMG / f"{name}.webp") as im:
            return im.width
    except Exception:
        return 1800


def img(r, name, alt, sizes="(min-width: 1080px) 33vw, (min-width: 700px) 50vw, 100vw", eager=False, cls=""):
    sm, lg = img_w(name + "-sm"), img_w(name)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{r}assets/img/{name}-sm.webp" '
            f'srcset="{r}assets/img/{name}-sm.webp {sm}w, {r}assets/img/{name}.webp {lg}w" '
            f'sizes="{sizes}" alt="{escape(alt)}" {load}>')


def beds_label(n):
    return f"{n} bedroom{'s' if n != 1 else ''}"


NAV = [("index.html", "Home"), ("stays.html", "Our Havens"), ("explore.html", "Explore"),
       ("about.html", "About"), ("contact.html", "Contact")]


def page(path, title, desc, body, active="", og_img="george-2", extra_head=""):
    depth = path.count("/")
    r = "../" * depth
    nav = "".join(
        f'<a href="{r}{href}"{" aria-current=\"page\"" if active == href else ""}>{label}</a>'
        for href, label in NAV)
    full_title = f"{title} | {BRAND}" if title != BRAND else f"{BRAND} | {TAGLINE}"
    phone = PHONES[0]
    html = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#f5f1e9">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{escape(full_title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{r}assets/img/{og_img}.webp">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{r}assets/css/site.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{r}index.html" aria-label="{BRAND} home"><img src="{r}assets/img/mark-dark.png" alt="{BRAND}" width="520" height="370"></a>
    <nav class="nav" aria-label="Main">{nav}<a class="btn btn-ink" href="{r}stays.html">Book a stay</a></nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu"><span></span><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <nav aria-label="Mobile">{nav}</nav>
  <div class="mm-foot">
    <span>Questions? We're happy to help.</span>
    <a href="tel:{phone['tel']}">{phone['display']}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
  </div>
</div>
<main id="main">
{body}
</main>
{footer(r)}
<script src="{r}assets/js/site.js" defer></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("built", path)


def socials_html():
    return "".join(
        f'<a href="{url}" target="_blank" rel="noopener" aria-label="{BRAND} on {name.title()}">{icon(name)}</a>'
        for name, url in SOCIALS.items())


def footer(r):
    stays = "".join(f'<li><a href="{r}stays/{p["slug"]}.html">{p["name"]}</a></li>' for p in PROPERTIES)
    phones = "".join(f'<li><a href="tel:{p["tel"]}">{p["display"]}</a></li>' for p in PHONES)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <p class="footer-big reveal">Another place<br><em>like home.</em></p>
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="{r}assets/img/logo-light.png" alt="{BRAND}: {TAGLINE}" width="520" height="418" loading="lazy">
        <p>A family-run business offering homely short-stay and holiday rentals near Heathrow, Staines and across west London.</p>
        <div class="socials">{socials_html()}</div>
      </div>
      <div><h3>Our Havens</h3><ul>{stays}</ul></div>
      <div><h3>Explore</h3><ul>
        <li><a href="{r}stays.html">All Havens</a></li>
        <li><a href="{r}explore.html">Local guide</a></li>
        <li><a href="{r}about.html">About us</a></li>
        <li><a href="{r}contact.html">Contact</a></li>
      </ul></div>
      <div><h3>Get in touch</h3><ul>{phones}<li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
    </div>
    <div class="footer-bottom"><span>&copy; {YEAR} {BRAND}. All rights reserved.</span><span>Book securely through Airbnb or Booking.com</span></div>
  </div>
</footer>"""


def stay_card(r, p, delay=0):
    return f"""<a class="stay reveal" data-delay="{delay % 3}" data-beds="{p['beds']}" href="{r}stays/{p['slug']}.html">
  <div class="stay-media">
    {img(r, p['cover'], f"{p['name']}, {p['area']}")}
    {img(r, p['hover'], "")}
    <span class="stay-tag">{escape(p['area'])}</span>
    <span class="stay-go" aria-hidden="true">{icon('arrow')}</span>
  </div>
  <div class="stay-body">
    <div class="stay-top"><h3>{p['name']}</h3><span class="beds">{beds_label(p['beds'])}</span></div>
    <p>{escape(p['short'])}</p>
  </div>
</a>"""


def stays_section(r, heading, eyebrow_num="02"):
    beds = sorted({p["beds"] for p in PROPERTIES})
    chips = '<button class="chip" type="button" data-filter="all" aria-pressed="true">All Havens</button>' + "".join(
        f'<button class="chip" type="button" data-filter="{b}" aria-pressed="false">{b} bedrooms</button>' for b in beds)
    cards = "\n".join(stay_card(r, p, i) for i, p in enumerate(PROPERTIES))
    return f"""<section class="section" id="havens">
  <div class="wrap">
    <div class="section-head split">
      <div class="reveal"><span class="eyebrow"><span class="index-num">{eyebrow_num}</span> The Havens</span>
        <h2 class="h2" style="margin-top:18px">{heading}</h2></div>
      <div class="reveal" data-delay="1"><p class="lead" style="margin-bottom:22px">Six self-contained homes, each fully equipped and ready for a short trip or a longer stay.</p>
        <div class="filters" role="group" aria-label="Filter by bedrooms">{chips}</div></div>
    </div>
    <div class="stays featured">
{cards}
    </div>
  </div>
</section>"""


def cta(r):
    return f"""<section class="section-tight">
  <div class="wrap">
    <div class="cta reveal">
      <h2 class="h2">Your home away from home is <em>ready.</em></h2>
      <p>Pick a Haven and book securely through Airbnb or Booking.com, or get in touch and we'll help you find the right fit.</p>
      <div class="cta-actions">
        <a class="btn btn-night" href="{r}stays.html">Find your Haven {icon('arrow')}</a>
        <a class="btn btn-outline-light" href="tel:{PHONES[0]['tel']}">{icon('phone')} {PHONES[0]['display']}</a>
      </div>
    </div>
  </div>
</section>"""


# ---------------------------------------------------------------- pages
def build_home():
    r = ""
    places = ["Staines-upon-Thames", "West Drayton", "Stanwell", "Harlington", "Windsor", "Heathrow"]
    marquee = "".join(f"<span>{p}</span>" for p in places * 2)
    features = [
        ("lock", "Private and self-contained", "Every Haven is entirely yours, with no shared spaces and no strangers."),
        ("kitchen", "Fully equipped", "TVs, Wi-Fi, laundry machines and full kitchens, so it feels like home."),
        ("plane", "Great locations", "Near Heathrow, the M25, Windsor, Thorpe Park and Legoland."),
        ("calendar", "Hassle-free", "From booking to checkout, the process is simple, flexible and seamless."),
    ]
    feats = "".join(
        f'<div class="feature reveal" data-delay="{i % 2}"><span class="ico">{icon(ic)}</span><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i, (ic, t, d) in enumerate(features))
    reviews = "".join(
        f"""<figure class="review{' active' if i == 0 else ''}"><blockquote>{escape(q)}</blockquote>
        <figcaption><span class="avatar" aria-hidden="true">{n[0]}</span><span>{n}<small>{escape(t)}</small></span></figcaption></figure>"""
        for i, (n, t, q) in enumerate(REVIEWS))
    dots = "".join(f'<button type="button" aria-label="Show review {i + 1}"></button>' for i in range(len(REVIEWS)))
    beds = [p["beds"] for p in PROPERTIES]
    schema = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LodgingBusiness","name":"{BRAND}","slogan":"{TAGLINE}","description":"Family-run short-stay and holiday homes near Heathrow, Staines and west London.","telephone":"{PHONES[1]['tel']}","email":"{EMAIL}","areaServed":["Staines-upon-Thames","West Drayton","Stanwell","Harlington","Heathrow"],"sameAs":["{SOCIALS['instagram']}","{SOCIALS['facebook']}"]}}</script>
"""
    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Short stays near Heathrow &amp; west London</span>
      <h1 class="display"><span class="line"><span>Another place</span></span><span class="line"><span><em>like home.</em></span></span></h1>
      <p class="lead">Six self-contained, fully equipped homes across Staines, West Drayton and the Thames Valley. Family-run, and minutes from Heathrow.</p>
      <div class="hero-actions">
        <a class="btn btn-ink" href="#havens">Browse our Havens {icon('arrow')}</a>
        <a class="btn btn-line" href="contact.html">Ask a question</a>
      </div>
      <div class="hero-facts">
        <div><strong>{len(PROPERTIES)}</strong><span>Havens to choose from</span></div>
        <div><strong>{min(beds)}–{max(beds)}</strong><span>Bedrooms per home</span></div>
        <div><strong>100%</strong><span>Private &amp; self-contained</span></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="roof-frame"><div class="roof">{img(r, 'george-2', 'A candle-lit bath with wine at George Street Haven', '(min-width: 980px) 45vw, 100vw', eager=True)}</div></div>
      <figure class="float-card float-photo">{img(r, 'pav-1', 'Pavilion Haven and its big garden', '240px')}<figcaption>Pavilion Haven <span>Staines</span></figcaption></figure>
      <div class="float-card float-quote"><p>“It has a real English charm.”</p><small>Tinia, guest</small></div>
    </div>
  </div>
  <div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>
</section>

<section class="section bg-2">
  <div class="wrap intro-grid">
    <div class="reveal">
      <span class="eyebrow"><span class="index-num">01</span> Why stay with us</span>
      <p class="intro-statement" style="margin-top:22px">Whatever brings you here, <em>a work trip, a family holiday or a long stay,</em> we've got you covered.</p>
      <p class="lead" style="margin-top:24px">We put your convenience at the heart of everything, from a hassle-free booking to a seamless checkout. Every home is fitted out to a high standard, so your stay is relaxing and comfortable.</p>
    </div>
    <div class="features">{feats}</div>
  </div>
</section>

{stays_section(r, 'Find the Haven that <em>fits your trip.</em>')}

<section class="section dark reviews">
  <div class="wrap">
    <span class="eyebrow"><span class="index-num" style="color:var(--green)">03</span> Guest stories</span>
    <div class="reviews-grid" style="margin-top:40px">
      <div>
        <div class="review-stage" aria-live="polite">{reviews}</div>
        <div class="review-controls"><div class="review-dots">{dots}</div></div>
      </div>
      <div class="review-side">
        <p class="muted">Stayed with us? We'd love to hear how it went.</p>
        <a class="btn btn-light" href="mailto:{EMAIL}?subject=My%20stay%20at%20Aces%20Haven">Leave a review {icon('arrow')}</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head split">
      <div class="reveal"><span class="eyebrow"><span class="index-num">04</span> Experience London</span>
        <h2 class="h2" style="margin-top:18px">A city full of life, <em>right on your doorstep.</em></h2></div>
      <div class="reveal" data-delay="1"><p class="lead" style="margin-bottom:22px">It can be hard to know where to go, where to eat and how to spend your time. Our local guide gathers our favourite places near the Havens and in the city.</p>
        <a class="link-arrow" href="explore.html">Open the local guide {icon('arrow')}</a></div>
    </div>
    <div class="mosaic">
      <figure class="m1 reveal">{img(r, 'att-3', 'The London Eye lit up at night', '(min-width: 900px) 40vw, 100vw')}<figcaption>Top sights</figcaption></figure>
      <figure class="m2 reveal" data-delay="1">{img(r, 'london-2', 'Leadenhall Market in the City of London', '(min-width: 900px) 30vw, 50vw')}<figcaption>Shopping</figcaption></figure>
      <figure class="m3 reveal" data-delay="2">{img(r, 'att-1', 'A roast dinner', '(min-width: 900px) 30vw, 50vw')}<figcaption>Eat</figcaption></figure>
      <figure class="m4 reveal" data-delay="1">{img(r, 'att-2', 'A warmly lit London bar', '(min-width: 900px) 60vw, 100vw')}<figcaption>Caf&eacute;s &amp; bars</figcaption></figure>
    </div>
  </div>
</section>

{cta(r)}
"""
    page("index.html", BRAND,
         "Aces Haven offers family-run, self-contained short-stay homes near Heathrow, Staines and west London. Book on Airbnb or Booking.com.",
         body, active="index.html", extra_head=schema)


def build_stays():
    r = ""
    included = "".join(f"<li>{x}</li>" for x in EVERY_HAVEN)
    body = f"""<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Our Havens</span></nav>
    <h1 class="display">Our <em>Havens.</em></h1>
    <p class="lead">Six homes across Staines, Stanwell, West Drayton, Harlington and the Thames Valley. Choose one, take a look around, then book securely on Airbnb or Booking.com.</p>
  </div>
</section>
{stays_section(r, 'Two, three or four bedrooms, <em>all yours.</em>', '01').replace('class="section" id="havens"', 'class="section" id="havens" style="padding-top:0"')}
<section class="section-tight bg-2">
  <div class="wrap intro-grid">
    <div class="reveal"><span class="eyebrow">In every Haven</span>
      <h2 class="h2" style="margin-top:18px">The essentials, <em>sorted.</em></h2></div>
    <div class="reveal" data-delay="1"><ul class="ticks">{included}</ul></div>
  </div>
</section>
{cta(r)}
"""
    page("stays.html", "Our Havens",
         "Browse all six Aces Haven short-stay homes near Heathrow, Staines and West Drayton, with two to four bedrooms.",
         body, active="stays.html")


def build_property(i, p):
    r = "../"
    n = len(p["imgs"])
    shots = "".join(
        f'<button type="button" data-full="{r}assets/img/{name}.webp" aria-label="View photo {k + 1} of {n}">'
        f'{img(r, name, f"{p["name"]}, photo {k + 1}", "(min-width: 860px) 50vw, 100vw" if k == 0 else "(min-width: 860px) 25vw, 50vw", eager=(k == 0))}'
        + (f'<span class="more">{icon("images")} All {n} photos</span>' if k == 0 else "") + '</button>'
        for k, name in enumerate(p["imgs"]))
    highlights = "".join(f"<li>{escape(h)}</li>" for h in p["highlights"])
    included = "".join(f"<li>{x}</li>" for x in EVERY_HAVEN)
    nearby = "".join(f"<li>{escape(a)}<span>{escape(b)}</span></li>" for a, b in p["nearby"])
    others = [PROPERTIES[(i + k) % len(PROPERTIES)] for k in (1, 2, 3)]
    other_cards = "\n".join(stay_card(r, o, k) for k, o in enumerate(others))
    phone = PHONES[0]
    gallery_cls = "gallery" + (" n4" if n == 4 else "")
    body = f"""<section class="prop-head">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{r}index.html">Home</a><span aria-hidden="true">/</span><a href="{r}stays.html">Our Havens</a><span aria-hidden="true">/</span><span>{p['name']}</span></nav>
    <div class="prop-title">
      <div>
        <h1 class="display">{p['name'].replace(' Haven', '')} <em>Haven</em></h1>
        <p class="prop-loc">{icon('pin')} {escape(p['area'])}</p>
      </div>
      <div class="pills">
        <span class="pill">{icon('bed')} {beds_label(p['beds'])}</span>
        <span class="pill">{icon('home')} Entire {p['kind'].lower()}</span>
        <span class="pill">{icon('lock')} Self-contained</span>
      </div>
    </div>
  </div>
</section>
<div class="wrap"><div class="{gallery_cls}">{shots}</div></div>
<div class="wrap prop-body">
  <div>
    <p class="about">{escape(p['about'])}</p>
    <div class="prop-block"><h2>Highlights</h2><ul class="ticks">{highlights}</ul></div>
    <div class="prop-block"><h2>What's included</h2><ul class="ticks">{included}</ul></div>
    <div class="prop-block"><h2>Getting around</h2><ul class="guide-list">{nearby}</ul></div>
  </div>
  <aside class="book-card" id="book">
    <span class="eyebrow">Ready to stay?</span>
    <h2>Book {p['name']}</h2>
    <p>Check live availability and prices, then book securely.</p>
    <a class="btn btn-airbnb btn-block" href="{p['airbnb']}" target="_blank" rel="noopener">Book on Airbnb {icon('arrow')}</a>
    <a class="btn btn-line btn-block" href="{p['booking']}" target="_blank" rel="noopener">Book on Booking.com</a>
    <span class="or">or ask us directly</span>
    <a class="call" href="tel:{phone['tel']}">{icon('phone')}<span><small>Call or text</small><strong>{phone['display']}</strong></span></a>
  </aside>
</div>
<div class="book-bar">
  <div><strong>{p['name']}</strong><small>{beds_label(p['beds'])} · {escape(p['area'])}</small></div>
  <a class="btn btn-airbnb" href="{p['airbnb']}" target="_blank" rel="noopener">Book now</a>
</div>
<section class="section bg-2">
  <div class="wrap">
    <div class="section-head split">
      <div><span class="eyebrow">Keep exploring</span><h2 class="h2" style="margin-top:18px">Other <em>Havens.</em></h2></div>
      <div><a class="link-arrow" href="{r}stays.html">See all Havens {icon('arrow')}</a></div>
    </div>
    <div class="stays">{other_cards}</div>
  </div>
</section>
<dialog class="lightbox" aria-label="Photo gallery">
  <div class="lb-top"><span class="lb-count"></span><button class="icon-btn" type="button" data-lb="close" aria-label="Close gallery">{icon('close')}</button></div>
  <div class="lb-stage"><img src="" alt=""></div>
  <div class="lb-nav"><button class="icon-btn" type="button" data-lb="prev" aria-label="Previous photo">{icon('left')}</button><button class="icon-btn" type="button" data-lb="next" aria-label="Next photo">{icon('right')}</button></div>
</dialog>
"""
    page(f"stays/{p['slug']}.html", p["name"],
         f"{p['name']}: a self-contained {beds_label(p['beds'])} {p['kind'].lower()} in {p['area']}. {p['short']}",
         body, active="stays.html", og_img=p["imgs"][0])


GUIDE = [
    ("eat", "Eat", "Restaurants", "Every cuisine, <em>close to home.</em>", "att-1", "A roast dinner",
     "Whether you dine in London or near your Haven, there is a huge choice of cuisines. Staines has Asian, Indian, Caribbean and British restaurants. In Hayes you can choose traditional British, Mediterranean or Indian. In London you can have anything. Why not try the African cuisine at Azou in Hammersmith?",
     [("Staines", "Asian, Indian, Caribbean, British"), ("Hayes", "British, Mediterranean, Indian"), ("Azou", "Hammersmith")], False),
    ("cafes", "Cafés & bars", "Cafés & bars", "Coffee by day, <em>cocktails by night.</em>", "att-2", "A warmly lit bar",
     "Fancy a cup of coffee or a glass of something cold? These come highly recommended by us, from local favourites near the Havens to some of London's best bars.",
     [("Marianne's Community Café", "Staines"), ("Nostrano Lounge", "Staines"), ("Attendant", "Foley St, London"), ("Draughts", "Acton Mews"),
      ("Lady Dinah's Cat Emporium", "Bethnal Green"), ("Nightjar", "Shoreditch"), ("Avery", "City of London"), ("68 and Boston", "Soho")], False),
    ("sights", "Top 10", "London's top ten", "The ten places <em>you can't miss.</em>", "att-3", "The London Eye at night",
     "London is full of hidden treasures. Some are on the map, others are a little harder to find. These are our top ten places to visit while you're in London.",
     [("The London Eye", ""), ("The British Museum", ""), ("The Tower of London", ""), ("Kew Gardens", ""), ("Somerset House", ""),
      ("Madame Tussauds", ""), ("The V&A", ""), ("The Wellcome Collection", ""), ("Sky Garden", ""), ("Deptford Creek low-tide walk", "")], True),
    ("galleries", "Galleries", "Galleries", "Art for <em>every taste.</em>", "att-4", "Antique ceramics on display",
     "London is blessed with a huge variety of art galleries. Here are some that will delight your artistic senses.",
     [("The National Gallery", "Trafalgar Square"), ("National Portrait Gallery", "Trafalgar Square"), ("Royal Academy of Arts", "Piccadilly"),
      ("Tate Modern", "Bankside"), ("Tate Britain", "Millbank"), ("Saatchi Gallery", "King's Road"), ("Serpentine Gallery", "Kensington Gardens"),
      ("Barbican Art Gallery", "Barbican"), ("Hayward Gallery", "Southbank")], False),
    ("days-out", "Days out", "Days out", "Thrills, magic <em>and open space.</em>", "london-1", "Big Ben against a blue sky",
     "All our Havens are close to Thorpe Park. If you want something different, here are some great days out in and around London.",
     [("Thorpe Park", "Close to every Haven"), ("Legoland Windsor Resort", "Windsor"), ("Chessington World of Adventures", "Chessington"),
      ("Warner Bros. Studio Tour: The Making of Harry Potter", "Leavesden"), ("Hyde Park", "Central London")], False),
    ("shopping", "Shopping", "Shopping", "Markets, arcades <em>and big-name stores.</em>", "london-2", "Leadenhall Market",
     "There are plenty of shops and markets near the Havens and in central London. For great shopping, try these.",
     [("Westfield London", "Shepherd's Bush"), ("Kensington Arcade", "Kensington"), ("Camden Market", "Camden Town"),
      ("Covent Garden", "Covent Garden"), ("Royal Arcade", "Mayfair"), ("Hay's Galleria", "London Bridge")], False),
]


def build_explore():
    r = ""
    nav = "".join(f'<a href="#{g[0]}">{escape(g[1])}</a>' for g in GUIDE)
    secs = []
    for k, (gid, _, eyebrow, heading, im, alt, text, items, numbered) in enumerate(GUIDE):
        lis = "".join(f"<li>{escape(a)}<span>{escape(b)}</span></li>" if b else f"<li>{escape(a)}</li>" for a, b in items)
        secs.append(f"""<section class="guide" id="{gid}">
  <div class="guide-media reveal">{img(r, im, alt, '(min-width: 900px) 50vw, 100vw')}</div>
  <div class="reveal" data-delay="1">
    <span class="eyebrow"><span class="index-num">{k + 1:02d}</span> {escape(eyebrow)}</span>
    <h2 class="h2">{heading}</h2>
    <p class="lead">{escape(text)}</p>
    <ul class="guide-list{' numbered' if numbered else ''}">{lis}</ul>
  </div>
</section>""")
    body = f"""<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Local guide</span></nav>
    <h1 class="display">Experience <em>London.</em></h1>
    <p class="lead">London is an extraordinary city full of life. To help you plan your visit, here are our favourite places to eat, drink, explore and shop while you stay at one of our Havens.</p>
  </div>
</section>
<nav class="explore-nav" aria-label="Guide sections"><div class="wrap">{nav}</div></nav>
<div class="wrap">
{''.join(secs)}
</div>
{cta(r)}
"""
    page("explore.html", "Local guide",
         "The Aces Haven guide to London and the areas around our Havens: restaurants, cafés, bars, top sights, galleries, days out and shopping.",
         body, active="explore.html", og_img="att-3")


def build_about():
    r = ""
    why = [
        ("Great locations", "Our Havens are in lively, well-connected places like Staines, West Drayton and Stanwell. They are safe, quiet residential areas with plenty of London attractions nearby."),
        ("Amenities", "Every Haven is fully kitted out with TVs, Wi-Fi, laundry machines, kitchens and appliances, for a comfortable, homelike stay."),
        ("Hassle-free", "From booking to checkout, our process is simple, flexible and seamless."),
        ("Great living", "A relaxed, homely space that brings together fresh, convenient and comfortable indoor living."),
    ]
    feats = "".join(
        f'<div class="feature reveal" data-delay="{i % 2}"><span class="ico">{icon(ic)}</span><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i, ((t, d), ic) in enumerate(zip(why, ["pin", "kitchen", "calendar", "home"])))
    body = f"""<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>About</span></nav>
    <h1 class="display">A family business, <em>built around home.</em></h1>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap story">
    <div class="story-text reveal">
      <span class="eyebrow">Our story</span>
      <p class="intro-statement" style="margin:22px 0 28px">Homely short-stay and <em>holiday homes.</em></p>
      <p>Aces Haven is a family-run business offering short-stay and holiday homes. The brand grew from our love of home, and our wish to create homelike experiences for other people.</p>
      <p>Our self-catering and short-term holiday rentals give you a residential base for exploring London and enjoying the local attractions.</p>
      <p>We offer secure online booking, helpful hosts, quality homes and homely touches, so you can relax and enjoy your stay.</p>
    </div>
    <div class="story-media reveal" data-delay="1">
      <div class="roof">{img(r, 'george-4', 'A bright twin bedroom', '(min-width: 960px) 25vw, 50vw')}</div>
      <figure>{img(r, 'pav-1', 'Pavilion Haven from the garden', '(min-width: 960px) 20vw, 50vw')}</figure>
      <figure>{img(r, 'benen-2', 'The kitchen at Benen Stock Haven', '(min-width: 960px) 20vw, 50vw')}</figure>
    </div>
  </div>
</section>
<section class="section dark">
  <div class="wrap">
    <div class="pillars">
      <div class="pillar reveal"><span class="tag">Our mission</span><p class="h3">To create memorable, positive experiences by offering homely short-stay and holiday rentals.</p></div>
      <div class="pillar reveal" data-delay="1"><span class="tag">Our promise</span><p class="h3">We never compromise on your satisfaction. At Aces Haven, you can truly feel at home.</p></div>
    </div>
  </div>
</section>
<section class="section bg-2">
  <div class="wrap intro-grid">
    <div class="reveal"><span class="eyebrow">Why stay with us</span>
      <h2 class="h2" style="margin-top:18px">More than a place <em>to sleep.</em></h2>
      <p class="lead" style="margin-top:22px">Beyond our thoughtful welcome packs and little keepsakes, here's why Aces Haven should be your first choice.</p></div>
    <div class="features">{feats}</div>
  </div>
</section>
{cta(r)}
"""
    page("about.html", "About us",
         "Aces Haven is a family-run business offering homely, self-contained short-stay and holiday rentals near Heathrow and west London.",
         body, active="about.html", og_img="george-4")


def build_contact():
    r = ""
    phones = "".join(
        f'<a class="contact-card reveal" href="tel:{p["tel"]}"><span class="ico">{icon("phone")}</span><span><small>{p["label"]}</small><strong>{p["display"]}</strong></span></a>'
        for p in PHONES)
    options = "".join(f"<option>{p['name']}</option>" for p in PROPERTIES)
    body = f"""<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Contact</span></nav>
    <h1 class="display">Let's <em>talk.</em></h1>
    <p class="lead">Questions about a Haven, a longer stay or a group booking? Call, email or send us a message and we'll get back to you quickly.</p>
  </div>
</section>
<div class="wrap contact-grid">
  <div class="contact-cards">
    {phones}
    <a class="contact-card reveal" href="mailto:{EMAIL}"><span class="ico">{icon('mail')}</span><span><small>Email</small><strong>{EMAIL}</strong></span></a>
    <div class="reveal" style="margin-top:18px"><span class="eyebrow">Follow along</span><div class="socials">{socials_html()}</div></div>
  </div>
  <form class="form reveal" id="enquiry" data-to="{EMAIL}" data-delay="1">
    <h2 class="h3">Send an enquiry</h2>
    <div class="row">
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
    </div>
    <div class="row">
      <div class="field"><label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><label for="f-haven">Which Haven?</label><select id="f-haven" name="haven"><option>Not sure yet</option>{options}</select></div>
    </div>
    <div class="row">
      <div class="field"><label for="f-in">Check-in</label><input id="f-in" name="checkin" type="date"></div>
      <div class="field"><label for="f-out">Check-out</label><input id="f-out" name="checkout" type="date"></div>
    </div>
    <div class="field"><label for="f-guests">Guests</label><input id="f-guests" name="guests" type="number" min="1" max="12" inputmode="numeric"></div>
    <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" placeholder="Tell us a little about your trip"></textarea></div>
    <button class="btn btn-ink" type="submit">Send enquiry {icon('arrow')}</button>
    <p class="form-note">This opens your email app with your message ready to send to {EMAIL}.</p>
  </form>
</div>
"""
    page("contact.html", "Contact",
         f"Contact Aces Haven about a stay. Call {PHONES[0]['display']} or {PHONES[1]['display']}, or email {EMAIL}.",
         body, active="contact.html")


def build_404():
    body = """<section class="notfound">
  <div>
    <span class="eyebrow">Page not found</span>
    <p class="display"><em>404</em></p>
    <p class="lead">This room seems to be empty. Let's get you back somewhere comfortable.</p>
    <a class="btn btn-ink" href="/">Back to home</a>
  </div>
</section>"""
    page("404.html", "Page not found", "This page could not be found.", body)


if __name__ == "__main__":
    build_home()
    build_stays()
    for i, p in enumerate(PROPERTIES):
        build_property(i, p)
    build_explore()
    build_about()
    build_contact()
    build_404()
