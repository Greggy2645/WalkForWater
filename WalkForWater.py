import math

def keuze():
	startding = str(input('Type \'shower\' to calculate.\n Type exit to stop.\n'))
	if startding == 'shower':
		shower()
	elif startding == 'exit':
		exit()
	else: 
		print('your fucking retarded')
		keuze()

def shower():
    kmperliter = 2
    literperminute = 7.9
    showertime = int(input('How long have you showered in minutes?\n'))
    total = showertime * literperminute
    total = math.floor(total)
    walktime = total * kmperliter
    hours = walktime / 6
    hours = math.floor(hours)
    print('You have used ' + str(total) + ' liters of water.')
    print('An african child has to walk ' + str(walktime) +
          'km for this amount of water.')
    print('That takes the child about ' + str(hours) + ' hours.\n')
    if showertime > 10:
        print('how the fuck did you shower over 10 mins tho')
    keuze()

eerstestartding = str(input('Type \'shower\' to calculate.\n'))
if eerstestartding == 'shower':
    shower()
else:
    print('wtf that isnt shower try again drunk bitch')
    keuze()
