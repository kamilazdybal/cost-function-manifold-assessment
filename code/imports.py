import numpy as np
import pandas as pd
import copy as cp
import time
import random
import pickle
import csv
import ast
import umap
from dml import DML_eig

from PCAfold import preprocess
from PCAfold import reduction
from PCAfold import analysis

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import ListedColormap
import matplotlib
from matplotlib import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.mplot3d import Axes3D

from sklearn import manifold
from sklearn import datasets
from sklearn.datasets import fetch_openml
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from scipy.signal import find_peaks

from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, InputLayer
from keras import optimizers
from keras import metrics
from keras import losses
import keras.layers as kl
import keras
from keras import layers

import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import initializers

import plotly as plty
from plotly import express as px
from plotly import graph_objects as go

# Common settings:
random_seed = 100