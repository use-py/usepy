import{_ as a,o as l,c as n,M as o}from"./chunks/framework.1eb289b4.js";const D=JSON.parse('{"title":"shuffle","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"api/list/shuffle.md","filePath":"api/list/shuffle.md","lastUpdated":1728486692000}'),p={name:"api/list/shuffle.md"};function e(t,s,r,c,y,i){return l(),n("div",null,s[0]||(s[0]=[o(`<h1 id="shuffle" tabindex="-1">shuffle <a class="header-anchor" href="#shuffle" aria-label="Permalink to &quot;shuffle&quot;">​</a></h1><p>随机打乱列表中的元素顺序。</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> shuffle</span></span></code></pre></div><h3 id="参数" tabindex="-1">参数 <a class="header-anchor" href="#参数" aria-label="Permalink to &quot;参数&quot;">​</a></h3><ul><li><code>lst</code>: 要打乱的列表</li></ul><h3 id="例子" tabindex="-1">例子 <a class="header-anchor" href="#例子" aria-label="Permalink to &quot;例子&quot;">​</a></h3><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> lst </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> </span><span style="color:#666666;">[</span><span style="color:#4C9A91;">1</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">3</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">4</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">5</span><span style="color:#666666;">]</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> shuffle</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">lst</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> lst</span></span>
<span class="line"><span style="color:#666666;">[</span><span style="color:#4C9A91;">3</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">1</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">4</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">5</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span><span style="color:#666666;">]</span><span style="color:#DBD7CAEE;">  </span><span style="color:#758575DD;"># 结果可能会不同，因为是随机打乱</span></span></code></pre></div>`,7)]))}const f=a(p,[["render",e]]);export{D as __pageData,f as default};