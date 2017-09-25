## Assignment 2
## Tejveer Singh and Niteesh Kanungo
from collections import Counter
from pygeodesy import ellipsoidalVincenty as ev

# Taking an input file from the User with full extension
input_file_from_user = input("Please give a complete file name with full file extension")
with open(input_file_from_user, 'r', ) as x:
    lines = x.readlines()

def storm_charasterstics():
   """
    This function will print/date range/storm name and maximum sustained wind-> Date Time and how many landfall occured
   :return:
   """
   for i in range(len(lines)):
       # looping on everyline in text file as a string
       if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0, 2) or lines[i].startswith("AL", 0, 2):
          #condition testing the storm name
          z = lines[i].split(sep=",")
          # splitting each element in a line as a separate string
          y = int(z[2])
          # converting string to integer
          if (lines[i][19:28].strip()) == "UNNAMED":
              print("Record Identifier for Unnamed Storm:", lines[i][0:8].strip())
          else:
              print("STORM NAME:", lines[i][19:28].strip())
              # print the storm name by stripping off the white spaces
              print("Date Range: " + str(lines[i + 1][4:6]) + "/"
                    + str(lines[i + 1][6:8]) + "/" + str(lines[i + 1][0:4])
                    + " to " + str(lines[i + y][4:6]) + "/" + str(lines[i + y][6:8])
                    + "/" + str(lines[i + y][0:4]))
          k=[]
          #creating the empty list
          count=0
          #initialize count to zero
          for l in range(y):
              #loop for creating list of sustained winds and counting the number of landstorm for each storm
            k.append((lines[i+l+1][38:41]))
              #appending elements into the array
            if lines[i+1+l][16]=="L":
                #testing the condition for landstorm
                count=count+1
          a=(max(k))
          #function to find the maximum sustained wind
          g=k.index(a)
          #find index on which maximum sustained wind occurs
          print("Maximum sustained winds:"+ str(a)+" Knots")
          #print the maximum sustained winds for each storm
          print("Date:"+ str(lines[i+g+1][4:6])+"/"+str(lines[i+g+1][6:8])+"/"+str(lines[i+g+1][0:4]))
          #print the date on which maximum sustained wind occurs
          print("Time:"+str(lines[i + g + 1][10:12])+":"+str(lines[i + g + 1][12:14]))
          #print the time on which maximum sustained wind occurs
          print("Landfall:",count)
          #print the landfall count for each storm
          print ("********************************************")


def storm_per_year():
  """
   This funtion will print name of storm per year
  :return:
  """
  J=[]
  for i in range(len(lines)):
      #for loop for counting storms per year
      if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0, 2) or lines[i].startswith("AL", 0, 2):
        #condition for testing the storm block
        J.append(lines[i][4:8])
        #appending the year in the array
  print ("Storms per Year:")
  a = dict(Counter(J))
  #counting the frequency of each elemenr in the list and converting it into dictionary
  print(a)

def Hurricanes_per_year():
  """
   This function will print the number of storms converted to hurricane per year.
  :return:
  """
  I=[]
  #creating an empty array for appending years in the array
  for i in range(len(lines)):
      #loop for reading lines in the file
      if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0, 2) or lines[i].startswith("AL", 0, 2):
        #testing the condition for starting of storm
        z = lines[i].split(sep=",")
        #splitting each element in a line as a separate string
        y = int(z[2])
        for n in range(y):
            #loop for reading a particular storm
            if lines[n+i+1][19:21]=="HU":
                #testing the condition for hurricane
                I.append(lines[i+1][0:4])
                #appending the year on which storm occur into the array
                break
                #coming out of the inner loop
  b=dict(Counter(I))
  #converting array into dictionary and counting the frequency of each element
  print("Hurricane per year:")
  print (b)
  #printing the dictionary

def Storm_speed():
  """
   This function will give the maximum speed/Average speed/Total distance and Greatest Directional Change
  :return:
  """
  for i in range(len(lines)):
      #loop for reading lines in the file
      if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0, 2) or lines[i].startswith("AL", 0, 2):
        #testing the condition for starting of storm
        z = lines[i].split(sep=",")
        #splitting each element in a line as a separate string
        y = int(z[2])
        bearing=[]
        #create an empty array for storing angles
        q=[]
        #create an empty array for calculating speed
        w=[]
        #create an empty array for storing time lags
        s=[]
        #create an empty array for storing distance
        for n in range(y-1):
            #loop for iteration into individual strorm

            a=ev.LatLon(lines[i+n+1][23:28].strip(),lines[i+n+1][30:36].strip())
            #passing latitute and longitude point into the function
            b=ev.LatLon(lines[i+n+2][23:28].strip(),lines[i+n+2][30:36].strip())
            #passing latitude nad longitude point into the function
            try:
                l=(a.distanceTo(b))/1852.0
                #calculate distance from point A to B and converting it into nautical miles
                s.append(l)
                #storing the distance in the array
                bearing.append(a.bearingTo(b))
                #appending the angle into the bearing array
            except ev.VincentyError:
                s.append(0)
                #appending 0 into the distance array if storm doesn't travel much distance
                bearing.append(0)
                #appending 0 into the bearing array if storm doesn't travel any distance
            if lines[i+n+2][10:12].startswith("00",0,2):
                #condition for time calculation
                c=int(lines[i+n+2][10:14])
                #storing hours and minutes in a variable
                b=str(c+2400)
                #Addition of 2400 to 0000 and converting it into string
                hours=abs(int(lines[i+n+1][10:12])-int(b[0:2]))
                #separating hours ,then getting the difference
                minutes=abs(int(lines[i+n+1][12:14])-int(b[2:4]))
                #storing minutes in the variable,then getting the difference
                w.append(hours*60 + minutes)
                #Appending time into the array , converting hours to minutes
                q.append(s[n]/w[n])
                #calculation of speed


            else:
                hours = abs(int(lines[i + n + 1][10:12]) - int(lines[i + n + 2][10:12]))
                #calulating hour
                minutes = abs(int(lines[i + n + 1][12:14]) -int(lines[i + n + 2][10:12]))
                #calculating minutes
                w.append(hours * 60 + minutes)
                #appending time into array
                q.append(s[n]/w[n])
                #appending to speed into array

        if (lines[i][19:28].strip()) == "UNNAMED":
            print("Record Identifier for Unnamed Storm:", lines[i][0:8].strip())
        else:
            print("STORM NAME:", lines[i][19:28].strip())
        try:
                 print ("Maximum speed:",max(q),"nautical miles/minute")
                 #print the maximum speed
                 print("Average Speed:",sum(s)/sum(w),"nautical miles/minute")
                 #print the average speed of each storm
                 print ("Total Distance:",sum(s),"nautical miles")
                 #print the total distance travell by each storm
                 v=[]
                 #creating empty array for storing directional changes
                 for s in range(0,len(bearing)-1):
                     #loop for calculating greatest directional change
                        v.append((abs(bearing[s]-bearing[s+1]))/(w[s]))
                     #appending directional change per unit time into the array
                 print ("Greatest directional Change per unit time",max(v),"deg/minute")
                 print("************************************************")
                 #print the greatest directional change

        except ValueError:
                 print ("Maximum Speed:",0,"miles/minute")
                 #print the maximum speed 0 ,if the storm doesnt travel any distance
                 print("Average Speed:",0, "miles/minute")
                 #print the Average speed 0 ,if the storm doesnt travel any distance
                 print("Total Distance:",0, "miles")
                 #print the total distance 0 ,if the storm doesnt travel any distance
                 print("Greatest directional Change per unit time",0, "deg/minute")
                 #print the greatest directional change per unit time  0 ,if the storm doesnt travel any distance

storm_charasterstics()
storm_per_year()
Hurricanes_per_year()
Storm_speed()