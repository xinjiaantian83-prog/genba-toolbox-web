(() => {
  const n=id=>{const value=Number(document.getElementById(id)?.value);return Number.isFinite(value)?value:null};
  const text=(x,y,value,anchor='middle',cls='value')=>`<text x="${x}" y="${y}" text-anchor="${anchor}" class="${cls}">${value}</text>`;
  const wrap=(body,viewBox)=>`<svg viewBox="${viewBox}" role="img" aria-label="入力寸法の模式図">${body}</svg>`;
  function drawSamples(){
    const tool=document.body.dataset.tool,box=document.getElementById('diagram');if(!box)return;
    if(tool==='slope'){
      const mode=document.querySelector('[data-mode].active')?.dataset.mode||'height';
      if(mode==='height'&&(!(n('horizontal')>0)||!(n('vertical')>=0)))box.innerHTML=wrap(`<line class="shape sample" x1="30" y1="160" x2="220" y2="160"/><line class="shape sample" x1="220" y1="160" x2="220" y2="95"/><line class="shape sample" x1="30" y1="160" x2="220" y2="95"/><path class="shape sample" d="M214 160V154H220"/>${text(125,184,'例：横 1,000')}${text(230,130,'例：縦 300','start')}${text(120,116,'例：斜距離','middle','alt')}`,'0 0 320 200');
    }
    if(tool==='gravity'&&!(n('height')>0))box.innerHTML=wrap(`<line class="measure" x1="8" y1="190" x2="272" y2="190"/><polygon class="shape sample" points="48,190 174,190 104,28 48,28"/><line class="shape sample" x1="34" y1="28" x2="34" y2="190"/>${text(76,20,'例：T=300')}${text(110,211,'例：B=660')}${text(24,112,'例：H=1,200','end')}${text(58,105,'前面','start')}${text(135,105,'背面','start')}`,'0 0 280 220');
    if(tool==='area'){
      const length=n('length'),width=n('width'),has=length>0&&width>0,a=has?length:5000,b=has?width:4000,scale=Math.min(300/b,190/a),rw=Math.max(52,b*scale),rh=Math.max(52,a*scale),x=300-rw/2,y=145-rh/2,p=has?'':'例：';
      box.innerHTML=wrap(`<rect class="shape${has?'':' sample'}" x="${x}" y="${y}" width="${rw}" height="${rh}"/><line class="measure" x1="${x}" y1="${y+rh+22}" x2="${x+rw}" y2="${y+rh+22}"/><line class="measure" x1="${x-22}" y1="${y}" x2="${x-22}" y2="${y+rh}"/>${text(300,y+rh+45,p+'横 '+Math.round(b)+'mm')}${text(x-30,150,p+'縦 '+Math.round(a)+'mm','end')}${text(300,150,has?(a*b/1e6).toFixed(2)+'㎡':'平面積')}`,'0 0 600 330');
    }
    if(tool==='rebar'){
      const mode=document.querySelector('[data-mode].active')?.dataset.mode||'wall';
      if(mode==='lwall'&&(!(n('lHeight')>0)||!(n('lBase')>0))){const panel=document.querySelector('.rebar-diagram');if(panel)panel.hidden=false;box.innerHTML=wrap(`<path d="M90 40V160H180" fill="none" stroke="#6bb8ff" stroke-width="4" stroke-linecap="round"/><circle cx="90" cy="160" r="6" fill="#ffd266" stroke="#ffb968"/>${text(80,104,'例：縦 1,460','end')}${text(135,184,'例：横 560')}${text(102,150,'曲げロス 50','start','alt')}${text(310,22,'例：合計 2,070mm','end','alt')}`,'0 0 320 220');}
    }
  }
  document.addEventListener('DOMContentLoaded',()=>{drawSamples();document.querySelectorAll('input,select').forEach(el=>el.addEventListener('input',drawSamples));document.querySelectorAll('[data-mode]').forEach(el=>el.addEventListener('click',()=>requestAnimationFrame(drawSamples)));});
})();
