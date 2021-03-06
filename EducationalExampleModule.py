# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:25:24 2018

@author: Mingming
"""
import numpy as np
import matplotlib.pyplot as plt 


#%%
################################################################
##################  EDUCATIONAL EXAMPLE ########################
################################################################

"""
FFT EXAMPLE
https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python

An educational example showing how to use fft to analyze signal in 
frequency domain.
"""
def fftExample():
    from scipy.fftpack import fft
    # Number of samplepoints
    N = 600
    # sample spacing
    T = 1.0 / 800.0
    # Signal in time domain
    x = np.linspace(0.0, N*T, N)
    y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    
    # Conduct fft and plot the signal as show case
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(x, y)
    plt.xlabel('time in s')
    plt.subplot(2,1,2)
    plt.plot(xf, 2.0/N * np.abs(yf[0:int(N/2)]))
    plt.xlabel('frequency')
    plt.grid()
    plt.show()







#%%  how to run a piece of code and check it is running time

import timeit
        
SETUP_CODE = ''' 
import EMGModule
import numpy as np
detect_start = 24
detect_end   = 96
my_wave = np.random.randint( -100 , high= 100, size = 257 )
'''
      
TEST_CODE = ''' 
threshold_res_label = EMGModule.TimeDomainTh(my_wave, detect_start, detect_end, care_noise='yes')  '''

# timeit.repeat statement 
times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 100) 
             
print('NormWave processing time: {}'.format(np.mean(times)))
        




#%%  how to plot and display time series signal in real time

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

plt.ion()  # turn the interactive mode on

fig = plt.figure(1)  # an instance of a figure plotting object
plt.clf()            # clear anything on current figure
# add an Axes instance to the figure as part of a subplot arrangement
ax     = fig.add_subplot(111) # Either a 3-digit integer or three separate integers describing the position of the subplot
line1, = ax.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 100):
    line1.set_ydata(np.sin(x + phase)) # update the ydata for next frame display
    fig.canvas.draw()                  # update the figure that has been altered
    fig.canvas.flush_events()    # speed up matplotlib plotting times

    
#%%  how to take the input from key board typing

from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

def on_release(key):
    #string = ('{0} release'.format(
      #  key))
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


#%%  how to plot and display signals real time

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

plt.ion()  # turn the interactive mode on

fig = plt.figure(1)  # an instance of a figure plotting object
plt.clf()            # clear anything on current figure
# add an Axes instance to the figure as part of a subplot arrangement
ax     = fig.add_subplot(111) # Either a 3-digit integer or three separate integers describing the position of the subplot
line1, = ax.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 100):
    
    line1.set_ydata(np.sin(x + phase)) # update the ydata for next frame display
    fig.canvas.draw()                  # update the figure that has been altered
    fig.canvas.flush_events()    # speed up matplotlib plotting times



#%% Example of writing data into a csv file
import csv
import pandas as pd
csvfile = open('eggs.csv', 'w', newline='')  # open a csv file in 'write' mode, will creat the file if the file is not exist
datawriter = csv.writer(csvfile)#,    # create a writer object
                            #delimiter=' ',  # a non-character string used to separate fields, defaults to ','
                            #quotechar='|')  # a non-character string used to quote fields containing special characters, defaults to '"'
                            #quoting=csv.QUOTE_NONNUMERIC)#, # instruct Writer object to never quote fields
                            #lineterminator='\n') # controls when quotes should be generated by the writer and recongnized by the reader
        
for count in range(3):
    my_data=[]
    for n in range(100):
        my_data.append(n*(count+1))
    datawriter.writerow(tuple(my_data))                     


# Then how to read the data back 
path       = "C:/Users/Mingming/Desktop/Work projects/Veressa/Data analysis"
file_name  = "eggs.csv"
df = pd.read_csv(path + "/" + file_name )   # read the data in as pandas data frame
data = df.values                            # convert the data frame into a numpy array


#%% example of generating a video with openCV
 
import cv2
import numpy as np
import pandas as pd

width   = 1280
height  = 720
FPS     = 24   # 24 frames per second
seconds = 10

fourcc = cv2.VideoWriter_fourcc(*'MP42')   # create a 4-byte code (FourCC) used to specify the video codec
video  = cv2.VideoWriter('./noise.avi',    # name of the output video
                         fourcc,           # 4-character code of codeC used to compress the frames
                         float(FPS),       # framerate of the created video stream
                         (width, height) ) # size of the video frames, a tuple (width, height)

for _ in range(FPS*seconds):
    frame = np.random.randint(0, 256, 
                              (height, width, 3), 
                              dtype=np.uint8)
    video.write(frame)

video.release()

#%%


#%% Turn an 1-D time series into a 2-D image. 
#  https://towardsdatascience.com/tensorflow-object-detection-api-ecg-analysis-8f456d563dfa
#  https://github.com/Nospoko/qrs-object/blob/master/main.ipynb

# TURN 1-D TIME SERIES SIGNAL INTO AN 2-D IMAGE.
#% FUNCTIONS
# Stretch helper, interpolate the signal to make it longer as required
def stretch(qrs, final_length):
    xa = np.linspace(0, 1, len(qrs))
    xb = np.linspace(0, 1, final_length)    
    longer = np.interp(xb, xa, qrs)    
    return longer

# Box generator
def get_box(qrs, box_half):
    # box_half = 64 # 64 points are 80 ms in time
    # Up and down are trivial
    top = qrs.min()
    bot = qrs.max()    
    
    # Find the middle point of the signal
    all_min_points =  np.where(qrs==qrs.min())[0]
    if len(all_min_points) == 1:
        middle = all_min_points# the lower peak defined as the middle point
    else:
        middle = all_min_points[0]
    #box_half = 64 # 64 points are 80 ms in time
    left = middle - box_half
    right = middle + box_half
    
    return left, right, top, bot


# Reshape to fit the screen
def reshape_img(qrs, top_offset, scale_factor):
    '''
    qrs, the original signal
    top_offset, half window of the imagie height   
    '''   
    # Rescale the qrs (and flip)
    qrs = -qrs  # in the final image, y-dimension axis is increasing from top to bottom
    qrs -= qrs.mean()
    qrs *= scale_factor

    # Prepare to be and y-position
    qrs += top_offset   
    return qrs


def EMG2Img(mysignal, final_length, scale_factor):
    # Rescale the signal based on user request

    top_offset  = final_length/2 # make the signal sits in the middle in the final images along y axis (height of the image)
    qrs = stretch(mysignal, final_length)
    qrs = reshape_img(qrs, top_offset, scale_factor)
    # Prepare the width (x) dimension of the image
    if final_length > len(mysignal): # 30, if the final signal image is wider than original signal,
        left_offset = (final_length - len(mysignal) )//2  # move the signal in the middle of the final image, along x axis (width of the image)                                                    
    else:
        left_offset = 0

    x = left_offset + np.arange(len(qrs)) # create the x dimension of the final image

    # Merge data into draw-able points for image
    mypoints=np.zeros((len(x),1,2),dtype='int32') #  data needs to be 'int32'
    for n in range(len(x)):  # 512 points, 1 channel of color, 2 dimensional coordinates, Don't know why in this format?????
        mypoints[n,:,:] = np.reshape( [x[n], qrs[n]], [1,2] )  # [512, 1, 2]

    # Prepare an background image of little noise
    img0 = np.random.randint(10, size = [final_length, final_length,3], dtype = 'uint8')
    # Draw signal on the canvas (great color control btw)
    cv2.polylines(img0, [mypoints], isClosed=False, color=(255, 255, 255), thickness = 2)     
    # Make it black and white
    img = cv2.bitwise_not(img0)

    #plt.figure()
    #plt.imshow(img)
    
    return img



#%%