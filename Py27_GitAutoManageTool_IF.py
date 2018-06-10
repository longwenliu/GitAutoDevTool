#!/usr/bin/env python
#coding:utf-8

#################### 
import sys
sys.path.append(r'C:\Python27\Scripts')

import Py27_GitAutoManageTool

#################### 

"""
This a Recell Script for AutoCreate Project DEMO!
Trick:You can move the Resources/Py27_AutoCreateProj_DEMO.pyc to C:\Python27\Scripts!
So that you only need run Py27_AutoCreateProj_IF.py without other files.
"""

if __name__ == "__main__":
    
    DEMO_Author = "Who are you ?"
    Py27_GitAutoManageTool.GitAutoManage(DEMO_Author) 