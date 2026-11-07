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
  sum='Early in December, Nativity figures begin disappearing across Reedy River. When a $500 reward is offered for catching the thief, Catherine and Susanna Mae decide to investigate. What begins as a Christmas mystery soon becomes a test of their judgment.',
  buy=[('Amazon',AMZ+'1620209330'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/baby-jesus-is-missing-michael-lapenna/1138393399?ean=9781620209332'),('Publisher','https://ambassador-international.com/books/baby-jesus-is-missing/')]),
 dict(n=2,slug='the-offering',title='The Offering',short='A mountain adventure',pub='Ambassador International',year='2023',
  details=['Paperback, 62 pages','Reading age 4 to 8'],
  cover='cover-the-offering.jpg',w=700,h=1000,
  sum='While visiting their grandparents in the mountains, Catherine and Susanna Mae discover a rusted tin full of money. Then their border collie, Atticus, chases a bear cub into woods their grandfather has warned them to avoid. Should they obey his warning or go after their dog?',
  buy=[('Amazon',AMZ+'1649603126'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/the-offering-michael-lapenna/1143777727?ean=9781649605870'),('Publisher','https://ambassador-international.com/books/the-offering/')]),
 dict(n=3,slug='angelina-grace',title='Angelina Grace',short='An autumn mystery',pub='Ambassador International',year='2025',
  details=['Paperback, 164 pages','Reading age 8 to 12'],
  cover='cover-angelina-grace.jpg',w=700,h=1130,
  sum='One autumn afternoon, Catherine meets Ulga, a young woman living alone in a secluded hollow outside town. As the sisters get to know her, they begin to wonder about her circumstances and what they can do to help her stay safe.',
  buy=[('Amazon',AMZ+'1649606133'),('Publisher','https://ambassador-international.com/books/angelina-grace/')]),
 dict(n=4,slug='lauras-locker',title='Laura’s Locker',short='A story about telling the truth',pub='En Route Books and Media',year='2026',
  details=['Paperback, 191 pages','Kindle and Audible'],
  cover='cover-lauras-locker.jpg',w=666,h=1000,
  sum='Susanna Mae sees a classmate framed for cheating. She knows what happened, but speaking up could cost her a friendship. During a visit to her grandparents in Gloucester, Massachusetts, she encounters mysterious woods and old legends. Back at school, the harder challenge remains.',
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
 ('school','Schools','Book readings for students, followed by time for questions and conversation.'),
 ('library','Libraries','Readings and conversations for children and their families.'),
 ('fair','Book fairs','Meet the author, hear a passage from a book, and have a copy signed.'),
 ('store','Bookstores','In-store readings and book signings for local readers.'),
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
  <a class="brand" href="index.html"><b>Michael LaPenna</b><span>Author</span></a>
  <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" aria-label="Main"><ul>{nav}</ul><a class="btn sm nav-cta" href="contact.html?topic=visit">Invite Michael</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer>
  <div class="f-strip"><div class="wrap">
    <div><b class="f-name">Michael LaPenna</b><p>Author of the LaRosa Sisters mystery series for young readers.</p></div>
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
    <p class="kicker">The LaRosa Sisters · Mysteries and adventures for young readers</p>
    <h1>Two sisters. One mystery after another.</h1>
    <p class="lede">Meet Catherine and Susanna Mae LaRosa. Between missing Nativity figures, a dog in danger, and a classmate falsely accused, the sisters have plenty of mysteries to untangle. Michael LaPenna’s four-book series brings together adventure, family, and Catholic faith.</p>
    <div class="ctas"><a class="btn" href="books.html">Explore the books</a><a class="btn ghost-light" href="visits.html">Arrange an author visit</a></div>
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
    <h2>The stories behind the mysteries</h2>
    <p class="drop">Someone is stealing baby Jesus figures from Nativity scenes in Reedy River. In the mountains, Atticus the border collie chases a bear cub into forbidden woods. Elsewhere, a young woman living alone needs help, and a schoolgirl is accused of cheating. Catherine and Susanna Mae find themselves drawn into each mystery.</p>
    <p>Each adventure asks the sisters to think beyond the clues and consider the people involved. Questions of honesty, loyalty, friendship, and faith become more complicated as Catherine and Susanna Mae grow older.</p>
    <a class="link" href="books.html">Explore all four stories</a>
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
  <div class="sec-h row"><div><p class="kicker dark">Readings and signings</p><h2>Bring a story to life with an author visit</h2></div><a class="link" href="visits.html">About author visits</a></div>
  {visit_cards()}
  <div class="center"><a class="btn" href="contact.html?topic=visit">Plan a visit</a></div>
</div></section>

<section class="band on-dark media-band"><div class="wrap two">
  {VIDEO}
  <div><p class="kicker">On the air</p><h2>Michael on The Catholic Bookworm</h2>
  <p>In an October 2026 interview on WCAT Radio’s <i>The Catholic Bookworm</i>, host Kiki Latimer speaks with Michael about <i>Baby Jesus Is Missing</i>, the book that introduced the LaRosa sisters.</p>
  <div class="buy"><a class="btn sm" href="https://www.youtube.com/watch?v={YT}" target="_blank" rel="noopener">Watch on YouTube</a><a class="btn sm ghost-light" href="{SPREAKER}" target="_blank" rel="noopener">Listen to the episode</a></div></div>
</div></section>

<section class="band paper"><div class="wrap two author">
  <img class="portrait" src="assets/michael-lapenna.jpg" width="573" height="720" alt="Michael LaPenna" loading="lazy">
  <div class="prose"><p class="kicker dark">About the author</p><h2>From the classroom to the writing desk</h2>
  <p>Before writing the LaRosa Sisters books, Michael spent 34 years teaching secondary school English north of Boston and coaching basketball and baseball. Today he writes mysteries for young readers.</p>
  <a class="btn ghost" href="about.html">Read the full biography</a></div>
</div></section>

<section class="band on-dark cta-band"><div class="wrap cta-in">
  <div><h2>Interested in hosting a reading or signing?</h2><p>Share a little about your venue, your readers, and the dates you have in mind.</p></div>
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
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Books</p><h1>The LaRosa Sisters</h1><p class="lede">From a missing Nativity figure to a difficult choice at school, each LaRosa Sisters book brings Catherine and Susanna Mae a new adventure. Explore the four stories in reading order.</p>
<ol class="jump">{''.join(f'<li><a href="#{b["slug"]}"><span>{b["n"]}</span>{b["title"]}</a></li>' for b in BOOKS)}</ol></div></section>
<section class="wrap books">{''.join(bookrow(b) for b in BOOKS)}</section>
<section class="band paper"><div class="wrap note-grid">
  <div><h2>For schools and libraries</h2><p>Organizing a reading or school event? Ask about signed copies when planning. For larger orders of <i>Laura’s Locker</i>, En Route Books and Media offers bulk purchasing.</p><a class="link" href="https://enroutebooksandmedia.com/lauraslocker/" target="_blank" rel="noopener">Bulk orders from En Route</a></div>
  <div><h2>Where to begin</h2><p>The first books are shorter, with longer and more complex stories as the series progresses. Readers can begin with <i>Baby Jesus Is Missing</i> and follow Catherine and Susanna Mae as they grow.</p></div>
</div></section>''')

P['visits.html']=('School Visits, Readings and Signings | Michael LaPenna','Invite Michael LaPenna for a reading at your school, library, or book fair, or a signing at your bookstore.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Visits</p><h1>Author visits and book signings</h1><p class="lede">After 34 years in the classroom, Michael enjoys sharing stories with young readers. His author events include readings at schools, libraries, and book fairs, as well as bookstore signings.</p>
<div class="ctas"><a class="btn" href="contact.html?topic=visit">Invite Michael</a></div></div></section>
<section class="band white"><div class="wrap">{visit_cards()}</div></section>
<section class="band paper"><div class="wrap two visit-detail">
  <div class="prose"><h2>What to expect</h2>
    <ul class="ticks"><li>A reading from a LaRosa Sisters book suited to the audience</li><li>Time for readers to ask about the stories and characters</li><li>Book signing when copies are available</li></ul>
  </div>
  <div class="prose"><h2>Explore the books</h2>
    <ul class="age">{''.join(f'<li>{cover(b,"cv xs")}<div><b><i>{b["title"]}</i></b><span>{b["short"]}</span></div></li>' for b in BOOKS)}</ul>
    <p class="small">The books range from a short illustrated Christmas story to longer mysteries for growing readers.</p>
  </div>
</div></section>
<section class="band white"><div class="wrap">
  <div class="sec-h"><p class="kicker dark">Planning</p><h2>Planning an event</h2></div>
  <ol class="steps"><li><b>Dates</b><span>Your preferred date or a few possible options.</span></li><li><b>Audience</b><span>Age or grade range and approximate group size.</span></li><li><b>Location</b><span>The name and location of your school, library, or bookstore.</span></li><li><b>Books</b><span>Whether copies will be available for sale or signing.</span></li></ol>
  <div class="center"><a class="btn" href="contact.html?topic=visit">Send a visit request</a></div>
</div></section>''')

P['about.html']=('About | Michael LaPenna','About Michael LaPenna, retired high school English teacher and author of the LaRosa Sisters series.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">About</p><h1>Michael LaPenna</h1></div></section>
<section class="band paper"><div class="wrap two about">
  <figure><img class="portrait" src="assets/michael-lapenna.jpg" width="573" height="720" alt="Michael LaPenna"></figure>
  <div class="prose">
    <p class="lede">Michael LaPenna grew up on the North Shore of Massachusetts and attended Colby College in Waterville, Maine. He later earned a master’s degree in American literature from Salem State University.</p>
    <p>For 34 years, Michael taught secondary school English at a public school north of Boston, where he also coached basketball and baseball.</p>
    <p>Since retiring, Michael has turned his attention to stories for young readers. His LaRosa Sisters series follows Catherine and Susanna Mae as they solve mysteries and wrestle with questions about honesty, friendship, and faith.</p>
    <p>Michael and his wife, Patti, live in upstate South Carolina and spend part of each year in western Maine and southeastern Florida. Away from his writing desk, he enjoys visiting his three granddaughters, splitting wood, reading, and keeping up with Boston sports.</p>
  </div>
</div></section>''')

P['media.html']=('Media | Michael LaPenna','Interviews with Michael LaPenna and a press kit with cover images, author photo, and short bio.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Media</p><h1>Interviews and media resources</h1></div></section>
<section class="band white"><div class="wrap two media-item">
  {VIDEO}
  <div><span class="no">The Catholic Bookworm · WCAT Radio · October 13, 2026</span><h2>Talking about <i>Baby Jesus Is Missing</i></h2>
  <p>In this October 2026 episode of <i>The Catholic Bookworm</i>, host Kiki Latimer talks with Michael about the Christmas mystery that introduced Catherine and Susanna Mae LaRosa.</p>
  <div class="buy"><a class="btn sm" href="https://www.youtube.com/watch?v={YT}" target="_blank" rel="noopener">Watch on YouTube</a><a class="btn sm ghost" href="{SPREAKER}" target="_blank" rel="noopener">Listen to the episode</a></div></div>
</div></section>
<section class="band paper"><div class="wrap">
  <div class="sec-h"><p class="kicker dark">For schools, bookstores, and press</p><h2>Press kit</h2><p>Download an author photograph, book covers, and a short biography for event announcements, newsletters, and media coverage.</p></div>
  <div class="kit">
    <a class="kit-photo" href="assets/michael-lapenna.jpg" target="_blank" rel="noopener"><img src="assets/michael-lapenna.jpg" width="573" height="720" alt="Author photo of Michael LaPenna" loading="lazy"><span>Author photo</span></a>
    <div class="kit-bio"><h3>Short bio</h3><p>Michael LaPenna is the author of the LaRosa Sisters mystery series for young readers. He graduated from Colby College and earned a master’s degree in American literature from Salem State University. After 34 years teaching secondary school English and coaching basketball and baseball north of Boston, he now lives in upstate South Carolina.</p></div>
  </div>
  <h3 class="kit-h">Book covers</h3>
  <div class="kit-covers">
    {''.join(f'<a class="kit-img" href="assets/{b["cover"]}" target="_blank" rel="noopener">{cover(b)}<span><i>{b["title"]}</i></span></a>' for b in BOOKS)}
  </div>
</div></section>''')

P['contact.html']=('Contact | Michael LaPenna','Invite Michael LaPenna to your school, library, book fair, or bookstore, or send a note.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Contact</p><h1>Get in touch</h1><p class="lede">Have a question about the books or an idea for a reading, signing, or interview? This page is for inquiries about Michael and the LaRosa Sisters series.</p></div></section>
<section class="band paper"><div class="wrap contact">
  <form id="cform" class="form" action="https://api.web3forms.com/submit" method="POST">
    <p class="form-off" role="note">The contact form is not active yet, so messages cannot currently be submitted.</p>
    <input type="hidden" name="access_key" value="MICHAEL_WEB3FORMS_KEY">
    <input type="hidden" name="subject" value="New message from the Michael LaPenna site">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <div class="f2"><label>Name<input name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label></div>
    <label>Reason for your message<select name="topic" id="topic"><option value="visit">A school, library, or book fair visit</option><option value="signing">A bookstore signing</option><option>A question about the books</option><option>A note from a reader</option><option>Something else</option></select></label>
    <div class="visit-only f2"><label>School, library, or store<input name="organization" autocomplete="organization"></label>
    <label>City and state<input name="location"></label>
    <label>Preferred dates<input name="dates"></label>
    <label>Ages or grades and approximate group size<input name="readers"></label></div>
    <label>Message<textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit">Send message</button>
    <p class="form-msg" id="fmsg" role="status"></p>
  </form>
  <aside class="c-side"><h2>Planning an event?</h2><p>Include your school, library, or bookstore name, the location, possible dates, and the ages or grades of your readers.</p><p>For interviews or event materials, visit the <a href="media.html">media page</a> for an author photograph, book covers, and a short biography.</p></aside>
</div></section>''')

for f,(t,d,b) in P.items():
    open(os.path.join(R,f),'w').write(page(f,t,d,b))
print('built',len(P))
