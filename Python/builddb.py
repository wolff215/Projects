#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS \
            Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
