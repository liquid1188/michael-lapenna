(function(){
var m=document.querySelector('.menu'),n=document.getElementById('nav');
if(m)m.addEventListener('click',function(){var o=n.classList.toggle('open');m.setAttribute('aria-expanded',o);m.textContent=o?'Close':'Menu'});
if(Math.min(screen.width,screen.height)<760)document.documentElement.classList.add('small');
var d=false;try{d=localStorage.getItem('ml-desktop')==='1'}catch(e){}
document.querySelectorAll('.vp-toggle').forEach(function(b){b.textContent=d?'View mobile version':'View desktop version';b.addEventListener('click',function(){try{d?localStorage.removeItem('ml-desktop'):localStorage.setItem('ml-desktop','1')}catch(e){}location.reload()})});
var t=document.getElementById('topic');if(t){var mm=location.search.match(/topic=(visit|signing)/);if(mm)t.value=mm[1];var vo=document.querySelector('.visit-only');var sync=function(){if(vo)vo.style.display=(t.value==='visit'||t.value==='signing')?'':'none'};t.addEventListener('change',sync);sync()}
var f=document.getElementById('cform');
if(f)f.addEventListener('submit',function(e){var k=f.querySelector('[name=access_key]').value;if(k.indexOf('_KEY')>-1){e.preventDefault();document.getElementById('fmsg').textContent='The contact form is not active yet, so messages cannot currently be submitted.'}});
})();
