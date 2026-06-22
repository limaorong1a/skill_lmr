#!/usr/bin/env python3
"""把仓库数据(data.json)渲染成自包含的交互式 HTML 学习引擎。

用法：
    python build_html.py [data.json] [index.html]

默认读取 ./data.json，输出 ./index.html（与 data.json 同目录）。
输出为单文件、零依赖，双击即可在浏览器打开。
功能：📅每日一库 / 🧭选型顾问 / 🔍搜索筛选排序 / 卡片展开深度内容 / 学习进度。
data.json 格式见 SKILL.md 的「学习引擎」一节。
"""
import json
import sys
from pathlib import Path

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub 学习引擎</title>
<style>
  :root{
    --bg:#0d1117; --panel:#161b22; --panel2:#1c2330; --border:#2d3340;
    --text:#e6edf3; --muted:#8b949e; --accent:#58a6ff; --accent2:#7ee787;
    --gold:#f0b429; --done:#238636;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;
    background:var(--bg);color:var(--text);line-height:1.6;padding:24px;max-width:1280px;margin:0 auto}
  a{color:var(--accent)}
  header h1{font-size:26px;display:flex;align-items:center;gap:10px}
  header h1 .dot{width:12px;height:12px;border-radius:50%;background:var(--accent2);box-shadow:0 0 12px var(--accent2)}
  .sub{color:var(--muted);font-size:13px;margin-top:4px}
  .stats{display:flex;gap:16px;margin:16px 0;flex-wrap:wrap}
  .stat{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:10px 16px;min-width:104px}
  .stat .n{font-size:22px;font-weight:700;color:var(--accent)}
  .stat .l{font-size:12px;color:var(--muted)}
  .progress-wrap{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:12px 16px;flex:1;min-width:220px}
  .bar{height:8px;background:var(--panel2);border-radius:4px;overflow:hidden;margin-top:8px}
  .bar > i{display:block;height:100%;background:linear-gradient(90deg,var(--done),var(--accent2));width:0;transition:width .4s}
  /* 今日一库 */
  .today{background:linear-gradient(135deg,#1c2330,#161b22);border:1px solid var(--accent);
    border-radius:14px;padding:18px 20px;margin:18px 0;position:relative;overflow:hidden}
  .today::before{content:"📅 今日一库";position:absolute;top:0;right:0;background:var(--accent);
    color:#0d1117;font-size:12px;font-weight:700;padding:4px 12px;border-bottom-left-radius:10px}
  .today h2{font-size:19px;margin:4px 0 6px}
  .today h2 a{text-decoration:none}
  .today .meta{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin-bottom:8px}
  .today .desc{font-size:14px;margin-bottom:10px}
  .today .acts{display:flex;gap:10px;flex-wrap:wrap}
  .toolbar{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:18px 0}
  input[type=search],input[type=text],select{background:var(--panel);border:1px solid var(--border);color:var(--text);
    border-radius:8px;padding:9px 12px;font-size:14px;outline:none}
  input[type=search]{flex:1;min-width:200px}
  input:focus,select:focus{border-color:var(--accent)}
  button{cursor:pointer;border:none;border-radius:8px;font-size:14px;font-weight:600;padding:9px 16px;transition:.15s}
  .btn-primary{background:var(--accent);color:#0d1117}
  .btn-primary:hover{background:#79b8ff}
  .btn-ghost{background:var(--panel2);color:var(--text);border:1px solid var(--border)}
  .btn-ghost:hover{border-color:var(--accent)}
  .chips{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px}
  .chip{background:var(--panel);border:1px solid var(--border);color:var(--muted);border-radius:20px;
    padding:5px 14px;font-size:13px;cursor:pointer;transition:.15s}
  .chip:hover{border-color:var(--accent)}
  .chip.active{background:var(--accent);color:#0d1117;border-color:var(--accent);font-weight:600}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:16px}
  .card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:16px;
    display:flex;flex-direction:column;gap:8px;transition:.15s;position:relative}
  .card:hover{border-color:var(--accent);transform:translateY(-2px)}
  .card.done{opacity:.55}
  .card.done::after{content:"已学 ✓";position:absolute;top:12px;right:12px;background:var(--done);
    color:#fff;font-size:11px;padding:2px 8px;border-radius:10px;font-weight:700}
  .card h3{font-size:16px;word-break:break-all}
  .card h3 a{text-decoration:none}
  .card h3 a:hover{text-decoration:underline}
  .meta{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted);align-items:center}
  .tag{background:var(--panel2);border:1px solid var(--border);border-radius:6px;padding:1px 8px}
  .tag.lang{color:var(--accent2)}
  .tag.star{color:var(--gold)}
  .tag.delta{color:var(--accent2)}
  .field{font-size:13px}
  .field b{color:var(--muted);font-weight:600}
  .detail-box{display:none;border-top:1px dashed var(--border);margin-top:6px;padding-top:8px;font-size:13px}
  .detail-box.show{display:block}
  .detail-box h4{font-size:12px;color:var(--accent);margin:8px 0 3px;text-transform:uppercase;letter-spacing:.5px}
  .detail-box ul{margin:0;padding-left:18px}
  .detail-box li{margin-bottom:3px}
  .detail-box code{background:var(--panel2);padding:2px 6px;border-radius:4px;font-size:12px;display:inline-block;word-break:break-all}
  .card .actions{margin-top:auto;display:flex;gap:8px;padding-top:8px;flex-wrap:wrap}
  .card .actions a,.card .actions button{font-size:12px;padding:6px 10px;flex:1;text-align:center;text-decoration:none;min-width:90px}
  .a-open{background:var(--panel2);color:var(--accent);border:1px solid var(--border)}
  .a-learn{background:transparent;color:var(--muted);border:1px solid var(--border)}
  .a-learn.is-done{background:var(--done);color:#fff;border-color:var(--done)}
  .a-detail{background:transparent;color:var(--gold);border:1px solid var(--border)}
  .empty{text-align:center;color:var(--muted);padding:60px 0}
  /* modal */
  .modal{position:fixed;inset:0;background:rgba(0,0,0,.72);display:none;align-items:flex-start;justify-content:center;padding:40px 20px;z-index:50;overflow:auto}
  .modal.show{display:flex}
  .modal .box{background:var(--panel);border:1px solid var(--accent);border-radius:14px;padding:24px;max-width:680px;width:100%}
  .modal h2{font-size:16px;color:var(--gold);margin-bottom:12px}
  .advisor-row{display:flex;gap:10px;margin-bottom:14px}
  .advisor-row input{flex:1}
  .res{background:var(--panel2);border:1px solid var(--border);border-radius:8px;padding:10px 12px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start}
  .res input{margin-top:5px}
  .res .info{flex:1}
  .res .nm{font-weight:600;color:var(--accent)}
  .res .sc{font-size:11px;color:var(--gold)}
  .cmp{width:100%;border-collapse:collapse;margin-top:12px;font-size:12px}
  .cmp th,.cmp td{border:1px solid var(--border);padding:6px 8px;text-align:left;vertical-align:top}
  .cmp th{background:var(--panel2);color:var(--accent)}
  .modal .close{margin-top:16px;width:100%}
  footer{text-align:center;color:var(--muted);font-size:12px;margin-top:28px}
</style>
</head>
<body>
<header>
  <h1><span class="dot"></span>GitHub 学习引擎</h1>
  <div class="sub">数据更新：__GENERATED__ ｜ 由 github-trending-digest 生成 ｜ 学习进度自动保存在本浏览器</div>
  <div class="stats">
    <div class="stat"><div class="n" id="s-total">0</div><div class="l">仓库总数</div></div>
    <div class="stat"><div class="n" id="s-domain">0</div><div class="l">领域</div></div>
    <div class="stat"><div class="n" id="s-done">0</div><div class="l">已学</div></div>
    <div class="progress-wrap">
      <div style="display:flex;justify-content:space-between;font-size:13px">
        <span>学习进度</span><span id="p-text">0%</span>
      </div>
      <div class="bar"><i id="p-bar"></i></div>
    </div>
  </div>
</header>

<div class="today" id="today"></div>

<div class="toolbar">
  <input type="search" id="q" placeholder="🔍 搜索仓库名 / 描述 / 适合谁…">
  <select id="sort">
    <option value="stars">按 Star 排序</option>
    <option value="name">按名称排序</option>
    <option value="domain">按领域排序</option>
  </select>
  <button class="btn-primary" id="advisor-btn">🧭 选型顾问</button>
</div>
<div class="chips" id="chips"></div>
<div class="grid" id="grid"></div>
<div class="empty" id="empty" style="display:none">没有匹配的仓库</div>

<div class="modal" id="modal"><div class="box" id="modal-box"></div></div>

<footer>双击本文件即可离线打开 · 学习记录存于 localStorage · 「深度内容」来自各仓库 README 提炼</footer>

<script>
const DATA = __DATA__;
const LS_KEY = "learning-engine-done";
let done = new Set(JSON.parse(localStorage.getItem(LS_KEY) || "[]"));
let activeDomain = "全部";
let cmpSel = new Set();

const domains = ["全部", ...Array.from(new Set(DATA.map(r => r.domain)))];
const $ = id => document.getElementById(id);
const esc = s => (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
const byName = n => DATA.find(r => r.name === n);

function save(){ localStorage.setItem(LS_KEY, JSON.stringify([...done])); }
function starText(s){ if(typeof s!=="number"||isNaN(s)) return "—"; return s >= 1 ? s + "k" : Math.round(s*1000); }
function toggleDone(name){ done.has(name) ? done.delete(name) : done.add(name); save(); renderAll(); }

/* ---------- 今日一库 (D) ---------- */
function todayRepo(){
  const pool = DATA.filter(r => !done.has(r.name));
  const src = pool.length ? pool : DATA;
  const d = new Date();
  const key = "" + d.getFullYear() + d.getMonth() + d.getDate();
  let h = 0; for(const c of key) h = (h*31 + c.charCodeAt(0)) >>> 0;
  return src[h % src.length];
}
function renderToday(){
  const r = todayRepo();
  const learned = done.has(r.name);
  $("today").innerHTML = `
    <h2><a href="${r.url}" target="_blank">${esc(r.name)}</a></h2>
    <div class="meta">
      <span class="tag lang">${esc(r.lang||'—')}</span>
      <span class="tag star">⭐ ${starText(r.stars)}</span>
      ${r.delta?`<span class="tag delta">${esc(r.delta)}</span>`:''}
      <span class="tag">${esc(r.domain)}</span>
    </div>
    <div class="desc"><b>是什么：</b>${esc(r.what)}　<b>亮点：</b>${esc(r.highlight)}</div>
    <div class="acts">
      <a class="btn-ghost" style="text-decoration:none;padding:7px 14px;border-radius:8px" href="${r.url}" target="_blank">打开仓库 →</a>
      ${r.detail?`<button class="btn-ghost" id="t-detail">查看深度内容</button>`:''}
      <button class="btn-primary" id="t-learn">${learned?'✓ 今天已学':'标记今天已学'}</button>
      <button class="btn-ghost" id="t-skip">换一个</button>
    </div>
    <div class="detail-box" id="t-detailbox">${detailHTML(r)}</div>`;
  if(r.detail) $("t-detail").onclick = () => $("t-detailbox").classList.toggle("show");
  $("t-learn").onclick = () => toggleDone(r.name);
  $("t-skip").onclick = () => { const p=DATA.filter(x=>!done.has(x.name)&&x.name!==r.name);
    const pick=(p.length?p:DATA)[Math.floor(Math.random()*(p.length?p.length:DATA.length))];
    showDetailModal(pick); };
}

/* ---------- 深度内容 (A) ---------- */
function detailHTML(r){
  if(!r.detail) return "";
  const d = r.detail;
  let h = "";
  if(d.capabilities&&d.capabilities.length){ h+=`<h4>核心能力</h4><ul>`+d.capabilities.map(x=>`<li>${esc(x)}</li>`).join("")+`</ul>`; }
  if(d.learnings&&d.learnings.length){ h+=`<h4>可学知识点</h4><ul>`+d.learnings.map(x=>`<li>${esc(x)}</li>`).join("")+`</ul>`; }
  if(d.quickstart){ h+=`<h4>上手</h4><code>${esc(d.quickstart)}</code>`; }
  return h;
}

/* ---------- 卡片网格 ---------- */
function cardHTML(r){
  const isDone = done.has(r.name);
  return `<div class="card ${isDone?'done':''}">
    <h3><a href="${r.url}" target="_blank">${esc(r.name)}</a></h3>
    <div class="meta">
      <span class="tag lang">${esc(r.lang||'—')}</span>
      <span class="tag star">⭐ ${starText(r.stars)}</span>
      ${r.delta?`<span class="tag delta">${esc(r.delta)}</span>`:''}
      <span class="tag">${esc(r.domain)}</span>
    </div>
    <div class="field"><b>是什么：</b>${esc(r.what)}</div>
    <div class="field"><b>亮点：</b>${esc(r.highlight)}</div>
    <div class="field"><b>适合谁：</b>${esc(r.forWho)}</div>
    <div class="detail-box">${detailHTML(r)}</div>
    <div class="actions">
      <a class="a-open" href="${r.url}" target="_blank">打开 →</a>
      ${r.detail?`<button class="a-detail" data-n="${esc(r.name)}">深度内容 ▾</button>`:''}
      <button class="a-learn ${isDone?'is-done':''}" data-n="${esc(r.name)}">${isDone?'✓ 已学':'标记已学'}</button>
    </div>
  </div>`;
}

function currentList(){
  const q = $("q").value.trim().toLowerCase();
  let list = DATA.filter(r => {
    if(activeDomain !== "全部" && r.domain !== activeDomain) return false;
    if(!q) return true;
    return (r.name+r.what+r.highlight+r.forWho+r.domain).toLowerCase().includes(q);
  });
  const sort = $("sort").value;
  list.sort((a,b) =>
    sort==="stars" ? b.stars-a.stars :
    sort==="name" ? a.name.localeCompare(b.name) :
    a.domain.localeCompare(b.domain) || b.stars-a.stars);
  return list;
}

function renderChips(){
  $("chips").innerHTML = domains.map(d =>
    `<span class="chip ${d===activeDomain?'active':''}" data-d="${esc(d)}">${esc(d)}</span>`).join("");
  document.querySelectorAll("#chips .chip").forEach(c =>
    c.onclick = () => { activeDomain = c.dataset.d; renderGrid(); });
}

function renderGrid(){
  const list = currentList();
  $("grid").innerHTML = list.map(cardHTML).join("");
  $("empty").style.display = list.length ? "none" : "block";
  document.querySelectorAll(".a-learn").forEach(b => b.onclick = () => toggleDone(b.dataset.n));
  document.querySelectorAll(".a-detail").forEach(b => b.onclick = () => {
    const box = b.closest(".card").querySelector(".detail-box");
    box.classList.toggle("show");
    b.textContent = box.classList.contains("show") ? "深度内容 ▴" : "深度内容 ▾";
  });
}

function renderStats(){
  $("s-total").textContent = DATA.length;
  $("s-domain").textContent = domains.length - 1;
  $("s-done").textContent = done.size;
  const pct = DATA.length ? Math.round(done.size/DATA.length*100) : 0;
  $("p-text").textContent = pct + "%";
  $("p-bar").style.width = pct + "%";
}

function renderAll(){ renderStats(); renderToday(); renderChips(); renderGrid(); }

/* ---------- 选型顾问 (C) ---------- */
function advise(q){
  const terms = q.toLowerCase().split(/[\s,，、]+/).filter(Boolean);
  if(!terms.length) return [];
  return DATA.map(r => {
    const hay = (r.name+" "+r.domain+" "+r.what+" "+r.highlight+" "+r.forWho+" "+
      (r.detail?JSON.stringify(r.detail):"")).toLowerCase();
    let score = 0; terms.forEach(t => { if(hay.includes(t)) score++; });
    return {r, score};
  }).filter(x => x.score>0).sort((a,b) => b.score-a.score || b.r.stars-a.r.stars).slice(0,8);
}

function openAdvisor(){
  cmpSel = new Set();
  $("modal-box").innerHTML = `
    <h2>🧭 选型顾问</h2>
    <div class="sub" style="margin-bottom:10px">描述你的需求/场景（如：本地代码检索 省token、做 RAG 文档处理、终端编码 agent），从已收录仓库中推荐并对比。</div>
    <div class="advisor-row">
      <input type="text" id="adv-q" placeholder="例如：本地 代码 知识图谱 省token">
      <button class="btn-primary" id="adv-go">推荐</button>
    </div>
    <div id="adv-res"></div>
    <div id="adv-cmp"></div>
    <button class="btn-ghost close" id="adv-close">关闭</button>`;
  $("modal").classList.add("show");
  $("adv-close").onclick = closeModal;
  $("adv-go").onclick = runAdvisor;
  $("adv-q").addEventListener("keydown", e => { if(e.key==="Enter") runAdvisor(); });
  $("adv-q").focus();
}

function runAdvisor(){
  const res = advise($("adv-q").value);
  if(!res.length){ $("adv-res").innerHTML = `<div class="sub">没找到匹配，换些关键词试试。</div>`; $("adv-cmp").innerHTML=""; return; }
  $("adv-res").innerHTML = res.map(x => `
    <div class="res">
      <input type="checkbox" class="cmp-ck" data-n="${esc(x.r.name)}" ${cmpSel.has(x.r.name)?'checked':''}>
      <div class="info">
        <div><span class="nm">${esc(x.r.name)}</span> <span class="sc">匹配度 ${x.score}</span>
          <span class="tag" style="margin-left:6px">${esc(x.r.domain)}</span>
          <span class="tag star">⭐${starText(x.r.stars)}</span></div>
        <div class="field">${esc(x.r.what)}　<b>亮点：</b>${esc(x.r.highlight)}</div>
      </div>
    </div>`).join("") +
    `<button class="btn-ghost" id="adv-cmp-btn" style="margin-top:6px">对比所选（勾选 2+ 个）</button>`;
  document.querySelectorAll(".cmp-ck").forEach(ck => ck.onchange = () => {
    ck.checked ? cmpSel.add(ck.dataset.n) : cmpSel.delete(ck.dataset.n); });
  $("adv-cmp-btn").onclick = renderCompare;
}

function renderCompare(){
  const sel = [...cmpSel].map(byName).filter(Boolean);
  if(sel.length < 2){ $("adv-cmp").innerHTML = `<div class="sub" style="margin-top:8px">请至少勾选 2 个进行对比。</div>`; return; }
  const rows = [
    ["语言", r => esc(r.lang)],
    ["Star", r => "⭐"+starText(r.stars)],
    ["领域", r => esc(r.domain)],
    ["是什么", r => esc(r.what)],
    ["亮点", r => esc(r.highlight)],
    ["适合谁", r => esc(r.forWho)],
  ];
  $("adv-cmp").innerHTML = `<table class="cmp"><tr><th>维度</th>${sel.map(r=>`<th>${esc(r.name)}</th>`).join("")}</tr>` +
    rows.map(([k,f]) => `<tr><td><b>${k}</b></td>${sel.map(r=>`<td>${f(r)}</td>`).join("")}</tr>`).join("") +
    `</table>`;
}

/* ---------- 详情弹窗（换一个时用） ---------- */
function showDetailModal(r){
  $("modal-box").innerHTML = `<h2>🎲 换一个：${esc(r.name)}</h2>` + cardHTML(r) +
    `<button class="btn-ghost close" id="m-close">关闭</button>`;
  $("modal").classList.add("show");
  $("m-close").onclick = closeModal;
  $("modal-box").querySelectorAll(".a-learn").forEach(b => b.onclick = () => { toggleDone(b.dataset.n); closeModal(); });
  $("modal-box").querySelectorAll(".a-detail").forEach(b => b.onclick = () => {
    const box = b.closest(".card").querySelector(".detail-box");
    box.classList.toggle("show");
  });
}
function closeModal(){ $("modal").classList.remove("show"); }

$("q").oninput = renderGrid;
$("sort").onchange = renderGrid;
$("advisor-btn").onclick = openAdvisor;
$("modal").onclick = e => { if(e.target.id==="modal") closeModal(); };
renderAll();
</script>
</body>
</html>
"""


def main():
    data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data.json")
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else data_path.with_name("index.html")

    if not data_path.exists():
        sys.exit(f"找不到数据文件：{data_path}")

    data = json.loads(data_path.read_text(encoding="utf-8"))
    repos = data.get("repos", data) if isinstance(data, dict) else data
    generated = data.get("generated", "") if isinstance(data, dict) else ""

    html = (TEMPLATE
            .replace("__DATA__", json.dumps(repos, ensure_ascii=False))
            .replace("__GENERATED__", generated or "—"))
    out_path.write_text(html, encoding="utf-8")
    detailed = sum(1 for r in repos if isinstance(r, dict) and r.get("detail"))
    print(f"已生成 {out_path}（{len(repos)} 个仓库，其中 {detailed} 个含深度内容）")


if __name__ == "__main__":
    main()
