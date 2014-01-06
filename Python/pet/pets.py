#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import argparse

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
bold = "\033[1m"
reset = "\033[0;0m"


def create_pets():
    with con:
        cur = con.cursor()
        cur.execute("LOAD DATA LOCAL INFILE '/home/wolff215/Projects/Python/pets.txt' INTO TABLE pet \
                FIELDS TERMINATED BY '*'")


def pet_ages():
    with con:

        cur = con.cursor()
        cur.execute("SELECT name,death,species,(YEAR(CURDATE())-YEAR(birth)) \
                     - (RIGHT(CURDATE(),5)<RIGHT(birth,5)) AS age FROM pet;")

        rows = cur.fetchall()

        for row in rows:
            age = str(row[3])
            species = row[2]
            name = row[0]
            death = row[1]

            if age != 'None':
                if death == None:
                    print name + ', the ' + species + ', is ' + age + ' years old.'


def pet_info():
    pet = raw_input(bold + "Which pet? (type all to list pets): " + reset)
    print

    with con:

        cur = con.cursor()

        if pet.lower() != 'all':
            cur.execute("SELECT * FROM pet WHERE name = %s", (pet))

        else:
            cur.execute("SELECT * FROM pet")

        rows = cur.fetchall()

        if rows == ():
            print "Pet Unknown..."

        for row in rows:

            if row:

                birth = str(row[4])

                if row[3] == 'f':

                    if birth != 'None':
                        print "%s is owned by %s, she is a %s, and she was born on %s." % (row[0], row[1], row[2], row[4])

                    else:
                        print "%s is owned by %s, she is a %s, and her date of birth is unknown." % (row[0], row[1], row[2])

                else:

                    if birth != 'None':
                        print "%s is owned by %s, he is a %s, and he was born on %s." % (row[0], row[1], row[2], row[4])

                    else:
                        print "%s is owned by %s, he is a %s, and his date of birth is unknown." % (row[0], row[1], row[2])



def add_pet():
    pet = raw_input("What is the pet's name? ")
    species = raw_input("What is the pet's species? ")
    sex = raw_input("What is the pet's sex? (m or f) ")
    owner = raw_input("Who owns the pet? ")
    birth = raw_input("When was the pet born? (yyyy-mm-dd) ")
    death = raw_input("Is the pet alive? (y or n) ")

    if death == 'n':
        death = raw_input("When did the pet die? (yyyy-mm-dd) ")
    else:
        death = ''

    with con:
        cur = con.cursor()

        if death == '':
            cur.execute("INSERT INTO pet VALUES (%s, %s, %s, %s, %s, NULL)", (pet, owner, species, sex, birth))
        else:
            cur.execute("INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s)", (pet, owner, species, sex, birth, death))

    print "%s successfully added." % (pet)


def remove_pet():
    pet = raw_input("What pet would you like to remove? ")

    while pet == '':
        pet = raw_input('Please enter a pet name: ')

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM pet WHERE name = %s", (pet))
        rows = cur.fetchall()

        if len(rows) == 0:
            print "\nPet not found..."

        elif len(rows) == 1:
            cur.execute("DELETE FROM pet WHERE name = %s", (pet))
            print "\nPet removed successfully."

        else:
            count = 1
            for row in rows:
                print "\n%s. %s is owned by %s, they are a %s." % (count, row[0], row[1], row[2])
                count = count + 1

            number = raw_input("\nMore than one pet with that name found,\n" \
                                + "Please enter number corresponding to correct pet: ")

            species = rows[int(number)-1][2]
            owner = rows[int(number)-1][1]
            cur.execute("SELECT * FROM pet WHERE species = %s AND name = %s AND owner = %s", (species,pet,owner))
            sel = cur.fetchall()

            if len(sel) == 0:
                print "\nPet not found..."

            else:
                cur.execute("DELETE FROM pet WHERE name = %s AND species = %s AND owner = %s", (pet,species,owner))
                print "\nPet removed successfully."
#    print len(rows)


def startup():

    functions = {'1' : add_pet,
                    '2' : pet_info,
                    '3' : pet_ages,
                    '4' : remove_pet,
    }

    while True:
        while True:
            selection = raw_input(bold + "\n1. Add pet" + \
                                    "\n2. Pet information" + \
                                    "\n3. Pet ages" + \
                                    "\n4. Remove pet" + \
                                    "\n5. Quit" + reset + \
                                    "\n\nWhat would you like to run? ")
            if selection.isdigit():
                if int(selection) >= 0  and int(selection) < (len(functions) + 2):
                    break

        if int(selection) == (len(functions) + 1):
            break

        else:
            functions[selection]()

#parser = argparse.ArgumentParser(
#        description='A command line utility to run the desired function.',
#        epilog='And now you know...')

#parser.add_argument('name', help='The function name...')

#args = parser.parse_args()

# Dynamically call a carefully named function based on user input...
#eval('%s()' % (args.name, ))

if __name__ == '__main__':
    startup()
