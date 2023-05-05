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

#title of the page 
st.markdown('## Seeing')

#page content explanation
st.write('The above cases are scenarios where only the fundamental limits of diffraction impact the width of the point spread \
function. These are what are known as “diffraction limited PSF.” However, when you are observing using a ground based telescope, \
the effects of the atmosphere will play a large role in how well point sources can be resolved. These PSFs are known as “seeing \
limited” and are considerably wider compared to diffraction dominated ones.')

#display image
see_gif = Image.open('seeing.gif')
see_gif = see_gif.resize((882,150))
st.image(see_gif, caption='the effects of seeing in an actual image')

#page slider instructions
st.write('Using the sliders below, you can adjust the wavelength, the diameter, as well as how poor the seeing conditions are \
to compare the shapes of the diffraction dominated PSF and seeing dominated PSF.')


#graph layout
sliders,diff, see = st.columns(3)

with sliders:
    #create sliders
    seeing = st.slider('seeing conditions', 1.0, 3.0, step=0.1)
    gwavelen = st.slider("wavelength [nm] ", 200, 400, step=10)
    gaperdiam = st.slider("aperture diameter [m] ", 5, 30, step=1)

#create gaussian models
xval = np.linspace(-10,10,100)
xvald = np.linspace(-10,10,100)

gratio = gwavelen/(10*gaperdiam)

#limit the extent to which better telescopes help seeing
if gaperdiam > 8:
    seeratio = gwavelen/80
else:
    seeratio = gratio

gauss = fun.gauss1d(xval, 1, 0, .9*gratio) #diffraction limited
seegauss = fun.gauss1d(xval, 1, 0, seeratio*seeing) #seeing limited

diff_airydisk = AiryDisk2DKernel(gratio*6, x_size=70, y_size=70) #diffraction limited
see_airydisk = AiryDisk2DKernel(seeratio*6*seeing, x_size=70, y_size=70) #seeing limited

with diff:
    fig5, ax = plt.subplots(figsize=(5,5))
    ax.plot(xval,gauss)
    ax.set_xlabel('distance')
    ax.set_ylabel('intensity')
    ax.set_title('Diffraction limited')
    st.pyplot(fig5)
    
    fig7, ax = plt.subplots(figsize=(5,5))
    ax.imshow(diff_airydisk, interpolation='none', origin='lower', cmap='bone')
    ax.set_xlabel('pixel distance')
    ax.set_ylabel('pixel distance')
    st.pyplot(fig7)

with see:
    fig6, ax = plt.subplots(figsize=(5,5))
    ax.plot(xval,seegauss)
    ax.set_xlabel('distance')
    ax.set_ylabel('intensity')
    ax.set_title('Seeing Limited')
    st.pyplot(fig6)
    
    fig8, ax = plt.subplots(figsize=(5,5))
    plt.tight_layout()
    ax.imshow(see_airydisk, interpolation='none', origin='lower', cmap='bone')
    ax.set_xlabel('pixel distance')
    ax.set_ylabel('pixel distance')
    st.pyplot(fig8)
    
#title and content explanation    
st.markdown('## Seeing and Rayleigh Criterion')
st.write('Using the sliders below, you can adjust the wavelength, the aperture diameter, the angular distance between sources, \
as well as how poor the seeing conditions are to compare angular resolution limits for diffraction dominated and seeing \
dominated PSF.')

#graph layout
sliders2d, diff2d, see2d = st.columns(3)

with sliders2d:
    #create sliders
    swavelen = st.slider("wavelength of both sources [nm] ", 200, 400, step=10)
    saperdiam = st.slider("aperture diameter detecting both [m] ", 5, 30, step=1)
    seeing2d = st.slider('seeing conditions ', 1.0, 3.0, step=0.1)
    sdist = st.slider('distance between sources ',0.4, 10.0, step=.2)

#create psf gaussian model
sratio = swavelen/(10*saperdiam)
sgauss = fun.dgauss(xvald, 1, -4, sratio, 1, -3+sdist, sratio) #diffraction limited

#create gaussian model for two sources
xvald = np.linspace(-10,10,400)
gaussd = fun.dgauss(xvald, 1, -4, .5*sratio, 1, -3+sdist, .5*sratio) #diffraction limited

#limit the extent to which better telescopes help seeing
if saperdiam > 8:
    dseeratio = swavelen/80
else:
    dseeratio = sratio
    
sgaussd = fun.dgauss(xvald, 1, -4, dseeratio*seeing2d*.5, 1, -3+sdist, dseeratio*seeing2d*.5) #seeing limited

#airy disks affected by seeing
twosairies = fun.two_airies(dseeratio, sdist, seeing=(seeing2d*.65)) 

#airy disks diffraction limited only
qtwosairies = fun.two_airies(sratio, sdist) 



with diff2d:
    fig11, ax = plt.subplots(figsize=(5,5))
    ax.plot(xvald,gaussd)
    ax.set_xlabel('distance')
    ax.set_ylabel('intensity')
    ax.set_title('Diffraction limited')    
    st.pyplot(fig11)
    
    fig10, ax = plt.subplots(figsize=(5,5))
    ax.imshow(qtwosairies, interpolation='none', origin='lower', cmap='bone')
    ax.set_xlabel('pixel distance')
    ax.set_ylabel('pixel distance')
    st.pyplot(fig10)

with see2d:
    fig12, ax = plt.subplots(figsize=(5,5))
    ax.plot(xvald,sgaussd)
    ax.set_xlabel('distance')
    ax.set_ylabel('intensity')
    ax.set_title('Seeing Limited')        
    st.pyplot(fig12)
    
    fig9, ax = plt.subplots(figsize=(5,5))
    ax.imshow(twosairies, interpolation='none', origin='lower', cmap='bone')
    ax.set_xlabel('pixel distance')
    ax.set_ylabel('pixel distance')
    st.pyplot(fig9)

#content note
st.write('You will notice that after a certain point, a larger aperture diameter does not help resolution for seeing dominated \
PSF. However, we still build ground based telescopes with larger and larger diameters because techniques like adaptive optics \
help us overcome seeing limitations.')
