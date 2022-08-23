import os
import pyheif
from PIL import Image

def commom_images_to_jpg(full_path, destiny):
    img = Image.open(full_path)
    
    rgb_img = img.convert('RGB')
    
    rgb_img.save(destiny)


def heic_images_to_jpg(full_path, destiny):
    heif_image = pyheif.read(full_path)

    img = Image.frombytes(
        heif_image.mode, 
        heif_image.size, 
        heif_image.data,
        "raw",
        heif_image.mode,
        heif_image.stride,
    )

    img.save(destiny, 'JPEG')



def main():
    print('Type the path from here you want to convert the image files to JPG: ')
  
    try:
        path = str(input())

        files = os.listdir(path)

        os.mkdir('../converted_images')

        for f in files:
            full_path = path + '/' + f
        
            if (not os.path.isfile(full_path)): continue
            
            origin_name = f.split('.')[0]

            destiny = '../converted_images/' + origin_name + '.jpg'
            
            if (not f.endswith('.heic')):
                commom_images_to_jpg(full_path, destiny)
            else:
                heic_images_to_jpg(full_path, destiny)

        print('Conversion completed successfully!')
    except Exception as err:
        print('Something went wrong. Check the path or files.')
        print(err)


main()
