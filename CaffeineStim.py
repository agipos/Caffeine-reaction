
# coding: utf-8

# In[6]:

#This was just to see where you should put the .mat file in order 
#to evaluate this code. 
import os 
os.getcwd()


# In[7]:

#These are the libraries we will be needing
import matplotlib.pyplot as plot 
import scipy.io
import numpy as np


# In[8]:

#This is to load the .mat data 
reactionData = scipy.io.loadmat('Assignment1_data.mat')


# In[9]:

#Assigning variable names to the data 
data_control = reactionData['data_control']
data_caffeine200 = reactionData['data_caffeine_200']
data_caffeine400 = reactionData['data_caffeine_400']
stim_time_control = reactionData['stimTime_control']
stim_time_caffeine200 = reactionData['stimTime_caffeine_200']
stim_time_caffeine400 = reactionData['stimTime_caffeine_400']


# In[10]:

#Casting the data into a workable type  
import numpy as np
dataControl = data_control.astype(np.int16)
dataCaffeine200 = data_caffeine200.astype(np.int16)
dataCaffeine400 = data_caffeine400.astype(np.int16) 
stimTimeControl = stim_time_control.astype(np.int16)
stimTimeCaffeine200 = stim_time_caffeine200.astype(np.int16)
stimTimeCaffeine400 = stim_time_caffeine400.astype(np.int16)


# In[11]:

#This gets the actual reaction time 
RT_control = dataControl-stimTimeControl
RT_caffeine200 = dataCaffeine200-stimTimeCaffeine200
RT_caffeine400 = dataCaffeine400-stimTimeCaffeine400


# In[12]:

# Here is where we seperate the valid trials from the invalid trials, and 
# assign them to a new variable.  
def valid(element):
    return element > 0
validTrials_control = filter(valid,RT_control)
validTrials_caffeine200 = filter(valid,RT_caffeine200)
validTrials_caffeine400 = filter(valid,RT_caffeine400)


# In[13]:

get_ipython().magic(u'matplotlib inline')

# setting up the plots
plot1 = plot.plot(validTrials_control)
plot.setp(plot1,color='k',linewidth=2,label='Control')
plot2 = plot.plot(validTrials_caffeine200)
plot.setp(plot2,color='b',linewidth=2,label='200 mg')
plot3 = plot.plot(validTrials_caffeine400)
plot.setp(plot3,color='r',linewidth=2,label='400 mg')

# defining axes limits
plot.axis([0, 275, 0, 4100])

# setting up the labels
plot.xlabel('Valid Trials',fontsize=14)
plot.ylabel('Reaction Time per Trial in milliseconds',fontsize=14)
plot.title('Caffeine reaction time effect',fontsize=14)

# setting up the legend
legend = plot.legend(loc='best')
plot.setp(plot.gca().get_legend().get_texts(),fontsize='12')

plot.show()


# In[ ]:



