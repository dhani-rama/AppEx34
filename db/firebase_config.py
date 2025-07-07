# -*- coding: utf-8 -*-
"""
Created on Sun May 25 11:38:28 2025

@author: ramad
"""

import firebase_admin
from firebase_admin import credentials, db

def get_db_root():
    if not firebase_admin._apps:
        cred = credentials.Certificate("C:/Disk D/Riset/AppEx34/db/")
        firebase_admin.initialize_app(cred, {
            "databaseURL": ""
        })
    return db.reference('/')
