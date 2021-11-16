#!/usr/bin/env python3

sentence = ""

s = input()
while s != "end":
    sentence = sentence + " " + s
    sentences = sentence.split(".")
    j = 0
    while j < len(sentences) - 1:
        print(" ".join(sentences[j].split()) + ".")
        j = j + 1
    sentence = sentences[len(sentences) - 1]
    s = input()
