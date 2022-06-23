# coding=utf-8
# @Time : 2022/6/22 16:52 
# @Author : hh
# @File : js2py.py 
# @Software: PyCharm

import  js2py
# this use 0.71
'''
# usage

#i want get:
<div class="social-meta">
    <a href="mailto:mbillingslea@hudson.org" class="social-item email">Email</a>            </div>

#but cawl this:
<div class="social-meta">
   <a href="/cdn-cgi/l/email-protection#28454a41444441464f5b444d4968405d4c5b474606475a4f" class="social-item email">Email</a>              
</div>

# js encry
!function(){"use strict";function e(e){try{if("undefined"==typeof console)return;"error"in console?console.error(e):console.log(e)}catch(e){}}function t(e){return d.innerHTML='<a href="'+e.replace(/"/g,"&quot;")+'"></a>',d.childNodes[0].getAttribute("href")||""}function r(e,t){var r=e.substr(t,2);return parseInt(r,16)}function n(n,c){for(var o="",a=r(n,c),i=c+2;i<n.length;i+=2){var l=r(n,i)^a;o+=String.fromCharCode(l)}try{o=decodeURIComponent(escape(o))}catch(u){e(u)}return t(o)}function c(t){for(var r=t.querySelectorAll("a"),c=0;c<r.length;c++)try{var o=r[c],a=o.href.indexOf(l);a>-1&&(o.href="mailto:"+n(o.href,a+l.length))}catch(i){e(i)}}function o(t){for(var r=t.querySelectorAll(u),c=0;c<r.length;c++)try{var o=r[c],a=o.parentNode,i=o.getAttribute(f);if(i){var l=n(i,0),d=document.createTextNode(l);a.replaceChild(d,o)}}catch(h){e(h)}}function a(t){for(var r=t.querySelectorAll("template"),n=0;n<r.length;n++)try{i(r[n].content)}catch(c){e(c)}}function i(t){try{c(t),o(t),a(t)}catch(r){e(r)}}var l="/cdn-cgi/l/email-protection#",u=".__cf_email__",f="data-cfemail",d=document.createElement("div");i(document),function(){var e=document.currentScript||document.scripts[document.scripts.length-1];e.parentNode.removeChild(e)}()}();
'''

# end
js = '''
function fn(n){
    var a = parseInt(n.substr(0,2), 16)
    for(var o="",i=0+2;i<n.length;i+=2){
        var l = parseInt(n.substr(i,2), 16)^a
        o+=String.fromCharCode(l)
    }
    return o
}
'''
r = js2py.eval_js(js)
print(r('5633243f3534163e233225393878392431'))
# ericb@hudson.org