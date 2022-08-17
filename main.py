import os
from PIL import Image
from wand.image import Image as ImageWand


def commom_images_to_jpg(f, path, origin_name):
    full_path = path + '/' + f
    
    img = Image.open(full_path)
    
    rgb_img = img.convert('RGB')
    
    rgb_img.save('../converted_images/' + origin_name + '.jpg')


def heic_images_to_jpg(f, path, origin_name):
    full_path = path + '/' + f

    destiny = '../converted_images/' + origin_name + '.JPG'

    print(destiny)
    img = ImageWand(filename=full_path)
    img.format='jpg'
    img.save(filename=destiny)
    img.close()



def main():
    print('Type the path from here you want to convert the image files to JPG:')
  
    try:
        path = str(input())

        files = os.listdir(path)

        os.mkdir('../converted_images')

        for f in files:
            origin_name = f.split('.')[0]
            
            if (not f.endswith('.heic')):
                commom_images_to_jpg(f, path, origin_name)
            else:
                heic_images_to_jpg(f, path, origin_name)

        print('Conversion completed successfully!')
    except Exception as err:
        print('Something went wrong. Check the path or files.')
        print(err)


main()

# to install the dependencies: pip install -r requirements.txt