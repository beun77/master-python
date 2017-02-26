# -*- coding: utf-8 -*-


import os
os.environ['PROVER9']='/home/benoit/Desktop/python/LADR-2009-11A/bin/'
#'/users/*****/LADR-2009-11A/bin'
import nltk

lp = nltk.sem.logic.LogicParser()

A = lp.parse('all x. (humain(x) -> mortel(x))')
B = lp.parse('humain(socrate)')
C = lp.parse('mortel(socrate)')

prover = nltk.Prover9()

print(prover.prove(goal=C,assumptions=[A,B],verbose=True))

"""
1. Tous ceux qui aiment tous les animaux sont aimés par qqun.
2. Quiconque tue un animal n’est aimé par personne.
3. Jack aime tous les animaux.
4. C’est soit Jack soit Curiosité qui a tué le chat appelé Luna.
5. Montrer que c’est Curiosité qui a tué le chat.
"""

"""
negation           -
conjunction        &
disjunction        |
implication        ->
equivalence        <->
equality           =
inequality         !=
existential        exists
universal          all
lambda			   backslash # Penser à précéder l'expression d'un r pour éviter que le backslash ne soit interprété comme le caractère d'échappement en Python
"""


lp = nltk.sem.logic.LogicParser()

# Syntaxe ci-dessous à revoir

A = lp.parse('all x y. (humain(x)&animal(y)&aime(x,y)) -> (exists z. humain(z)&aime(z,x))')
B = lp.parse('all x. exists y. (humain(x)&animal(y)&tue(x,y)) -> (all z. humain(z)&-aime(z,x))')
C = lp.parse('all x. (animal(x)) -> (aime(J,x))')
D = lp.parse('(tue(J,L)|tue(C,L))&chat(L)')
E = lp.parse('all x. (chat(x)) -> (animal(x))')
F = lp.parse('tue(C,L)')

prover = nltk.Prover9()

print(prover.prove(goal = F, assumptions = [A,B,C,D,E], verbose = True))


