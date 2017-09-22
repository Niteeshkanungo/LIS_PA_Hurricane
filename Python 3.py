
from collections import Counter
from pygeodesy import ellipsoidalVincenty as ev

with open('hurdat2-nepac-1949-2016-041317.txt','r', ) as x:
    lines = x.readlines()
for i in range(len(lines)):                                                # looping on everyline in text file as a string
    if lines[i].startswith("EP",0,2) or lines[i].startswith("CP",0,2) :    #condition testing the strom name
        z = lines[i].split(sep=",")                                        # splitting each element in a line as a separate string
        y = int(z[2])                                                      # converting string to integer
        print ("STROM NAME:",lines[i][19:28].strip())                      #print the strom name by stripping off the white spaces
        print ("Date Range:",lines[i+1][4:6],"/",lines[i+1][6:8],"/",lines[i+1][0:4],"to",lines[i+y][4:6],"/",lines[i+y][6:8],"/",lines[i+y][0:4])  #printing data range of each strom
        k=[]                                                               #creating the empty list

        count=0                                                            #initialize count to zero
        for l in range(y):                                                 #loop for creating list of sustained winds and counting the number of landstrom for each strom
            k.append((lines[i+l+1][38:41]))                                #appending elements into the array

            if lines[i+1+l][16]=="L":                                      #testing the condition for landstrom
                count=count+1
        a=(max(k))                                                         #function to find the maximum sustained wind
        g=k.index(a)                                                       #find index on which maximum sustained wind occurs
        print ("Maximum sustained winds:",a,"Knots")                       #print the maximum sustained winds for each strom
        print("Date:",lines[i+g+1][4:6], "/", lines[i+g+1][6:8], "/", lines[i+g+1][0:4])  #print the date on which maximum sustained wind occurs
        print("Time:",lines[i + g + 1][10:12],":", lines[i + g + 1][12:14])               #print the time on which maximum sustained wind occurs
        print("Landfall:",count)                                                          #print the landfall count for each strom

J=[]
for i in range(len(lines)):                                                #for loop for counting stroms per year
    if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0,2) : #condition for testing the strom block
        J.append(lines[i][4:8])                                            #appending the year in the array
print ("Stroms per Year:")
a = dict(Counter(J))                                                       #counting the frequency of each elemenr in the list and converting it into dictionary
print (a)

I=[]                                                                                           #creating an empty array for appending years in the array
for i in range(len(lines)):                                                                    #loop for reading lines in the file
    if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0, 2):                     #testing the condition for starting of strom
        z = lines[i].split(sep=",")                                                            #splitting each element in a line as a separate string
        y = int(z[2])
        for n in range(y):                                                                     #loop for reading a particular strom
            if lines[n+i+1][19:21]=="HU":                                                       #testing the condition for hurricane
                I.append(lines[i+1][0:4])                                                       #appending the year on which strom occur into the array
                break                                                                           #coming out of the inner loop
b=dict(Counter(I))                                                                             #converting array into dictionary and counting the frequency of each element
print("Hurricane per year:")
print (b)                                                                                      #printing the dictionary


for i in range(len(lines)):                                                                    #loop for reading lines in the file
    if lines[i].startswith("EP", 0, 2) or lines[i].startswith("CP", 0, 2):                     #testing the condition for starting of strom
        z = lines[i].split(sep=",")                                                            #splitting each element in a line as a separate string
        y = int(z[2])

        q=[]                                                                                   #create an empty array
        for n in range(y-1):                                                                   #loop for iteration into individual strom

            a=ev.LatLon(lines[i+n+1][23:28].strip(),lines[i+n+1][30:36].strip())                 #passing latitute and longitude point into the function
            b =ev.LatLon(lines[i+n+2][23:28].strip(),lines[i+n+2][30:36].strip())                #passing latitude nad longitude point into the function
            try:
                s=(a.distanceTo(b))                                                                  #calculate distance from point A to B
            except ev.VincentyError:
                s=0
            s=s/1852.0                                                                           #convert meters to nautical miles
            if lines[i+n+2][10:12].startswith("00",0,2):                                         #condition for time calculation
              c=int(lines[i+n+2][10:14])
              b=c+2400                                                                            #Addition of 2400 to 0000
              f=str(abs(int(lines[i+n+1][10:14])-b))                                              #calcuation of time ,a strom has travelled

              if f[0]=="0":                                                                        #condition to convert hours to minutes
                w=int(f[1])*60 + int(f[2:4])
                q.append(s/w)                                                                      #calculation of speed

              else:
                w=int(f[0:2])*60+int(f[2:4])                                                       #condition for converting hours to minutes
                q.append(s/w)                                                                      #calculation of speed and putting it into array

            else:
               f=int(lines[i + n + 1][10:14]) - int(lines[i + n + 2][10:14])                  #time calculation
               f=str(abs(f))                                                                  #taking absolute value

               if f=="0":                                                                     #checking condition for converting the time to minutes
                   w = int(f[1]) * 60 + int(f[2:4])                                           #conversion of hours to minutes
                   q.append(s / w)                                                            #calculate speed and append into array

               else:
                   w = int(f[0:2]) * 60 + int(f[2:4])
                   q.append(s/w)

        print("STROM NAME:", lines[i][19:28].strip())                                           #print strom name
        print (q)                                                                               #print speed array of each strom
        try:
         print ("Maximum speed:",max(q),"miles/minute")                                          #print the maximum speed
        except ValueError:
         print ("Maximum Speed",0,"miles/minute")



