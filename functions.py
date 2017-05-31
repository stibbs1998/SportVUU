import xml.etree.ElementTree as et # import etree
import numpy as np
import matplotlib.pylab as plt

time = [] 

bx = []
by = []
bz = [] 

p3234x = []
p3234y = []
p3234z = []
p3234t = []

p295809x = []
p295809y = []
p295809z = []
p295809t = []

p463135x = []
p463135y = []
p463135z = []
p463135t = []

p552336x = []
p552336y = []
p552336z = []
p552336t = []

p698635x = []
p698635y = []
p698635z = []
p698635t = []

p173520x = []
p173520y = []
p173520z = []
p173520t = []

p699947x = []
p699947y = []
p699947z = []
p699947t = []

p65820x = []
p65820y = []
p65820z = []
p65820t = []

p606701x = []
p606701y = []
p606701z = []
p606701t = []

p552309x = []
p552309y = []
p552309z = []
p552309t = []

p922594x = []
p922594y = []
p922594z = []
p922594t = []

p401093x = []
p401093y = []
p401093z = []
p401093t = []

p555263x = []
p555263y = []
p555263z = []
p555263t = []

p214168x = []
p214168y = []
p214168z = []
p214168t = []

p338365x = []
p338365y = []
p338365z = []
p338365t = []

p457611x = []
p457611y = []
p457611z = []
p457611t = []

p468895x = []
p468895y = []
p468895z = []
p468895t = []

p847005x = []
p847005y = []
p847005z = []
p847005t = []

p168051x = []
p168051y = []
p168051z = []
p168051t = []

p333212x = []
p333212y = []
p333212z = []
p333212t = []

p504523x = []
p504523y = []
p504523z = []
p504523t = []

p253980x = []
p253980y = []
p253980z = []
p253980t = []

p57934x = []
p57934y = []
p57934z = []
p57934t = []

p609569x = []
p609569y = []
p609569z = []
p609569t = []

p846499x = []
p846499y = []
p846499z = []
p846499t = []

p3234m = 111.1 # Dirk
p65820m = 83.9 # Devin Harris
p173520m = 83.9 # JJ Barea
p295809m = 99.8 # Wesley Matthews
p401093m = 83.9 # Manny Harris
p463135m = 83.9 # Seth Curry
p555263m = 111.1 # Sala Mejri
p552309m = 108.9 # Dwight Powell
p552336m = 102.1 # Harrison Barnes
p606701m = 99.8 # Dorian Finney-Smith
p698635m = 81.6 # Yogi
p699947m = 103.4 # Nerlens Noel
p922594m = 97.5 # Nicolas Brussino

#### Warriors ####
p57934m = 113.4 # David West
p168051m = 102.5 # Matt Barnes
p214168m = 124.7 # Zaza Pachulia
p253980m = 87.1 # Shaun Livingston
p333212m = 122.5 # JaVale McGee
p338365m = 86.2 # Steph Curry
p457611m = 97.5 # Klay Thompson
p468895m = 104.3 # Draymond Green
p504523m = 79.4 # Ian Clark
p609569m = 108.9 # James Michael-McAdoo
p846499m = 99.8 # Kevon Looney
p847005m = 83.9 # Patrick McCaw



def position (filename):
    tree = et.parse(filename)
    root = tree.getroot()
    
    for a in root.iter('sequences'):
        r = (float)(a.attrib['period'])
        
        #r = get(period)
        for b in root.iter('moment'):
        
            
            
            temp = b.attrib['locations']
            temp = temp.split(";")
            clock = (float)(b.attrib['game-clock'])
            if r == 1:
                clock = abs(clock - 720.0)
            elif r == 2:
                clock = abs(clock - 1440.0)
            elif r == 3:
                clock = abs(clock - 2160.0)
            elif r == 4:
                clock = (float)(abs(clock - 2880.0))
    
            time.append(clock)
    
            for i in range(0,len(temp)):
                t = temp[i].split(",")
#       
################ BALL #####################
                if i%11 == 0:
                    bx.append((float)(t[2]))
                    by.append((float)(t[3]))
                    bz.append((float)(t[4]))
                
################# MAVS ####################                
                if (int)(t[1]) == 3234:
                    p3234t.append(clock)
                    p3234x.append((float)(t[2]))
                    p3234y.append((float)(t[3]))
                    p3234z.append((float)(t[4]))
                
                
                elif (int)(t[1]) == 295809:
                    
                    p295809t.append(clock)
                    p295809x.append((float)(t[2]))
                    p295809y.append((float)(t[3]))
                    p295809z.append((float)(t[4]))
                
                elif (int)(t[1]) == 463135:
                    
                    p463135t.append(clock)
                    p463135x.append((float)(t[2]))
                    p463135y.append((float)(t[3]))
                    p463135z.append((float)(t[4]))    

                elif (int)(t[1]) == 698635:
                    
                    p698635t.append(clock)
                    p698635x.append((float)(t[2]))
                    p698635y.append((float)(t[3]))
                    p698635z.append((float)(t[4]))

                elif (int)(t[1]) == 173520:
                   
                    p173520t.append(clock)
                    p173520x.append((float)(t[2]))
                    p173520y.append((float)(t[3]))
                    p173520z.append((float)(t[4]))   

                elif (int)(t[1]) == 699947:
                   
                    p699947t.append(clock)
                    p699947x.append((float)(t[2]))
                    p699947y.append((float)(t[3]))
                    p699947z.append((float)(t[4]))   

                elif (int)(t[1]) == 552336:
                   
                    p552336t.append(clock)
                    p552336x.append((float)(t[2]))
                    p552336y.append((float)(t[3]))
                    p552336z.append((float)(t[4]))   

                elif (int)(t[1]) == 65820:
                    p65820t.append(clock)
                    p65820x.append((float)(t[2]))
                    p65820y.append((float)(t[3]))
                    p65820z.append((float)(t[4]))

                elif (int)(t[1]) == 606701:
                    p606701t.append(clock)
                    p606701x.append((float)(t[2]))
                    p606701y.append((float)(t[3]))
                    p606701z.append((float)(t[4]))

                elif (int)(t[1]) == 922594:
                    p922594t.append(clock)
                    p922594x.append((float)(t[2]))
                    p922594y.append((float)(t[3]))
                    p922594z.append((float)(t[4]))    

                elif (int)(t[1]) == 552309:
                    p552309t.append(clock)
                    p552309x.append((float)(t[2]))
                    p552309y.append((float)(t[3]))
                    p552309z.append((float)(t[4]))

                elif (int)(t[1]) == 401093:
                    p401093t.append(clock)
                    p401093x.append((float)(t[2]))
                    p401093y.append((float)(t[3]))
                    p401093z.append((float)(t[4]))

                elif (int)(t[1]) == 555263:
                    p555263t.append(clock)
                    p555263x.append((float)(t[2]))
                    p555263y.append((float)(t[3]))
                    p555263z.append((float)(t[4]))

    ###################### WARRIORS ########################

                elif (int)(t[1]) == 214168:
                    p214168t.append(clock)
                    p214168x.append((float)(t[2]))
                    p214168y.append((float)(t[3]))
                    p214168z.append((float)(t[4]))

                elif (int)(t[1]) == 338365:
                    p338365t.append(clock)
                    p338365x.append((float)(t[2]))
                    p338365y.append((float)(t[3]))
                    p338365z.append((float)(t[4]))

                elif (int)(t[1]) == 457611:
                    p457611t.append(clock)
                    p457611x.append((float)(t[2]))
                    p457611y.append((float)(t[3]))
                    p457611z.append((float)(t[4]))

                elif (int)(t[1]) == 468895:
                    p468895t.append(clock)
                    p468895x.append((float)(t[2]))
                    p468895y.append((float)(t[3]))
                    p468895z.append((float)(t[4]))

                elif (int)(t[1]) == 847005:
                    p847005t.append(clock)
                    p847005x.append((float)(t[2]))
                    p847005y.append((float)(t[3]))
                    p847005z.append((float)(t[4]))

                elif (int)(t[1]) == 168051:
                    p168051t.append(clock)
                    p168051x.append((float)(t[2]))
                    p168051y.append((float)(t[3]))
                    p168051z.append((float)(t[4]))

                elif (int)(t[1]) == 333212:
                    p333212t.append(clock)
                    p333212x.append((float)(t[2]))
                    p333212y.append((float)(t[3]))
                    p333212z.append((float)(t[4]))

                elif (int)(t[1]) == 504523:
                    p504523t.append(clock)
                    p504523x.append((float)(t[2]))
                    p504523y.append((float)(t[3]))
                    p504523z.append((float)(t[4]))

                elif (int)(t[1]) == 253980:
                    p253980t.append(clock)
                    p253980x.append((float)(t[2]))
                    p253980y.append((float)(t[3]))
                    p253980z.append((float)(t[4]))

                elif (int)(t[1]) == 57934:
                    p57934t.append(clock)
                    p57934x.append((float)(t[2]))
                    p57934y.append((float)(t[3]))
                    p57934z.append((float)(t[4]))

                elif (int)(t[1]) == 609569:
                    p609569t.append(clock)
                    p609569x.append((float)(t[2]))
                    p609569y.append((float)(t[3]))
                    p609569z.append((float)(t[4]))

                elif (int)(t[1]) == 846499:
                    p846499t.append(clock)
                    p846499x.append((float)(t[2]))
                    p846499y.append((float)(t[3]))
                    p846499z.append((float)(t[4]))



#
#####################################################################
                
def getPlayerNumbers(filename):
    tree = et.parse(filename)
    root = tree.getroot()
    
    for a in root.iter('moment'):
        temp = a.attrib['locations']
        temp = temp.split(";")
        
    
        t = []
        for i in range(0,len(temp)):
            t = temp[i].split(",")
        
        
            if (int)(t[0]) == 6:
                if (int)(t[1]) not in mavsID:
                    mavsID.append((int)(t[1]))
            elif (int)(t[0]) == 9:
                if (int)(t[1]) not in warriorsID:
                    warriorsID.append((int)(t[1]))


def distance(x1, x2, y1, y2, z1, z2):
    dis = 0
    dis += np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2) * 0.3048  ### Converts from ft/s ---> m/s ###
    return dis

def allDistance(x, y, z):
    d = []
    for i in range(0, len(x)):
        d.append(distance(x[i], x[i-1], y[i], y[i-1], z[i], z[i-1]))
    return d
def posToVel(d,t):
    boo = True
    v = []
    holder = []
    for i in range(0, len(d)-2):
        if abs(((float)(t[i+2])-(float)(t[i]))) > .01 and abs(((float)(t[i+2])-(float)(t[i]))) < .09:
            v.append(abs(((float)(d[i+2])-(float)(d[i])/((float)(t[i+2])-(float)(t[i])))))
        else:
            v.append(0)

    if len(v) != len(t):
        del t[0]
        del t[len(t)-1]
####### accounts for outlying points, v > 32 fps ( 22 mph) ############
    for j in range(0,len(v)):
        if v[j] > 10:
                v[j] = v[j-1]

    return v

def percentage(velocity):
    
    ###################
    
    on_bench = 0
    percent_over_0 = 0
    percent_over_0_5 = 0
    percent_over_1_0 = 0
    percent_over_1_0 = 0
    percent_over_1_5 = 0 
    percent_over_2_0 = 0
    percent_over_2_5 = 0
    percent_over_3_0 = 0
    percent_over_3_5 = 0
    percent_over_4_0 = 0
    ##############################
    for i in range(0,len(velocity)):
        
        if velocity[i]>=4.0:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            percent_over_1_5 += 1
            percent_over_2_0 += 1
            percent_over_2_5 += 1
            percent_over_3_0 += 1
            percent_over_3_5 += 1
            percent_over_4_0 += 1
        
        elif velocity[i]>= 3.5:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            percent_over_1_5 += 1
            percent_over_2_0 += 1
            percent_over_2_5 += 1
            percent_over_3_0 += 1
            percent_over_3_5 += 1
            percent_over_4_0 += 1
            percent_over_3_5 += 1
            
        
        elif velocity[i]>= 3.0:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            percent_over_1_5 += 1
            percent_over_2_0 += 1
            percent_over_2_5 += 1            
            percent_over_3_0 += 1
        
        
        
        elif velocity[i]>= 2.5:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            percent_over_1_5 += 1
            percent_over_2_0 += 1
            percent_over_2_5 += 1
            
            
        elif velocity[i]>= 2.0:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            percent_over_1_5 += 1
            percent_over_2_0 += 1
            
            
        
        elif velocity[i]>= 1.5:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            percent_over_1_5 += 1 
            

        elif velocity[i]>= 1.0:
            percent_over_0 += 1
            percent_over_0_5 += 1
            percent_over_1_0 += 1
            
            
        elif velocity[i]>= 0.5:
            percent_over_0_5 += 1
            percent_over_0 += 1
        
        elif velocity[i]>= 0.1:
            percent_over_0 += 1
        else:
            on_bench += 1
            
        ########################################  
        
    x = len(velocity) - on_bench
    if x == 0:
        return 0
    zero = 1.0 * (float)(percent_over_0)/x     
    zero_five = 1.0*(float)(percent_over_0_5)/x
    
    one = 1.0*(float)(percent_over_1_0)/x
    one_five = 1.0*(float)(percent_over_1_5)/x
    
    two = 1.0*(float)(percent_over_2_0)/x
    two_five = 1.0*(float)(percent_over_2_5)/x
    
    three = 1.0*(float)(percent_over_3_0)/x
    three_five = 1.0*(float)(percent_over_3_5)/x
    
    four = 1.0*(float)(percent_over_4_0)/(x)
    

    return zero, zero_five, one, one_five, two, two_five, three, three_five, four

def getQuarterVelo(t, v, qnum):
    vq = []
    
    if qnum == 1:
        for i in range(0, len(t)):
            if t[i] <= 720.0:
                if len(v) > i:
                    vq.append(v[i])
                else:
                    vq.append(0)
    elif qnum == 2:
        for i in range(0, len(t)):
            if t[i] >= 720.0 and t[i] <= 1440.0:
                if len(v) > i:
                    vq.append(v[i])
                else:
                    vq.append(0)
    elif qnum == 3:
        for i in range(0, len(t)):
            if t[i] >= 1440.0 and t[i] <= 2160.0:                     
                if len(v) > i:
                    vq.append(v[i])
                else:
                    vq.append(0)
    elif qnum == 4:
        for i in range(0, len(t)):
            if t[i] <= 2160.0:
                if len(v) > i:
                    vq.append(v[i])
                else:
                    vq.append(0)
                
    return vq

def getMiles(d):
    sumDistance = 0
    for i in range(0, len(d)):
        sumDistance += d[i]
    sumDistance = 82.0 * sumDistance / 1000.0
    return sumDistance*0.621371

def power(velocity,mass): # when entering mass and velocity, make sure player numbers match up!
    holder = []
    k_instantaneous = []
    ticks = 0
    for i in range(0,len(velocity)):
        
        holder.append( 0.5 * mass * velocity[i]**2 )
        ticks += 1
        if ticks == 25:
            x = float(sum(holder)/len(holder))
            k_instantaneous.append(x)
            
            
            holder = []
            ticks = 0
        
    return k_instantaneous

def power_by_min(velocity,mass): # when entering mass and velocity, make sure player numbers match up!
    holder = []
    k_instantaneous = []
    ticks = 0
    for i in range(0,len(velocity)):
        
        holder.append( 0.5 * mass * velocity[i]**2 )
        ticks += 1
        if ticks == 1500:   # the product of 25 times 60 (or 1 minute)
            x = float(sum(holder)/len(holder))
            k_instantaneous.append(x)
            
            
            holder = []
            ticks = 0
        
    return k_instantaneous

p3234v = posToVel(allDistance(p3234x, p3234y, p3234z), p3234t)
p463135v = posToVel(allDistance(p463135x, p463135y, p463135z), p463135t)
p606701v = posToVel(allDistance(p606701x, p606701y, p606701z), p606701t)
p698635v = posToVel(allDistance(p698635x, p698635y, p698635z), p698635t)
p699947v = posToVel(allDistance(p699947x, p699947y, p699947z), p699947t)
p552309v = posToVel(allDistance(p552309x, p552309y, p552309z), p552309t)
p295809v = posToVel(allDistance(p295809x, p295809y, p295809z), p295809t)
p552336v = posToVel(allDistance(p552336x, p552336y, p552336z), p552336t)
p922594v = posToVel(allDistance(p922594x, p922594y, p922594z), p922594t)
p401093v = posToVel(allDistance(p401093x, p401093y, p401093z), p401093t)
p555263v = posToVel(allDistance(p555263x, p555263y, p555263z), p555263t)
p65820v = posToVel(allDistance(p65820x, p65820y, p65820z), p65820t)
p173520v = posToVel(allDistance(p173520x, p173520y, p173520z), p173520t)
# ### DUBS ###
p57934v = posToVel(allDistance(p57934x, p57934y, p57934z), p57934t)
p168051v = posToVel(allDistance(p168051x, p168051y, p168051z), p168051t)
p253980v = posToVel(allDistance(p253980x, p253980y, p253980z), p253980t)
p457611v = posToVel(allDistance(p457611x, p457611y, p457611z), p457611t)
p504523v = posToVel(allDistance(p504523x, p504523y, p504523z), p504523t)
p468895v = posToVel(allDistance(p468895x, p468895y, p468895z), p468895t)
p847005v = posToVel(allDistance(p847005x, p847005y, p847005z), p847005t)
p609569v = posToVel(allDistance(p609569x, p609569y, p609569z), p609569t)
p846499v = posToVel(allDistance(p846499x, p846499y, p846499z), p846499t)
p338365v = posToVel(allDistance(p338365x, p338365y, p338365z), p338365t)
p214168v = posToVel(allDistance(p214168x, p214168y, p214168z), p214168t)
p333212v = posToVel(allDistance(p333212x, p333212y, p333212z), p333212t)

def to_string(velocity):
    if velocity == p57934v:
        return "David West"
    elif velocity == p168051v:
        return "Matt Barnes"
    elif velocity == p214168v:
        return "Zaza Pachulia"
    elif velocity == p253980v:
        return "Shaun Livingston"
    elif velocity == p333212v:
        return "JaVale McGee"
    elif velocity == p338365v:
        return "Steph Curry"
    elif velocity == p457611v:
        return "Klay Thompson"
    elif velocity == p468895v:
        return "Draymond Green"
    elif velocity == p504523v:
        return "Ian Clark"
    elif velocity == p609569v:
        return "J. Michael-McAdoo"
    elif velocity == p846499v:
        return "Kevon Looney"
    elif velocity == p847005v:
        return "Patrick McCaw"
    
    
    ##########################
    elif velocity == p3234v:        
        return "Dirk Nowitzki"
    elif velocity == p65820v:
        return "Devin Harris"
    elif velocity == p173520v:
        return "J.J. Barea"
    elif velocity == p295809v:
        return "W. Matthews"
    elif velocity == p401093v:
        return "Manny Harris"
    elif velocity == p463135v:
        return "Seth Curry"
    elif velocity == p555263v:
        return "Salah Mejri"
    elif velocity == p552309v:
        return "Dwight Powell"
    elif velocity == p552336v:
        return "Harrison Barnes"
    elif velocity == p606701v:
        return "D. Finney-Smith"
    elif velocity == p698635v:
        return "Yogi Ferrell"
    elif velocity == p699947v:
        return "Nerlens Noel"
    elif velocity == p922594v:
        return "Nicolas Brussino"

