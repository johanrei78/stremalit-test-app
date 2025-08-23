# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 14:19:24 2025

@author: johvik
"""

import random

def generer_mor(fenotype):
    if fenotype == "røde øyne":
        return ("X^H", "X^H")  # alltid homozygot
    else:
        return ("X^h", "X^h")

def generer_far(fenotype):
    if fenotype == "røde øyne":
        return ("X^H", "Y")
    else:
        return ("X^h", "Y")

def simuler_avkom(mor, far, antall):
    fenotype_telling = {
        "rødøyd hunn": 0,
        "hvitøyd hunn": 0,
        "rødøyd hann": 0,
        "hvitøyd hann": 0
    }
    for _ in range(antall):
        allel_mor = random.choice(mor)
        allel_far = random.choice(far)
        if allel_far == "Y":  # Hann
            if allel_mor == "X^H":
                fenotype_telling["rødøyd hann"] += 1
            else:
                fenotype_telling["hvitøyd hann"] += 1
        else:  # Hunn
            genotype = (allel_mor, allel_far)
            if "X^H" in genotype:
                fenotype_telling["rødøyd hunn"] += 1
            else:
                fenotype_telling["hvitøyd hunn"] += 1
    return fenotype_telling