#import numpy as np 
#import matplotlib.pyplot as plt 
import tensorflow as tf 

temp = tf.constant( [3,4,5])
temp2 = tf.constant( [6,7,8])
temp3 = tf.constant( [[6,7], [4,5], [8,9]])
temp4 = tf.constant( [[6,7], [4,5], [8,9]])

print(temp + temp2)
print(temp * temp2)
print(temp3 * temp4)
print(temp3.shape)