import{_ as s,o as n,c as a,R as l}from"./chunks/framework.4314545f.js";const d=JSON.parse('{"title":"","description":"","frontmatter":{"outline":"deep"},"headers":[],"relativePath":"decorator/listify.md","filePath":"decorator/listify.md","lastUpdated":1677473775000}'),p={name:"decorator/listify.md"},o=l(`<div class="info custom-block"><p class="custom-block-title">INFO</p><pre><code>@Author: MicLon
@Date: 2023/02/27
@Description: 将函数的返回值转换为列表
</code></pre></div><h2 id="使用" tabindex="-1">使用 <a class="header-anchor" href="#使用" aria-label="Permalink to &quot;使用&quot;">​</a></h2><p><code>@useListify</code>将函数的返回值转换为列表。</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#666666;">@</span><span style="color:#80A665;">useDecorator</span><span style="color:#666666;">.</span><span style="color:#80A665;">listify</span><span style="color:#666666;">()</span></span>
<span class="line"><span style="color:#CB7676;">def</span><span style="color:#DBD7CAEE;"> </span><span style="color:#80A665;">listify</span><span style="color:#666666;">():</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">1</span></span>
<span class="line"></span>
<span class="line"></span>
<span class="line"><span style="color:#666666;">@</span><span style="color:#80A665;">useDecorator</span><span style="color:#666666;">.</span><span style="color:#80A665;">listify</span><span style="color:#666666;">(</span><span style="color:#BD976A;">collection</span><span style="color:#CB7676;">=</span><span style="color:#B8A965;">set</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">def</span><span style="color:#DBD7CAEE;"> </span><span style="color:#80A665;">listify2</span><span style="color:#666666;">():</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">1</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span></span>
<span class="line"></span>
<span class="line"></span>
<span class="line"><span style="color:#666666;">@</span><span style="color:#80A665;">useDecorator</span><span style="color:#666666;">.</span><span style="color:#80A665;">listify</span><span style="color:#666666;">(</span><span style="color:#BD976A;">collection</span><span style="color:#CB7676;">=</span><span style="color:#B8A965;">dict</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">def</span><span style="color:#DBD7CAEE;"> </span><span style="color:#80A665;">listify3</span><span style="color:#666666;">():</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">1</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">3</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">yield</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">2</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#4C9A91;">4</span></span>
<span class="line"></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">listify</span><span style="color:#666666;">()</span><span style="color:#DBD7CAEE;">  </span><span style="color:#758575DD;"># [1]</span></span>
<span class="line"><span style="color:#DBD7CAEE;">listify2</span><span style="color:#666666;">()</span><span style="color:#DBD7CAEE;">  </span><span style="color:#758575DD;"># {1, 2}</span></span>
<span class="line"><span style="color:#DBD7CAEE;">listify3</span><span style="color:#666666;">()</span><span style="color:#DBD7CAEE;">  </span><span style="color:#758575DD;"># {1: 2, 2: 3}</span></span></code></pre></div>`,4),e=[o];function t(c,r,y,i,D,E){return n(),a("div",null,e)}const C=s(p,[["render",t]]);export{d as __pageData,C as default};
