import{_ as a,o as n,c as l,M as o}from"./chunks/framework.1eb289b4.js";const A=JSON.parse('{"title":"","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"utils/bloom_filter.md","filePath":"utils/bloom_filter.md","lastUpdated":1677464985000}'),p={name:"utils/bloom_filter.md"};function e(t,s,r,c,y,D){return n(),l("div",null,s[0]||(s[0]=[o(`<div class="info custom-block"><p class="custom-block-title">INFO</p><pre><code>@Author: MicLon
@Date: 2023/02/25
@Description: 布隆过滤器
</code></pre></div><h2 id="介绍" tabindex="-1">介绍 <a class="header-anchor" href="#介绍" aria-label="Permalink to &quot;介绍&quot;">​</a></h2><p>布隆过滤器是一种空间效率很高的随机数据结构，它可以用来告诉你，一个元素是否在一个集合中。它的优点是空间效率和查询时间都远远超过一般的算法，缺点是有一定的误识别率和删除困难。</p><p>参考：<a href="https://www.cnblogs.com/cpselvis/p/6265825.html" target="_blank" rel="noreferrer">布隆过滤器</a></p><h2 id="使用" tabindex="-1">使用 <a class="header-anchor" href="#使用" aria-label="Permalink to &quot;使用&quot;">​</a></h2><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark has-highlighted-lines"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> redis </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> Redis</span></span>
<span class="line highlighted"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> useBloomFilter</span></span>
<span class="line"></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">rds </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> Redis</span><span style="color:#666666;">(</span><span style="color:#BD976A;">host</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#C98A7D;">localhost</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#BD976A;">port</span><span style="color:#666666;">=</span><span style="color:#4C9A91;">6379</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#BD976A;">db</span><span style="color:#666666;">=</span><span style="color:#4C9A91;">0</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#DBD7CAEE;">bf </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> useBloomFilter</span><span style="color:#666666;">(</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">client</span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;">rds</span></span>
<span class="line"><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#DBD7CAEE;">bf</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">add</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#C98A7D;">hello</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#DBD7CAEE;">bf</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">add</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#C98A7D;">world</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#B8A965;">print</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">bf</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">exists</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#C98A7D;">hello</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#666666;">))</span><span style="color:#DBD7CAEE;"> </span><span style="color:#758575DD;"># True</span></span>
<span class="line"><span style="color:#B8A965;">print</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">bf</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">exists</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#C98A7D;">world</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#666666;">))</span><span style="color:#DBD7CAEE;"> </span><span style="color:#758575DD;"># True</span></span>
<span class="line"><span style="color:#B8A965;">print</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">bf</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">exists</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#C98A7D;">python</span><span style="color:#C98A7D99;">&#39;</span><span style="color:#666666;">))</span><span style="color:#DBD7CAEE;"> </span><span style="color:#758575DD;"># False</span></span>
<span class="line"><span style="color:#B8A965;">print</span><span style="color:#666666;">(</span><span style="color:#DBD7CAEE;">bf</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">exists</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&#39;&#39;</span><span style="color:#666666;">))</span><span style="color:#DBD7CAEE;"> </span><span style="color:#758575DD;"># False</span></span></code></pre></div>`,6)]))}const E=a(p,[["render",e]]);export{A as __pageData,E as default};