from sense_hat import SenseHat
from time import sleep, strftime

sense = SenseHat()

# ------------------------------------------------
# DATA
# ------------------------------------------------

# Colours
colours = {
    
  'r' : [255, 0, 0],
  'o' : [255, 165, 0],
  'y' : [255, 255, 0],
  'g' : [0, 128, 0],
  'b' : [0, 0, 255],
  'i' : [75, 0, 130],
  'v' : [238, 130, 238],
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

with open("pictures.txt", "r") as f:
  all_pics = f.readlines()
  
door = all_pics[0]



# ------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------

display_pic(door)

event = sense.stick.wait_for_event()
while True:
  if event.action == "pressed" and event.direction == "middle":
    day = int(strftime("%d"))
    month = strftime("%B")
    if month == "December" and day < 25:
      sense.show_message(str(day))
      display_pic(all_pics[day])
      sleep(5)
    elif month == "December" and day == 25:
      sense.show_message("Merry Christmas!")
      sleep(5)
    else:
      sense.show_message("Keep Waiting")
      sleep(5)


  
