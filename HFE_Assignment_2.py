#!/usr/bin/env python
# coding: utf-8

# In[11]:


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def analyze_data():
    # Use a breakpoint in the code line below to debug your script.
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # (Step 1) Selecting the one data for further data analysis. Give the path & file name below. - 1 point
    affected_filename = f'/Users/sreyatummala/Desktop/data/2966/RUE/NEO1B41100012 (2011-04-26)RAW.csv'
    affected_df = pd.read_csv(affected_filename, skiprows=10)

    acc_x = np.array(affected_df['Accelerometer X'])
    acc_y = np.array(affected_df['Accelerometer Y'])
    acc_z = np.array(affected_df['Accelerometer Z'])
    acc_mag = np.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z) - 1
    
    plt.plot(range(len(acc_mag)), acc_mag)
    plt.show()

    # (Step 3) Identifying the data for sedentary behavior (i.e., sleeping) - 1 point
    # If you identify the beginning index of the sedentary behavior, the ending index will be automatically done.
    # If you select the beginning index too loosely, the subsequent sedentary_data may include active behavior.
    # So, be careful.
    start_index = int(1.2e6)
    end_index = start_index + int(0.500e6)

    sedentary_range = range(start_index, end_index)
    sedentary_data = acc_mag[sedentary_range]

    plt.plot(range(len(sedentary_data)), sedentary_data)
    plt.show()
    
    # (Step 5) Computing beta - 1 point
    # Computing mu
    mu = np.mean(sedentary_data)
    print(mu)
    # Computing std
    sigma = np.std(sedentary_data)
    print(sigma)
    # Then, computing beta, using mu and std
    beta = mu+ (1.96*sigma)
    print(beta)

    # (Step 6) Computing M3 for the entire data - 1 point
    # You can apply beta to identify the data of active behavior.
    active_data = acc_mag[acc_mag > beta]
    M3 = len(active_data)/len(acc_mag)

    # (Step 7) Plotting M3 - 1 point
    plt.plot(M3,1, 'o')
    plt.show()
    
    plt.bar(['Active data', 'Sedentary data'], [M3, 1-M3])
    plt.title('M3')
    plt.show()

    M3_25h = [0 for i in range(0, 25)]

    samples_per_sec = 30
    samples_per_hour = 30*60*60

    for i in range(0, 24):
        # You have to identify the range (i.e., beginning index and ending index for each hour range).
        start_idx = i * samples_per_hour
        end_idx = (i+1) * samples_per_hour
        
        tmp_acc_mag = acc_mag[start_idx:end_idx]
        # Then, you can apply beta to identify the data of active behavior.
        tmp_active_data = tmp_acc_mag[tmp_acc_mag > beta]
        M3_25h[i] = len(tmp_active_data)/len(tmp_acc_mag)
    # print(M3_25h)

    tmp_acc_mag = acc_mag[range(30*60*60*24, len(acc_mag))]
    tmp_active_data = tmp_acc_mag[tmp_acc_mag > beta]
    M3_25h[24] = len(tmp_active_data) / len(tmp_acc_mag)
# print(M3_25h[24])
# print(M3_25h)

    # (Step 9) Plotting M3_25h - 1 point
    plt.plot(range(len(M3_25h)), M3_25h)
    plt.xlabel('Hours')
    plt.ylabel('M3 values')
    plt.title('M3 for every Hour')
    plt.show()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
analyze_data()


# In[ ]:


### 11770- Right


# In[8]:


# (Step 1) Selecting the one data for further data analysis. Give the path & file name below. - 1 point
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### 
affected_filename = f'/Users/sreyatummala/Desktop/data/11770/RUE/NEO1C16110292 (2011-07-07)RAW.csv'
affected_df = pd.read_csv(affected_filename, skiprows=10)


acc_x = np.array(affected_df['Accelerometer X'])
acc_y = np.array(affected_df['Accelerometer Y'])
acc_z = np.array(affected_df['Accelerometer Z'])
acc_mag = np.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z) - 1

plt.plot(range(len(acc_mag)), acc_mag)
plt.show()


# In[ ]:


### 2966- Right


# In[9]:


affected_filename = f'/Users/sreyatummala/Desktop/data/2966/RUE/NEO1B41100012 (2011-04-26)RAW.csv'
affected_df = pd.read_csv(affected_filename, skiprows=10)


acc_x = np.array(affected_df['Accelerometer X'])
acc_y = np.array(affected_df['Accelerometer Y'])
acc_z = np.array(affected_df['Accelerometer Z'])
acc_mag = np.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z) - 1

plt.plot(range(len(acc_mag)), acc_mag)
plt.show()


# In[ ]:


# 7177- Left


# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
affected_filename = f'/Users/sreyatummala/Desktop/data/7177/LUE/NEO1D25110047 (2012-05-21)RAW.csv'
affected_df = pd.read_csv(affected_filename, skiprows=9)


acc_x = np.array(affected_df['Accelerometer X'])
acc_y = np.array(affected_df['Accelerometer Y'])
acc_z = np.array(affected_df['Accelerometer Z'])
acc_mag = np.sqrt(acc_x * acc_x + acc_y * acc_y + acc_z * acc_z) - 1

plt.plot(range(len(acc_mag)), acc_mag)
plt.show()


# In[ ]:




