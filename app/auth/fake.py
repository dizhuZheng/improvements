from faker import Faker 

import json		 

from random import randint	 

fake = Faker() 

def fake_user_data(): 
		name = fake.name()
	# dictionary dumped as json in a json file 
	with open('users.json', 'w') as fp: 
		json.dump(user_data, fp) 
	

def main(): 
	number_of_users = 100
	input_data(number_of_users)

main() 
# The folder or location where this python code 
# is save there a students.json will be created 
# having 10 students data. 
