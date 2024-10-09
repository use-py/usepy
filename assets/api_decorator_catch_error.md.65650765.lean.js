import{_ as a,o as n,c as o,M as l}from"./chunks/framework.1eb289b4.js";const d=JSON.parse('{"title":"catch_error","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"api/decorator/catch_error.md","filePath":"api/decorator/catch_error.md","lastUpdated":1728486692000}'),p={name:"api/decorator/catch_error.md"};function e(t,s,r,c,y,i){return n(),o("div",null,s[0]||(s[0]=[l(`<h1 id="catch-error" tabindex="-1">catch_error <a class="header-anchor" href="#catch-error" aria-label="Permalink to &quot;catch_error&quot;">​</a></h1><p>捕获函数执行过程中的错误并返回指定值</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> catch_error</span></span></code></pre></div><h3 id="参数" tabindex="-1">参数 <a class="header-anchor" href="#参数" aria-label="Permalink to &quot;参数&quot;">​</a></h3><ul><li><code>return_val</code>: 发生异常时返回的值（可选）</li></ul><h3 id="例子" tabindex="-1">例子 <a class="header-anchor" href="#例子" aria-label="Permalink to &quot;例子&quot;">​</a></h3><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> logging</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> logging</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">basicConfig</span><span style="color:#666666;">(</span><span style="color:#BD976A;">level</span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;">logging</span><span style="color:#666666;">.</span><span style="color:#C99076;">DEBUG</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> </span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> </span><span style="color:#CB7676;">@</span><span style="color:#DBD7CAEE;">catch_error</span><span style="color:#666666;">(</span><span style="color:#BD976A;">return_val</span><span style="color:#666666;">=</span><span style="color:#4C9A91;">0</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#C99076;">...</span><span style="color:#DBD7CAEE;"> </span><span style="color:#CB7676;">def</span><span style="color:#DBD7CAEE;"> </span><span style="color:#80A665;">divide</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">a</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> b</span><span style="color:#666666;">):</span></span>
<span class="line"><span style="color:#C99076;">...</span><span style="color:#DBD7CAEE;">     </span><span style="color:#4D9375;">return</span><span style="color:#DBD7CAEE;"> a </span><span style="color:#CB7676;">/</span><span style="color:#DBD7CAEE;"> b</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> </span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> divide</span><span style="color:#666666;">(</span><span style="color:#4C9A91;">10</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#4C9A91;">5.0</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> divide</span><span style="color:#666666;">(</span><span style="color:#4C9A91;">10</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">0</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#4C9A91;">0</span></span></code></pre></div>`,7)]))}const C=a(p,[["render",e]]);export{d as __pageData,C as default};