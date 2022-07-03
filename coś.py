#! /usr/bin/env python3
# -*- coding: utf-8 -*-

KLUCZ = 2


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny


tekst = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
i = szyfruj(tekst)
print (i)
i.maketrans()