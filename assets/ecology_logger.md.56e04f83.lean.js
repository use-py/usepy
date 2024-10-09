import{_ as a,o as n,c as o,M as l}from"./chunks/framework.1eb289b4.js";const d=JSON.parse('{"title":"usepy-plugin-logger","description":"","frontmatter":{"title":"usepy-plugin-logger","outline":"deep"},"headers":[],"relativePath":"ecology/logger.md","filePath":"ecology/logger.md","lastUpdated":1728486692000}'),p={name:"ecology/logger.md"};function e(t,s,c,r,y,D){return n(),o("div",null,s[0]||(s[0]=[l(`<h1 id="usepy-plugin-logger" tabindex="-1">usepy-plugin-logger <a class="header-anchor" href="#usepy-plugin-logger" aria-label="Permalink to &quot;usepy-plugin-logger&quot;">​</a></h1><div class="vp-code-group"><div class="tabs"><input type="radio" name="group-7O0f8" id="tab--kOVnLq" checked="checked"><label for="tab--kOVnLq">pip</label><input type="radio" name="group-7O0f8" id="tab--rG0eOS"><label for="tab--rG0eOS">poetry</label></div><div class="blocks"><div class="language-bash active"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#80A665;">pip</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D;">install</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">usepy[logger]</span><span style="color:#C98A7D99;">&quot;</span></span></code></pre></div><div class="language-bash"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#80A665;">poetry</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D;">add</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">usepy[logger]</span><span style="color:#C98A7D99;">&quot;</span></span></code></pre></div></div></div><p><code>loguru</code>是一个十分优秀的日志库，但是大部分第三方库都是使用<code>logging</code>模块来进行日志记录的，当项目中同时使用了<code>loguru</code>和<code>logging</code>时，会导致日志记录混乱。</p><p><code>useLogger</code>就是为了解决这个问题而生的，它可以将<code>logging</code>模块的日志记录转换为<code>loguru</code>的日志记录。并且能够统一格式输出。</p><p>当你在<strong>项目入口处</strong>使用<code>useLogger</code>后，你可以在任何地方使用<code>logging</code>/<code>loguru</code>模块来进行日志记录，它们统统会被无感转换为<code>loguru</code>的日志记录。</p><h2 id="使用" tabindex="-1">使用 <a class="header-anchor" href="#使用" aria-label="Permalink to &quot;使用&quot;">​</a></h2><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> useLogger</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">useLogger</span><span style="color:#666666;">()</span><span style="color:#DBD7CAEE;"> </span><span style="color:#758575DD;"># 使用默认配置</span></span></code></pre></div><p>如果你自身项目正在使用<code>loguru</code>，这一切似乎感觉毫无变化。因为默认的配置只是修改了一点输出样式。</p><p>如果想要感受它带来的“魔法”，需要稍微配置一下。</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> useLogger</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">useLogger</span><span style="color:#666666;">(</span><span style="color:#BD976A;">packages</span><span style="color:#666666;">=[</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">scrapy</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">django</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">usepy</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">])</span></span></code></pre></div><p>如果你在使用如<code>scrapy</code>/<code>django</code>等第三方库时，你会发现它们的日志记录也被统一了。</p><p>晚一些时候，这里会提供演示。</p><h2 id="logstash-filebeat" tabindex="-1">Logstash/Filebeat <a class="header-anchor" href="#logstash-filebeat" aria-label="Permalink to &quot;Logstash/Filebeat&quot;">​</a></h2><p>日志的更重要能力是将日志记录发送到<code>Logstash</code>/<code>Filebeat</code>，这样就可以将日志记录存储到<code>Elasticsearch</code>中，方便进行日志分析。所以统一日志的最终输出格式是非常重要的。</p><p><code>useLogger</code>内置一个<code>logstash_handler</code>统一化输出格式。</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark has-highlighted-lines"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> useTimeIt</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> useLogger</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> logstash_handler</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">useLogger</span><span style="color:#666666;">(</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">handlers</span><span style="color:#666666;">=[</span></span>
<span class="line"><span style="color:#DBD7CAEE;">        logstash_handler</span><span style="color:#666666;">(</span><span style="color:#BD976A;">level</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">DEBUG</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#BD976A;">extra</span><span style="color:#666666;">={</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">app_name</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">:</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">spider</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">})</span></span>
<span class="line highlighted"><span style="color:#DBD7CAEE;">    </span><span style="color:#666666;">],</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">packages</span><span style="color:#666666;">=[</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">usepy</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">],</span><span style="color:#DBD7CAEE;">  </span><span style="color:#758575DD;"># hook拦截 usepy 的日志</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">extra</span><span style="color:#666666;">={</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">project_name</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">:</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">usepy</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">}</span></span>
<span class="line"><span style="color:#666666;">)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">logger</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">warning</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">test warning</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#DBD7CAEE;">logger</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">info</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">test info</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#DBD7CAEE;">logger</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">debug</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">test debug</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#758575DD;"># 这里测试调用函数的耗时，这是一个在usepy包中的函数</span></span>
<span class="line"><span style="color:#DBD7CAEE;">useTimeIt</span><span style="color:#666666;">(</span><span style="color:#CB7676;">lambda</span><span style="color:#666666;">:</span><span style="color:#DBD7CAEE;"> logger</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">debug</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">start run test function</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">))()</span></span></code></pre></div><p>运行结果：</p><p><img src="https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230228222300.png" alt=""></p><p>有了以上输出，如果你使用过类似<code>filebeat</code>的工具，你就可以通过它自动收集docker的日志产物，发往<code>elasticsearch</code>中，方便进行日志分析。</p><h2 id="另类模块" tabindex="-1">另类模块 <a class="header-anchor" href="#另类模块" aria-label="Permalink to &quot;另类模块&quot;">​</a></h2><h3 id="uvicorn" tabindex="-1">uvicorn <a class="header-anchor" href="#uvicorn" aria-label="Permalink to &quot;uvicorn&quot;">​</a></h3><p><code>uvicorn</code>是一个非常优秀的<code>ASGI</code>服务器。它是<code>fastapi</code>的最佳拍档。它的日志拦截稍微特殊，我们将它单独拿出来。</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#758575DD;"># app.py</span></span>
<span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> fastapi </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> FastAPI</span></span>
<span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> useLoggerInterceptUvicorn</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">useLoggerInterceptUvicorn</span><span style="color:#666666;">()</span><span style="color:#DBD7CAEE;">  </span><span style="color:#758575DD;"># 在 app 实例化前调用即可</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">app </span><span style="color:#666666;">=</span><span style="color:#DBD7CAEE;"> FastAPI</span><span style="color:#666666;">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#666666;">@</span><span style="color:#80A665;">app</span><span style="color:#666666;">.</span><span style="color:#80A665;">get</span><span style="color:#666666;">(</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">/</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">)</span></span>
<span class="line"><span style="color:#CB7676;">def</span><span style="color:#DBD7CAEE;"> </span><span style="color:#80A665;">home</span><span style="color:#666666;">():</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#4D9375;">return</span><span style="color:#DBD7CAEE;"> </span><span style="color:#666666;">{</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">message</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">:</span><span style="color:#DBD7CAEE;"> </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">hello</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">}</span></span></code></pre></div><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#758575DD;"># main.py</span></span>
<span class="line"><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> uvicorn</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">uvicorn</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">run</span><span style="color:#666666;">(</span><span style="color:#BD976A;">app</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">app:app</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span><span style="color:#DBD7CAEE;"> </span><span style="color:#BD976A;">host</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">127.0.0.1</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">)</span></span></code></pre></div><p><img src="https://miclon-job.oss-cn-hangzhou.aliyuncs.com/img/20230228223646.png" alt=""></p><h2 id="兼容性" tabindex="-1">兼容性 <a class="header-anchor" href="#兼容性" aria-label="Permalink to &quot;兼容性&quot;">​</a></h2><p><code>useLogger</code>兼容<code>loguru</code>和<code>logging</code>模块，你可以在任何地方使用它们来进行日志记录。</p><p>当你需要其他handler时，可以使用<code>loguru</code>的<code>add</code>方法来添加。</p><div class="language-python"><button title="Copy Code" class="copy"></button><span class="lang">python</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> loguru </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> logger</span></span>
<span class="line"><span style="color:#4D9375;">from</span><span style="color:#DBD7CAEE;"> usepy </span><span style="color:#4D9375;">import</span><span style="color:#DBD7CAEE;"> useLogger</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">useLogger</span><span style="color:#666666;">()</span></span>
<span class="line"></span>
<span class="line"><span style="color:#DBD7CAEE;">logger</span><span style="color:#666666;">.</span><span style="color:#DBD7CAEE;">add</span><span style="color:#666666;">(</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">file_</span><span style="color:#C99076;">{time}</span><span style="color:#C98A7D;">.log</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">rotation</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">00:00</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">retention</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">10 days</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">enqueue</span><span style="color:#666666;">=</span><span style="color:#4D9375;">True</span><span style="color:#666666;">,</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">encoding</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">utf-8</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span></span>
<span class="line"><span style="color:#DBD7CAEE;">    </span><span style="color:#BD976A;">level</span><span style="color:#666666;">=</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#C98A7D;">DEBUG</span><span style="color:#C98A7D99;">&quot;</span><span style="color:#666666;">,</span></span>
<span class="line"><span style="color:#666666;">)</span></span></code></pre></div><div class="language-text"><button title="Copy Code" class="copy"></button><span class="lang">text</span><pre class="shiki vitesse-dark"><code><span class="line"><span style="color:#dbd7caee;"># file_2023-02-28_22-26-56_570490.log</span></span>
<span class="line"><span style="color:#dbd7caee;">2023-02-28 22:26:56.590 | WARNING  | __main__:&lt;module&gt;:50 - test warning</span></span>
<span class="line"><span style="color:#dbd7caee;">2023-02-28 22:26:56.593 | INFO     | __main__:&lt;module&gt;:51 - test info</span></span>
<span class="line"><span style="color:#dbd7caee;">2023-02-28 22:26:56.593 | DEBUG    | __main__:&lt;module&gt;:52 - test debug</span></span>
<span class="line"><span style="color:#dbd7caee;">2023-02-28 22:26:56.593 | DEBUG    | __main__:&lt;lambda&gt;:53 - start run test function</span></span>
<span class="line"><span style="color:#dbd7caee;">2023-02-28 22:26:56.594 | DEBUG    | usepy.decorator.timeit:_timer:18 - &lt;lambda&gt; took 0 seconds</span></span></code></pre></div>`,30)]))}const u=a(p,[["render",e]]);export{d as __pageData,u as default};
