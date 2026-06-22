#!/usr/bin/env python3
"""把仓库数据(data.json)渲染成自包含的交互式 HTML 学习看板。

用法：
    python build_html.py [data.json] [index.html]

默认读取 ./data.json，输出 ./index.html（与 data.json 同目录）。
输出为单文件、零依赖，双击即可在浏览器打开。
data.json 格式见 SKILL.md 的「一键生成 HTML 看板」一节。
"""
import json
import sys
from pathlib import Path

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub 学习雷达</title>
<style>
  :root{
    --bg:#0d1117; --panel:#161b22; --panel2:#1c2330; --border:#2d3340;
    --text:#e6edf3; --muted:#8b949e; --accent:#58a6ff; --accent2:#7ee787;
    --gold:#f0b429; --done:#238636;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei",sans-serif;
    background:var(--bg);color:var(--text);line-height:1.6;padding:24px;max-width:1280px;margin:0 auto}
  header{margin-bottom:20px}
  h1{font-size:26px;display:flex;align-items:center;gap:10px}
  h1 .dot{width:12px;height:12px;border-radius:50%;background:var(--accent2);box-shadow:0 0 12px var(--accent2)}
  .sub{color:var(--muted);font-size:13px;margin-top:4px}
  .stats{display:flex;gap:16px;margin:16px 0;flex-wrap:wrap}
  .stat{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:10px 16px;min-width:110px}
  .stat .n{font-size:22px;font-weight:700;color:var(--accent)}
  .stat .l{font-size:12px;color:var(--muted)}
  .progress-wrap{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:12px 16px;flex:1;min-width:220px}
  .bar{height:8px;background:var(--panel2);border-radius:4px;overflow:hidden;margin-top:8px}
  .bar > i{display:block;height:100%;background:linear-gradient(90deg,var(--done),var(--accent2));width:0;transition:width .4s}
  .toolbar{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin:18px 0}
  input[type=search],select{background:var(--panel);border:1px solid var(--border);color:var(--text);
    border-radius:8px;padding:9px 12px;font-size:14px;outline:none}
  input[type=search]{flex:1;min-width:220px}
  input[type=search]:focus,select:focus{border-color:var(--accent)}
  button{cursor:pointer;border:none;border-radius:8px;font-size:14px;font-weight:600;padding:9px 16px;transition:.15s}
  .btn-primary{background:var(--accent);color:#0d1117}
  .btn-primary:hover{background:#79b8ff}
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
  .card h3 a{color:var(--accent);text-decoration:none}
  .card h3 a:hover{text-decoration:underline}
  .meta{display:flex;gap:8px;flex-wrap:wrap;font-size:12px;color:var(--muted);align-items:center}
  .tag{background:var(--panel2);border:1px solid var(--border);border-radius:6px;padding:1px 8px}
  .tag.lang{color:var(--accent2)}
  .tag.star{color:var(--gold)}
  .tag.delta{color:var(--accent2)}
  .field{font-size:13px}
  .field b{color:var(--muted);font-weight:600}
  .card .actions{margin-top:auto;display:flex;gap:8px;padding-top:8px}
  .card .actions a,.card .actions button{font-size:12px;padding:6px 12px;flex:1;text-align:center;text-decoration:none}
  .a-open{background:var(--panel2);color:var(--accent);border:1px solid var(--border)}
  .a-learn{background:transparent;color:var(--muted);border:1px solid var(--border)}
  .a-learn.is-done{background:var(--done);color:#fff;border-color:var(--done)}
  .empty{text-align:center;color:var(--muted);padding:60px 0}
  .modal{position:fixed;inset:0;background:rgba(0,0,0,.7);display:none;align-items:center;justify-content:center;padding:20px;z-index:50}
  .modal.show{display:flex}
  .modal .box{background:var(--panel);border:1px solid var(--accent);border-radius:14px;padding:24px;max-width:440px;width:100%}
  .modal h2{font-size:14px;color:var(--gold);margin-bottom:10px}
  .modal .close{margin-top:16px;width:100%;background:var(--panel2);color:var(--text);border:1px solid var(--border)}
  footer{text-align:center;color:var(--muted);font-size:12px;margin-top:28px}
</style>
</head>
<body>
<header>
  <h1><span class="dot"></span>GitHub 学习雷达</h1>
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

<div class="toolbar">
  <input type="search" id="q" placeholder="🔍 搜索仓库名 / 描述 / 适合谁…">
  <select id="sort">
    <option value="stars">按 Star 排序</option>
    <option value="name">按名称排序</option>
    <option value="domain">按领域排序</option>
  </select>
  <button class="btn-primary" id="pick">🎲 今天学一个</button>
</div>
<div class="chips" id="chips"></div>
<div class="grid" id="grid"></div>
<div class="empty" id="empty" style="display:none">没有匹配的仓库</div>

<div class="modal" id="modal">
  <div class="box" id="modal-box"></div>
</div>

<footer>双击本文件即可离线打开 · 学习记录存于 localStorage</footer>

<script>
const DATA = __DATA__;
const LS_KEY = "learning-radar-done";
let done = new Set(JSON.parse(localStorage.getItem(LS_KEY) || "[]"));
let activeDomain = "全部";

const domains = ["全部", ...Array.from(new Set(DATA.map(r => r.domain)))];
const $ = id => document.getElementById(id);

function save(){ localStorage.setItem(LS_KEY, JSON.stringify([...done])); }
function starText(s){ return s >= 1 ? s + "k" : Math.round(s*1000); }

function toggleDone(name){
  if(done.has(name)) done.delete(name); else done.add(name);
  save(); render();
}

function renderChips(){
  $("chips").innerHTML = domains.map(d =>
    `<span class="chip ${d===activeDomain?'active':''}" data-d="${d}">${d}</span>`
  ).join("");
  document.querySelectorAll(".chip").forEach(c =>
    c.onclick = () => { activeDomain = c.dataset.d; render(); });
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

function cardHTML(r){
  const isDone = done.has(r.name);
  return `<div class="card ${isDone?'done':''}">
    <h3><a href="${r.url}" target="_blank">${r.name}</a></h3>
    <div class="meta">
      <span class="tag lang">${r.lang||'—'}</span>
      <span class="tag star">⭐ ${starText(r.stars)}</span>
      ${r.delta?`<span class="tag delta">${r.delta}</span>`:''}
      <span class="tag">${r.domain}</span>
    </div>
    <div class="field"><b>是什么：</b>${r.what}</div>
    <div class="field"><b>亮点：</b>${r.highlight}</div>
    <div class="field"><b>适合谁：</b>${r.forWho}</div>
    <div class="actions">
      <a class="a-open" href="${r.url}" target="_blank">打开仓库 →</a>
      <button class="a-learn ${isDone?'is-done':''}" data-n="${r.name.replace(/"/g,'&quot;')}">
        ${isDone?'✓ 已学':'标记已学'}</button>
    </div>
  </div>`;
}

function render(){
  const list = currentList();
  $("grid").innerHTML = list.map(cardHTML).join("");
  $("empty").style.display = list.length ? "none" : "block";
  document.querySelectorAll(".a-learn").forEach(b =>
    b.onclick = () => toggleDone(b.dataset.n));
  $("s-total").textContent = DATA.length;
  $("s-domain").textContent = domains.length - 1;
  $("s-done").textContent = done.size;
  const pct = DATA.length ? Math.round(done.size/DATA.length*100) : 0;
  $("p-text").textContent = pct + "%";
  $("p-bar").style.width = pct + "%";
}

function pickRandom(){
  const pool = DATA.filter(r => !done.has(r.name));
  const r = (pool.length ? pool : DATA)[Math.floor(Math.random()*(pool.length?pool.length:DATA.length))];
  $("modal-box").innerHTML = `<h2>🎲 今天学这个</h2>` + cardHTML(r) +
    `<button class="close" id="m-close">关闭</button>`;
  $("modal").classList.add("show");
  $("m-close").onclick = () => $("modal").classList.remove("show");
  $("modal-box").querySelectorAll(".a-learn").forEach(b =>
    b.onclick = () => { toggleDone(b.dataset.n); $("modal").classList.remove("show"); });
}

$("q").oninput = render;
$("sort").onchange = render;
$("pick").onclick = pickRandom;
$("modal").onclick = e => { if(e.target.id==="modal") $("modal").classList.remove("show"); };
renderChips(); render();
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
    print(f"已生成 {out_path}（{len(repos)} 个仓库）")


if __name__ == "__main__":
    main()
