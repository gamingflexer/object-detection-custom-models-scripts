import pandas as pd
import sys
import os
from PIL import Image,ImageFilter

# init and number in for loop is for the number of images you have it will generate the double of that number

init = 9
for i in range(0,9):  
    
    file = f'path.../img_{i}.jpeg'
    var = os.path.isfile(file)
    if var == True:
        df = pd.read_csv(f'path../img_{i}.txt',header=None,sep=" ")
        df[1] = df.apply(lambda x: (1 - x[1]),axis=1)

        
        sys.stdout = open(f"img_{init}.txt",'w')
        print(df.to_csv(header=False,index=False,sep=' '))
    

        image = Image.open(f"path../img_{i}.jpeg")

            # image.show()
        #FlipImage = image.transpose(Image.FLIP_LEFT_RIGHT) #use for first iteration
        FlipImage = image.transpose(Image.FLIP_LEFT_RIGHT).filter(ImageFilter.MinFilter(size=3)) #use for second iteration
        

        FlipImage.save(f"img_{init}.jpeg",'jpeg')
        init += 1
    else:
        continue