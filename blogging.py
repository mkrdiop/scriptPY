#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:35:04 2019

@author: makhtardiop
"""

from oauth2client.client import flow_from_clientsecrets
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
import webbrowser

def get_credentials():
    scope = 'https://www.googleapis.com/auth/blogger'
    flow = flow_from_clientsecrets(
        '/Users/makhtardiop/client_secret_61.json', scope,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    storage = Storage('credentials.dat')
    credentials = storage.get()

    if  not credentials or credentials.invalid:
        auth_uri = flow.step1_get_authorize_url()
        webbrowser.open(auth_uri)
        auth_code = input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)
        storage.put(credentials)
    return credentials

def get_service():
    """Returns an authorised blogger api service."""
    credentials = get_credentials()
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('blogger', 'v3', http=http)
    return service

if __name__ == '__main__':
    body = {
        "kind": "blogger#post",
        "id": "4042989347074748096",
        "title": "TEST POST TEST POST",
        "content":"""<div>hello world test</div>
                     <div>
                     <span style="color: black; font-family: &quot;menlo&quot;; font-size: 11pt;">You can find a good article about this subject</span> 
                     <a href="http://www.adsmuze.com/how-to-do-actionnable-keyword-research-in-2019-for-maximum-traffic/" style="color: black; font-family: &quot;menlo&quot;; font-size: 11pt;">here</a>
                     </div>"""
        }
    
    served = get_service()
    blogs = served.blogs()
    
    blog_get_obj=blogs.get(blogId='4042989347074748096')
    details = blog_get_obj.execute()
    print (details)
    
    posts = served.posts()
    posts.insert(blogId='4042989347074748096', body=body, isDraft=False).execute()