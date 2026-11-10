"""Michael LaPenna author site (concept). Run: python3 _build.py"""
import os
R=os.path.dirname(os.path.abspath(__file__))
import hashlib
CSSV=hashlib.sha1(open(os.path.join(R,'assets/site.css'),'rb').read()).hexdigest()[:8]
JSV=hashlib.sha1(open(os.path.join(R,'assets/site.js'),'rb').read()).hexdigest()[:8]
NAV=[('index.html','Home'),('books.html','Books'),('visits.html','Visits'),('about.html','About'),('media.html','Media'),('contact.html','Contact')]
AMZ='https://www.amazon.com/dp/'
YT='POn3cG_RTKs'
SPREAKER='https://www.spreaker.com/episode/episode-330-michael-lapenna-on-his-book-baby-jesus-is-missing-october-13-2026--75766588'

BOOKS=[
 dict(n=1,slug='baby-jesus-is-missing',pages='44 pages',age='7 to 12',formats='Hardcover, Paperback, Kindle',title='Baby Jesus Is Missing',short='A Christmas mystery',pub='Ambassador International',year='2020',
  details=['Hardcover, 44 pages','Paperback and Kindle','Illustrated by Chris Jackson','Reading age 7 to 12'],
  cover='cover-baby-jesus-is-missing.jpg',w=700,h=1144,
  sum='Early in December, Nativity figures begin disappearing across Reedy River. When a $500 reward is offered for catching the thief, Catherine and Susanna Mae decide to investigate. What begins as a Christmas mystery soon becomes a test of their judgment.',
  quote=('One mark of a good children’s book is that it delights adults as well. I found <i>Baby Jesus Is Missing</i> to be such a book. Author Michael LaPenna introduces us to sisters Catherine and Susanna Mae as they solve the local town crime of the stolen baby Jesus figurines while also introducing us to the slang of the criminal and detective world in hilarious jaunts of language. The girls soon discover that one’s vocation, even crime solving, requires faith, virtue, and sacrifice. This is a fun faith-filled teaching story, full of surprises, and part of a book series that helps us all find the Baby Jesus and keep him in our lives.','Kiki Latimer','Catholic author and host of <i>The Catholic Bookworm</i>'),
  buy=[('Hardcover',AMZ+'1620209330'),('Paperback',AMZ+'1649601468'),('Kindle',AMZ+'B08PBYHGYH'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/baby-jesus-is-missing-michael-lapenna/1138393399?ean=9781620209332'),('Publisher','https://ambassador-international.com/books/baby-jesus-is-missing/')]),
 dict(n=2,slug='the-offering',pages='61 pages',age='7 to 12',formats='Paperback, Hardcover, Kindle',title='The Offering',short='A mountain adventure',pub='Ambassador International',year='2023',
  details=['Paperback, 61 pages','Hardcover and Kindle','Reading age 7 to 12'],
  cover='cover-the-offering.jpg',w=700,h=1000,
  sum='While visiting their grandparents in the mountains, Catherine and Susanna Mae discover a rusted tin full of money. Then their border collie, Atticus, chases a bear cub into woods their grandfather has warned them to avoid. Should they obey his warning or go after their dog?',
  buy=[('Paperback',AMZ+'1649603126'),('Hardcover',AMZ+'1649605870'),('Kindle',AMZ+'B0C9KLXPFF'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/the-offering-michael-lapenna/1143777727?ean=9781649605870'),('Publisher','https://ambassador-international.com/books/the-offering/')]),
 dict(n=3,slug='angelina-grace',pages='161 pages',age='8 to 14',formats='Paperback, Kindle',title='Angelina Grace',short='An autumn mystery',pub='Ambassador International',year='2025',
  details=['Paperback, 161 pages','Kindle','Reading age 8 to 14'],
  cover='cover-angelina-grace.jpg',w=700,h=1130,
  sum='One autumn afternoon, Catherine meets Ulga, a young woman living alone in a secluded hollow outside town. As the sisters get to know her, they begin to wonder about her circumstances and what they can do to help her stay safe.',
  quote=('Michael LaPenna has given us a charming mystery story that unfolds the deeper mysteries about growing up, caring for others and learning to forgive and be reconciled. Join Susanna Mae and her sister Catherine as they solve the mystery of the strange girl in the woods and the stranger men who are searching for her. Written with clear simplicity, LaPenna has a gift for story telling that will attract and absorb the attention of young readers.','Fr. Dwight Longenecker','author of <i>Immortal Combat</i> and <i>Beheading Hydra</i> and the blog <i>Standing on My Head</i>'),
  buy=[('Paperback',AMZ+'1649606133'),('Kindle',AMZ+'B0G4DMMJ9V'),('Publisher','https://ambassador-international.com/books/angelina-grace/')]),
 dict(n=4,slug='lauras-locker',pages='191 pages',age='7 to 12',formats='Paperback, Kindle, Audible',title='Laura’s Locker',short='A story about telling the truth',pub='En Route Books and Media',year='2026',
  details=['Paperback, 191 pages','Kindle and Audible','Reading age 7 to 12'],
  cover='cover-lauras-locker.jpg',w=666,h=1000,
  sum='Susanna Mae sees a classmate framed for cheating. She knows what happened, but speaking up could cost her a friendship. During a visit to her grandparents in Gloucester, Massachusetts, she encounters mysterious woods and old legends. Back at school, the harder challenge remains.',
  quote=('Michael LaPenna invites young readers into a compelling encounter with conscience, courage, and grace. <i>Laura’s Locker</i> reveals how faith strengthens the heart to confront injustice, embrace truth, and discover the healing power of authentic friendship.','Dr. Sebastian Mahfood, OP','author of <i>The Narrative Spirituality of Dante’s Divine Comedy</i>'),
  buy=[('Paperback',AMZ+'B0HPS6LFQ8'),('Kindle',AMZ+'B0HMDQLXDR'),('Audible','https://www.audible.com/pd/Audiobook/B0HL6SZ6DQ'),('Publisher','https://enroutebooksandmedia.com/lauraslocker/')]),
]
BOOKS[3]['n']=5
PLACE=dict(n=4,slug='haddies-locket',pages='75 pages',age='7 to 12',formats='Paperback',title='Haddie’s Locket',short='A story about a family keepsake',pub='Independently published',year='2026',
  details=['Paperback, 75 pages','Reading age 7 to 12'],
  cover='cover-haddies-locket.jpg',w=700,h=1119,
  sum='When the girls’ great-grandmother Haddie comes to visit, Catherine borrows her locket while Haddie is away on a short trip, and the locket goes missing. It is the last keepsake Haddie has of her late husband. Catherine dreads telling her, until an old map leads to an adventure and a possible way to make things right.',
  buy=[('Paperback',AMZ+'B0GCJK65KQ')])
BOOKS=BOOKS[:3]+[PLACE]+BOOKS[3:]
PUB=BOOKS[:]
L=BOOKS[4]
PH=lambda t:f'<p class="ph-note">{t}</p>'
VIDEO=f'<div class="frame"><iframe src="https://www.youtube-nocookie.com/embed/{YT}" title="Michael LaPenna on The Catholic Bookworm" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>'

ICON={
 'school':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10 12 5l9 5-9 5-9-5Z"/><path d="M7 12.5V17c3 2 7 2 10 0v-4.5"/></svg>',
 'library':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h4v16H4zM10 4h4v16h-4z"/><path d="m16 5 3.5-1 3 15.5-3.5 1z"/></svg>',
 'fair':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9h18l-2-4H5L3 9Z"/><path d="M5 9v11h14V9M9 20v-6h6v6"/></svg>',
 'store':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19c4-1 6-6 8-11 1 4 3 8 8 11"/><path d="M14 4l3 3-8 8H6v-3z"/></svg>',
}
VISITS=[
 ('school','visit-schools-3.jpg','Students sitting in a circle on a classroom rug','Schools','Book readings for students, followed by time for questions and conversation.'),
 ('library','visit-libraries-5.jpg','Bookshelves and a reading table in a public library','Libraries','Readings and conversations for children and their families.'),
 ('fair','visit-book-fairs-4.jpg','A table of picture books at a school book fair','Book fairs','Meet the author, hear a passage from a book, and have a copy signed.'),
 ('store','visit-bookstores-5.jpg','A display table of new books in a Barnes and Noble store','Bookstores','In-store readings and book signings for local readers.'),
]

import json as _json
ISBN={'baby-jesus-is-missing':'9781620209332','the-offering':'9781649603128','angelina-grace':'9781649606136','lauras-locker':'9798888706558','haddies-locket':'9798279096312'}
BASE='https://liquid1188.github.io/michael-lapenna/'
def ld(fname):
    person={"@type":"Person","@id":BASE+"#michael","name":"Michael LaPenna","jobTitle":"Author","url":BASE,"image":BASE+"assets/michael-lapenna.jpg","alumniOf":[{"@type":"CollegeOrUniversity","name":"Colby College"},{"@type":"CollegeOrUniversity","name":"Salem State University"}]}
    if fname=='books.html':
        g=[person]+[{"@type":"Book","name":b['title'].replace('’',"'"),"author":{"@id":BASE+"#michael"},"isbn":ISBN[b['slug']],"datePublished":b['year'],"publisher":{"@type":"Organization","name":b['pub']},"image":BASE+"assets/"+b['cover'],"bookFormat":"https://schema.org/Paperback" if 'Hardcover' not in b['details'][0] else "https://schema.org/Hardcover"} for b in PUB]
    else: g=[person]
    return '<script type="application/ld+json">'+_json.dumps({"@context":"https://schema.org","@graph":g})+'</script>'

def page(fname,title,desc,body):
    LD=ld(fname)
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
<meta property="og:image" content="https://liquid1188.github.io/michael-lapenna/assets/og-card.jpg">
<meta name="twitter:card" content="summary_large_image">
{LD}
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css?v={CSSV}">
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
  <div class="wrap f-cols">
    <div><h3>Explore</h3><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul></div>
    <div><h3>The books</h3><ul>{''.join(f'<li><a href="books.html#{b["slug"]}"><i>{b["title"]}</i></a></li>' for b in PUB)}</ul></div>
    <div><h3>For hosts</h3><ul><li><a href="visits.html">Author visits</a></li><li><a href="contact.html?topic=signing">Bookstore signings</a></li><li><a href="media.html">Press kit</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h3>Publishers</h3><ul><li><a href="https://ambassador-international.com/book-author/michael-lapenna/" target="_blank" rel="noopener">Ambassador International</a></li><li><a href="https://enroutebooksandmedia.com/lauraslocker/" target="_blank" rel="noopener">En Route Books and Media</a></li></ul></div>
  </div>
  <div class="wrap"><p class="f-credits">Photos: USAG-Humphreys on Flickr, CC BY 2.0; oddharmonic and brewbooks, CC BY-SA 2.0; D Coetzee, CC0. Woods photo by Johannes Plenio, CC0. Classroom photo, U.S. National Archives, public domain.</p>
  <div class="f-base"><span>© 2026 Michael LaPenna</span><button type="button" class="vp-toggle">View desktop version</button><a href="https://lickitysplitweb.com" target="_blank" rel="noopener">Site by Lickity Split Web Design</a></div></div>
</footer>
<script src="assets/site.js?v={JSV}"></script>
</body>
</html>
'''

def cover(b,cls='cv',lazy=True):
    return f'<img class="{cls}" src="assets/{b["cover"]}" width="{b["w"]}" height="{b["h"]}" alt="Cover of {b["title"]}"{" loading=\"lazy\"" if lazy else ""}>'
def buys(b,cls='sm'): return '' if not b['buy'] else '<div class="buy">'+''.join(f'<a class="btn {cls}{" ghost" if i else ""}" href="{u}" target="_blank" rel="noopener">{t}</a>' for i,(t,u) in enumerate(b['buy']))+'</div>'
def visit_cards(): return '<div class="v-grid">'+''.join(f'<article class="v-card"><img class="v-ph" src="assets/photos/{ph}" alt="{alt}" loading="lazy" width="1000" height="640"><div class="v-body"><h3>{t}</h3><p>{d}</p><a class="v-go" href="contact.html?topic={"signing" if k=="store" else "visit"}">{"Ask about a signing" if k=="store" else "Request a visit"}</a></div></article>' for k,ph,alt,t,d in VISITS)+'</div>'

P={}
q=L['quote']
P['index.html']=('Michael LaPenna | Author of the LaRosa Sisters','Michael LaPenna is the author of the LaRosa Sisters, Catholic mysteries for young readers. He visits schools, libraries, book fairs, and bookstores.',f'''
<section class="hero on-dark"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="kicker">The LaRosa Sisters · Mysteries and adventures for young readers</p>
    <h1>Two sisters. One mystery after another.</h1>
    <p class="lede">Meet Catherine and Susanna Mae LaRosa. Between missing Nativity figures, a dog in danger, and a classmate falsely accused, the sisters have plenty of mysteries to untangle. Michael LaPenna’s five-book series brings together adventure, family, and Catholic faith.</p>
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

<section class="band router"><div class="wrap">
  <h2 class="sr-only">Find what you need</h2>
  <div class="r-grid">
    <a class="r-card" href="books.html"><span class="r-who">Readers and families</span><b>Meet Catherine and Susanna Mae</b><span class="r-go">Explore the books</span></a>
    <a class="r-card" href="visits.html"><span class="r-who">Teachers and librarians</span><b>Plan a reading for your students</b><span class="r-go">Arrange an author visit</span></a>
    <a class="r-card" href="contact.html?topic=signing"><span class="r-who">Booksellers</span><b>Host a signing at your store</b><span class="r-go">Ask about a signing</span></a>
  </div>
</div></section>

<section class="band paper"><div class="wrap intro">
  <div class="prose"><p class="kicker dark">About the series</p><h2>The stories behind the mysteries</h2>
    <p class="drop">Someone is stealing baby Jesus figures from Nativity scenes in Reedy River. In the mountains, Atticus the border collie chases a bear cub into forbidden woods. Elsewhere, a young woman living alone needs help, and a schoolgirl is accused of cheating. Catherine and Susanna Mae find themselves drawn into each mystery.</p>
    <p>Each adventure asks the sisters to think beyond the clues and consider the people involved. Questions of honesty, loyalty, friendship, and faith become more complicated as Catherine and Susanna Mae grow older.</p>
  </div>
  <figure class="intro-ph"><img src="assets/photos/woods-path.jpg" width="960" height="640" alt="A misty path leading into the woods" loading="lazy"></figure>
</div></section>

<section class="band quote-band"><div class="wrap q-pair">
  <blockquote class="big-q"><span class="q-on">On <i>Baby Jesus Is Missing</i></span><p>“One mark of a good children’s book is that it delights adults as well. I found <i>Baby Jesus Is Missing</i> to be such a book. … This is a fun faith-filled teaching story, full of surprises.”</p><cite><b>Kiki Latimer</b>, Catholic author and host of <i>The Catholic Bookworm</i></cite></blockquote>
  <blockquote class="big-q"><span class="q-on">On <i>Laura’s Locker</i></span><p>“{q[0]}”</p><cite><b>{q[1]}</b>, {q[2]}</cite></blockquote>
</div></section>

<section class="band on-dark"><div class="wrap">
  <div class="sec-h"><p class="kicker">Reading order</p><h2>The series so far</h2></div>
  <ol class="order">{''.join(f'<li><a href="books.html#{b["slug"]}">{cover(b)}<span class="no">Book {b["n"]}{(" · "+b["year"]) if b["year"] else ""}</span><b>{b["title"] if not b.get("ph") else "Title coming soon"}</b><span class="sm-t">{b["short"]}</span></a></li>' for b in BOOKS)}</ol>
  <div class="center"><a class="btn gold" href="books.html">Explore the series</a></div>
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
  <img class="cta-ph" src="assets/photos/classroom-hands.jpg" width="996" height="668" alt="Students raising their hands in a classroom" loading="lazy">
  <div class="cta-txt"><h2>Interested in hosting a reading or signing?</h2><p>Share a little about your venue, your readers, and the dates you have in mind.</p><a class="btn" href="contact.html?topic=visit">Invite Michael</a></div>
</div></section>''')

def bookrow(b):
    qb=''
    if b.get('quote'):
        qq=b['quote'];qb=f'<blockquote class="mini-q"><p>“{qq[0]}”</p><cite>{qq[1]}, {qq[2]}</cite></blockquote>'
    return f'''<article class="book" id="{b["slug"]}"><div class="cv-wrap">{cover(b)}</div><div>
<span class="no">Book {b["n"]}{(" · "+b["year"]) if b["year"] else ""}</span><h2>{b["title"] if not b.get("ph") else "Title coming soon"}</h2><p class="meta">{b["pub"]}</p>
<p>{b["sum"]}</p>{qb}
<ul class="facts">{''.join(f'<li>{d}</li>' for d in b["details"])}</ul>{buys(b)}</div></article>'''
P['books.html']=('Books | Michael LaPenna','The LaRosa Sisters books by Michael LaPenna in reading order, with links to buy each one.',f'''
<section class="page-h on-dark"><div class="wrap"><p class="kicker">Books</p><h1>The LaRosa Sisters</h1><p class="lede">From a missing Nativity figure to a difficult choice at school, each LaRosa Sisters book brings Catherine and Susanna Mae a new adventure. Explore the stories in reading order.</p>
<ol class="jump">{''.join(f'<li><a href="#{b["slug"]}"><span>{b["n"]}</span>{b["title"]}</a></li>' for b in BOOKS)}</ol></div></section>
<section class="band white glance-band"><div class="wrap">
  <h2 class="glance-h">At a glance</h2>
  <div class="tbl-wrap"><table class="glance"><thead><tr><th>Book</th><th>Published</th><th>Length</th><th>Reading age</th><th>Formats</th></tr></thead><tbody>
  {''.join(f'<tr><td><a href="#{b["slug"]}"><i>{b["title"]}</i></a><span>Book {b["n"]}</span></td><td data-l="Published">{(b["year"]+", "+b["pub"]) if b["year"] else "Coming soon"}</td><td data-l="Length">{b["pages"]}</td><td data-l="Reading age">{b["age"]}</td><td data-l="Formats">{b["formats"]}</td></tr>' for b in BOOKS)}
  </tbody></table></div>
</div></section>
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
    {''.join(f'<a class="kit-img" href="assets/{b["cover"]}" target="_blank" rel="noopener">{cover(b)}<span><i>{b["title"]}</i></span></a>' for b in PUB)}
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
