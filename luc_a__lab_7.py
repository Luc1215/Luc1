# -*- coding: utf-8 -*-
"""Luc.A_ Lab 7

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wAKSnm_qzDiMYJ65NWyS60s26mN-3BU1

Never Say Never - Documentary on Belousov–Zhabotinsky Reaction BZ

https://www.youtube.com/watch?v=FvXwVZPOoBI


Image Kernels Explained Visually

https://setosa.io/ev/image-kernels/
"""

import numpy as np
from skimage import io as io
import matplotlib.pyplot as plt
from scipy import signal
import torch.nn.functional as F
from torch.nn.functional import *
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import time
from matplotlib import animation, rc
from IPython.display import HTML
rc('animation', html='html5')

def make_ani(A, colormap='gray'):

    fig, ax = plt.subplots() # Create a new figure and axes for plotting
    im = ax.imshow(A[0,:,:], cmap = colormap); # Plot the first frame of the animation as an image using the specified colormap
    ax.axis('off') # Turn off axis labels and ticks
    fig.set_size_inches(12, 12) # Set the size of the figure to 12x12 inches

    def animate(data, im): # Function to update the image data with each frame of the animation
        im.set_data(data)

    def step():
        for i in range(A.shape[0]): # Iterate over the first dimension of the array A
            data = A[i,:,:] # Extract a 2D slice from A at index i
            yield data # Yield the data for each iteration

    return animation.FuncAnimation(fig, animate, step, interval=100, repeat=True, fargs=(im,))

def plot(x):
    fig, ax = plt.subplots() # Create a new figure and axis
    im = ax.imshow(x, cmap = 'gray') # Display the image represented by the array x, using a grayscale colormap
    ax.axis('off') # Turn off axis
    fig.set_size_inches(15, 15) # Set the size of the figure
    plt.show() # Show the plot

image = io.imread("https://www.filfre.net/wp-content/uploads/2013/12/bbc4.png") # Web

image.shape #RGBa

plot(image)

image.shape

plot(image[:,:,0])

plot(image[:,:,1])

plot(image[:,:,2])

image.shape # image

image = np.mean(image, axis=2)

plot(image)

image.shape

a = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]]) # Define a 3x3 matrix for edge detection (Sobel operator for horizontal edges)

a

plot(a)

image.shape

y = signal.convolve2d(image, a, mode='same') ## Create a  2D convolution operation on the image with the specified filter (a) and ensure that the output has the same size as the input image

plot(y)

a = np.transpose(a)

a

plot(a)

y = signal.convolve2d(image, a, mode='same') # Create a  2D convolution operation on the image with the  filter (a) and ensure that the output has the same size as the input image

plot(y)

b = np.random.random((25,25)) # Create a 25x25 matrix filled with random numbers from a uniform distribution over [0, 1)

y = signal.convolve2d(image, b) # Create a 2D convolution operation on the image with the specified filter (b).

plot(y)

x = io.imread("https://ichef.bbci.co.uk/news/660/cpsprodpb/C342/production/_88068994_thinkstockphotos-493881770.jpg") # Web
x = x[:,:,0] # Select only the first channel in the RGB channel

x = x.astype(float)

x

x = x / 255.0 # Normalize the pixel values of the image array 'x' to the range [0, 1]
plot(x) # Plot image

x

a

a[1,1]

def conv2(x,f):
    x2 = np.zeros(x.shape)
    for i in range(1,x.shape[0]-1): # Iterate over each element of the input array 'x' excluding the boundary pixels
        for j in range(1,x.shape[1]-1):  # Perform the convolution operation at the current pixel location

            x2[i,j] = f[0,0] * x[i-1,j-1]  \ # Top left
            +         f[0,1] * x[i-1,j]    \ # Top center
            +         f[0,2] * x[i-1,j+1]  \ # Top right
            +         f[1,0] * x[i,j-1]    \ # Middle left
            +         f[1,1] * x[i,j]      \ # Middle center
            +         f[1,2] * x[i,j+1]    \ # Middle right
            +         f[2,0] * x[i+1,j-1]  \ # Bottom left
            +         f[2,1] * x[i+1,j]    \ # Bottom center
            +         f[2,2] * x[i+1,j+1] # Bottom right

    return x2 # Return the result of the convolution

a = np.matrix([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
# a = np.matrix([[1,2,1],[0,0,0],[-1,-2,-1]])
# a = np.matrix([[1,1,1],[1,1,1],[1,1,1]])
# a = 5*np.random.random((3,3))-5*np.random.random((3,3))

a

z = conv2(x,a)

plot(z)

for i in range(10):
    a = 2*np.random.random((3,3))-1 # Create a random 3x3 filter
    print(a) # Print
    z=conv2(x,a) # Create convolution with x using the conv2 function
    plot(z) # Plot z



#Homemade Conv Loop Timing
a = 2*np.random.random((9,3,3))-1
start_time = time.time() # Start time
for i in range(9):

    z=conv2(x,a[i,:,:]) # Create operation using custom function conv2

print("Seconds:", (time.time() - start_time)) # Print time

#Optimized Code Timing
a = 2*np.random.random((9,3,3))-1
start_time = time.time() # Start time
for i in range(9):

    z = signal.convolve2d(x,a[i,:,:])  #  Create operation using signal.convolve2d

print("--- %s seconds ---" % (time.time() - start_time)) # Print time

#GPU Processing Timing, No Loop, 96 filters!!
a2 = 2*np.random.random((96,1,3,3))-1
x2 = torch.tensor(x).cuda() # Change input data x to a PyTorch tensor and move it to the GPU
a2 = torch.tensor(a2).cuda() # Change filters a2 to a PyTorch tensor and move them to the GPU
x2 = x2[None,None,:,:] # Insert batch and channel dimensions to the input data

start_time = time.time() # Start time
z = conv2d(x2,a2) # Execute the convolution operation
print("--- %s seconds ---" % (time.time() - start_time)) # Print time

z.shape



image = io.imread("https://img.jagranjosh.com/imported/images/E/Articles/Fastest-Fish-img.jpg").astype(float)/255.0 # Web
plot(image) # Plot image

image.shape

plot(np.random.random((11,11,3)))

image = np.transpose(image, (2, 0, 1))

image.shape

f = np.random.random((1,3,11,11))

image.shape

image = image[None,:,:,:]

image.shape,f.shape

f =  torch.tensor(f)
image =  torch.tensor(image)

image2 = F.conv2d(image,f)

image2 = image2.numpy()

image2.shape

image2[0,0,:,:].shape

plot(image2[0,0,:,:])



image = io.imread("http://ian-albert.com/games/super_mario_bros_maps/mario-2-2.gif") # Web
image = image[:,0:700,:] # Pick a portion of the image by slicing along the width dimension
plot(image) # Plot image

coin = image[185:200,224:239,:]

plot(coin)

image = image[60:,0:700,:]
plot(image)

def scale1(x):
    return (x-np.min(x))/(np.max(x)-np.min(x))

image = np.mean(image,axis=2)
coin = np.mean(coin,axis=2)

image = scale1(image)
coin = scale1(coin)

plot(image)
plot(coin)

coin.shape

image = image - np.mean(image)
coin = coin - np.mean(coin)

image.shape,coin.shape

coin = np.rot90(coin, 2)

plot(coin)

z = signal.convolve2d(image,coin)

# z = conv2(image,coin)

plot(z)

z == np.max(z)

plot(z==np.max(z))

np.where(z == np.amax(z))

[y,x] = np.where(z == np.amax(z))

plt.plot(x,-y,'.')

fig, ax = plt.subplots() # Create a matplotlib figure and axis
im = ax.imshow(image, cmap = 'gray') # Show the image with a grayscale colormap
ax.axis('off') # Remove axis ticks and labels
ax.scatter(x-6, y-6, c='red', s=40) # Add red scatter points at coordinates (x, y)
fig.set_size_inches(18, 10) # Set the figure size









def conv2(w,f): #GPU conv with padding

    n = conv2d(w.type(torch.int),f.type(torch.int)) # Create a 2D convolution operation on grid w using filter f
    n = pad(n, (1, 1, 1, 1)) # Add ones to the sides of the matrix

    return n

#Game of Life

w = (np.random.random((100,100)) > 0.5) # Game of life world grid w
f = np.matrix([[1,1,1],[1,0,1],[1,1,1]]) # Create a filter for computing cell neighborhoods

f

plot(w)

steps = 1000 # The number of simulation steps
A = torch.zeros((steps,100,100)) # storage for frames for animation
w = torch.tensor(w.astype(int))[None,None,:,:] # Convert grid w to PyTorch tensors
f = torch.tensor(f.astype(int))[None,None,:,:] # Convert filter f to PyTorch tensors

# %%timeit
n = conv2(w,f)

# (n==2)[0,0,:,:].shape

plot((n==2)[0,0,:,:])

for i in range(steps): # Iterate over the specified number of steps

    n = conv2(w,f) # Convolve the grid with the filter to compute cell neighborhoods
    w = (w * (n==2)) + (n==3)  ## A cell stays alive if it has exactly 2 neighbors and was previously alive,  or if it has exactly 3 neighbors and was previously dead.
    A[i] = w # Store the updated state of cells at step i

make_ani(A)







#Surface Tension Model

w = (np.random.random((100,100)) > 0.5).astype(int) # Initialize the grid with random binary values based on a probability threshold of 0.5
f = np.matrix([[1,1,1],[1,1,1],[1,1,1]]) # Create a filter for computing cell neighborhoods

steps = 200 # The number of simulation steps
A = torch.zeros((steps,100,100)) # storage for frames for animation
w = torch.tensor(w)[None,None,:,:] # Convert grid w to PyTorch tensors
f = torch.tensor(f)[None,None,:,:] # Convert filter f to PyTorch tensors

for i in range(steps): # Iterate over the specified number of steps

    n = conv2(w,f) # Convolve the grid with the filter to compute cell neighborhoods

    w = ~((n<4) + (n==5))# Cells that are fewer than 4 neighbors or exactly 5 neighbors transition to alive (1), indicated by

    A[i] = w # Store the updated state of cells at step i

make_ani(A)



#Forest Fire Model

# veg = {empty=0 burning=1 green=2}

# Define the probability of lightning and growth
Plightning = 0.00005
Pgrowth = 0.01

w = (np.random.random((100,100)) > 0.5).astype(int) # Initialize the grid with random binary values based on a probability threshold
f = np.matrix([[1,1,1],[1,0,1],[1,1,1]]) # Create filter for computing cell neighborhoods

steps = 1000 # The number of simulation steps
A = torch.zeros((steps,100,100)) # storage for frames for animation
w = torch.tensor(w)[None,None,:,:] # Convert grid w to PyTorch tensors
f = torch.tensor(f)[None,None,:,:] # Convert grid to PyTorch tensors

for i in range(steps): # Iterate over the specified number of steps

    n = w == 1 # Define a binary mask representing cells in state 1

    n = conv2(n,f) # Convolve the binary mask with a filter to compute cell neighborhoods

    w =  2*((w == 2)).type(torch.int)                                                 \ # Cells in state 2 transition to state 2 with a probability of 2
    -    1*((w == 2) * ( n > 0 ) ).type(torch.int)                                   \ # Cells in state 2 transition to state 0 if they have neighbors in state 1
    -    1*((w == 2) * ( np.random.random((100,100)) < Plightning)).type(torch.int)  \ # Cells in state 2 transition to state 0 with a probability of Plightning
    +    2*((w == 0) * ( np.random.random((100,100)) < Pgrowth)).type(torch.int) # Cells in state 0 transition to state 2 with a probability of Pgrowth

    A[i] = w # Store the updated state of cells at step i

make_ani(A, colormap='magma')





#Nonlinear Waves

w = np.random.random((100,100)) < 0.1 # Initialize the grid with random boolean values (True/False) with a probability of True being 0.1
f = np.matrix([[1,1,1],[1,0,1],[1,1,1]]) # Define a filter for computing cell neighborhoods

t  = 6  #center value=6; 7 makes fast pattern; 5 analiating waves
t1 = 3  #center value=3

steps = 1000 # Set the number of simulation steps
A = torch.zeros((steps,100,100)) # storage for frames for animation
w = torch.from_numpy(w)[None,None,:,:] # Convert grid w to PyTorch tensors
f = torch.from_numpy(f)[None,None,:,:] # Convert filter f to PyTorch tensors

for i in range(1000): ## Iterate over 1000 steps

    n = (w>0)&(w<t) ## Define a mask representing cells with states greater than 0 and less than a threshold t

    n = conv2(n,f) ## Convolve the neighborhood defined by the mask with a filter

    w = ((w==0) & (n>=t1)) \
    +  2*(w==1)            \
    +  3*(w==2)            \
    +  4*(w==3)            \
    +  5*(w==4)            \
    +  6*(w==5)            \
    +  7*(w==6)            \
    +  8*(w==7)            \
    +  9*(w==8)            \
    +  0*(w==9)            \

    A[i] = w ## Store the updated state of cells at step i

make_ani(A)





#Wireword Wire
#{empty=0 electron_head=1 electron_tail=2, wire=3}

w = np.zeros((100,100))
w[50,:] = 3 # Set an entire row to state 3
w[50,5] = 2 # Set a specific cell to state 2
w[50,6] = 1 # Set a specific cell to state 1

f = np.matrix([[1,1,1],[1,0,1],[1,1,1]]) # Define a filter for computing cell neighborhoods

steps = 1000 # The number of simulation steps
A = torch.zeros((steps,100,100)) # storage for frames for animation
w = torch.from_numpy(w)[None,None,:,:] # Convert grid w PyTorch tensors
f = torch.from_numpy(f)[None,None,:,:]# Convert filter f to PyTorch tensors

for i in range(100): # Iterate over 100 steps

    n=w==1 # Compute the number of neighbors for cells in state 1

    n = conv2(n,f) # Convolve the neighborhood with a filter

    w = 1*((w==3)& ((n==1) | (n==2)))                 \ # If a cell is in state 3 and has 1 or 2 neighbors in state 1, it transitions to state 1
    +   3*((w==3)& ((n!=1) & (n!=2)))                 \ # If a cell is in state 3 and does not have 1 or 2 neighbors in state 1, it remains in state 3
    +   0*(w==0)                    \ # If a cell is in state 0, it remains in state 0
    +   2*(w==1)                    \ #  If a cell is in state 1, it remains in state 1
    +   3*(w==2)                    \ # If a cell is in state 2, it remains in state 2

    A[i] = w ## Store the updated state of cells at step i

make_ani(A, colormap='magma')



#Wireworld Oscillator

# Initialize the grid with zeros and set specific cells to predefined states
w = np.zeros((100,100))
w[50,15:-1] = 3
w[48,5:15] = 3
w[52,5:15] = 3
w[49:52,4] = 3
w[49:52,15] = 3
w[52,14] = 1
w[52,13] = 2

f = np.matrix([[1,1,1],[1,0,1],[1,1,1]]) # Define a filter for computing cell neighborhoods

steps = 1000 # The number of simulation steps
A = torch.zeros((steps,100,100)) # storage for frames for animation
w = torch.from_numpy(w)[None,None,:,:] # Convert grid w to PyTorch tensors
f = torch.from_numpy(f)[None,None,:,:] # Convert grid filter f to PyTorch tensors

for i in range(steps): # Iterate over a certain number of steps

    n = w == 1 # Compute the number of neighbors for each cell

    n = conv2(n,f) # Convolve the neighborhood with a filter (possibly a convolutional kernel

    w = 0*((w==0))                                    \ # If the cell is in state 0, it remains in state 0 (0 * (w == 0))
    +   2*((w==1))                                    \ # If the cell is in state 1, it remains in state 1 (2 * (w == 1))
    +   3*((w==2))                                    \ # If the cell is in state 2, it remains in state 2 (3 * (w == 2))
    +   3*((w==3)& ((n!=1) & (n!=2)))                 \ # Ff the cell is in state 3 and has 1 or 2 neighbors in state 1,
    +   1*((w==3)& ((n==1) | (n==2)))                 \ # it transitions to state 1; otherwise, it remains in state 3

    A[i] = w # Store the updated state of cells at step i

make_ani(A, colormap='magma')





#FitzHugh-Nagumo Reaction Diffusion

def laplacian(U):
    n = conv2d(U,laplace) # Perform 2D convolution of U with the Laplace filter
    n = pad(n, (1, 1, 1, 1),'circular') # Pad the result of the convolution with one extra row and column on each side using circular padding
    return n

# Create a Laplace filter as a 3x3 NumPy array and multiple by 0.5 scaling the filter
laplace = 0.5*np.array([[0.5, 1.0, 0.5],
                        [1.0, -6., 1.0],
                        [0.5, 1.0, 0.5]])

N = 256 # Size of the grid
h = 0.05 # Time step
# Initialize array A with zeros and set initial concentration to -0.7
A = np.zeros([N, N], dtype=np.float32)
A = A + -0.7

# Generate noise and add it to a specific region of array A
noise_shape = A[:,120:130].shape
A[:,120:130] = (np.random.normal(0.9,0.05,size=noise_shape))

# Initialize array B with zeros and set initial concentration to -0.3
B = np.zeros([N, N], dtype=np.float32)
B = B + -0.3

w1 = plot(A)

a0 = -0.1 # Constant term affecting the baseline production or decay rate of chemical B
a1 = 2 # Coefficient controlling the effect of chemical A on the production or decay of chemical B
epsilon = 0.05 # Coefficient controlling the overall effect of chemical A on the production or decay of chemical B
delta = 4 # Coefficient controlling the diffusion rate of chemical B
k1 = 1 # Coefficient controlling the production rate of chemical A
k2 = 0  # Coefficient controlling the quadratic term in the equation for chemical A
k3 = 1 # Coefficient controlling the effect of chemical A on the production or decay of chemical B

A = torch.from_numpy(A)[None,None,:,:].cuda() # Convert A to a tensor and add batch and channel dimensions, then move to GPU
B = torch.from_numpy(B)[None,None,:,:].cuda() # Convert B to a tensor and add batch and channel dimensions, then move to GPU
laplace = torch.from_numpy(laplace)[None,None,:,:].type(torch.float).cuda() # Convert laplace to a tensor, add dimensions, change data type to float, and move to GPU

steps = 100 # Total number of steps
P = torch.zeros((steps,N,N)) # storage for frames for animation

j = 0 # Initialize index for storing states
for i in range(steps*1000): # Iterate over a certain number of steps (iterations)
# Update the concentrations of chemicals A and B using the given differential equations
    A += h*( k1*A - k2*A**2 - A**3 - B + laplacian(A))
    B += h*( epsilon*(k3*A - a1*B -a0) + delta*laplacian(B) )

    if i % 1000 == 0: # Store the state of the system at regular intervals
        P[j] = A # Store the concentration of chemical A
        j += 1 # Increment index for storing the next state

make_ani(P)



#Gray Scott Reaction Diffusion

# Define a Laplace filter as a 3x3 NumPy array
laplace = 0.5*np.array([[0.5, 1.0, 0.5],
                        [1.0, -6., 1.0],
                        [0.5, 1.0, 0.5]])

laplace = torch.from_numpy(laplace)[None,None,:,:].type(torch.float).cuda() # Convert Laplace filter to a PyTorch tensor

def laplacian(U):
    n = conv2d(U,laplace) # Perform 2D convolution of U with the Laplace filter
    n = pad(n, (1,1,1,1)) # Pad the result of the convolution with one extra row and column on each side
    n = pad(n, (0,0,0,0)) # Pad the result with zeros to match the input size
    return n

(Du, Dv, F, k) = ((0.16, 0.08, 0.035, 0.065)) # Bacteria 1
# (Du, Dv, F, k) = ((0.14, 0.06, 0.035, 0.065)) # Bacteria 2
# (Du, Dv, F, k) = ((0.16, 0.08, 0.060, 0.062)) # Coral
# (Du, Dv, F, k) = ((0.19, 0.05, 0.060, 0.062)) # Fingerprint
# (Du, Dv, F, k) = ((0.10, 0.10, 0.018, 0.050)) # Spirals
# (Du, Dv, F, k) = ((0.12, 0.08, 0.020, 0.050)) # Spirals Dense
# (Du, Dv, F, k) = ((0.10, 0.16, 0.020, 0.050)) # Spirals Fast
# (Du, Dv, F, k) = ((0.16, 0.08, 0.020, 0.055)) # Unstable
# (Du, Dv, F, k) = ((0.16, 0.08, 0.050, 0.065)) # Worms 1
# (Du, Dv, F, k) = ((0.16, 0.08, 0.054, 0.063)) # Worms 2
# (Du, Dv, F, k) = ((0.16, 0.08, 0.035, 0.060)) # Zebrafish

N = 256

U = np.zeros((N,N)) # Clear Chemicals
V = np.zeros((N,N))

U = U + 1.0
r = 5
U[N//2-r:N//2+r,N//2-r:N//2+r] = 0.50 # Add Disturbance in Center Square Radius r
V[N//2-r:N//2+r,N//2-r:N//2+r] = 0.25

U += 0.05*np.random.random((N,N)) # Add Noise to Chemicals
V += 0.05*np.random.random((N,N))

U = torch.from_numpy(U)[None,None,:,:].type(torch.float).cuda()
V = torch.from_numpy(V)[None,None,:,:].type(torch.float).cuda()

steps = 2000
skip = 100
P = torch.zeros((steps,N,N)) # storage for frames for animation

j = 0 # Initialize index for storing states
for i in range(steps*skip): # Iterate over a certain number of steps (iterations)
# Update the concentrations of chemicals U and V using the Gray-Scott model equations
    U += ( Du*laplacian(U) - U*V**2 +  F   *(1-U) )
    V += ( Dv*laplacian(V) + U*V**2 - (F+k)*V     )

    if i % skip == 0: # Store the state of the system at regular intervals
        P[j] = U # Store the state of U
        j += 1 # Increment index for storing the next state

make_ani(P)











# (Du, Dv, F, k) = ((0.16, 0.08, 0.035, 0.065)) # Bacteria 1
# (Du, Dv, F, k) = ((0.14, 0.06, 0.035, 0.065)) # Bacteria 2
# (Du, Dv, F, k) = ((0.16, 0.08, 0.060, 0.062)) # Coral
# (Du, Dv, F, k) = ((0.19, 0.05, 0.060, 0.062)) # Fingerprint
# (Du, Dv, F, k) = ((0.10, 0.10, 0.018, 0.050)) # Spirals
# (Du, Dv, F, k) = ((0.12, 0.08, 0.020, 0.050)) # Spirals Dense
# (Du, Dv, F, k) = ((0.10, 0.16, 0.020, 0.050)) # Spirals Fast
# (Du, Dv, F, k) = ((0.16, 0.08, 0.020, 0.055)) # Unstable
# (Du, Dv, F, k) = ((0.16, 0.08, 0.050, 0.065)) # Worms 1
# (Du, Dv, F, k) = ((0.16, 0.08, 0.054, 0.063)) # Worms 2
(Du, Dv, F, k) = ((0.16, 0.08, 0.035, 0.060)) # Zebrafish

N = 256

U = np.zeros((N,N)) # Clear Chemicals
V = np.zeros((N,N))

U = U + 1.0
r = 5
U[N//2-r:N//2+r,N//2-r:N//2+r] = 0.50 # Add Disturbance in Center Square Radius r
V[N//2-r:N//2+r,N//2-r:N//2+r] = 0.25

U += 0.05*np.random.random((N,N)) # Add Noise to Chemicals
V += 0.05*np.random.random((N,N))

U = torch.from_numpy(U)[None,None,:,:].type(torch.float).cuda()
V = torch.from_numpy(V)[None,None,:,:].type(torch.float).cuda()

steps = 2000
skip = 100
P = torch.zeros((steps,N,N)) # storage for frames for animation

j = 0 # Start index for storing states
for i in range(steps*skip): # Iterate over a certain number of steps
# Update the concentrations of chemicals U and V using the Gray-Scott model equations
    U += ( Du*laplacian(U) - U*V**2 +  F   *(1-U) )
    V += ( Dv*laplacian(V) + U*V**2 - (F+k)*V     )

    if i % skip == 0: # Store the state of the system at regular intervals
        P[j] = U # Store the state of U
        j += 1 # Increment index for storing next state

make_ani(P)









# (Du, Dv, F, k) = ((0.16, 0.08, 0.035, 0.065)) # Bacteria 1
# (Du, Dv, F, k) = ((0.14, 0.06, 0.035, 0.065)) # Bacteria 2
(Du, Dv, F, k) = ((0.16, 0.08, 0.060, 0.062)) # Coral
# (Du, Dv, F, k) = ((0.19, 0.05, 0.060, 0.062)) # Fingerprint
# (Du, Dv, F, k) = ((0.10, 0.10, 0.018, 0.050)) # Spirals
# (Du, Dv, F, k) = ((0.12, 0.08, 0.020, 0.050)) # Spirals Dense
# (Du, Dv, F, k) = ((0.10, 0.16, 0.020, 0.050)) # Spirals Fast
# (Du, Dv, F, k) = ((0.16, 0.08, 0.020, 0.055)) # Unstable
# (Du, Dv, F, k) = ((0.16, 0.08, 0.050, 0.065)) # Worms 1
# (Du, Dv, F, k) = ((0.16, 0.08, 0.054, 0.063)) # Worms 2
# (Du, Dv, F, k) = ((0.16, 0.08, 0.035, 0.060)) # Zebrafish

N = 256

U = np.zeros((N,N)) # Clear Chemicals
V = np.zeros((N,N))

U = U + 1.0
r = 5
U[N//2-r:N//2+r,N//2-r:N//2+r] = 0.50 # Add Disturbance in Center Square Radius r
V[N//2-r:N//2+r,N//2-r:N//2+r] = 0.25

U += 0.05*np.random.random((N,N)) # Add Noise to Chemicals
V += 0.05*np.random.random((N,N))

U = torch.from_numpy(U)[None,None,:,:].type(torch.float).cuda()
V = torch.from_numpy(V)[None,None,:,:].type(torch.float).cuda()

steps = 8000
skip = 100
P = torch.zeros((steps,N,N)) # storage for frames for animation

j = 0 # Initialize index for storing states
for i in range(steps*skip): # Iterate over a certain number of steps (iterations)
     # Update the concentrations of chemicals U and V using the Gray-Scott model equations
    U += ( Du*laplacian(U) - U*V**2 +  F   *(1-U) )
    V += ( Dv*laplacian(V) + U*V**2 - (F+k)*V     )

    if i % skip == 0: # Store the state of the system at regular intervals
        P[j] = U # Store the state of U
        j += 1 # Increment index for storing next state

make_ani(P)

