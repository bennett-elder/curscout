#!/usr/bin/env python
# This will compile a list of access points users nearby have sent probe requests out for
# and display a count of how many times a particular AP has been asked for
# Useful for client-side security testing
 
from scapy.all import *
import curses
 
def callback(pkt):
  if Dot11ProbeReq in pkt:
    ssid = pkt.sprintf("%Dot11ProbeReq.info%")
    s.clear()
    s.move(0,0)
    ssid=str(ssid)
    if len(ssid) == 0:
      return #return #temp = ''
    elif len(ssid) > 45:
      return
    elif "\n" in ssid:
      return
    else:
      s.refresh()
      if ssid in d:
    d[ssid] = d[ssid]+1
      else:
    d[ssid] = 1
      counter=5
      for key, value in d.iteritems():
    s.addstr(counter,15,str(value).rjust(6) + " " + str(key),curses.A_BOLD)
    counter=counter+1
      s.addstr(2,15,"Press Ctrl-Z to stop",curses.A_REVERSE)
      s.refresh()
      return
    #return str(len(ssid)) + '  ' + ssid
      #return temp
 
print("test")
global s
global d
d = {}
s=curses.initscr()
#curses.start_color()
curses.noecho()
curses.cbreak()
s.keypad(1)
 
try:
  while 1:
    sniff(iface="mon0",prn=callback, store=0)#, count=1)
except:
  curses.nocbreak()
  s.keypad(0)
  curses.echo()
  curses.endwin()
 
# Press Ctrl-Z to stop and then kill the process. Necessary because sniff just runs until you stop it.
#
# Still... works better than this scapy one-liner I built it from:
#sniff(,prn=lambda x:x.sprintf("{Dot11ProbeReq:%Dot11.addr3%\t%Dot11ProbeReq.info%\t}"
