import{u as c}from"./framework.1eb289b4.js";function i(){const{theme:r}=c(),{sidebar:t}=r.value,e=[];return Object.keys(t).forEach(s=>{for(const a of t[s])a.items.forEach(o=>e.push({...o,parentLink:s,parentText:a.text,tags:o.tags}))}),e}export{i as u};
