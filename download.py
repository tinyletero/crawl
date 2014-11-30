#!/usr/bin/python
# -*- coding:utf-8 -*-
#
#
import sys
import os
import re
import urllib2

reg_dict = {
             #'download':r'href=("|\')(?P<url>http://download\.[\w\._/-?]+)("|\')',
             'download':r'href=("|\')(?P<url>http://download\..+.pdf)("|\')\s*>',
             'src':r'href=("|\')(?P<src>http://[\w\._/-]+)("|\')'
            }

def url_get(url):
    '''
    读取网页
    '''
    print '-----begin parse url---------'
    try:
        respone =  urllib2.urlopen(url)
        html = respone.read()
    except Exception ,e:
        print e
        return None
    print '----end parse url-----------'
    return html

def read_html(html,reg):
    '''
    根据规则提取url中链接
    '''
    print '-----begin read html---------'
    #print html
    print reg
    reg = re.compile(reg)
    url_temp = re.findall(reg,html)
    #print url
    try:
        fd = open('url.log','w+')
    except Exception,e:
        print e
        fd = None
    if url_temp:
        print len(url_temp)
        for url in url_temp:
            try:
                if fd:
                    cmd = 'wget ' + str(url[1])
                    print cmd
                    os.system(cmd)
                    fd.write(str(url[1])+'\n')
            except Exception,e:
                print e
                continue
    else:
        print 'kong'

    fd.close()
def run():
    global reg_dict
    html = url_get(sys.argv[1])
    if not html:
        print '解析出错'
        sys.exit(0)
    read_html(html,reg_dict['download']) 
    #read_html(html,reg_dict['src']) 
    

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "usage python download.py url"
        sys.exit(0)
    #print url_get(sys.argv[1])
    run()
    print 'ok'
