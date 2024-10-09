import{_ as a,o as n,c as l,M as o}from"./chunks/framework.1eb289b4.js";const C=JSON.parse('{"title":"singleton","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"api/decorator/singleton.md","filePath":"api/decorator/singleton.md","lastUpdated":1728486692000}'),p={name:"api/decorator/singleton.md"};function e(t,s,c,r,y,i){return n(),l("div",null,s[0]||(s[0]=[o(`<h1 id="singleton" tabindex="-1">singleton <a class="header-anchor" href="#singleton" aria-label="Permalink to &quot;singleton&quot;">​</a></h1><p>实现单例模式的装饰器</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> singleton</span></span></code></pre></div><h3 id="例子" tabindex="-1">例子 <a class="header-anchor" href="#例子" aria-label="Permalink to &quot;例子&quot;">​</a></h3><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> </span><span style="color:#CB7676;">@</span><span style="color:#DBD7CAEE;">singleton</span></span>
<span class="line"><span style="color:#C99076;">...</span><span style="color:#DBD7CAEE;"> </span><span style="color:#CB7676;">class</span><span style="color:#DBD7CAEE;"> </span><span style="color:#5DA994;">MyClass</span><span style="color:#666666;">:</span></span>
<span class="line"><span style="color:#C99076;">...</span><span style="color:#DBD7CAEE;">     </span><span style="color:#CB7676;">def</span><span style="color:#DBD7CAEE;"> </span><span style="color:#B8A965;">__init__</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">self</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> value</span><span style="color:#666666;">):</span></span>
<span class="line"><span style="color:#C99076;">...</span><span style="color:#DBD7CAEE;">         </span><span style="color:#C99076;">self</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">value </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> value</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> </span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> instance1 </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> MyClass</span><span style="color:#666666;">(</span><span style="color:#4C9A91;">42</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> instance2 </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> MyClass</span><span style="color:#666666;">(</span><span style="color:#4C9A91;">24</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> instance1</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">value</span></span>
<span class="line"><span style="color:#4C9A91;">42</span></span>
<span class="line"><span style="color:#CB7676;">&gt;&gt;&gt;</span><span style="color:#DBD7CAEE;"> instance1 </span><span style="color:#CB7676;">is</span><span style="color:#DBD7CAEE;"> instance2</span></span>
<span class="line"><span style="color:#4D9375;">True</span></span></code></pre></div>`,5)]))}const E=a(p,[["render",e]]);export{C as __pageData,E as default};
