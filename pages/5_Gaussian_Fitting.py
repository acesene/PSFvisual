#!/usr/bin/env python
# coding: utf-8

#import python packages 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spec 

#import my functions
import functions as fun

#create range to model gaussian over 
x = np.linspace(-15, 15, 400)

#create random noise
np.random.seed(7)
noise = np.random.normal(-.05,.05, 400)

#create bessel function and add nosie
inten = 4 * (spec.j1(x) / x)**2
noise_inten = inten + noise

#create gaussian fit
gauss_fit = fun.gauss1d(x,1,0,1.5)

#title and content explanation
st.markdown('## Gaussian Fitting')
st.write('This section demonstrates how a gaussian function would be fitted to a non idealized PSF. If we had perfect \
measurement tools, we would only see the idealized psf. However, due to random noise from the measuring we get something that \
is closer to what is displayed below.')

#options to display different fits
model = st.checkbox('Show Gaussian Fit')
psf = st.checkbox('Show Ideal PSF')

#display graph
fig1, ax = plt.subplots(figsize=(5,5))
ax.plot(x, noise_inten, '.')
ax.set_xlabel('distance')
ax.set_ylabel('intensity')

#Determine which plots are displayed based on user input
if model:
    #gaussian plot
    ax.plot(x, gauss_fit, color='red')

if psf:
    #bessel plot
    ax.plot(x, inten, color='purple')
    
st.pyplot(fig1)

