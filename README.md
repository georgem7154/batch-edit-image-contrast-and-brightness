# batch-edit-image-contrast-and-brightness
this python script when run in a folder of png will take each png and add contrast and brightness specified to each and move them to a newly created folder

so in short it takes all png in the folder the py file is run and puts a specifies contrast and brightness to each one of them and moves it to another folder in the same directory. 

to edit contrast and brightness you can edit values in line 40 and 41

a value 1 is used to keep it as is and every 0.1 increases the contrast by 10 percent and -0.1 decreases

contrast_factor = 2  # Increase contrast by 100%
brightness_factor = 1  # Increase brightness by 0%

so here 2 means 1+1 and 1 is got by 0.1*10 so it increase 10*10 times
if i give 1.1 it increases by 10%
if i give 1.4 it increases by 40%
if i give 2.7 it increases by 170%

and same for -ve 
if i give 0.9 it decreases by 10%
if i give 0.5 it decreases by 50%
if i give 0.8 it decreases by 20%
