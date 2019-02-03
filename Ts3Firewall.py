#!/usr/bin/python
# -*- coding: latin-1 -*-
# IpTables Firewall Teamspeak3 
# #Skype : Polatbay54@gmail.com
import os

# IPTABLEST KOMUTLARI

os.system('iptables -t filter -F')
os.system('iptables -t filter -X')
os.system('iptables -t filter -P INPUT DROP')
os.system('iptables -t filter -P FORWARD DROP')
os.system('iptables -t filter -P OUTPUT DROP')
os.system('iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT')
os.system('iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT')
os.system('iptables -t filter -A INPUT -i lo -j ACCEPT')
os.system('iptables -t filter -A OUTPUT -o lo -j ACCEPT')

# HACKER SAVAR CMD 

os.system('iptables -t filter -A INPUT -p icmp -j REJECT')
os.system('iptables -t filter -A OUTPUT -p icmp -j REJECT')



# DNS PORTLARI 

os.system('iptables -t filter -A OUTPUT -p tcp --dport 53 -j ACCEPT')
os.system('iptables -t filter -A OUTPUT -p udp --dport 53 -j ACCEPT')
os.system('iptables -t filter -A INPUT -p tcp --dport 53 -j ACCEPT')
os.system('iptables -t filter -A INPUT -p udp --dport 53 -j ACCEPT')



# NTP PORTLARI 

os.system('iptables -t filter -A OUTPUT -p udp --dport 53 -j ACCEPT')


# LIMIT SAVAR

os.system('iptables -A FORWARD -p tcp --syn -m limit --limit 1/second -j ACCEPT')
os.system('iptables -A FORWARD -p udp -m limit --limit 1/second -j ACCEPT')
os.system('iptables -A FORWARD -p icmp --icmp-type echo-request -m limit --limit 1/second -j ACCEPT')
os.system('iptables -A FORWARD -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s -j ACCEPT')
os.system('iptables -A INPUT -p tcp -m tcp --tcp-flags RST RST -m limit --limit 2/second --limit-burst 2 -j ACCEPT')



# GELEN DROPLARI ENGELLEME

os.system('iptables -A INPUT -m state --state INVALID -j DROP')
os.system('iptables -A FORWARD -m state --state INVALID -j DROP')
os.system('iptables -A OUTPUT -m state --state INVALID -j DROP')
os.system('iptables -A INPUT -p tcp -m tcp --tcp-flags RST RST -m limit --limit 2/second --limit-burst 2 -j ACCEPT')



# SCAN ATMA OC KOMUTU.
os.system('iptables -A INPUT   -m recent --name portscan --rcheck --seconds 86400 -j DROP')
os.system('iptables -A FORWARD -m recent --name portscan --rcheck --seconds 86400 -j DROP')

# 1 GUN BAN KALDIRMA 
os.system('iptables -A INPUT   -m recent --name portscan --remove')
os.system('iptables -A FORWARD -m recent --name portscan --remove')



# LOG EKLER ROOT MAIL KISMINA DUSER. 

os.system('iptables -A INPUT   -p tcp -m tcp --dport 139 -m recent --name portscan --set -j LOG --log-prefix "Portscan:"')
os.system('iptables -A INPUT   -p tcp -m tcp --dport 139 -m recent --name portscan --set -j DROP')
os.system('iptables -A FORWARD -p tcp -m tcp --dport 139 -m recent --name portscan --set -j LOG --log-prefix "Portscan:"')
os.system('iptables -A FORWARD -p tcp -m tcp --dport 139 -m recent --name portscan --set -j DROP')



# DROP SAVAR V1

os.system('iptables -A INPUT -m state --state INVALID -j DROP')
os.system('iptables -A FORWARD -m state --state INVALID -j DROP')
os.system('iptables -A OUTPUT -m state --state INVALID -j DROP')


# V1.1

os.system('iptables -A INPUT -p tcp --syn -m limit --limit 2/s --limit-burst 30 -j ACCEPT')
os.system('iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s -j ACCEPT')
os.system('iptables -A INPUT -p tcp --tcp-flags ALL NONE -m limit --limit 1/h -j ACCEPT')
os.system('iptables -A INPUT -p tcp --tcp-flags ALL ALL -m limit --limit 1/h -j ACCEPT')


# TS APPS

os.system('iptables -t filter -A OUTPUT -p tcp --dport 41144 -j ACCEPT')
os.system('iptables -t filter -A INPUT -p tcp --dport 41144 -j ACCEPT')



# BILDIGINIZ UZERE 10011 PORTUNA KORUMA EKLEDIK ANAIZI SKERIM EXPLOIT ATMAYIN


os.system('iptables -t filter -A OUTPUT -p tcp --dport 10011-j ACCEPT')
os.system('iptables -t filter -A INPUT -p tcp --dport 10011 -j ACCEPT')
os.system('iptables -t filter -A OUTPUT -p tcp --dport 30033 -j ACCEPT')
os.system('iptables -t filter -A INPUT -p tcp --dport 30033 -j ACCEPT')




# TS3 PORTLARI

os.system('iptables -t filter -A OUTPUT -p udp --dport 9987 -j ACCEPT')
os.system('iptables -t filter -A INPUT -p udp --dport 9987 -j ACCEPT')

print (''' \033[93mTeampseak3 \033[93mIptablest\033[93m Firewall \033[92mSuccessful!  
      \033[90mCode : POLATBEY
     \033[94mForum : SpyHackerz.Com
    \033[97mGithub : Github.com/Polatbey/
   \033[91mYoutube : Youtube.com/POLATBEY/
   \033[96mTwitter : Twitter.com/p0latbey''')

