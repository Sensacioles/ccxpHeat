import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import cv2

#Input your data here, the values themselves can be ordered or not 
stickersLocations = {
    'a': [4,5,26,3,15,12,15,15,4,37,5,5,6,3],
    'b': [18,6,27,23,24,23,24,27,18],
    'c': [28,6],
    'd': [6,17],
    'e': [9,5,7,7,9,11,29,5,6,36,36,12,13,6,3,11,4],
    'f': [16,43,44,30,25,16,43,44,1,2,19,21,22,25,9,12,13,6,19,19,20,17,18,20],
    'g': [25,25,28],
    'h': []
}
#Stands numbers and positions, ordered
ccxpTop = [1,2,3,4,5,6,7,8,9,10,11,0,12,13,14,15,16,17,18,19,20,21,22]
ccxpBot = [23,24,25,26,27,28,29,30,31,32,33,0,34,35,36,37,38,39,40,41,42,43,44]

stickersDensity = {}

for k in stickersLocations:    #For all keys in the dictionary with the remaining stickers
    topDensity = [0]*len(ccxpTop)    #Create a list for all top and bottom stands and fill them with zeroes
    botDensity = [0]*len(ccxpBot)    
    for i in range(len(ccxpTop)):    #Then for n-times, n being the stands row size
        if ccxpTop[i] in stickersLocations[k]:
            topDensity[i]+=stickersLocations[k].count(ccxpTop[i])    #Add how many stickers are left in a certain stand to a density array
        if ccxpBot[i] in stickersLocations[k]:
            botDensity[i]+=stickersLocations[k].count(ccxpBot[i])    #The bottom ones too
    stickersDensity[k+' Top'] = topDensity    #Labelling the each stand row
    stickersDensity[k+' Bottom'] = botDensity    #and adding the occurency lists to a dictionary

#Creating and transposing the dataframe so it can match the overrall map of the event
dfLocations = pd.DataFrame(stickersDensity)
dfTransposed = dfLocations.transpose()
transposedLeft = dfTransposed.iloc[:8,:]
transposedRight = dfTransposed.iloc[8:,:]

#Creating a heatmap for the left wing
leftHeat = sns.heatmap(transposedLeft,cbar=False,annot=True)
leftHeat.xaxis.tick_top()
leftHeat.set(ylabel="standArea"), leftHeat.set_title("standNumber(-1)")
leftHeat.tick_params(bottom=False)
leftFig = leftHeat.figure.savefig("left.png")
plt.clf()

#And another for the right wing
rightHeat = sns.heatmap(transposedRight,cbar=False,annot=True)
rightHeat.xaxis.tick_top()
rightHeat.set(ylabel="standArea"), rightHeat.set_title("standNumber(-1)")
rightFig = rightHeat.figure.savefig("right.png")
plt.clf()

#Concatanate the two wings to create a heatmap for the whole event
imgLeft = cv2.imread('left.png')
imgRight = cv2.imread('right.png')
im_h = cv2.hconcat([imgLeft,imgRight])
cv2.imwrite('ccxpHeat.png',im_h)