# -*- coding: utf-8 -*-
"""Copy of Luc lab 1Math 24 Lab 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AnqKzUOWP60mFJRaea5X6YZtgeE5vw5T

## Python Basics

### Calculator
"""

# Comments with hashtag, python ignores this

30.34321 + 9.12313 - 3.5567 # example of calculation

2*2 # example of calculation

2**8 # example of calculation

2**123 # example of calculation

2**12345 # example of calculation

import sys
sys.set_int_max_str_digits(100000)
2**45678
# Adjusting integer display settings

8/4 # Integer and float division, modulo operations

8//4 # Integer and float division, modulo operations

8%12 # Integer and float division, modulo operations

13%12 # Integer and float division, modulo operations

22%12 # Integer and float division, modulo operations

24%12 # Integer and float division, modulo operations

"""### Variables"""

apples = 5  # Variables

oranges = 8 # Variables

total = apples + oranges # Variables

total # Variables

apples**2 # Variables

cost_per_apple = 0.25 # Variables

total_apple_costs = cost_per_apple * apples # Variables

total_apple_costs # Variables

"""### Vectors"""

import numpy as np
import matplotlib.pyplot as plt
# Vectors using NumPy

np.arange(10) # Vectors using NumPy

x = np.arange(10) # Vectors using NumPy

x # Vectors using NumPy

y = 3 * x + 5 # Vectors using NumPy

y # Vectors using NumPy

# x = np.array([133,24,333,4,5,6])
# y = np.array([11,22,33,44,55,66])
# Vectors using NumPy

x,y # Vectors using NumPy

"""### Plotting"""

plt.plot(x,y) # Plotting

plt.plot(x,y,'.') # Plotting

plt.plot(x,y,'r.') # Plotting

plt.plot(x,y,'b--') # Plotting

import matplotlib.pyplot as plt # Plotting

plt.plot(x,y) # Plotting

x = np.linspace(0,5,10) # Plotting

x # Plotting

y = x**2 # Plotting

plt.plot(x,y) # Plotting

plt.plot(x,y) # Plotting
plt.title("New Graph of x**2"); # Plotting
plt.xlabel("x"); # Plotting
plt.ylabel("y"); # Plotting
# Plotting

plt.plot(x,y,label="x squared")
plt.title("Graph of x**2");
plt.xlabel("x");
plt.ylabel("y");
plt.legend()
# Plotting

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()
# Plotting

labels = 'Frogs', 'Dogs', 'Cats', 'Birds'
sizes = [15, 30, 40, 15]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Dogs')


fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)

plt.plot(t, s)
plt.title(r'$\alpha_i > \beta_i$', fontsize=20)
plt.text(1, -0.6, r'$\sum_{i=0}^\infty x_i$', fontsize=20)
plt.text(0.5, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',fontsize=15)
plt.xlabel('time (s)')
plt.ylabel('volts (mV)')
plt.show()

"""Plot the following functions from $x = -10$ to $x = 10$

(Hint: np.sin, np.exp)
# Plotting

$y = 10x+7$

$y = -3x-12$

$y=\sin(x)$

$y=e^x$

$y=e^{-x^2}$

Pick out a plot of your choice from [here](https://matplotlib.org/stable/gallery/index.html), copy the code to this notebook, run, and document to the best of your abilities.
"""

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import Normalize
from matplotlib.markers import MarkerStyle
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D

SUCCESS_SYMBOLS = [
    TextPath((0, 0), "☹"),
    TextPath((0, 0), "😒"),
    TextPath((0, 0), "☺"),
]

N = 25
skills = np.random.uniform(5, 80, size=N) * 0.1 + 5
takeoff_angles = np.random.normal(0, 90, N)
thrusts = np.random.uniform(size=N)
successful = np.random.randint(0, 3, size=N)
positions = np.random.normal(size=(N, 2)) * 5
data = zip(skills, takeoff_angles, thrusts, successful, positions)

cmap = plt.colormaps["jet"]
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))


plt.show()







"""### Graphics Output"""

from IPython.core.display import display, HTML

display(HTML('<h1>Hello World!</h1>'))

"""### Numpy - Numerical Python"""

import numpy as np

np.random.random()

np.random.random() > 0.5;

r = np.random.random(); print(r); r >0.5

r

r > 0.5







def flip_coin():
    if np.random.random() > 0.5:
        print("Heads")
    else:
        print("Tails")

flip_coin()

np.random.randint(15,20)

def coin():
  return np.random.randint(2)

coin()

display(HTML('<img src="https://random-ize.com/coin-flip/us-quarter/us-quarter-front.jpg">'))

heads = 'https://random-ize.com/coin-flip/us-quarter/us-quarter-front.jpg'
tails = 'https://random-ize.com/coin-flip/us-quarter/us-quarter-back.jpg'

def show_img(img):
  display(HTML('<img src=' + img + '>'))

show_img(heads)

show_img(tails)

def flip_coin():

    if coin():
        show_img(heads)
    else:
        show_img(tails)

flip_coin()

for i in range(5):
    flip_coin()





"""# Cards"""



card_url_head = "https://www.improvemagic.com/wp-content/uploads/2020/11/"
card_url_tail = ".png"

suit = ['k','p','s','l'] #clubs,spades,hearts,diamonds
card = ['a','2','3','4','5','6','7','8','9','10','j','q','k']

i = np.random.randint(4)
j = np.random.randint(13)

i,j

suit[i]

card[j]

def card_image(card_number):

    i = card_number//13
    j = card_number%13

    return suit[i]+card[j]

card_image(3)

img = card_url_head + card_image(3) + card_url_tail

img

show_img(img)

for i in range(52):
    img = card_url_head + card_image(i) + card_url_tail
    show_img(img)

import random

def initialize_deck():
    #Create and shuffle a deck of 52 cards represented by numbers 0-51.
    deck = list(range(52))
    random.shuffle(deck)
    return deck

def draw_cards(deck, top_index, num=5):
    drawn_cards = deck[top_index:top_index + num]
    return drawn_cards, top_index + num

# Initialize and shuffle the deck
deck = initialize_deck()
top_index = 0  # Start at the beginning of the deck

deck

# Draw 5 cards for a poker hand
hand, top_index = draw_cards(deck, top_index, 5)

hand

hand, top_index = draw_cards(deck, top_index, 5)

hand

# Display the hand
for card_number in hand:
    img_url = card_url_head + card_image(card_number) + card_url_tail
    show_img(img_url)

def show_hand(hand):
    images_html = ''.join([f'<img src="{card_url_head + card_image(card_number) + card_url_tail}" style="display:inline-block; margin:5px;" />' for card_number in hand])
    display(HTML(images_html))

show_hand(hand)





"""# Rank Hand"""

def evaluate_hand(hand):
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 11, 'q': 12, 'k': 13, 'a': 14}
    suits = ['k', 'p', 's', 'l']  # clubs, spades, hearts, diamonds

    # Convert the hand to a list of (rank, suit) tuples
    converted_hand = [(rank_values[card[card_number % 13]], suits[card_number // 13]) for card_number in hand]
    converted_hand.sort()

    rank_counts = {rank: 0 for rank in rank_values.values()}
    suit_counts = {suit: 0 for suit in suits}
    for rank, suit in converted_hand:
        rank_counts[rank] += 1
        suit_counts[suit] += 1

    # Check for flush
    is_flush = max(suit_counts.values()) == 5

    # Check for straight and royal flush
    rank_sequence = [rank for rank, _ in converted_hand]
    is_straight = all(rank_sequence[i] - rank_sequence[i - 1] == 1 for i in range(1, 5))
    is_royal = is_straight and rank_sequence[0] == 10

    # Check for other hand types
    pairs = sum(1 for count in rank_counts.values() if count == 2)
    three_of_a_kind = 3 in rank_counts.values()
    four_of_a_kind = 4 in rank_counts.values()

    if is_royal and is_flush:
        return "Royal Flush"
    elif is_straight and is_flush:
        return "Straight Flush"
    elif four_of_a_kind:
        return "Four of a Kind"
    elif three_of_a_kind and pairs == 1:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif three_of_a_kind:
        return "Three of a Kind"
    elif pairs == 2:
        return "Two Pair"
    elif pairs == 1:
        return "One Pair"
    else:
        return "High Card"



# Initialize and shuffle the deck
deck = initialize_deck()
top_index = 0  # Start at the beginning of the deck

hand, top_index = draw_cards(deck, top_index, 5)


print(evaluate_hand(hand))
show_hand(hand)



for i in range(10):
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)


    print(evaluate_hand(hand))
    show_hand(hand)



for i in range(100):
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)

    if evaluate_hand(hand) == "Two Pair":
        print("Winner!")
        show_hand(hand)



for i in range(1000):
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)

    if evaluate_hand(hand) == "Flush":
        print("Winner!")
        show_hand(hand)

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# # Initialize and shuffle the deck
# deck = initialize_deck()
# top_index = 0  # Start at the beginning of the deck
# 
# hand, top_index = draw_cards(deck, top_index, 5)
# 
# if evaluate_hand(hand) == "Royal Flush":
#     print("Winner!")
#     show_hand(hand)

for i in range(1000000):
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)

    if evaluate_hand(hand) == "Royal Flush":
        print("Winner!")
        show_hand(hand)



wins = 0
N = 10000000

for i in range(N):
    # Initialize and shuffle the deck
    deck = initialize_deck()
    top_index = 0  # Start at the beginning of the deck

    hand, top_index = draw_cards(deck, top_index, 5)

    if evaluate_hand(hand) == "Royal Flush":
        wins += 1
        print("Winner!")
        show_hand(hand)

wins/N

