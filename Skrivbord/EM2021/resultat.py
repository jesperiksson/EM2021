#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:21:55 2021

@author: jesper
"""

import pandas as pd

italien = pd.DataFrame([
    [3,0],#Turkiet
    [4,0],#Tjeckien
    [7,0],#San Marino
    [2,0],#Litauen
    [2,0],#Bulgarien
    [2,0],#Nordirland
    [2,0],#Bosnien och Herzegovina
    [2,0],#Polen
    [1,1],#Nederländerna
    [0,0],#Polen
    [1,0],#Nederländerna
    [1,1],#Bosnien och Herzegovina
    ],columns=['gjorda','insläppta'])

turkiet = pd.DataFrame([
    [0,3],#Italien
    [2,0],#Moldavien
    [0,0],#Guinea
    [2,1],#Azerbajdzjan
    [3,3],#Lettland
    [3,0],#Norge
    [4,2],#Nederländerna
    [0,2],#Ungern
    [3,2],#Ryssland
    [2,2],#Serbien
    [1,1],#Ryssland
    [0,0],#Serbien
    [0,1],#Ungern
    ],columns=['gjorda','insläppta'])

wales = pd.DataFrame([
    [0,2],#Schweiz
    [0,0],#Albanien
    [1,3],#Frankrike
    [1,0],#Tjeckien
    [1,0],#Mexico
    [1,3],#Belgien
    [3,1],#Finland
    [1,0],#Irland
    [1,0],#Bulgarien
    [0,0],#Irland
    [1,0],#Bulgarien
    [1,0],#Finland
    ],columns=['gjorda','insläppta'])

schweiz = pd.DataFrame([
    [2,0],#Wales
    [7,0],#Liechtenstein
    [2,1],#USA
    [3,2],#Finland
    [1,0],#Litauen
    [3,1],#Bulgarien
    [3,0],#Ukraina
    [1,1],#Spanien
    [3,3],#Tyskland
    [0,1],#Spanien
    [1,1],#Tyskland
    [1,2],#Ukraina
    ],columns=['gjorda','insläppta'])

finland = pd.DataFrame([
    [1,0],#Danmark
    [0,1],#Estland
    [0,2],#Sverige
    [2,3],#Schweiz
    [1,1],#Ukraina
    [2,2],#Bosnien och Hercegovina
    [1,3],#Wales
    [2,1],#Bulgarien
    [1,0],#Irland
    [2,0],#Bulgarien
    [1,0],#Irland
    [0,1],#Wales
    ],columns=['gjorda','insläppta'])

belgien = pd.DataFrame([
    [3,0],#Ryssland
    [1,0],#Kroatien
    [1,1],#Grekland
    [8,0],#Vitryssland
    [1,1],#Tjeckien
    [3,1],#Wales
    [4,2],#Danmark
    [2,0],#England
    [2,1],#Island
    [1,2],#England
    [5,1],#Island
    [2,0],#Danmark
    ],columns=['gjorda','insläppta'])

danmark = pd.DataFrame([
    [0,1],#Finland
    [2,0],#Bosnien och Hercegovina
    [1,1],#Tyskland
    [4,0],#Österrike
    [8,0],#Moldavien
    [2,0],#Israel
    [2,4],#Belgien
    [2,1],#Island
    [1,0],#England
    [3,0],#Island
    [0,0],#England
    [0,2],#Belgien
    ],columns=['gjorda','insläppta'])

ryssland = pd.DataFrame([
    [0,3],#Belgien
    [1,0],#Bulgarien
    [1,1],#Polen
    [1,2],#Slovakien
    [2,1],#Slovenien
    [3,1],#Malta
    [0,5],#Serbien
    [2,3],#Turkiet
    [0,0],#Ungern
    [1,1],#Turkiet
    [3,2],#Ungern
    [3,1],#Serbien
    ],columns=['gjorda','insläppta'])
# Grupp C
österrike = pd.DataFrame([
    [0,0],#Slovakien
    [0,1],#England
    [0,4],#Danmark
    [3,1],#Färöarna
    [2,2],#Skottland
    [1,1],#Norge
    [2,1],#Nordirland
    [1,0],#Rumänien
    [1,0],#Nordirland
    [2,3],#Rumänien
    [2,1],#Norge
    ],columns=['gjorda','insläppta'])

nederländerna = pd.DataFrame([
    [3,0],#Georgien
    [2,2],#Skottland
    [7,0],#Gibraltar
    [2,0],#Lettland
    [2,4],#Turkiet
    [2,1],#Polen
    [3,1],#Bosnien och Hercegovina
    [1,1],#Italien
    [0,0],#Bosnien och Hercegovina
    [0,1],#Italien
    [1,0],#Polen
    ],columns=['gjorda','insläppta'])

nordmakedonien = pd.DataFrame([
    [4,0],#Kazakstan
    [1,1],#Slovenien
    [2,1],#Tyskland
    [5,0],#Liechtenstein
    [2,3],#Rumänien
    [0,1],#Armenien
    [2,1],#Estland
    [1,0],#Georgien
    [1,1],#Georgien
    [3,3],#Estland
    [2,1],#Kosovo
    [1,1],#Georgien
    [2,1],#Armenien
    ],columns=['gjorda','insläppta'])

ukraina = pd.DataFrame([
    [4,0],#Cypern
    [1,0],#Nordirland
    [1,1],#Bahrain
    [1,1],#Kazakstan
    [1,1],#Finland
    [1,1],#Frankrike
    [0,3],#Schweiz
    [1,3],#Tyskland
    [1,0],#Spanien
    [1,2],#Tyskland
    [0,4],#Spanien
    [2,1],#Schweiz
    ],columns=['gjorda','insläppta'])
# Grupp D
england = pd.DataFrame([
    [1,0],#Rumänien
    [1,0],#Österrike
    [2,1],#Polen
    [2,0],#Albanien
    [5,0],#San Marino
    [4,0],#Island
    [0,2],#Belgien
    [0,1],#Danmark
    [2,1],#Belgien
    [0,0],#Damnark
    [0,1],#Island
    ],columns=['gjorda','insläppta'])

kroatien = pd.DataFrame([
    [1,1],#Belgien
    [1,1],#Armenien
    [3,0],#Malta
    [1,0],#Cypern
    [0,1],#Slovenien
    [2,3],#Portugal
    [1,2],#Sverige
    [1,2],#Frakrike
    [2,1],#Sverige
    [2,4],#Frankrike
    [1,4],#Portugal
    ],columns=['gjorda','insläppta'])

tjeckien = pd.DataFrame([
    [3,1],#Albanien
    [0,4],#Italien
    [0,1],#Wales
    [1,1],#Belgien
    [6,2],#Estland
    [2,0],#Slovakien
    [1,0],#Israel
    [0,1],#Skottland
    [2,1],#Israel
    [1,2],#Skottland
    [3,1],#Slovakien
    ],columns=['gjorda','insläppta'])

skottland = pd.DataFrame([
    [1,0],#Luxemburg
    [2,2],#Nederländerna
    [4,0],#Färöarna
    [1,1],#Israel
    [2,2],#Österrike
    [0,1],#Israel
    [0,1],#Slovakien
    [1,1],#Serbien
    [1,0],#Tjeckien
    [1,0],#Slovakien
    [0,0],#Israel
    [2,1],#Tjeckien
    [1,1],#Israel
    ],columns=['gjorda','insläppta'])




















