"""Michael LaPenna author site (concept). Run: python3 _build.py"""
import os
R=os.path.dirname(os.path.abspath(__file__))
NAV=[('index.html','Home'),('books.html','Books'),('visits.html','Visits'),('about.html','About'),('media.html','Media'),('contact.html','Contact')]
AMZ='https://www.amazon.com/dp/'
YT='POn3cG_RTKs'
SPREAKER='https://www.spreaker.com/episode/episode-330-michael-lapenna-on-his-book-baby-jesus-is-missing-october-13-2026--75766588'

BOOKS=[
 dict(n=1,slug='baby-jesus-is-missing',title='Baby Jesus Is Missing',short='A Christmas mystery',pub='Ambassador International',year='2020',
  details=['Hardcover, 44 pages','Illustrated by Chris Jackson','Reading age 5 to 12'],
  cover='cover-baby-jesus-is-missing.jpg',w=700,h=1144,
  sum='In the small town of Reedy River, baby Jesus figurines are vanishing from Nativity scenes all over town in early December. When Catherine and her younger sister, Susanna Mae, hear about a $500 reward, they set out to catch the thief, and find the case asks more of them than they expected.',
  buy=[('Amazon',AMZ+'1620209330'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/baby-jesus-is-missing-michael-lapenna/1138393399?ean=9781620209332'),('Publisher','https://ambassador-international.com/books/baby-jesus-is-missing/')]),
 dict(n=2,slug='the-offering',title='The Offering',short='A mountain adventure',pub='Ambassador International',year='2023',
  details=['Paperback, 62 pages','Reading age 4 to 8'],
  cover='cover-the-offering.jpg',w=700,h=1000,
  sum='On a visit to their grandparents’ house in the mountains, the sisters turn up a rusted tin of money. Then their border collie, Atticus, takes off after a bear cub into the woods their grandfather told them to stay out of, and the girls have to decide what to do.',
  buy=[('Amazon',AMZ+'1649603126'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/the-offering-michael-lapenna/1143777727?ean=9781649605870'),('Publisher','https://ambassador-international.com/books/the-offering/')]),
 dict(n=3,slug='angelina-grace',title='Angelina Grace',short='An autumn mystery',pub='Ambassador International',year='2025',
  details=['Paperback, 164 pages'],
  cover='cover-angelina-grace.jpg',w=700,h=1130,
  sum='One autumn afternoon Catherine comes upon a young woman living alone in a secluded hollow outside town. As the sisters get to know their new friend, Ulga, they are drawn into the questions surrounding her, and into a decision about her safety.',
  buy=[('Amazon',AMZ+'1649606133'),('Publisher','https://ambassador-international.com/books/angelina-grace/')]),
 dict(n=4,slug='lauras-locker',title='Laura’s Locker',short='A story about telling the truth',pub='En Route Books and Media',year='2026',
  details=['Paperback, 191 pages','Kindle and Audible'],
  cover='cover-lauras-locker.jpg',w=666,h=1000,
  sum='Susanna Mae watches a classmate get framed for cheating and has to find the courage to tell the truth. Along the way, a visit to her grandparents in Gloucester, Massachusetts, brings mysterious woods and old legends.',
  quote=('Michael LaPenna invites young readers into a compelling encounter with conscience, courage, and grace. Laura’s Locker reveals how faith strengthens the heart to confront injustice, embrace truth, and discover the healing power of authentic friendship.','Dr. Sebastian Mahfood, OP','author of <i>The Narrative Spirituality of Dante’s Divine Comedy</i>'),
  buy=[('Paperback',AMZ+'B0HPS6LFQ8'),('Kindle',AMZ+'B0HMDQLXDR'),('Audible','https://www.audible.com/pd/Audiobook/B0HL6SZ6DQ'),('Publisher','https://enroutebooksandmedia.com/lauraslocker/')]),
]
L=BOOKS[3]
PH=lambda t:f'<p class="ph-note">{t}</p>'
VIDEO=f'<div class="frame"><iframe src="https://www.youtube-nocookie.com/embed/{YT}" title="Michael LaPenna on The Catholic Bookworm" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'

ICON={
 'school':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10 12 5l9 5-9 5-9-5Z"/><path d="M7 12.5V17c3 2 7 2 10 0v-4.5"/></svg>',
 'library':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h4v16H4zM10 4h4v16h-4z"/><path d="m16 5 3.5-1 3 15.5-3.5 1z"/></svg>',
 'fair':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9h18l-2-4H5L3 9Z"/><path d="M5 9v11h14V9M9 20v-6h6v6"/></svg>',
 'store':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19c4-1 6-6 8-11 1 4 3 8 8 11"/><path d="M14 4l3 3-8 8H6v-3z"/></svg>',
}
VISITS=[
 ('school','Schools','Readings for classrooms and assemblies, with time for students’ questions.'),
 ('library','Libraries','Story time and reading events for young readers and their families.'),
 ('fair','Book fairs','Readings and signing tables at school and community book fairs.'),
 ('store','Bookstores','Book signings and readings at bookstores.'),
]

def page(fname,title,desc,body):
    nav=''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>try{{if(localStorage.getItem('ml-desktop')==='1')document.querySelector('meta[name=viewport]').setAttribute('content','width=1200')}}catch(e){{}}</script>
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/cover-lauras-locker.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><b>Michael LaPenna</b><span>The LaRosa Sisters</span></a>
  <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" aria-label="Main"><ul>{nav}</ul><a class="btn sm nav-cta" href="contact.html?topic=visit">Invite Michael</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer>
  <div class="f-strip"><div class="wrap">
    <div><b class="f-name">Michael LaPenna</b><p>Author of the LaRosa Sisters, Catholic mysteries for young readers.</p></div>
    <div class="f-ctas"><a class="btn gold sm" href="books.html">Get the books</a><a class="btn ghost-light sm" href="contact.html?topic=visit">Invite Michael</a></div>
  </div></div>
  <div class="wrap">
    <ul class="f-nav">{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul>
    <div class="f-base"><span>© 2026 Michael LaPenna</span><button type="button" class="vp-toggle">View desktop version</button><a href="https://lickitysplitweb.com" target="_blank" rel="noopener">Site by Lickity Split Web Design</a></div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
'''

def cover(b,cls='cv',lazy=True):
    return f'<img class="{cls}" src="assets/{b["cover"]}" width="{b["w"]}" height="{b["h"]}" alt="Cover of {b["title"]}"{" loading=\"lazy\"" if lazy else ""}>'
def buys(b,cls='sm'): return '<div class="buy">'+''.join(f'<a class="btn {cls}{" ghost" if i else ""}" href="{u}" target="_blank" rel="noopener">{t}</a>' for i,(t,u) in enumerate(b['buy']))+'</div>'
def visit_cards(): return '<div class="v-grid">'+''.join(f'<article class="v-card"><span class="ic">{ICON[k]}</span><h3>{t}</h3><p>{d}</p></article>' for k,t,d in VISITS)+'</div>'

P={}
q=L['quote']
P['index.html']=('Michael LaPenna | Author of the LaRosa Sisters','Michael LaPenna is the author of the LaRosa Sisters, Catholic mysteries for young readers. He visits schools, libraries, book fairs, and bookstores.',f'''
<section class="hero on-dark"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="kicker">The LaRosa Sisters · Catholic mysteries for young readers</p>
    <h1>Two sisters, a small town, and the courage to do what’s right.</h1>
    <p class="lede">Michael LaPenna writes the LaRosa Sisters, mysteries in which Catherine and Susanna Mae LaRosa solve puzzles and learn about faith, friendship, and telling the truth. Four books so far, from a 44-page Christmas mystery to a 191-page novel.</p>
    <div class="ctas"><a class="btn" href="books.html">See all four books</a><a class="btn ghost-light" href="visits.html">Invite Michael to your school</a></div>
  </div>
  <div class="hero-book">
    <span class="badge">New · October 2026</span>
    <a href="books.html#lauras-locker">{cover(L,'cv big',False)}</a>
  </div>
</div></section>

<section class="logos"><div class="wrap logos-in">
  <p class="eyebrow">Published by</p>
  <a href="https://ambassador-international.com/" target="_blank" rel="noopener"><img src="assets/logos/ambassador-international.png" width="441" height="64" alt="Ambassador International" class="lg-amb"></a>
  <a href="https://enroutebooksandmedia.com/" target="_blank" rel="noopener"><img src="assets/logos/en-route-books.png" width="1263" height="340" alt="En Route Books and Media" class="lg-er"></a>
  <span class="sep" aria-hidden="true"></span>
  <p class="eyebrow">Heard on</p>
  <a href="{SPREAKER}" target="_blank" rel="noopener"><img src="assets/logos/wcat-radio.png" width="276" height="279" alt="WCAT Radio" class="lg-wcat"></a>
</div></section>

<section class="band paper"><div class="wrap two why">
  <div class="prose">
    <p class="kicker dark">About the series</p>
    <h2>Mysteries with a conscience.</h2>
    <p class="drop">Every LaRosa Sisters book starts with a puzzle. A thief is stealing baby Jesus figurines from Nativity scenes all over town. A border collie bolts after a bear cub into forbidden woods. A young woman is living alone in a hollow outside town. A classmate is framed for cheating.</p>
    <p>Solving each one asks something of Catherine and her younger sister, Susanna Mae. They have to be brave, tell the truth, and decide what is right when it costs them something. The sisters grow up as the series goes on, and the books grow with them.</p>
    <a class="link" href="books.html">Read about every book</a>
  </div>
  <div class="fan" aria-hidden="true">{''.join(f'<a href="books.html#{b["slug"]}" tabindex="-1" style="--i:{i}">{cover(b)}</a>' for i,b in enumerate(BOOKS))}</div>
</div></section>

<section class="band quote-band"><div class="wrap">
  <blockquote class="big-q"><p>“{q[0]}”</p><cite><b>{q[1]}</b>, {q[2]}</cite></blockquote>
</div></section>

<section class="band on-dark"><div class="wrap">
  <div class="sec-h"><p class="kicker">Reading order</p><h2>The series so far</h2></div>
  <ol class="order">{''.join(f'<li><a href="books.html#{b["slug"]}">{cover(b)}<span class="no">Book {b["n"]} · {b["year"]}</span><b>{b["title"]}</b><span class="sm-t">{b["details"][0]}</span></a></li>' for b in BOOKS)}</ol>
</div></section>

<section class="band white"><div class="wrap">
  <div class="sec-h row"><div><p class="kicker dark">Readings and signings</p><h2>Bring the LaRosa Sisters to your readers.</h2></div><a class="link" href="visits.html">How visits work</a></div>
  {visit_cards()}
  <div class="center"><a class="btn" href="contact.html?topic=visit">Plan a visit</a></div>
</div></section>

<section class="band on-dark media-band"><div class="wrap two">
  {VIDEO}
  <div><p class="kicker">On the air</p><h2>Michael on The Catholic Bookworm</h2>
  <p>Host Kiki Latimer talks with Michael about <i>Baby Jesus Is Missing</i> on WCAT Radio’s The Catholic Bookworm, episode 330, October 13, 2026.</p>
  <div class="buy"><a class="btn sm" href="https://www.youtube.com/watch?v={YT}" target="_blank" rel="noopener">Watch on YouTube</a><a class="btn sm ghost-light" href="{SPREAKER}" target="_blank" rel="noopener">Listen to the episode</a></div></div>
</div></section>

<section class="band paper"><div class="wrap two author">
  <img class="portrait" src="assets/michael-lapenna.jpg" width="573" height="720" alt="Michael LaPenna" loading="lazy">
  <div class="prose"><p class="kicker dark">About the author</p><h2>Thirty-four years in the classroom.</h2>
  <p>Michael LaPenna grew up on the North Shore of Massachusetts and taught secondary school English for thirty-four years, coaching basketball and baseball along the way. Since retiring he has been writing for young readers.</p>
  <a class="btn ghost" href="about.html">Read the full biography</a></div>
</div></section>

<section class="band on-dark cta-band"><div class="wrap cta-in">
  <div><h2>Planning a school visit, book fair, or signing?</h2><p>Tell Michael about your readers and the dates you have in mind.</p></div>
  <a class="btn" href="contact.html?topic=visit">Invite Michael</a>
</div></section>''')

def bookrow(b):
    qb=''
    if b.get('quote'):
        qq=b['quote'];qb=f'<blockquote class="mini-q"><p>“{qq[0]}”</p><cite>{qq[1]}</cite></blockquote>'
    return f'''<article class="book" id="{b["slug"]}"><div class="cv-wrap">{cover(b)}</div><div>
<span class="no">Book {b["n"]} · {b["year"]}</span><h2>{b["title"]}</h2><p class="meta">{b["pub"]}</p>
<p>{b["sum"]}</p>{qb}
<ul class="facts">{''.join(f'<li>{d}</li>' for d in b["details"])}</ul>{buys(b)}</div></article>'''
P['books.html']=('Books | Michael LaPenna','All four LaRosa Sisters books by Michael LaPenna in reading order, with links to buy each one.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Books</p><h1>The LaRosa Sisters</h1><p class="lede">Catherine and her younger sister, Susanna Mae, grow up a little with each book. Here are all four in reading order, from Ambassador International and En Route Books and Media.</p>
<ol class="jump">{''.join(f'<li><a href="#{b["slug"]}"><span>{b["n"]}</span>{b["title"]}</a></li>' for b in BOOKS)}</ol></div></section>
<section class="wrap books">{''.join(bookrow(b) for b in BOOKS)}</section>
<section class="band paper"><div class="wrap note-grid">
  <div><h2>For schools and libraries</h2><p>Planning a visit? Michael can sign copies at readings, book fairs, and signings. For larger orders of <i>Laura’s Locker</i>, En Route Books and Media takes bulk orders.</p><a class="link" href="https://enroutebooksandmedia.com/lauraslocker/" target="_blank" rel="noopener">Bulk orders from En Route</a></div>
  <div><h2>Summaries</h2><p>The descriptions on this page are drawn from each publisher’s description of the book.</p>{PH("Pre-planning. Michael to confirm which age or grade range he recommends for each book, and whether he wants a short line in his own words for each.")}</div>
</div></section>''')

P['visits.html']=('School Visits, Readings and Signings | Michael LaPenna','Invite Michael LaPenna for a reading at your school, library, or book fair, or a signing at your bookstore.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Visits</p><h1>Readings and signings</h1><p class="lede">Michael reads from the LaRosa Sisters at schools, libraries, and book fairs, and is now adding signings at bookstores.</p>
<div class="ctas"><a class="btn" href="contact.html?topic=visit">Invite Michael</a></div></div></section>
<section class="band white"><div class="wrap">{visit_cards()}</div></section>
<section class="band paper"><div class="wrap two visit-detail">
  <div class="prose"><h2>A visit can include</h2>
    <ul class="ticks"><li>A reading from one of the LaRosa Sisters books chosen for the age of the group</li><li>Questions from students and readers</li><li>Signed copies for readers who bring or buy a book</li></ul>
    {PH("Pre-planning. Michael to confirm what a visit includes, how long it runs, group sizes, and whether he offers a talk on writing or on his years teaching English.")}
  </div>
  <div class="prose"><h2>Which book for which readers</h2>
    <ul class="age">{''.join(f'<li>{cover(b,"cv xs")}<div><b>{b["title"]}</b><span>{b["details"][-1] if "Reading age" in b["details"][-1] else b["details"][0]}</span></div></li>' for b in BOOKS)}</ul>
    <p class="small">Reading ages are from the publishers’ listings where they give one.</p>
  </div>
</div></section>
<section class="band white"><div class="wrap">
  <div class="sec-h"><p class="kicker dark">Planning</p><h2>What helps Michael plan a visit</h2></div>
  <ol class="steps"><li><b>Dates</b><span>A date or a window of dates that would work.</span></li><li><b>Readers</b><span>Grade levels or ages, and about how many.</span></li><li><b>Place</b><span>Where it is, and the room or space you have in mind.</span></li><li><b>Books</b><span>Whether readers will buy copies, through you, a bookstore, or Michael.</span></li></ol>
  {PH("Pre-planning. Michael to confirm his travel area, any fee or honorarium, and whether he does virtual visits.")}
  <div class="center"><a class="btn" href="contact.html?topic=visit">Send a visit request</a></div>
</div></section>''')

P['about.html']=('About | Michael LaPenna','About Michael LaPenna, retired high school English teacher and author of the LaRosa Sisters series.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">About</p><h1>Michael LaPenna</h1></div></section>
<section class="band paper"><div class="wrap two about">
  <figure><img class="portrait" src="assets/michael-lapenna.jpg" width="573" height="720" alt="Michael LaPenna"></figure>
  <div class="prose">
    <p class="lede">Michael LaPenna grew up on the North Shore of Massachusetts. He graduated from Colby College in Waterville, Maine, and later earned a master’s degree in American literature from Salem State University.</p>
    <p>He taught secondary school English for thirty-four years and coached basketball and baseball at a public school north of Boston.</p>
    <p>Since retiring, he has been writing for young readers. His LaRosa Sisters series follows Catherine and Susanna Mae through mysteries that test their courage and their faith.</p>
    <p>Michael and his wife, Patti, live in Upstate South Carolina and spend parts of the year in the hills of western Maine and in southeast Florida. When he isn’t writing, you’ll find him visiting his three granddaughters, splitting wood, following the Boston teams, or reading.</p>
    {PH("Bio adapted from Michael’s publisher biography. Pre-planning. Michael to confirm it and add a few lines on why he writes the LaRosa Sisters.")}
  </div>
</div></section>
<section class="band white"><div class="wrap facts-row">
  <div><b>34 years</b><span>teaching secondary school English</span></div>
  <div><b>4 books</b><span>in the LaRosa Sisters series</span></div>
  <div><b>2 publishers</b><span>Ambassador International and En Route Books and Media</span></div>
</div></section>''')

P['media.html']=('Media | Michael LaPenna','Interviews with Michael LaPenna and a press kit with cover images, author photo, and short bio.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Media</p><h1>Interviews and press kit</h1></div></section>
<section class="band white"><div class="wrap two media-item">
  {VIDEO}
  <div><span class="no">The Catholic Bookworm · WCAT Radio · October 13, 2026</span><h2>Michael LaPenna on Baby Jesus Is Missing</h2>
  <p>In episode 330 of The Catholic Bookworm, host Kiki Latimer interviews Michael about <i>Baby Jesus Is Missing</i>, the first LaRosa Sisters book.</p>
  <div class="buy"><a class="btn sm" href="https://www.youtube.com/watch?v={YT}" target="_blank" rel="noopener">Watch on YouTube</a><a class="btn sm ghost" href="{SPREAKER}" target="_blank" rel="noopener">Listen to the episode</a></div></div>
</div></section>
<section class="band paper"><div class="wrap">
  <div class="sec-h"><p class="kicker dark">For schools, bookstores, and press</p><h2>Press kit</h2><p>Images and a short bio for event flyers, newsletters, and announcements.</p></div>
  <div class="kit">
    <div class="kit-bio"><h3>Short bio</h3><p>Michael LaPenna is the author of the LaRosa Sisters, Catholic mysteries for young readers. A graduate of Colby College with a master’s degree in American literature from Salem State University, he taught secondary school English for thirty-four years. He lives in Upstate South Carolina.</p></div>
    <a class="kit-img" href="assets/michael-lapenna.jpg" target="_blank" rel="noopener"><img src="assets/michael-lapenna.jpg" width="573" height="720" alt="Author photo of Michael LaPenna" loading="lazy"><span>Author photo</span></a>
    {''.join(f'<a class="kit-img" href="assets/{b["cover"]}" target="_blank" rel="noopener">{cover(b)}<span>{b["title"]}</span></a>' for b in BOOKS)}
  </div>
  {PH("Pre-planning. Michael to send any other interviews, articles, or event photos, and a higher-resolution author photo if he has one.")}
</div></section>''')

P['contact.html']=('Contact | Michael LaPenna','Invite Michael LaPenna to your school, library, book fair, or bookstore, or send a note.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Contact</p><h1>Invite Michael</h1><p class="lede">Visit requests, signings, questions about the books, or a note from a reader. Messages come straight to Michael.</p></div></section>
<section class="band paper"><div class="wrap contact">
  <form id="cform" class="form" action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="MICHAEL_WEB3FORMS_KEY">
    <input type="hidden" name="subject" value="New message from the Michael LaPenna site">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <div class="f2"><label>Name<input name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label></div>
    <label>What is this about?<select name="topic" id="topic"><option value="visit">A school, library, or book fair visit</option><option value="signing">A bookstore signing</option><option>A question about the books</option><option>A note from a reader</option><option>Something else</option></select></label>
    <div class="visit-only f2"><label>School, library, or store<input name="organization" autocomplete="organization"></label>
    <label>City and state<input name="location"></label>
    <label>Dates you have in mind<input name="dates"></label>
    <label>Grades or ages, and group size<input name="readers"></label></div>
    <label>Message<textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit">Send message</button>
    <p class="form-msg" id="fmsg" role="status"></p>
  </form>
  <aside class="c-side"><h2>Good to know</h2><p>Michael reads at schools, libraries, and book fairs, and signs books at bookstores.</p><p>For press and event flyers, the <a href="media.html">press kit</a> has cover images, an author photo, and a short bio.</p>
  {PH("Concept preview. The form goes live once it is connected to Michael’s own email.")}</aside>
</div></section>''')

for f,(t,d,b) in P.items():
    open(os.path.join(R,f),'w').write(page(f,t,d,b))
print('built',len(P))
