#!/usr/bin/env python3

with open("dracula.txt", "r") as draculafile:
    for line in draculafile:
        line = line.rstrip('\n')
        if "ampire" in line:
            print(line)
