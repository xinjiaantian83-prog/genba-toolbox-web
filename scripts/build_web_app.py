from pathlib import Path
import html
import json
import shutil

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web'
# 独自ドメイン取得後は、この1か所だけ正規URLへ変更する。
SITE_ORIGIN='https://genba-toolbox.com'
# GA4データストリーム作成後、Measurement IDをこの1か所へ設定する。
GA4_MEASUREMENT_ID='G-POCVQ4SNYR'
APP_STORE_URL='https://apps.apple.com/jp/app/%E7%8F%BE%E5%A0%B4%E9%9B%BB%E5%8D%93/id6776547872'
GOOGLE_PLAY_URL='https://play.google.com/store/apps/details?id=com.genbatoolbox.genbacalcnew'
CWEB_URL='https://construction-web-terra.com/'
BLOG_URL='https://jiriki-keiei.com/'
TOOLS=[
 ('slope','勾配・カーポート','横・縦寸法から勾配を、柱間寸法と角度から柱高低差を計算'),
 ('ordinary','普通','四則演算と割合をすぐに確認できる普通電卓'),
 ('density','比重','材料の体積と比重から重量を概算'),
 ('memo','メモ','寸法・材料・連絡事項を端末内へ自動保存'),
 ('radius','R / 円','弦長と矢高からRを、直径から円周と面積を計算'),
 ('area','平面拾い','縦横寸法から平方メートルと坪を同時表示'),
 ('gravity','重力','重力式擁壁の底幅・断面積・コンクリート量を計算'),
 ('rebar','鉄筋','直壁の寸法・かぶり・ピッチから本数と総延長を拾う'),
 ('block','ブロック','延長と段数からブロック枚数・配筋本数を拾う'),
]
SEO={
 'home':{
  'title':'現場電卓Web｜現場で使える無料計算ツール',
  'h1':'現場の計算を、ブラウザですぐ。',
  'description':'勾配、高低差、面積、坪、R・円弧、重力式擁壁、鉄筋、ブロックなどをスマホで計算できる無料の現場電卓です。ログイン不要で結果をすぐ確認できます。',
 },
 'slope':{
  'title':'勾配・高低差・カーポート柱高計算｜現場電卓Web',
  'h1':'勾配・カーポートの高低差計算',
  'description':'横・縦寸法から勾配、角度、斜距離を計算。カーポートの柱間寸法と屋根勾配から柱の高低差も確認できる無料計算ツールです。',
  'guide':'横寸法と縦寸法を入力すると、斜距離・角度・勾配率を計算します。カーポートモードでは、柱間寸法と勾配角度から柱の高低差を確認できます。',
 },
 'ordinary':{
  'title':'現場で使える無料の普通電卓｜現場電卓Web',
  'h1':'現場で使える普通電卓',
  'description':'四則演算と割合計算をスマホですぐ使える、ログイン不要の無料電卓です。現場での数量や金額の確認に利用できます。',
  'guide':'足し算・引き算・掛け算・割り算と割合を、その場ですぐ確認できるシンプルな電卓です。',
 },
 'density':{
  'title':'比重から材料重量を計算｜現場電卓Web',
  'h1':'比重から材料重量を計算',
  'description':'体積と比重からコンクリート、砕石、砂、残土などの重量を概算する無料ツールです。m³からt・kgをすぐ確認できます。',
  'guide':'材料の体積と比重を入力し、重量をt・kgで概算します。含水率や締固めで変わるため、積載量や処分量の目安として利用してください。',
 },
 'memo':{
  'title':'現場メモ｜寸法・材料をブラウザに保存｜現場電卓Web',
  'h1':'現場メモ',
  'description':'現場の寸法、材料、連絡事項をスマホのブラウザ内に保存できる無料メモです。ログイン不要で入力内容を自動保存します。',
  'guide':'現場の寸法や材料、連絡事項をブラウザ内へ自動保存します。入力内容はサーバーへ送信せず、この端末に残ります。',
 },
 'radius':{
  'title':'R・円弧半径・円周計算｜現場電卓Web',
  'h1':'R・円弧・円周計算',
  'description':'弦長と矢高から円弧のR・半径・中心角・円弧長を計算。直径から円周と円面積も確認できる無料ツールです。',
  'guide':'アールモードでは弦長と矢高からR、中心角、円弧長を計算します。真円モードでは直径から円周と面積を確認できます。',
 },
 'area':{
  'title':'平米・坪・面積計算｜㎡と坪を同時変換｜現場電卓Web',
  'h1':'平面拾い・平米／坪計算',
  'description':'縦横寸法から面積を㎡と坪で同時計算。コンクリート体積やメッシュ枚数も確認できる、床・敷地・人工芝・舗装向けの無料ツールです。',
  'guide':'縦と横の寸法から平面積を㎡と坪で同時表示します。厚みを入力するとコンクリート体積、メッシュ寸法を入力すると必要枚数も確認できます。',
 },
 'gravity':{
  'title':'重力式擁壁の底幅・断面積計算｜現場電卓Web',
  'h1':'重力式擁壁計算',
  'description':'重力式擁壁の高さ、天端幅、法勾配から底幅と断面積、コンクリート量を計算する無料ツールです。確認高さごとの幅も表示します。',
  'guide':'擁壁の全高、天端幅、法勾配から底幅と断面積を計算します。延長を入力するとコンクリート総量も確認できます。',
 },
 'rebar':{
  'title':'鉄筋の本数・総延長・重量計算｜現場電卓Web',
  'h1':'鉄筋の本数・重量計算',
  'description':'直壁・L型擁壁の寸法、かぶり、鉄筋ピッチから必要本数、総延長、概算重量を計算する無料の鉄筋拾いツールです。',
  'guide':'直壁とL型擁壁の寸法、かぶり、配筋ピッチから鉄筋本数と総延長、概算重量を拾います。鉄筋径と定尺も選択できます。',
 },
 'block':{
  'title':'コンクリートブロック枚数・配筋本数計算｜現場電卓Web',
  'h1':'ブロック枚数計算',
  'description':'施工延長と段数からコンクリートブロックの必要枚数、縦筋・横筋本数を計算する無料ツールです。ブロック塀の数量拾いに使えます。',
  'guide':'施工延長と段数からコンクリートブロックの枚数を計算し、指定したピッチから縦筋・横筋の本数も確認します。',
 },
}
FIELDS={
'slope':'''<div class="tabs"><button class="tab active" data-mode="height">高さから</button><button class="tab" data-mode="carport">カーポート</button></div><div data-pane="height" class="fields"><div class="field"><label>横寸法（mm）</label><input id="horizontal" type="number" inputmode="decimal" placeholder="1000"></div><div class="field"><label>縦寸法（mm）</label><input id="vertical" type="number" inputmode="decimal" placeholder="100"></div></div><div data-pane="carport" class="fields hidden"><div class="field"><label>柱間寸法（mm）</label><input id="span" type="number" inputmode="decimal" value="2900" data-default="2900"></div><div class="field"><label>勾配（°）</label><input id="degree" type="number" inputmode="decimal" value="4" step="0.1" data-default="4"></div></div>''',
'area':'''<div class="fields"><div class="field"><label>縦（mm）</label><input id="length" type="number" inputmode="decimal" placeholder="5000"></div><div class="field"><label>横（mm）</label><input id="width" type="number" inputmode="decimal" placeholder="4000"></div><div class="field"><label>厚み（mm）</label><input id="thickness" type="number" inputmode="decimal" placeholder="100"></div><div class="field"><label>メッシュ縦（mm）</label><input id="meshLength" type="number" inputmode="decimal" value="2000" data-default="2000"></div><div class="field"><label>メッシュ横（mm）</label><input id="meshWidth" type="number" inputmode="decimal" value="1000" data-default="1000"></div><div class="field"><label>被せ（mm）</label><input id="meshLap" type="number" inputmode="decimal" value="100" data-default="100"></div></div><p class="note">アプリ版「土間」の計算を継承し、Web版では面積を㎡と坪で併記します。</p>''',
'radius':'''<div class="tabs"><button class="tab active" data-mode="arc">アール</button><button class="tab" data-mode="circle">真円</button></div><div data-pane="arc" class="fields"><div class="field"><label>弦長（mm）</label><input id="chord" type="number" inputmode="decimal" placeholder="5000"></div><div class="field"><label>矢高（mm）</label><input id="sagitta" type="number" inputmode="decimal" placeholder="500"></div></div><div data-pane="circle" class="fields hidden"><div class="field full"><label>直径（mm）</label><input id="diameter" type="number" inputmode="decimal" placeholder="3600"></div></div>''',
'density':'''<div class="fields"><div class="field"><label>体積（m³）</label><input id="volume" type="number" inputmode="decimal" placeholder="1.5"></div><div class="field"><label>材料・比重（t/m³）</label><select id="density"><option value="2.3">コンクリート 2.3</option><option value="2.3">アスファルト 2.3</option><option value="1.7">残土 1.7</option><option value="1.6">砕石 1.6</option><option value="1.5">砂 1.5</option><option value="1.4">真砂土 1.4</option></select></div></div><p class="note">含水率・締固めで変動します。積載・処分量の概算用です。</p>''',
'gravity':'''<div class="fields"><div class="field"><label>全高 H（mm）</label><input id="height" type="number" inputmode="decimal" placeholder="1500"></div><div class="field"><label>天端幅 T（mm）</label><input id="top" type="number" inputmode="decimal" value="300" data-default="300"></div><div class="field"><label>勾配（0.3＝3分）</label><input id="wallSlope" type="number" inputmode="decimal" value="0.3" step="0.01" data-default="0.3"></div><div class="field"><label>底幅 B（mm・空欄で自動）</label><input id="wallBottom" type="number" inputmode="decimal" placeholder="自動計算"></div><div class="field"><label>確認高さ h1（mm / 上端）</label><input id="h1" type="number" inputmode="decimal" placeholder="300"></div><div class="field"><label>確認高さ h2（mm / 上端）</label><input id="h2" type="number" inputmode="decimal" placeholder="800"></div><div class="field"><label>確認高さ h3（mm / 上端）</label><input id="h3" type="number" inputmode="decimal" placeholder="1300"></div><div class="field"><label>延長 L（m・任意）</label><input id="wallLength" type="number" inputmode="decimal" placeholder="10"></div></div>''',
'rebar':'''<div class="tabs"><button class="tab active" data-mode="wall">直壁</button><button class="tab" data-mode="lwall">L型擁壁</button></div><div data-pane="wall" class="fields"><div class="field"><label>総延長 L（mm）</label><input id="rebarLength" type="number" inputmode="decimal" placeholder="10000"></div><div class="field"><label>高さ H（mm）</label><input id="rebarHeight" type="number" inputmode="decimal" placeholder="1500"></div><div class="field"><label>横筋ピッチ（mm）</label><input id="rebarHPitch" type="number" inputmode="decimal" value="200" data-default="200"></div><div class="field"><label>縦筋ピッチ（mm）</label><input id="rebarVPitch" type="number" inputmode="decimal" value="200" data-default="200"></div><div class="field"><label>かぶり（mm）</label><input id="cover" type="number" inputmode="decimal" value="40" data-default="40"></div><div class="field"><label>定尺（mm）</label><input id="stock" type="number" inputmode="decimal" value="5000" data-default="5000"></div><div class="field full"><label>鉄筋径</label><select id="diameter"><option>D10</option><option>D13</option><option>D16</option><option>D19</option></select></div></div><div data-pane="lwall" class="fields hidden"><div class="field"><label>総延長 L（mm）</label><input id="lLength" type="number" inputmode="decimal" placeholder="10000"></div><div class="field"><label>立上り高さ H（mm）</label><input id="lHeight" type="number" inputmode="decimal" placeholder="1500"></div><div class="field"><label>ベース幅 B（mm）</label><input id="lBase" type="number" inputmode="decimal" placeholder="600"></div><div class="field"><label>かぶり（mm）</label><input id="lCover" type="number" inputmode="decimal" value="40" data-default="40"></div><div class="field"><label>縦筋ピッチ（mm）</label><input id="lVPitch" type="number" inputmode="decimal" value="200" data-default="200"></div><div class="field"><label>横筋ピッチ（mm）</label><input id="lHPitch" type="number" inputmode="decimal" value="200" data-default="200"></div><div class="field"><label>定尺（mm）</label><input id="lStock" type="number" inputmode="decimal" value="5000" data-default="5000"></div><div class="field"><label>鉄筋径</label><select id="lDiameter"><option>D10</option><option>D13</option><option>D16</option><option>D19</option></select></div></div><p class="note">アプリ版の直壁・L型擁壁モードと同じ計算条件です。</p>''',
'block':'''<div class="fields"><div class="field"><label>延長（mm）</label><input id="blockLength" type="number" inputmode="decimal" placeholder="10000"></div><div class="field"><label>段数</label><input id="rows" type="number" inputmode="numeric" placeholder="5"></div><div class="field"><label>ブロック長さ（mm）</label><input id="unit" type="number" inputmode="numeric" value="400" data-default="400"></div><div class="field"><label>縦筋ピッチ（mm）</label><input id="verticalPitch" type="number" inputmode="numeric" value="800" data-default="800"></div><div class="field"><label>横筋（○段ごと）</label><input id="horizontalEvery" type="number" inputmode="numeric" value="2" data-default="2"></div></div>'''
}
RESULTS={
'slope':['斜距離 / 柱高低差','角度 / 勾配','勾配率 / 柱間寸法','分数表記 / 対象'],
'area':['面積','坪数','コンクリート体積','メッシュ枚数'],
'radius':['円弧実長 / 円周','半径','中心角 / 面積','円周参考 / 直径'],
'density':['重量','重量','使用比重'],
'gravity':['底幅 B','断面面積','延長1mあたり','総コンクリート量','h1位置の幅','h2位置の幅','h3位置の幅'],
'rebar':['縦筋本数 / L型縦筋本数','横筋段数 / L型横筋本数','横筋本数 / 段','鉄筋総延長 / 1本長さ','概算重量 / 合計重量'],
'block':['CB枚数','縦筋本数','横筋本数']}

def page_url(slug='home'):
 return f'{SITE_ORIGIN}/' if slug=='home' else f'{SITE_ORIGIN}/{slug}/'
def structured_data(slug,name,desc):
 url=page_url(slug)
 if slug=='home':
  data={'@context':'https://schema.org','@type':'WebSite','name':'現場電卓Web','url':url,'description':desc,'inLanguage':'ja'}
 else:
  data={'@context':'https://schema.org','@graph':[
   {'@type':'WebApplication','name':name,'url':url,'description':desc,'applicationCategory':'UtilitiesApplication','operatingSystem':'Web','browserRequirements':'JavaScriptを有効にしてください','isAccessibleForFree':True,'inLanguage':'ja'},
   {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'現場電卓Web','item':page_url()},{'@type':'ListItem','position':2,'name':name,'item':url}]}
  ]}
 return json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
def head(slug,depth=''):
 seo=SEO[slug];url=page_url(slug)
 ga4=f'''<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4_MEASUREMENT_ID}');</script>''' if GA4_MEASUREMENT_ID else ''
 return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{html.escape(seo['title'])}</title><meta name="description" content="{html.escape(seo['description'])}"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow,max-image-preview:large"><meta property="og:type" content="website"><meta property="og:locale" content="ja_JP"><meta property="og:site_name" content="現場電卓Web"><meta property="og:title" content="{html.escape(seo['title'])}"><meta property="og:description" content="{html.escape(seo['description'])}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><meta name="theme-color" content="#06110e"><link rel="stylesheet" href="{depth}assets/app.css"><link rel="stylesheet" href="{depth}assets/diagram.css"><link rel="stylesheet" href="{depth}assets/related.css"><script type="application/ld+json">{structured_data(slug,seo['h1'],seo['description'])}</script>{ga4}<script src="{depth}assets/app.js" defer></script><script src="{depth}assets/diagram-samples.js" defer></script>'''
def chrome(depth=''):
 return f'''<header class="topbar"><div class="shell"><a class="brand" href="{depth}index.html">現場電卓<small>GENBA TOOLBOX WEB</small></a>{'<a class="home-link" href="../index.html">ツール一覧</a>' if depth else ''}</div></header>'''
def related(depth=''):
 return f'''<aside class="related-services" aria-labelledby="relatedTitle"><div class="shell"><p class="related-kicker">RELATED SERVICES</p><h2 id="relatedTitle">関連サービス</h2><div class="related-grid"><section class="related-app"><p>現場電卓をスマホで持ち歩くならアプリ版</p><div class="store-badges"><a href="{APP_STORE_URL}" target="_blank" rel="noopener noreferrer" aria-label="現場電卓をApp Storeで見る"><img src="{depth}assets/app-store-badge.svg" alt="App Storeからダウンロード" width="240" height="80" loading="lazy" decoding="async"></a><a href="{GOOGLE_PLAY_URL}" target="_blank" rel="noopener noreferrer" aria-label="現場電卓をGoogle Playで見る"><img src="{depth}assets/google-play-badge.png" alt="Google Playで手に入れよう" width="240" height="93" loading="lazy" decoding="async"></a></div></section><div class="related-links"><a href="{CWEB_URL}" target="_blank" rel="noopener noreferrer"><small>現場職人向けホームページ制作</small><strong>C-WEB – Construction Web Terra</strong><span aria-hidden="true">↗</span></a><a href="{BLOG_URL}" target="_blank" rel="noopener noreferrer"><small>下請け依存から直客を増やした実録</small><strong>現場屋の自力経営</strong><span aria-hidden="true">↗</span></a></div></div></div></aside>'''
def tool_links(current):
 links=''.join(f'<a href="../{slug}/">{name}</a>' for slug,name,_ in TOOLS if slug!=current)
 return f'''<nav class="tool-links" aria-label="他の計算ツール"><h2>他の計算ツール</h2><div>{links}</div></nav>'''
def home():
 cards=''.join(f'<a class="tool-card" href="{slug}/"><span>{i:02}</span><strong>{name}</strong><small>{desc}</small></a>' for i,(slug,name,desc) in enumerate(TOOLS,1))
 seo=SEO['home']
 return f'''<!doctype html><html lang="ja"><head>{head('home')}</head><body>{chrome()}<main class="shell"><section class="hero"><p class="eyebrow">NO LOGIN · INSTANT CALC</p><h1>{seo['h1'].replace('、','、<br>',1)}</h1><p>アプリ版「現場電卓」の主要機能を、ログインなしで使えるWeb版です。数値を入れるとその場で計算し、結果をまとめてコピーできます。</p></section><section class="tool-grid">{cards}</section></main>{related()}<footer class="footer"><div class="shell">計算結果は参考値です。実施工は設計図書・メーカー資料・現場条件を優先してください。</div></footer></body></html>'''
def ordinary():
 keys=['C','⌫','%','/','7','8','9','*','4','5','6','-','1','2','3','+','0','00','.','='];buttons=''.join(f'<button class="key {"op" if k in "+-*/%" else "eq" if k=="=" else ""}" data-key="{k}">{ {"/":"÷","*":"×"}.get(k,k)}</button>' for k in keys)
 return f'''<div class="panel"><div class="calc-display"><small id="calcSub"></small><output id="calcMain">0</output></div><div class="keypad">{buttons}</div></div>'''
def memo():return '''<div class="panel"><textarea id="memo" class="memo" placeholder="寸法、材料、連絡事項など"></textarea><div class="actions"><button class="action" id="reset">全消去</button><button class="action primary" id="copy">コピー</button></div><p class="copy-status" id="copyStatus"></p><p class="note">入力内容はこの端末のブラウザ内に自動保存されます。</p></div>'''
def tool_page(slug,name,desc):
 seo=SEO[slug]
 if slug=='ordinary': body=ordinary()
 elif slug=='memo': body=memo()
 else:
  ids=['main','secondary','third','fourth','fifth','sixth','seventh']
  rows=''.join(f'<div class="result {"hero-result" if i==0 else ""}"><span>{label}</span><output id="{ids[i]}">—</output></div>' for i,label in enumerate(RESULTS[slug]))
  diagram=f'''<section class="panel diagram-panel{' rebar-diagram' if slug=='rebar' else ''}" aria-labelledby="diagramTitle"><h2 id="diagramTitle">模式図</h2><div id="diagram" class="diagram" aria-live="polite"></div><p class="diagram-note">未入力時は説明用のサンプル図です。縮尺より入力寸法を優先してください。</p></section>''' if slug in ('slope','radius','gravity','rebar','area') else ''
  body=f'''<div class="workspace"><section class="panel"><h2>入力</h2>{FIELDS[slug]}<div class="actions"><button class="action" id="reset">リセット</button></div></section>{diagram}<section class="panel"><h2>計算結果</h2><div class="results">{rows}</div><div class="actions"><button class="action primary" id="copy">結果をコピー</button></div><p class="copy-status" id="copyStatus"></p></section></div>'''
 return f'''<!doctype html><html lang="ja"><head>{head(slug,'../')}</head><body data-tool="{slug}">{chrome('../')}<main class="shell"><section class="tool-head"><p class="eyebrow">WEB CALCULATOR</p><h1>{seo['h1']}</h1><p>{desc}</p></section>{body}<section class="seo-guide" aria-labelledby="guideTitle"><h2 id="guideTitle">この計算ツールでできること</h2><p>{seo['guide']}</p></section>{tool_links(slug)}</main>{related('../')}<footer class="footer"><div class="shell">参考値としてご利用ください。実施工は設計図書・法令・メーカー資料を優先してください。</div></footer></body></html>'''
def build():
 OUT.mkdir(exist_ok=True)
 (OUT/'assets').mkdir(exist_ok=True)
 shutil.copy2(ROOT/'assets'/'app-store-badge.svg',OUT/'assets'/'app-store-badge.svg')
 shutil.copy2(ROOT/'assets'/'google-play-badge.png',OUT/'assets'/'google-play-badge.png')
 (OUT/'index.html').write_text(home(),encoding='utf-8')
 for slug,name,desc in TOOLS:
  d=OUT/slug;d.mkdir(exist_ok=True);(d/'index.html').write_text(tool_page(slug,name,desc),encoding='utf-8')
 urls=['home']+[slug for slug,_,_ in TOOLS]
 sitemap='''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''+''.join(f'  <url><loc>{page_url(slug)}</loc></url>\n' for slug in urls)+'</urlset>\n'
 (OUT/'sitemap.xml').write_text(sitemap,encoding='utf-8')
 (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE_ORIGIN}/sitemap.xml\n',encoding='utf-8')
 (OUT/'CNAME').write_text(f'{SITE_ORIGIN.removeprefix("https://")}\n',encoding='utf-8')
if __name__=='__main__':build()
