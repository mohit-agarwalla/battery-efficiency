AIR_DENSITY=1.225
MILESTOHOURTOMETRESTOSECOND=0.44
STRING="----------"

def milesperhourtometrespersecond(milesperhour):
	mps=milesperhour*MILESTOHOURTOMETRESTOSECOND
	mps//=1
	return mps

def DragForce(constantspeed, coefficient, frontalarea):
	speedlist=[]
	dragforcelist=[]
	constantspeed=milesperhourtometrespersecond(constantspeed)
	constantspeed=constantspeed//1
	constantspeed=int(constantspeed)
	print(constantspeed)
	for speed in range (1,(constantspeed*10)+1):
		speed/=10
		speedlist.append(speed)
		dragforce=0.5*coefficient*frontalarea*AIR_DENSITY*(speed**2)
		dragforcelist.append(dragforce)
		dragforcearray=[speedlist, dragforcelist]
	return(dragforcearray)


def kwhtoJoules(carname):
	kwh=int(input("What is the " + carname+ " battery capacity in kwh? "))
	joules=kwh*3.6*(10**6)
	return joules

def bhptowatts(bhp):
	watts=bhp*745.7
	return watts

def NetForce(dragforcearray, mass):
	forcearray=dragforcearray
	netforcelist=[]
	thrustforcelist=[]
	accelerationlist=[]
	bhp=int(input("What is the bhp of the car? "))
	watts=bhptowatts(bhp)
	length = int(len(dragforcearray[0]))
	for speed in range(0,length):
		speed2=dragforcearray[0][speed]
		netforce=watts/speed2
		netforcelist.append(netforce)
		thrustforce=netforce+(dragforcearray[1][speed])
		thrustforcelist.append(thrustforce)
		acceleration=netforce/mass
		accelerationlist.append(acceleration)
	forcearray.append(thrustforcelist)
	forcearray.append(netforcelist)
	forcearray.append(accelerationlist)
	return forcearray

def DistanceAccelerationTime(forcearray):
	array=forcearray
	timelist=[]
	distancelist=[]
	workdonelist=[]
	for acc in range(0,len(array[4])):
		if acc==0:
			timelist.append(0)
			distancelist.append(0)
			workdonelist.append(0)
		else:
			force=array[2][acc]
			speed=array[0][acc]
			acc=array[4][acc]
			time=0.1/acc
			timelist.append(time)
			distance=time*speed
			distancelist.append(distance)
			workdone=force*distance
			workdonelist.append(workdone)

	array.append(timelist)
	array.append(distancelist)
	array.append(workdonelist)			
	return array

def WorkDoneA(distancearray):
	total=0
	for x in range(0,len(distancearray[4])):
		total+=distancearray[4][x]
	return total

def DistanceWhileA(distancearray):
	distance=0
	for x in range(0,len(distancearray[6])):
		distance+=x
	return distance

def formattext(printtext):
	print (STRING*4)
	print('{0:^20}'.format(printtext))

def Efficiency(distance):
	yes=str(input("Do you want to calculate the relative efficiency of the car? '(Press Y if yes)' "))
	if yes == "Y":
		actual=float(input("What is the actual range of the kar in kilometres? "))
		actual*=1000
		efficiency=(actual/distance)
		efficiency*=100
		string="The efficiency considering the battery percentage used is "+ str(efficiency)
		formattext(string)



def Calculator():
	print("WELCOME TO THE RANGE CALCULATOR!")
	carname=input("What is the name of the car being investigated? ")
	joules=kwhtoJoules(carname)
	mass=int(input("What is the mass of the car? "))
	print("Battery capacity in joules is ", joules)
	constantspeed=int(input("What is the assumed constant speed after acceleration finishes? "))
	coefficient=float(input("What is the drag coefficient for the "+ carname+"? "))
	width=float(input("What is the maximum width of the car? "))
	height=float(input("What is the maximum height of the car? "))
	frontalarea=height*width
	dragforcearray=DragForce(constantspeed, coefficient, frontalarea)
	forcearray=NetForce(dragforcearray, mass)
	distancearray=DistanceAccelerationTime(forcearray)
	joules-=(WorkDoneA(distancearray))
	distance=joules/distancearray[7][len(distancearray[7])-1]*10
	distance+=DistanceWhileA(distancearray)
	text="Range of the car is theoretically "+ str(distance)
	formattext(text)
	distance*=0.75
	text="Range considering that a car only uses 0.75 of the capacity "+ str(distance)
	formattext(text)
	Efficiency(distance)


Calculator()