#!/usr/bin/env python
# coding: utf-8

#import python packages used 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from astropy.convolution import AiryDisk2DKernel
from PIL import Image

#import functions made for this webapp
import functions as fun

#Titles and content explanation
st.markdown('## Point Spread Function')

st.write('We can measure the brightness of light sources at each pixel it occupies, to see how quickly it dims as you move \
away from the central point. The resulting graph is called a Point Spread Function (PSF) [see below]. The shape, in partiulcar \
the width of the peak, of the PSF can tell you how precisely the telescope is measuring your souces. The wider the PSF, the more \
diffraction is impacting it, and the less precise the data is. The width of the point spread function depends on the wavelength \
of incoming light and the size of the telescope aperture used. To minimize the effects of diffraction, we want a larger \
telescope aperture, which will show a narrower point spread function.')

#interactive graph use instructions
st.write('Using the sliders below you can adjust the wavelength and telescope aperture diameter to see how it affects the shape \
of the point spread function. The simulations here only take into account the central point and not the rings of the airy disk.')


#create sliders 
wavelen = st.slider("wavelength [nm]", 200, 400, step=10)
aperdiam = st.slider("aperture diameter [m]", 5, 30, step=1)

#establish relationship between sliders valus and FWHM 
ratio = wavelen/(10*aperdiam)

#create gaussian to model PSF
xval = np.linspace(-10,10,400)
gauss = fun.gauss1d(xval, 1, 0, ratio)

#put graphs in columns for better formatting
diff1d, diff2d, = st.columns(2)

with diff1d:
    fig1, ax = plt.subplots(figsize=(5,5))
    ax.plot(xval,gauss)
    ax.set_xlabel('distance')
    ax.set_ylabel('intensity')
    st.pyplot(fig1)

with diff2d:
    fig3, ax = plt.subplots(figsize=(5,5))
    airydisk_2D_kernel = AiryDisk2DKernel(ratio*8, x_size=90, y_size=90)
    ax.imshow(airydisk_2D_kernel, interpolation='none', origin='lower', cmap='bone')
    ax.set_xlabel('x pixel distance')
    ax.set_ylabel('y pixel distance')
    #ax.colorbar()
    st.pyplot(fig3)

