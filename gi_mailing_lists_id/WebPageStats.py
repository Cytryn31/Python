'''
Created on Nov 1, 2013

@author: Edoardo Foco
'''

class AddressStats(object):
    
    web_address = ''
    news_count='' 
    sub_count='' 
    mailing_list_count=''
    maillist_count = ''
    news_sub_count='' 
    mailing_list_sub_count=''

    def __init__(self, web_address, news_count, sub_count, 
                 mailing_list_count, maillist_count, 
                 news_sub_count, mailing_list_sub_count):
        
        self.web_address=web_address
        self.news_count=news_count 
        self.sub_count=sub_count 
        self.mailing_list_count=mailing_list_count
        self.maillist_count = maillist_count
        self.news_sub_count=news_sub_count
        self.mailing_list_sub_count=mailing_list_sub_count
        
   
        
        
        

        