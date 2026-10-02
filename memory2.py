from fltk import*
import random
from PIL import Image
import io
import time

def img_resize(fname,width):
    #resizes any image type using high quality PIL library
    img = Image.open(fname) #opens all image formats supported by PIL
    w,h = img.size
    height = int(width*h/w)  #correct aspect ratio
    img = img.resize((width, height), Image.BICUBIC) #high quality resizing
    mem = io.BytesIO()  #byte stream memory object
    img.save(mem, format="PNG") #converts image type to PNG byte stream
    siz = mem.tell() #gets size of image in bytes without reading again
    return Fl_PNG_Image(None, mem.getbuffer(), siz)

def cards(wid):						#callback function for events happening to widgets
	global finisher					#uses 
	loc = ButL.index(wid)			#gets index of pressed button
	indexlist.append(loc)	
	ButL[loc].image(I[loc])			#using index adds image to pressed button
	ButL[loc].deactivate()			#temporarily disables button
	compare = fnames[loc]			#gets filename of image opened
	comparenames.append(compare)
	
	if len(indexlist) == 2:								#this if statement is performed because the finisher needs to update immediately after a matching pair is found
		if comparenames.count(comparenames[-1]) == 2:	#checks if opened images are the same using count()
			finisher += 1								#counter is updated each time previous line is sucessful
			for x in indexlist:
				ButL[x].deactivate()
				ButL[x].image().inactive()
				ButL[x].redraw()
				
			for x in range(2):					#deactivates matching buttons
				indexlist.pop(0)						#removes the first two elements in indexlist, leaves third	
		comparenames.clear()							#clears comparenames so that it can fulfill the first if statement again
			
	if len(indexlist) == 3:			#
		for x in indexlist[:2]:
			ButL[x].activate()		#reactivates the temporarily disabled buttons
			ButL[x].image(Logo)		#cover image is added to the reactivated unmatching buttons 
			ButL[x].redraw()		#makes the cover image visible
			
		indexlist.pop(0)			#removes the first two elements in indexlist, leaves third
		indexlist.pop(0)

	if finisher == 6:		#finisher will be 6 after 6 matches have been found
		fl_message('YOU WIN!!!!')
		
win = Fl_Window(400,400,400,300)	
Logo = Fl_PNG_Image('Garfield_Logo.png').copy(100,100)		#create cover image
indexlist = []			#list of indexes of pressed buttons
comparenames = []		#list of filenames of bressed buttons
finisher = 0			#counter used to determine if you win
ButL = []				#list where buttons will be added

fnames = ['Garf.png','Arlene.png','Nermal.png','Lasagna.png','Odie.png','Jon.png','Garf.png','Arlene.png','Nermal.png','Lasagna.png','Odie.png','Jon.png']
random.shuffle(fnames)		#randomizes the file names
I = []						#list where Fl_Images will be added
count = 0					#counter used to go through fnames in loop below
for name in fnames:			#creating Fl_images using the img_resize function and appending to a list
	I.append(img_resize(fnames[count],100))
	count = count+1

win.begin()
for row in range(3):	#Nested loop creates button widgets
	for col in range(4):
		but = Fl_Button(col*100,row*100,100,100)
		but.image(Logo)
		but.clear_visible_focus()		#removes outline on buttons for looks
		ButL.append(but)				#appends buttons to list for convenience
		ButL[-1].callback(cards)		#

win.end()

win.resizable(win)
win.show()
Fl.run()		
