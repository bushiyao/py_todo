# coding=utf-8
# @Time : 2022/6/22 16:52 
# @Author : hh
# @File : js2py.py 
# @Software: PyCharm

import  js2py
# this use 0.71

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