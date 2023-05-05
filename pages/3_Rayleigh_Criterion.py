#!/usr/bin/env python
# coding: utf-8

#import python packages 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from astropy.convolution import AiryDisk2DKernel
from PIL import Image

#import my functions
import functions as fun

#title and content explanation
st.markdown('## Rayleigh Criterion: Resolving two sources')
st.write('When we observe the night sky, the night sky gets projected into a flat image. This means that two stars that are in \
reality far apart from each other will appear right next to each other. As you have seen from the previous section, the size of \
the central point can vary depending on the size of your telescope and the wavelength range you are observing in. This can \
result in scenarios where two sources of light can appear as one.')

#display image
rc = Image.open('rayleigh_criterion.jpeg')
rc = rc.resize((272,417))
st.image(rc, caption='visual of rayleigh criterion')

st.write('The minimum distance that two equally bright sources can be resolved as two separate points is called the limit of \
angular resolution. This can be calculated by using an equation known as the Rayleigh Criterion:')

#display equation
st.latex('a_{c} = \lambda / D_{0}')

st.write('This gives you an angular distance in radians when you divide the wavelength by the diameter of the telescope when \
those are given in the same units.')

#instructions for page use
st.write('Using the sliders below,  you can adjust the wavelength, telescope aperture diameter, and angular distance between two sources to see how it affects the shape of the two point spread functions together. The simulations here only take into account the central point and not the rings of the airy disk.')

#create sliders
dwavelen = st.slider("wavelength of both sources [nm]", 200, 400, step=10)
daperdiam = st.slider("aperture diameter detecting both [m]", 5, 30, step=1)
dist = st.slider('distance between sources',0.4, 10.0, step=.2)

#create gaussian model for psf and multiply by scale factors for the display 
dratio = dwavelen/(8*daperdiam)
xvald = np.linspace(-10,10,400)
gaussd = fun.dgauss(xvald, 1, -4, dratio, 1, -3+dist, dratio)

#create airy disks and multiply by scale factors for display
twoairies = fun.two_airies(dratio*2, dist)

#graph layout
ray1d, ray2d = st.columns([3,4])

with ray1d:
    fig2, ax = plt.subplots(figsize=(5,5))
    ax.plot(xvald,gaussd)
    ax.set_xlabel('distance')
    ax.set_ylabel('intensity')
    st.pyplot(fig2)

with ray2d:
    fig4, ax = plt.subplots(figsize=(5,5))
    ax.imshow(twoairies, interpolation='none', origin='lower', cmap='bone')
    ax.set_xlabel('pixel distance')
    ax.set_ylabel('pixel distance')
    st.pyplot(fig4)

    