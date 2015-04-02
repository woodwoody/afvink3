import re
import tkinter

def main():
    wajoo()

def wajoo():
    file = open('IRC_representative_list.txt','r')
    i = 0

    for line in file:    
        found = re.search(r"C.[DNEHQSTI]C.{4,6}[ST].{2,2}[WM][HR][RKENAMSLPGQT].{3,4}[GNEP].{3,6}C[NES][ASNR]C", line)
        if found:
            irc = re.findall(r'IRC_[0-9]{0,20}',line)
            seq = re.findall(r'[A-Z]+',line)
            dic = {irc[0]:seq[len(seq)-1]}
            print(irc)

main()

