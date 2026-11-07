"""Michael LaPenna author site (concept). Run: python3 _build.py"""
import os
R=os.path.dirname(os.path.abspath(__file__))
NAV=[('index.html','Home'),('books.html','Books'),('about.html','About'),('media.html','Media'),('speaking.html','Speaking'),('contact.html','Contact')]

AMZ='https://www.amazon.com/dp/'
BOOKS=[
 dict(n='1',slug='baby-jesus-is-missing',title='Baby Jesus Is Missing',pub='Ambassador International',year='2020',fmt='Hardcover, 44 pages',
  cover='cover-baby-jesus-is-missing.jpg',w=350,h=557,
  sum='In the small town of Reedy River, baby Jesus figurines are vanishing from Nativity scenes all over town in early December. When Catherine and her younger sister, Susanna Mae, hear about a $500 reward, they set out to catch the thief, and find the case asks more of them than they expected.',
  buy=[('Amazon',AMZ+'1620209330'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/baby-jesus-is-missing-michael-lapenna/1138393399?ean=9781620209332'),('Publisher','https://ambassador-international.com/books/baby-jesus-is-missing/')]),
 dict(n='2',slug='the-offering',title='The Offering',pub='Ambassador International',year='2023',fmt='Paperback and hardcover',
  cover='cover-the-offering.jpg',w=700,h=1000,
  sum='On a September visit to their grandparents’ house in the mountains, the sisters turn up a rusted tin of money. Then their border collie, Atticus, takes off after a bear cub into the woods their grandfather told them to stay out of, and the girls have to decide what to do.',
  buy=[('Amazon',AMZ+'1649603126'),('Barnes &amp; Noble','https://www.barnesandnoble.com/w/the-offering-michael-lapenna/1143777727?ean=9781649605870'),('Publisher','https://ambassador-international.com/books/the-offering/')]),
 dict(n='3',slug='angelina-grace',title='Angelina Grace',pub='Ambassador International',year='2025',fmt='Paperback, 164 pages',
  cover='cover-angelina-grace.jpg',w=700,h=1130,
  sum='One autumn afternoon Catherine comes upon a young woman living alone in a secluded hollow outside town. As the sisters get to know their new friend, Ulga, they are drawn into the questions surrounding her, and into a decision about her safety.',
  buy=[('Amazon',AMZ+'1649606133'),('Publisher','https://ambassador-international.com/books/angelina-grace/')]),
 dict(n='4',slug='book-four',title=None),
 dict(n='5',slug='lauras-locker',title='Laura’s Locker',pub='En Route Books and Media',year='2026',fmt='Paperback, Kindle, and Audible',
  cover='cover-lauras-locker.jpg',w=666,h=1000,
  sum='Susanna Mae watches a classmate get framed for cheating and has to find the courage to tell the truth. Along the way, a visit to her grandparents in Gloucester, Massachusetts, brings mysterious woods and old legends.',
  buy=[('Paperback',AMZ+'B0HPS6LFQ8'),('Kindle',AMZ+'B0HMDQLXDR'),('Audible','https://www.audible.com/pd/Audiobook/B0HL6SZ6DQ'),('Publisher','https://enroutebooksandmedia.com/lauraslocker/')]),
]
PH=lambda t:f'<span class="ph-note">{t}</span>'

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
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><b>Michael LaPenna</b><span>The LaRosa Sisters</span></a>
  <button class="menu" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
  <div class="f-top">
    <div><b class="f-name">Michael LaPenna</b><p>Author of the LaRosa Sisters mysteries for young readers.</p></div>
    <ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul>
  </div>
  <div class="f-base"><span>© 2026 Michael LaPenna</span><button type="button" class="vp-toggle">View desktop version</button><a href="https://lickitysplitweb.com" target="_blank" rel="noopener">Site by Lickity Split Web Design</a></div>
</div></footer>
<script src="assets/site.js"></script>
</body>
</html>
'''

def cover(b,cls='cv',lazy=True):
    return f'<img class="{cls}" src="assets/{b["cover"]}" width="{b["w"]}" height="{b["h"]}" alt="Cover of {b["title"]}"{" loading=\"lazy\"" if lazy else ""}>'
def buys(b): return '<div class="buy">'+''.join(f'<a class="btn sm" href="{u}" target="_blank" rel="noopener">{t}</a>' for t,u in b['buy'])+'</div>'

P={}
L=BOOKS[4]
P['index.html']=('Michael LaPenna | Author of the LaRosa Sisters','Michael LaPenna is the author of the LaRosa Sisters series, Catholic mysteries for young readers featuring sisters Catherine and Susanna Mae.',f'''
<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <p class="kicker">Catholic mysteries for young readers</p>
    <h1>Two sisters, a small town, and the courage to do what’s right.</h1>
    <p class="lede">Michael LaPenna writes the LaRosa Sisters series, mysteries for young readers in which Catherine and Susanna Mae LaRosa solve puzzles and learn about faith, friendship, and telling the truth.</p>
    <div class="ctas"><a class="btn" href="books.html">See the series</a><a class="btn ghost" href="about.html">Meet the author</a></div>
  </div>
  <div class="hero-book">
    <span class="badge">New · October 2026</span>
    <a href="books.html#lauras-locker">{cover(L,'cv big',False)}</a>
  </div>
</div></section>

<section class="sec new"><div class="wrap two">
  <div><p class="kicker">The newest LaRosa Sisters book</p><h2>Laura’s Locker</h2>
  <p class="lede">{L['sum']}</p>
  <p class="meta">En Route Books and Media · {L['fmt']}</p>{buys(L)}</div>
  <div class="vid"><div class="frame"><iframe src="https://www.youtube-nocookie.com/embed/POn3cG_RTKs" title="WCAT TV presents Michael LaPenna" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div><p class="cap">WCAT TV presents Michael LaPenna. Also featured on En Route Books and Media’s page for <i>Laura’s Locker</i>.</p></div>
</div></section>

<section class="sec shelf-sec"><div class="wrap">
  <div class="sec-h"><p class="kicker">The series so far</p><h2>The LaRosa Sisters</h2><p>All five books in reading order, from two publishers, gathered in one place.</p></div>
  <ol class="shelf">{''.join(f'<li><a href="books.html#{b["slug"]}">{cover(b) if b["title"] else '<span class="cv blank">Book 4</span>'}<span class="no">Book {b["n"]}</span><b>{b["title"] or "Title to confirm"}</b></a></li>' for b in BOOKS)}</ol>
  <p class="center"><a class="link" href="books.html">Read about every book</a></p>
</div></section>

<section class="sec author"><div class="wrap two">
  <img class="portrait" src="assets/michael-lapenna.jpg" width="573" height="720" alt="Michael LaPenna" loading="lazy">
  <div><p class="kicker">About the author</p><h2>Thirty-four years in the classroom</h2>
  <p class="lede">Michael LaPenna grew up on the North Shore of Massachusetts and taught secondary school English for thirty-four years. Now he writes for children.</p>
  <a class="link" href="about.html">More about Michael</a></div>
</div></section>

<section class="sec band"><div class="wrap band-in">
  <div><h2>Invite Michael to your school or parish</h2><p>Michael is available to speak with students, readers, and parish groups about the LaRosa Sisters and about writing.</p></div>
  <a class="btn light" href="speaking.html">Speaking</a>
</div></section>''')

def bookrow(b):
    if not b['title']:
        return f'''<article class="book" id="{b["slug"]}"><div class="cv-wrap"><span class="cv blank">Book 4</span></div><div><span class="no">Book 4</span><h2>Title to confirm</h2>{PH("Placeholder. Publisher listings show four LaRosa Sisters titles. If there is a fourth book before Laura’s Locker, Michael can confirm the title, publisher, and links.")}</div></article>'''
    return f'''<article class="book" id="{b["slug"]}"><div class="cv-wrap">{cover(b)}</div><div><span class="no">Book {b["n"]} · {b["year"]}</span><h2>{b["title"]}</h2><p class="meta">{b["pub"]} · {b["fmt"]}</p><p>{b["sum"]}</p><p class="src">Summary drawn from the publisher’s description.</p>{buys(b)}</div></article>'''
P['books.html']=('Books | Michael LaPenna','Every LaRosa Sisters book by Michael LaPenna in reading order, with links to buy each one.',f'''
<section class="page-h"><div class="wrap"><p class="kicker">Books</p><h1>The LaRosa Sisters series</h1><p class="lede">Catherine and her younger sister, Susanna Mae, grow up a little with each book. Here is the whole series in reading order, across both publishers.</p></div></section>
<section class="wrap books">{''.join(bookrow(b) for b in BOOKS)}</section>
<section class="sec"><div class="wrap note-box"><h2>Coming next</h2><p>Michael is at work on the sixth LaRosa Sisters book.</p>{PH("Placeholder. Add the title and timing when Michael is ready to share them.")}</div></section>''')

P['about.html']=('About | Michael LaPenna','About Michael LaPenna, former high school English teacher and author of the LaRosa Sisters series.',f'''
<section class="page-h"><div class="wrap"><p class="kicker">About</p><h1>Michael LaPenna</h1></div></section>
<section class="wrap two about">
  <figure><img class="portrait" src="assets/michael-lapenna.jpg" width="573" height="720" alt="Michael LaPenna"><figcaption>Photo from Michael’s publisher materials.</figcaption></figure>
  <div class="prose">
    <p class="lede">Michael LaPenna grew up on the North Shore of Massachusetts. He graduated from Colby College in Waterville, Maine, and later earned a master’s degree in American literature from Salem State University.</p>
    <p>He taught secondary school English for thirty-four years and coached basketball and baseball at a public school north of Boston.</p>
    <p>Since retiring, he has been writing for young readers. His LaRosa Sisters series follows Catherine and Susanna Mae through mysteries that test their courage and their faith.</p>
    <p>Michael and his wife, Patti, live in Upstate South Carolina and spend parts of the year in the hills of western Maine and in southeast Florida. When he isn’t writing, you’ll find him with his three granddaughters, splitting wood, following the Boston teams, or reading.</p>
    {PH("Bio adapted from Michael’s publisher biography. Michael to confirm, update, or add a personal note on why he writes these books.")}
  </div>
</section>''')

P['media.html']=('Media | Michael LaPenna','Interviews and video featuring Michael LaPenna and the LaRosa Sisters books.',f'''
<section class="page-h"><div class="wrap"><p class="kicker">Media</p><h1>Interviews and video</h1></div></section>
<section class="wrap media">
  <article class="m-item"><div class="frame"><iframe src="https://www.youtube-nocookie.com/embed/POn3cG_RTKs" title="WCAT TV presents Michael LaPenna" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
  <div><span class="no">Interview · WCAT TV</span><h2>WCAT TV presents Michael LaPenna</h2><p>A WCAT TV interview with Michael, also featured on En Route Books and Media’s page for <i>Laura’s Locker</i>.</p><a class="link" href="https://enroutebooksandmedia.com/lauraslocker/" target="_blank" rel="noopener">See the publisher page</a>
  {PH("Michael to confirm the interview’s title and date, and whether it is the Catholic Bookworm conversation with Kiki Latimer about Baby Jesus Is Missing or a separate interview.")}</div></article>
  <article class="m-item"><div class="m-card"><b>The Catholic Bookworm</b><span>WCAT Radio · with Kiki Latimer</span></div>
  <div><span class="no">Interview</span><h2>Baby Jesus Is Missing on The Catholic Bookworm</h2><p>Michael spoke with host Kiki Latimer about <i>Baby Jesus Is Missing</i>.</p><a class="link" href="https://wcatradio.com/thecatholicbookworm/" target="_blank" rel="noopener">The Catholic Bookworm on WCAT</a>
  {PH("Add the direct episode link once confirmed. If this is the same conversation as the video above, this card can be removed.")}</div></article>
  <div class="note-box"><h2>For press</h2><p>Cover images and an author photo are available on request through the contact page.</p></div>
</section>''')

P['speaking.html']=('Speaking | Michael LaPenna','Invite author Michael LaPenna to speak at your school, library, parish, or reading group.',f'''
<section class="page-h"><div class="wrap"><p class="kicker">Speaking</p><h1>Invite Michael to speak</h1><p class="lede">Michael is available to visit schools, libraries, parishes, and reading groups, in person or by video.</p></div></section>
<section class="wrap two speak">
  <div class="prose">
    <h2>Possible topics</h2>
    <ul class="ticks"><li>The LaRosa Sisters books and the questions they raise for young readers</li><li>How a story gets written, from idea to finished book</li><li>Writing advice for students, from a longtime English teacher</li></ul>
    {PH("Topics are suggestions. Michael to confirm which talks he offers, audiences, and whether he travels.")}
  </div>
  <div class="note-box"><h2>Request a visit</h2><p>Tell Michael about your group, the date you have in mind, and the age of your readers.</p><a class="btn" href="contact.html?topic=speaking">Send a request</a></div>
</section>''')

P['contact.html']=('Contact | Michael LaPenna','Get in touch with author Michael LaPenna.',f'''
<section class="page-h"><div class="wrap"><p class="kicker">Contact</p><h1>Get in touch</h1><p class="lede">Questions about the books, speaking requests, or a note from a reader. Messages come straight to Michael.</p></div></section>
<section class="wrap contact">
  <form id="cform" class="form" action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="MICHAEL_WEB3FORMS_KEY">
    <input type="hidden" name="subject" value="New message from michaellapenna site">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Email<input type="email" name="email" required autocomplete="email"></label>
    <label>What is this about?<select name="topic" id="topic"><option>A question about the books</option><option value="speaking">A speaking request</option><option>A note from a reader</option><option>Something else</option></select></label>
    <label>Message<textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit">Send message</button>
    <p class="form-msg" id="fmsg" role="status"></p>
  </form>
  {PH("Concept preview. The form goes live once it is connected to Michael’s own email.")}
</section>''')

for f,(t,d,b) in P.items():
    open(os.path.join(R,f),'w').write(page(f,t,d,b))
print('built',len(P))
