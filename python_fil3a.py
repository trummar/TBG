# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:28:15 2022

@author: vande
"""
print("*********** 1 *****************")
svar = input("Hva heter du? ")
print(svar)

print("*********** 1 *****************")
svar = input("Hvor gammel er du? ")
print(svar)

print("*********** 2 *****************")
svar = input("Hvor gammel er du? ")
print("Du er",svar,"år gammel")


print("*********** 2 *****************")
svar = input("Hvor gammel er du? ")
print("Du er",svar,"år gammel")
print("om 30 år er du", svar + 30,"år")  # fix!!!


print("********** 1. måte ******************")
svar = input("Hvor gammel er du? ")
print("Du er",svar,"år gammel")
svar = int(svar)
print("om 30 år er du", svar + 30,"år")


print("********** 2. måte ******************")
svar = input("Hvor gammel er du? ")
print("Du er",svar,"år gammel")
# svar = int(svar)
print("om 30 år er du", int(svar) + 30,"år")


print("********** 3. måte ******************")
svar = int(input("Hvor gammel er du? "))
print("Du er",svar,"år gammel")
# svar = int(svar)
print("om 30 år er du", svar + 30, "år")



