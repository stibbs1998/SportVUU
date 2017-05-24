
# coding: utf-8

# In[387]:

# 5/23
import xml.etree.ElementTree as et # import etree
import numpy as np
import matplotlib.pylab as plt
get_ipython().magic(u'matplotlib notebook')



tree = et.parse('quarter1.XML')
root = tree.getroot()
time = [] 
for n in root.iter('moment'):
    time.append(n.attrib['game-clock'])
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


def position (filename):
    tree = et.parse(filename)
    root = tree.getroot()
    
    
    for b in root.iter('moment'):
        
        
        temp = b.attrib['locations']
        temp = temp.split(";")
        
    
    
        for i in range(0,len(temp)):
            t = temp[i].split(",")
#             if (int)(t[1]) == 3234:
#                 p3234t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 295809:
                p295809t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 463135:
                p463135t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 698635:
                p698635t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 173520:
                p173520t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 699947:
                p699947t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 65820:
                p65820t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 606701:
                p606701t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 922594:
                p922594t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 552309:
                p552309t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 401093:
                p401093t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 555263:
                p555263t.append((float)(b.attrib['game-clock']))
                
                ################################################
                
            if (int)(t[1]) == 214168:
                p214168t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 338365:
                p338365t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 457611:
                p457611t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 468895:
                p468895t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 847005:
                p847005t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 168051:
                p168051t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 333212:
                p333212t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 504523:
                p504523t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 253980:
                p253980t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 57934:
                p57934t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 609569:
                p609569t.append((float)(b.attrib['game-clock']))
            if (int)(t[1]) == 846499:
                p846499t.append((float)(b.attrib['game-clock']))
################ BALL #####################
            if i%11 == 0:
                bx.append((float)(t[2]))
                by.append((float)(t[3]))
                bz.append((float)(t[4]))
                
################# MAVS ####################                
            if (int)(t[1]) == 3234:
                p3234t.append((float)(b.attrib['game-clock']))
                p3234x.append((float)(t[2]))
                p3234y.append((float)(t[3]))
                p3234z.append((float)(t[4]))
                
                
            elif (int)(t[1]) == 295809:
                p295809x.append((float)(t[2]))
                p295809y.append((float)(t[3]))
                p295809z.append((float)(t[4]))
                
            elif (int)(t[1]) == 463135:
                p463135x.append((float)(t[2]))
                p463135y.append((float)(t[3]))
                p463135z.append((float)(t[4]))    
                
            elif (int)(t[1]) == 698635:
                p698635x.append((float)(t[2]))
                p698635y.append((float)(t[3]))
                p698635z.append((float)(t[4]))
            
            elif (int)(t[1]) == 173520:
                p173520x.append((float)(t[2]))
                p173520y.append((float)(t[3]))
                p173520z.append((float)(t[4]))   
            
            elif (int)(t[1]) == 699947:
                p699947x.append((float)(t[2]))
                p699947y.append((float)(t[3]))
                p699947z.append((float)(t[4]))   
            
            elif (int)(t[1]) == 65820:
                p65820x.append((float)(t[2]))
                p65820y.append((float)(t[3]))
                p65820z.append((float)(t[4]))
                
            elif (int)(t[1]) == 606701:
                p606701x.append((float)(t[2]))
                p606701y.append((float)(t[3]))
                p606701z.append((float)(t[4]))
                
            elif (int)(t[1]) == 922594:
                p922594x.append((float)(t[2]))
                p922594y.append((float)(t[3]))
                p922594z.append((float)(t[4]))    
            
            elif (int)(t[1]) == 552309:
                p552309x.append((float)(t[2]))
                p552309y.append((float)(t[3]))
                p552309z.append((float)(t[4]))
                
            elif (int)(t[1]) == 401093:
                p401093x.append((float)(t[2]))
                p401093y.append((float)(t[3]))
                p401093z.append((float)(t[4]))
                
            elif (int)(t[1]) == 555263:
                p555263x.append((float)(t[2]))
                p555263y.append((float)(t[3]))
                p555263z.append((float)(t[4]))
                
###################### WARRIORS ########################
            
            elif (int)(t[1]) == 214168:
                p214168x.append((float)(t[2]))
                p214168y.append((float)(t[3]))
                p214168z.append((float)(t[4]))
            
            elif (int)(t[1]) == 338365:
                p338365x.append((float)(t[2]))
                p338365y.append((float)(t[3]))
                p338365z.append((float)(t[4]))
                
            elif (int)(t[1]) == 457611:
                p457611x.append((float)(t[2]))
                p457611y.append((float)(t[3]))
                p457611z.append((float)(t[4]))
                
            elif (int)(t[1]) == 468895:
                p468895x.append((float)(t[2]))
                p468895y.append((float)(t[3]))
                p468895z.append((float)(t[4]))
                
            elif (int)(t[1]) == 847005:
                p847005x.append((float)(t[2]))
                p847005y.append((float)(t[3]))
                p847005z.append((float)(t[4]))
                
            elif (int)(t[1]) == 168051:
                p168051x.append((float)(t[2]))
                p168051y.append((float)(t[3]))
                p168051z.append((float)(t[4]))
                
            elif (int)(t[1]) == 333212:
                p333212x.append((float)(t[2]))
                p333212y.append((float)(t[3]))
                p333212z.append((float)(t[4]))
                
            elif (int)(t[1]) == 504523:
                p504523x.append((float)(t[2]))
                p504523y.append((float)(t[3]))
                p504523z.append((float)(t[4]))
                
            elif (int)(t[1]) == 253980:
                p253980x.append((float)(t[2]))
                p253980y.append((float)(t[3]))
                p253980z.append((float)(t[4]))
            
            elif (int)(t[1]) == 57934:
                p57934x.append((float)(t[2]))
                p57934y.append((float)(t[3]))
                p57934z.append((float)(t[4]))
                
            elif (int)(t[1]) == 609569:
                p609569x.append((float)(t[2]))
                p609569y.append((float)(t[3]))
                p609569z.append((float)(t[4]))
                
            elif (int)(t[1]) == 846499:
                p846499x.append((float)(t[2]))
                p846499y.append((float)(t[3]))
                p846499z.append((float)(t[4]))
                
                
position('quarter1.XML')
position('quarter2.XML')
position('quarter3.XML')
position('quarter4.XML')


# In[186]:

mavsID = []
warriorsID = []

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
    


# In[187]:


getPlayerNumbers('quarter1.XML')
getPlayerNumbers('quarter2.XML')
getPlayerNumbers('quarter3.XML')
getPlayerNumbers('quarter4.XML')


# In[188]:

print mavsID
print warriorsID


# In[351]:

###################### DISTANCE FORMULA ###########################
def distance(x1, x2, y1, y2, z1, z2):
    dis = 0
    dis += np.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2-z1)**2)
    return dis


# In[394]:

##################### TAKES IN 3 LISTS FOR INPUT ##################
def allDistance(x, y, z):
    d = []
    for i in range(0, len(x)):
        d.append(distance(x[i], x[i-1], y[i], y[i-1], z[i], z[i-1]))
    return d
###################################################################


# In[395]:

d = allDistance(p3234x, p3234y, p3234z)
############### FEET PER SECOND #####################
############## VELOCITY FUNCTION ####################
def posToVel(d,t):
    v = []
#     holder = []
    for i in range(0, len(d)-2):
        if abs(((float)(t[i+2])-(float)(t[i]))) > .01 and abs(((float)(t[i+2])-(float)(t[i]))) < .09:
            v.append(((float)(d[i+2])-(float)(d[i])/((float)(t[i+2])-(float)(t[i]))))
#         else:
#             holder.append(t[i])
#             holder.append(t[i+2])
#     for k in range(0,len(holder)):
#         if holder[k] in t:
#             t.remove(holder[k])
#     for i in range(0, len(d)-1):
#         if abs((float)(t[i+1])- (float)(t[i])) > .01 and abs((float)(t[i+1])- (float)(t[i])) < .05:
#             v.append(((float)(d[i+1]) - (float)(d[i]))/ ((float)(t[i+1])- (float)(t[i])))
        
    return v



print len(allDistance(p3234x, p3234y, p3234z))
print len(p3234t)
print len(p3234x)


# In[393]:

########## VELOCITY GLOBAL VARIALBES ################
### MAVS ###
p3234v = posToVel(allDistance(p3234x, p3234y, p3234z), p3234t)
# p463135v = posToVel(allDistance(p463135x, p463135y, p463135z), p463135t)
# p606701v = posToVel(allDistance(p606701x, p606701y, p606701z), p606701t)
# p698635v = posToVel(allDistance(p698635x, p698635y, p698635z), p698635t)
# p699947v = posToVel(allDistance(p699947x, p699947y, p699947z), p699947t)
# p552309v = posToVel(allDistance(p552309x, p552309y, p552309z), p552309t)
# p295809v = posToVel(allDistance(p295809x, p295809y, p295809z), p295809t)
# p552336v = posToVel(allDistance(p552336x, p552336y, p552336z), p552336t)
# p922594v = posToVel(allDistance(p922594x, p922594y, p922594z), p922594t)
# p698635v = posToVel(allDistance(p698635x, p698635y, p698635z), p698635t)
# p401093v = posToVel(allDistance(p401093x, p401093y, p401093z), p401093t)
# p555263v = posToVel(allDistance(p555263x, p555263y, p555263z), p555263t)
# p65820v = posToVel(allDistance(p65820x, p65820y, p65820z), p65820t)
# p173520v = posToVel(allDistance(p173520x, p173520y, p173520z), p173520t)
### DUBS ###
# p57934v = posToVel(allDistance(p57934x, p57934y, p57934z), p57934t)
# p168051v = posToVel(allDistance(p168051x, p168051y, p168051z), p168051t)
# p253980v = posToVel(allDistance(p253980x, p253980y, p253980z), p253980t)
# p457611v = posToVel(allDistance(p457611x, p457611y, p457611z), p457611t)
# p504523v = posToVel(allDistance(p504523x, p504523y, p504523z), p504523t)
# p468895v = posToVel(allDistance(p468895x, p468895y, p468895z), p468895t)
# p847005v = posToVel(allDistance(p847005x, p847005y, p847005z), p847005t)
# p609569v = posToVel(allDistance(p609569x, p609569y, p609569z), p609569t)
# p846499v = posToVel(allDistance(p846499x, p846499y, p846499z), p846499t)
# p338365v = posToVel(allDistance(p338365x, p338365y, p338365z), p338365t)
# p214168v = posToVel(allDistance(p214168x, p214168y, p214168z), p214168t)
# p333212v = posToVel(allDistance(p333212x, p333212y, p333212z), p333212t)


########################################################################
# plt.figure()
# plt.plot(p3234v, p3234t)
print len(p3234v)
print len(p3234t)


# # Mavericks
# 
#     *3234 - Dirk Nowitski 
#     *463135 - Seth Curry
#     *606701 - Dorian Finney-Smith
#     *698635 - Yogi Ferrell
#     *699947 - Nerlens Noel
#     *552309 - Dwight Powell
#     *295809 - Wesley Matthews
#     *552336 - Harrison Barnes
#     *922594 - Nicolas Brussino
#     *401093 - Manny Harris
#     *555263 - Salah Mejri
#     *65820 - Devin Harris
#     *173520 - JJ Barea
# # Warriors
# 
#     *57934 - David West
#     *168051 - Matt Barnes
#     *253980 - Shaun Livingston
#     *457611 - Klay Thompson
#     *504523 - Ian Clark
#     *468895 - Draymond Green
#     *847005 - Patrick McCaw
#     *609569 - James McAdoo
#     *846499 - Kevon Looney
#     *338365 - Steph Curry
#     *214168 - Zaza Pachulia
#     *333212 - Javal McGee
# 

# In[192]:

plt.figure()
plt.plot(p3234x, p3234y, linewidth = 0.3)
plt.plot(p295809x, p295809y, linewidth = 0.3)
plt.plot(p463135x, p463135y, linewidth = 0.3)
plt.plot(p606701x, p606701y, linewidth = .3)
plt.plot(p698635x, p698635y, linewidth = .3)
plt.plot(p699947x, p699947y, linewidth = .3)
plt.plot(p552309x, p552309y, linewidth = .3)
plt.plot(p922594x, p922594y, linewidth = .3)
plt.plot(p401093x, p401093y, linewidth = .3)
plt.plot(p555263x, p555263y, linewidth = .3)
plt.plot(p65820x, p65820y, linewidth = .3)
plt.plot(p173520x, p173520y, linewidth = .3)
plt.plot(p552336x, p552336y, linewidth = .3)
plt.title("Mavericks Quarters 1-4")


# In[193]:

print mavsID
print warriorsID



# In[194]:

plt.figure()
plt.plot(p57934x, p57934y, linewidth = 0.3)
plt.plot(p168051x, p168051y, linewidth = 0.3)
plt.plot(p253980x, p253980y, linewidth = 0.3)
plt.plot(p457611x, p457611y, linewidth = .3)
plt.plot(p504523x, p504523y, linewidth = .3)
plt.plot(p468895x, p468895y, linewidth = .3)
plt.plot(p847005x, p847005y, linewidth = .3)
plt.plot(p609569x, p609569y, linewidth = .3)
plt.plot(p846499x, p846499y, linewidth = .3)
plt.plot(p338365x, p338365y, linewidth = .3)
plt.plot(p214168x, p214168y, linewidth = .3)
plt.plot(p333212x, p333212y, linewidth = .3)

plt.title("Warriors Quarters 1-4")


# In[363]:

########## TIME FUNCTION ##################
time_ascending = []

def time(filename):

    tree = et.parse(filename)
    root = tree.getroot()
    
    for b in root.iter('sequences'):
        t = b.attrib['period']
        
    for a in root.iter('moment'):
        r = (float)(a.attrib['game-clock'])
        
        q = r/60.0
        if (float)(t) == 1:
            time_ascending.append(12.0-q)
        elif (float)(t) == 2:
            time_ascending.append(24.0-q)
        elif (float)(t) == 3:
            time_ascending.append(36.0-q)
        elif (float)(t) == 4:
            time_ascending.append(48.0-q)



# In[364]:

time('quarter1.XML')
time('quarter2.XML')
time('quarter3.XML')
time('quarter4.XML')


# In[ ]:



