# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:47:30 2020
@author: minimilien
"""

import requests
import time as tempo


def test1():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://127.0.0.1:5000/RAM', json=dictToSend)
    print('response from server:',res.text)
    print(res)


def test2():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://127.0.0.1:5000/horloge', json=dictToSend)
    print('response from server:',res.text)
    print(res)
    
    
def test3():
    dictToSend = {'question':'what is the answer?'}
    res = requests.post('http://127.0.0.1:5000/sfggd', json=dictToSend)
    print ('response from server:',res.text)
    print(res)

"""
def test4():
    from AI import analyse
    res=analyse("I like love")
    print(res)
"""

def test5():
    dictToSend = {'phrase':'wall'}
    res = requests.post('http://127.0.0.1:5000/sentimements', json=dictToSend)
    print('response from server:',res.text)
    print(res)
    
def test6():
    dictToSend = {'phrase':'wall'}
    res = requests.post('http://127.0.0.1:5000/SIM', json=dictToSend)
    print('response from server:',res.text)
    print(res)

class Test:
    def __init__(self,test):
        self.name=test.__name__
        self.test=test
        self.validation=False
    def execution(self):
        try:
            self.test()
            self.validation=True
            print(self.name+' is completed.')
        except Exception as e:
            print(e)
            self.validation=False
            print(self.name+' has failed.')

def deploiement(*tests):
    print("Begining of the tests...")
    cpt=0
    for test in tests:
        tempo.sleep(1)
        cpt+=1
        print('Test {}/{}'.format(cpt,len(tests)))
        test_=Test(test)
        test_.execution()
        if test_.validation==False:
            print("false")
            raise Exception("False")
    return True

t0=tempo.time()
list(map(lambda x : test3(),list(range(1000))))
print(tempo.time()-t0)
t0=tempo.time()
list(map(lambda x : test1(),list(range(1000))))
print(tempo.time()-t0)
t0=tempo.time()
list(map(lambda x : test2(),list(range(1000))))
print(tempo.time()-t0)
