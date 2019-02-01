import numpy as np
from scipy import constant as const
from scipy.fftpack import fftn,ifftn,ifftshift,fftshift,ifft
from scipy.linalg import eigh
from scipy.integrate import ode
from scipy.interpolate import interp1d


class FourierGrid(object):

    def __init__(self,dims=1,size=1001,bound=[-5,5],T=lambda k, *b:0.5*k**2):
        
