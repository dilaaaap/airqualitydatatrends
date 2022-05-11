import csv
import sys
name1 = "Air_Quality_Survey.csv"

with open(name1, mode = 'r') as f:
	dict1 = csv.reader(f)
	dict2 = {}
	for row in dict1:
		key = row[0]
		if key in dict2:
			pass
		dict2[key]= row[1:]

#print(dict1)
#for i in range(len(dict2)-1):

#	print(i,dict2[str(i)][7])

def ObjectID():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][0]
		print(k)
	return k

def Date():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][1]
		print(k)
	return k

def Sample_ID():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][2]
		print(k)
	return k

def Parameter():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][3]
		print(k)
	return k

def Results():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][4]
		print(k)
	return k

def Units():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][5]
		print(k)
	return k

def CAS():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][6]
	return k

def HRV():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][7]
		print(k)
	return k

def Units1():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][8]
		print(k)
	return k
def HRV_Types():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][9]
		print(k)
	return k
def Name():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][10]
		print(k)
	return k
def Description():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][11]
		print(k)
	return k
def Address():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][12]
		print(k)
	return k

def City1():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][13]
		print(k)
	return k

def State():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][14]
		print(k)
	return k

def Zip():
	for i in range(len(dict2)-1):
		k = dict2[str(i)][15]
		print(k)
	return k
	
if __name__ == '__main__':
	globals()[sys.argv[1]]()
