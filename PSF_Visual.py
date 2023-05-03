#!/usr/bin/env python
# coding: utf-8

#import fucntions 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#page title 
st.title('Welcome to PSF Visual!')

st.markdown('## Point Spread Function Visualizer')


#whole site introduction 
st.write('This site will introduce you to the Point Spread Function or PSF.')

st.write('PSF is an important topic for understanding how a telescope detects the light from stars and what that means for our observations.')

pic = Image.open('psf_examples.jpeg')
pic = pic.resize((536,322))
st.image(pic, caption='A variety of point spread function examples')

st.write('Follow the tabs in order to be walked through the demo.')

