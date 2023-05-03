#!/usr/bin/env python
# coding: utf-8

#import python packages
import streamlit as st
from PIL import Image

#title and content explanation
st.markdown('## Diffraction')
st.markdown('### A brief recap')

st.write('Diffraction, the bending of light when it passes an edge, is an effect that comes into play when we talk about telescope observations. When observing a light source that appears as a point, as distant stars will, with a circular aperture it will show a characteristic diffraction pattern called an Airy Disk [see image]. The extra “rings” that appear around the central point are not actually part of the observed object, but they appear as a byproduct of the way we observe with telescopes.')

#display image
ideal = Image.open('ideal_airy.jpeg')
ideal = ideal.resize((400,400))
st.image(ideal, caption='an example of an airy disk')

