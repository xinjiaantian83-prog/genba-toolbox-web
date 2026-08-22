from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://xinjiaantian83-prog.github.io/genba-toolbox-web"
PUBLIC = "/genba-toolbox-web"
APP_STORE = "https://apps.apple.com/jp/app/%E7%8F%BE%E5%A0%B4%E9%9B%BB%E5%8D%93/id6776547872"
GOOGLE_PLAY = "https://play.google.com/store/apps/details?id=com.genbatoolbox.genbacalcnew"

PAGES = [
    {
        "slug": "carport-height-difference",
        "title": "カーポート柱高低差の計算方法｜勾配と柱間寸法から算出",
        "description": "フラットタイプのカーポート施工で使う柱高低差を、柱間寸法と勾配角度から求める方法を簡潔に解説します。無料アプリ現場電卓でも計算できます。",
        "h1": "カーポート柱高低差の計算",
        "lead": "柱間寸法と屋根勾配から、左右の柱に必要な高さの差を確認できます。",
        "formula": "柱高低差 ＝ 柱間寸法 × tan（勾配角度）",
        "method": "柱間寸法を L、勾配角度を θ とすると、高低差は L × tan(θ) です。寸法と結果の単位はそろえて計算します。勾配が割合で示される場合は、L × 勾配率で求めます。",
        "example": "柱間寸法2,900mm、勾配4°の場合は、2,900 × tan(4°) ≒ 203mmが目安です。",
        "image": "images/carport.png",
        "alt": "現場電卓のカーポート柱高低差計算画面",
    },
    {
        "slug": "slope-angle-distance",
        "title": "勾配・角度・斜距離の計算方法｜高さと横寸法から算出",
        "description": "横寸法と高さから、斜距離・角度・勾配率・分数勾配を求める方法を現場向けに解説。無料アプリ現場電卓でも入力だけで確認できます。",
        "h1": "勾配・角度・斜距離の計算",
        "lead": "横寸法と高さから、斜距離・角度・勾配率・分数表記をまとめて確認できます。",
        "formula": "斜距離 ＝ √（横寸法² ＋ 高さ²）",
        "method": "横寸法を a、高さを b とすると、斜距離は √(a²+b²)、角度は atan(b÷a)、勾配率は b÷a×100です。分数勾配は、立ち上がり1に対する横方向の比で表します。",
        "example": "横5,830mm、高さ1,350mmなら、斜距離は約5,984.3mm、角度は約13.04°、勾配率は約23.16%です。",
        "image": "images/slope.png",
        "alt": "現場電卓の勾配角度斜距離計算画面",
    },
    {
        "slug": "radius-arc",
        "title": "R・アール寸法の計算方法｜弦長と矢高から半径を算出",
        "description": "弦長と矢高からR（半径）、中心角、円弧長を求める方法を解説。外構や型枠のアール確認に使える無料アプリ現場電卓も案内します。",
        "h1": "R・アール寸法の計算",
        "lead": "弦長と矢高から、半径R・中心角・円弧実長を確認できます。",
        "formula": "R ＝ 弦長² ÷（8 × 矢高）＋ 矢高 ÷ 2",
        "method": "弦長を c、矢高を h とすると、半径Rは c²÷(8h)+h÷2です。中心角は 2×asin(c÷2R)、円弧長は R×中心角（ラジアン）で求めます。",
        "example": "弦長5,000mm、矢高500mmの場合、半径Rは6,500mm、円弧実長は約5,132.3mmです。材料の曲げ許容や施工条件は別途確認します。",
        "image": "images/radius.png",
        "alt": "現場電卓のRアール寸法計算画面",
    },
    {
        "slug": "circle-circumference-area",
        "title": "直径から円周・面積を計算｜真円の計算方法",
        "description": "直径から円周、半径、円の面積を求める式を簡潔に解説。真円施工や材料数量の確認に使える無料アプリ現場電卓も案内します。",
        "h1": "直径から円周・面積を計算",
        "lead": "真円の直径を入力して、円周・半径・面積をまとめて確認できます。",
        "formula": "円周 ＝ 直径 × π　／　面積 ＝ π ×（直径 ÷ 2）²",
        "method": "直径を D とすると、半径は D÷2、円周は πD、面積は π(D÷2)²です。面積をm²で求める場合は、入力寸法をmに換算してから計算します。",
        "example": "直径3,600mm（3.6m）の場合、円周は約11,309.7mm、面積は約10.179m²です。",
        "image": "images/circle.png",
        "alt": "現場電卓の直径から円周面積を求める画面",
    },
    {
        "slug": "concrete-volume",
        "title": "土間コンクリート数量計算｜面積・厚みから体積を算出",
        "description": "土間コンクリートの長さ・幅・厚みから必要体積m³を求める方法を解説。形状別に分けて合計する考え方と現場電卓アプリを紹介します。",
        "h1": "土間コンクリート数量計算",
        "lead": "施工範囲の長さ・幅・厚みから、コンクリート体積の目安を確認できます。",
        "formula": "体積（m³）＝ 長さ（m）× 幅（m）× 厚み（m）",
        "method": "寸法をすべてmにそろえて掛けます。複雑な形状は長方形や三角形に分割して各体積を合計します。ロス、路盤の不陸、勾配による厚みの変化は別途見込みます。",
        "example": "長さ5m、幅3m、厚み100mm（0.1m）の場合、基本体積は1.5m³です。実発注量は現場条件を踏まえて判断します。",
        "image": "images/home.png",
        "alt": "現場電卓のホーム画面",
    },
    {
        "slug": "rebar-count",
        "title": "鉄筋拾い・本数計算｜寸法とピッチから必要本数を算出",
        "description": "施工幅、かぶり、鉄筋ピッチから必要本数を拾う基本的な計算方法を解説。縦横の鉄筋数量を確認できる無料アプリ現場電卓も紹介します。",
        "h1": "鉄筋拾い・本数計算",
        "lead": "施工寸法・かぶり・配筋ピッチから、縦横方向の鉄筋本数と総延長を確認できます。",
        "formula": "本数の目安 ＝ 切り上げ（有効幅 ÷ ピッチ）＋ 1",
        "method": "有効幅は全体寸法から両側のかぶりを差し引きます。最大間隔が指定ピッチを超えないよう、有効幅÷ピッチを切り上げて端部の1本を加えます。縦横方向をそれぞれ計算します。",
        "example": "施工幅、かぶり、ピッチを入力して方向別に本数を確認します。継手長さ、定着、重ね、加工ロスは図面や仕様書に従って別途加算します。",
        "image": "images/home.png",
        "alt": "鉄筋拾い機能を含む現場電卓のホーム画面",
    },
]


def store_url(base: str, page: str, store: str) -> str:
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}utm_source=genba_toolbox_web&utm_medium=organic&utm_campaign=seo&utm_content={page}_{store}"


def schema(page: dict) -> str:
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "TechArticle",
                "headline": page["h1"],
                "description": page["description"],
                "url": f"{BASE}/{page['slug']}/",
                "inLanguage": "ja",
                "about": "建設・外構・土木の現場計算",
                "publisher": {"@id": f"{BASE}/#organization"},
            },
            {
                "@type": "SoftwareApplication",
                "name": "現場電卓",
                "alternateName": "GENBA TOOLBOX",
                "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "iOS, Android",
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "JPY"},
                "downloadUrl": [APP_STORE, GOOGLE_PLAY],
                "url": BASE + "/",
            },
            {
                "@type": "Organization",
                "@id": f"{BASE}/#organization",
                "name": "GENBA TOOLBOX",
                "url": BASE + "/",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "現場電卓", "item": BASE + "/"},
                    {"@type": "ListItem", "position": 2, "name": page["h1"], "item": f"{BASE}/{page['slug']}/"},
                ],
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def head(title: str, description: str, url: str, image: str) -> str:
    return f'''<meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#00130e">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="現場電卓｜GENBA TOOLBOX">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}/{image}">
  <meta property="og:locale" content="ja_JP">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{PUBLIC}/assets/icon.png">
  <link rel="stylesheet" href="{PUBLIC}/assets/style.css">'''


def cards(current: str | None = None) -> str:
    items = []
    for page in PAGES:
        if page["slug"] == current:
            continue
        items.append(
            f'<a class="tool-link" href="{PUBLIC}/{page["slug"]}/"><span>{html.escape(page["h1"])}</span><b aria-hidden="true">›</b></a>'
        )
    return "\n".join(items)


def badges(page: str) -> str:
    app_href = html.escape(store_url(APP_STORE, page, "ios"), quote=True)
    play_href = html.escape(store_url(GOOGLE_PLAY, page, "android"), quote=True)
    return f'''<div class="store-actions" aria-label="アプリストアへのリンク">
      <a class="store-link" data-store="app_store" data-page="{page}" href="{app_href}" target="_blank" rel="noopener noreferrer"><img src="{PUBLIC}/assets/app-store-badge.svg" alt="App Storeからダウンロード" width="240" height="80"></a>
      <a class="store-link" data-store="google_play" data-page="{page}" href="{play_href}" target="_blank" rel="noopener noreferrer"><img src="{PUBLIC}/assets/google-play-badge.png" alt="Google Playで手に入れよう" width="240" height="93"></a>
    </div>'''


def page_html(page: dict) -> str:
    url = f"{BASE}/{page['slug']}/"
    return f'''<!doctype html>
<html lang="ja">
<head>
  {head(page["title"], page["description"], url, page["image"])}
  <script type="application/ld+json">{schema(page)}</script>
</head>
<body data-page="{page['slug']}">
  <header class="site-header"><a class="brand" href="{PUBLIC}/"><img src="{PUBLIC}/assets/icon.png" alt="" width="42" height="42"><span>現場電卓<small>GENBA TOOLBOX</small></span></a></header>
  <main>
    <nav class="breadcrumb" aria-label="パンくず"><a href="{PUBLIC}/">トップ</a><span>›</span><span>{html.escape(page['h1'])}</span></nav>
    <article class="article">
      <section class="hero compact"><div><p class="eyebrow">現場計算ガイド</p><h1>{html.escape(page['h1'])}</h1><p>{html.escape(page['lead'])}</p></div><img src="{PUBLIC}/{page['image']}" alt="{html.escape(page['alt'])}" width="420" height="910"></section>
      <div class="steps">
        <section class="panel"><span class="step">01</span><h2>何を計算できるか</h2><p>{html.escape(page['lead'])}</p></section>
        <section class="panel"><span class="step">02</span><h2>計算方法</h2><p class="formula">{html.escape(page['formula'])}</p><p>{html.escape(page['method'])}</p></section>
        <section class="panel"><span class="step">03</span><h2>現場での使用例</h2><p>{html.escape(page['example'])}</p></section>
        <section class="app-cta"><span class="step">04</span><h2>現場電卓なら入力だけで計算できます</h2><p>勾配・カーポート、R・真円、土間、鉄筋など、現場で使う計算をひとつにまとめた無料アプリです。</p>{badges(page['slug'])}</section>
      </div>
      <aside class="notice"><strong>施工前にご確認ください</strong><p>掲載内容と計算結果は数量・寸法検討の参考値です。実施工では設計図書、構造条件、法令、メーカー資料、現場責任者の判断を優先してください。</p></aside>
    </article>
    <section class="related"><h2>ほかの現場計算</h2><div class="tool-grid">{cards(page['slug'])}</div></section>
  </main>
  <footer><a href="{PUBLIC}/privacy/">プライバシーポリシー</a><span>© GENBA TOOLBOX</span></footer>
  <script src="{PUBLIC}/assets/analytics.js" defer></script>
</body>
</html>'''


def home_html() -> str:
    description = "外構・土木・建設・DIYで使う勾配、カーポート柱高低差、R、円周、土間コンクリート、鉄筋本数の計算方法と無料アプリ現場電卓を紹介します。"
    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "name": "現場電卓｜GENBA TOOLBOX", "url": BASE + "/", "inLanguage": "ja"},
            {"@type": "SoftwareApplication", "name": "現場電卓", "alternateName": "GENBA TOOLBOX", "applicationCategory": "UtilitiesApplication", "operatingSystem": "iOS, Android", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "JPY"}, "downloadUrl": [APP_STORE, GOOGLE_PLAY]},
            {"@type": "Organization", "@id": f"{BASE}/#organization", "name": "GENBA TOOLBOX", "url": BASE + "/"},
        ],
    }
    return f'''<!doctype html><html lang="ja"><head>
  {head("現場電卓｜外構・土木・建設の現場計算ガイド", description, BASE + "/", "images/og-home.png")}
  <script type="application/ld+json">{json.dumps(schema_data, ensure_ascii=False, separators=(",", ":"))}</script>
</head><body data-page="home">
  <header class="site-header"><a class="brand" href="{PUBLIC}/"><img src="{PUBLIC}/assets/icon.png" alt="" width="42" height="42"><span>現場電卓<small>GENBA TOOLBOX</small></span></a></header>
  <main><section class="home-hero"><div><p class="eyebrow">職人のための無料計算アプリ</p><h1>現場の計算を、<em>もっと早く。</em></h1><p>勾配・カーポート、R・真円、土間、鉄筋など。計算方法を確認して、そのまま無料アプリで使えます。</p>{badges('home')}</div><img src="{PUBLIC}/images/home.png" alt="現場電卓のアプリ画面" width="420" height="910"></section>
  <section class="tools"><div class="section-heading"><p class="eyebrow">CALCULATION GUIDE</p><h2>計算方法を選ぶ</h2></div><div class="tool-grid">{cards()}</div></section>
  <aside class="notice"><strong>参考値としてご利用ください</strong><p>実施工では設計図書、構造条件、法令、メーカー資料、現場責任者の判断を優先してください。</p></aside></main>
  <footer><a href="{PUBLIC}/privacy/">プライバシーポリシー</a><span>© GENBA TOOLBOX</span></footer><script src="{PUBLIC}/assets/analytics.js" defer></script></body></html>'''


def privacy_html() -> str:
    return f'''<!doctype html><html lang="ja"><head>{head("プライバシーポリシー｜現場電卓", "現場電卓Webサイトのプライバシーポリシーです。", BASE + "/privacy/", "images/og-home.png")}</head><body><header class="site-header"><a class="brand" href="{PUBLIC}/"><img src="{PUBLIC}/assets/icon.png" alt="" width="42" height="42"><span>現場電卓<small>GENBA TOOLBOX</small></span></a></header><main><article class="legal"><h1>プライバシーポリシー</h1><p>本サイトでは、利用状況の把握と改善のため、リンクのクリック元を識別できるパラメータを使用する場合があります。個人を直接特定する情報を本サイト上で入力・収集する機能は設けていません。</p><h2>外部サービス</h2><p>App StoreおよびGoogle Playへのリンク先では、各事業者のプライバシーポリシーが適用されます。</p><h2>変更</h2><p>必要に応じて本方針を変更する場合があります。</p></article></main><footer><a href="{PUBLIC}/">トップへ戻る</a><span>© GENBA TOOLBOX</span></footer></body></html>'''


def build() -> None:
    (ROOT / "index.html").write_text(home_html(), encoding="utf-8")
    for page in PAGES:
        target = ROOT / page["slug"]
        target.mkdir(parents=True, exist_ok=True)
        (target / "index.html").write_text(page_html(page), encoding="utf-8")
    target = ROOT / "privacy"
    target.mkdir(exist_ok=True)
    (target / "index.html").write_text(privacy_html(), encoding="utf-8")
    urls = [BASE + "/"] + [f"{BASE}/{p['slug']}/" for p in PAGES] + [BASE + "/privacy/"]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    build()
