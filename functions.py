#!/usr/bin/env python
# coding: utf-8

#import python packages
import streamlit as st
import numpy as np
from astropy.convolution import AiryDisk2DKernel

def gauss1d(x, peak, mu, sig):
    '''
    A function that generates one gaussian peak
    
        Parameters
        ----------
        x: array_like
            x values to generate gaussian over 
        peak: float
            Peak height above background 
        mu: float
            Central value of gaussian
        sig: float
            Standard deviation 
            
      Returns
      -------
      one output: array_like
          the y values for a gaussian curve
      
      Notes
      -----
      requires numpy
    '''
    return peak*np.exp(-1.*(x-mu)**2/(2.*sig**2))


def dgauss(x, peak1, mu1, sig1, peak2, mu2, sig2):
    '''
    A function that generates two gaussian peaks
    
        Parameters
        ----------
        x: array_like
            x values to generate gaussians over 
        peak1: float
            Peak height above background for first gaussian
        mu1: float
            Central value of first gaussian
        sig1: float
            Standard deviation of first gaussian
        peak2: float
            Peak height above background for second gaussian
        mu2: float
            Central value of second gaussian
        sig2: float
            Standard deviation of second gaussian
            
      Returns
      -------
      one output: array_like
          the y values for two gaussian curves
      
      Notes
      -----
      requires numpy
    '''
    return peak1*np.exp(-1.*(x-mu1)**2/(2.*sig1**2)) + peak2*np.exp(-1.*(x-mu2)**2/(2.*sig2**2))


def two_airies(ratio, dist, **kwargs):
    '''
    A function to create two airy disks within one 2d array 
    
        Parameters
        ----------
        ratio: float
            the wavelength over diameter ratio to be used for radius of airy disk
        dist: float
            distance between two airy disks 
        
        **kwargs: dict_like, optional
            option to provide a value for seeing
            
      Returns
      -------
      one output: 2D array
          two airy disks a variabel distance apart
      
      Notes
      -----
      Requires numpy and astropy
    '''
    
    spread = ratio*5
    
    if ('seeing') in kwargs.keys():
        spread = 5*ratio*kwargs['seeing']

    airy1 = np.array(AiryDisk2DKernel(spread, x_size=120, y_size=120))
    airy2 = np.array(AiryDisk2DKernel(spread, x_size=120, y_size=120))

    width = dist*3.5
    width = int(width)

    empty = np.zeros((width,120))

    mod_airy1 = np.append(airy1, empty, axis=0)
    mod_airy2 = np.append(empty, airy2, axis=0)

    twoairies = mod_airy1 + mod_airy2
    
    return twoairies.T
