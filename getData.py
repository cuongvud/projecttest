import os

def getData():
	counter = 0
	trainData = []
	with os.scandir(os.getcwd() + '/spam') as entries:
		for entry in entries:
			try:
				with open (entry, 'r') as f:
					trainData.append((True, f.read()))
			except:
				counter += 1
				pass

	print ('Number of spam files added: ', len(trainData))
	print ('Number of spam discarded files: ', counter)
	oldcounter = counter
	oldlen = len(trainData)

	with os.scandir(os.getcwd() + '/ham') as entries:
		for entry in entries:
			try:
				with open (entry, 'r') as f:
					trainData.append((False, f.read()))
			except:
				counter += 1
				pass

	print ('Number of non-spam files added: ', len(trainData) - oldlen)
	print ('Number of non-spam discarded files: ', counter - oldcounter)

	return trainData

