# uncompyle6 version 3.3.1
# Python bytecode 3.5 (3350)
# Decompiled from: Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
# [GCC 8.2.0]
# Embedded file name: TimingAttackModule.py
# Compiled at: 2019-04-16 10:44:38
# Size of source mod 2**32: 1504 bytes
"""
Created on Thu May  3 00:30:38 2018

@author: Michele
"""
import numpy as np, random
k_567xfuthfretw6 = [
 1,
 1,
 1,
 0,
 1,
 0,
 0,
 1,
 0,
 1,
 1,
 0,
 0,
 1,
 0,
 0,
 0,
 0,
 1,
 1,
 1,
 0,
 1,
 1,
 1,
 0,
 0,
 1,
 1,
 1,
 1,
 0,
 1,
 0,
 0,
 1,
 0,
 0,
 1,
 1,
 0,
 0,
 1,
 1,
 0,
 1,
 1,
 1,
 0,
 0,
 0,
 1,
 1,
 0,
 1,
 1,
 0,
 1,
 0,
 1,
 0,
 0,
 1,
 0]
keylength = len(k_567xfuthfretw6)

def victimdevice(c, mu=1000, sigma=50):
    np.random.seed(c % 4294967296)
    delay = 0
    for i in range(keylength):
        delay = delay + np.random.normal(mu, sigma)
        if k_567xfuthfretw6[i] == 1:
            delay = delay + np.random.normal(mu, sigma)

    return delay


def attackerdevice(c, d, mu=1000, sigma=50):
    np.random.seed(c % 4294967296)
    coupled = True
    delay = 0
    for i in range(len(d)):
        delay = delay + np.random.normal(mu, sigma)
        if (d[i] != k_567xfuthfretw6[i]) & coupled:
            coupled = False
            np.random.seed(random.randint(1, 4294967295))
        if d[i] == 1:
            delay = delay + np.random.normal(mu, sigma)

    return delay


def test(d):
    f = sum([int(k_567xfuthfretw6[i] == d[i]) for i in range(len(d))]) / keylength
    if f < 0.75:
        print('Less than 75% of key bits recovered.')
    else:
        if f < 1:
            print('At least 75%, but less than 100% of key bits recovered.')
        else:
            print('100% of key bits recovered.')
# okay decompiling TimingAttackModule.pyc
