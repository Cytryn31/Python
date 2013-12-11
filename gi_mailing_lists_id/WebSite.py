'''
Created on Nov 1, 2013

WebSite.py
Scope: Return websites that may contain mailing lists or newsletters

Variables:
    -rootdir - is the path to the website pages
    -stats_for_complete_website - array that holds the statistics of each page
    -has_mailinglist - dictionary containing {interesting: bool , address: path of website}
    
@author: Edoardo Foco
'''

import os
import sys
import re
import WebPageStats


def analyse_website(path):
    rootdir= path
    
    #data structures
    dirs=[]
    stats_for_complete_website=[] #holds stats for each page being analyzed
    has_mailinglist = {}          #is the final dictionary that is returned
    file_list = ''
    
    # get list of files in directory
    for file in os.walk(rootdir):
        file_list = file[2]
    
    #create list of files for a website
    for address in file_list:
        dir = str(rootdir+'/'+address)
        dirs.append(dir)
    
    
    
    #for each file   
    for file in dirs:
        
        page = open(file)
        text = page.read()
        page.close()
        lower_text = text.lower()
        
        #looking for newsletter
        news_occ = re.findall('newsletter', lower_text) 
        news_count = len(news_occ)
        
        #looking for subscription
        sub_occ = re.findall('subscription', lower_text) 
        sub_count = len(sub_occ)
        
        #looking for mail list
        maillist_occ = re.findall('mail\s*list', lower_text) 
        maillist_count = len(maillist_occ)
        
        #looking for mailing list
        mailing_list_occ = re.findall('mailing\s*list', lower_text) 
        mailing_list_count = len(mailing_list_occ)
        
        #looking for newsletter subscription
        news_sub_occ = re.findall('newsletter\s*subscription', lower_text)  
        news_sub_count = len(news_sub_occ)
        
        #looking for mailing list subscription
        mailing_list_sub_occ = re.findall('mailing\s*list\s*subscription', lower_text)
        mailing_list_sub_count = len(mailing_list_sub_occ) 
        
        
        #inserting webpagestats into complete website sites array
        stats = WebPageStats.AddressStats(file, news_count, sub_count, 
                     mailing_list_count, maillist_count, 
                     news_sub_count, mailing_list_sub_count)
    
        stats_for_complete_website.append(stats)
    
    # calculating totals
    final_results={}
    total_news_count=0
    total_sub_count=0
    total_mailing_list_count=0
    total_maillist_count=0
    total_news_sub_count=0
    total_mailing_list_sub_count=0
    
    for stats in stats_for_complete_website:
        total_news_count += stats.news_count
        total_sub_count += stats.sub_count
        total_mailing_list_count += stats.mailing_list_count
        total_maillist_count += stats.maillist_count
        total_news_sub_count+= stats.news_sub_count
        total_mailing_list_sub_count += stats.mailing_list_sub_count
       
    
    final_results['total_news_count']= total_news_count
    final_results['total_sub_count']= total_sub_count
    final_results['total_mailing_list_count']=total_mailing_list_count
    final_results['total_maillist_count']= total_mailing_list_count
    final_results['total_news_sub_count']=total_news_sub_count
    final_results['total_mailing_list_sub_count']= total_mailing_list_sub_count
   
    # final results
    identified = False
    values = final_results.values()
    for x in values:
        #threshold
        if x > 2:
            identified= True
    
    
    has_mailinglist['address']=rootdir
    has_mailinglist['interesting'] = identified
    
    return has_mailinglist 
        

