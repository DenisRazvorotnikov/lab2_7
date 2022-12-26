#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Universe
    u = set("abcdefghijklmnopqrstuvwxyz")

    # Set Data
    a = {"a", "b", "d", "i", "x"}
    b = {"d", "e", "h", "i", "n", "u"}
    c = {"e", "f", "m", "n"}
    d = {"a", "c", "h", "k", "r", "s", "w", "x"}

    # Inverses for a b and c
    ne_a = u.difference(a)
    ne_b = u.difference(b)
    ne_c = u.difference(c)

    # Definition X
    x = ne_b.intersection(a.difference(c))
    print(f'X = {x}')

    # Definition Y
    y = (ne_a.intersection(d)).union(c.difference(b))
    print(f'Y = {y}')
