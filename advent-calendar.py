from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours
colours = {

  'r' : [255, 0, 0],
  'n' : [135, 80, 22],
  'w' : [255, 255, 255],
  'e' : [0, 0, 0]  # e stands for empty/black

}

# Pictures


# ------------------------------------------------
# FUNCTIONS
# ------------------------------------------------
# Display a given picture string on the sense HAT
# ------------------------------------------------
def display_pic(pic_string):

  # Get rid of newline and split the line into a list
  pic_string = pic_string.strip("\n")
  pic_string = pic_string.split(",")

  # Look up each letter in the dictionary of colours and add it to the list
  pic_list = []
  for letter in pic_string:
      pic_list.append(colours[letter])

  # Display the pixel colours from the file
  sense.set_pixels(pic_list)



# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------
