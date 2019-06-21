# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:49:53 2019

@author: David
"""

import numpy as np

"""
create to cartisine space
great way to achieve x y plane space
"""
print('a')
x = np.linspace(1,3,3)
y = np.linspace(1,3,3)
xy = np.dstack(np.meshgrid(x, y)).reshape(-1, 2)

#print(x_y_domain)


print(xy[1][2])
#print(y)