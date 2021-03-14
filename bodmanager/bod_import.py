import os
import pyautogui
from wand.image import Image
from wand.display import display
import pytesseract
from PIL import Image as image
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv

# Read in list of BODs
bod_data = []
with open('../data/bod_list2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for lines in reader:
        bod_data.append(lines)

unique_bods = { 'ringmail leggings', 'ringmail tunic', 'ringmail gloves', 
    'ringmail sleeves', 'chainmail leggings', 'chainmail tunic', 'chainmail coif',
    'platemail helmet', 'platemail gorget', 'platemail tunic', 'platemail arms',
    'platemail legs', 'platemail gloves'}

class BODImporter():
    def __init__(self):
        self.captureBOD

    def captureBOD(self):

        # Find location of BOD on screen and make a screenshot
        bodLoc = pyautogui.locateOnScreen('locator1.png', grayscale = True)
        class gng():
            myScreenshot = pyautogui.screenshot(
                region = (bodLoc[0], bodLoc[1], 350, 300)
            )
            myScreenshot.save('save.png')
        gng()

        # Process screenshot
        with Image(filename='save.png') as img:
            with img.clone() as i:
                i.resize(width = 350*4, height = 300*4) # Increase image size
                i.sharpen(0, 15) # Sharpen (this is the main bottle neck)
                i.despeckle() # Denoise
                i.negate() # Make negative
                i.save(filename = 'save.png') # Save processed screenshot
        
        # Extract text using Google tesseract
        bodText = pytesseract.image_to_string(image.open('save.png'))
        bodText = ' '.join(bodText.split())

        # Delete screenshot
        os.remove('save.png')

        # Read in list of BODs
        # bod_data = []
        # bod_data2 = []
        # with open('../data/bod_list2.csv', 'r') as f:
        #     reader = csv.reader(f, delimiter = ',')
        #     for lines in reader:
        #         # print(lines[2])
        #         bod_data.append(lines[2])
        #         bod_data2.append(' '.join(lines[2:6]))
        #         print(' '.join(lines[2:6]))
        
        # Compare extracted text to a list of BODs
        ratios = [fuzz.token_set_ratio(bodText, ' '.join(name)) + 
            fuzz.token_sort_ratio(bodText, ' '.join(name)) for name in bod_data]
        best_match = ratios.index(max(ratios))
        
        # Return the best match
        return(best_match)