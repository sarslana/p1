#p_8. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
#Person	      Relation, Darth Vader	  father, Leia	        sister, Han	          brother in law

#Examples
#relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
#relation_to_luke("Leia") ➞ "Luke, I am your sister."
#relation_to_luke("Han") ➞ "Luke, I am your brother in law."


select= (input('Whom do you want to relate?  ')).capitalize()
family_members=['Darth', 'Mercy', 'Leia', 'Han']

if select == str ('Darth'):
    print("Luke, I am your father.")
elif select== str ('Mercy'):
    print("Luke, I am your mother.")
elif select== str ('Leia'):
    print("Luke, I am your sister.")
elif select== str ('Han'):
    print("Luke, I am your brother in law.")
else:
    print("Sorry Luke, there is no such name in your family")