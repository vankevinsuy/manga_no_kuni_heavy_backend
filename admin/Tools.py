import io
import os
import zipfile
import getopt
import sys
import CommonVariables

import requests
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def imagesToPDF(img_dir, img_name_pattern):
    im_list = []
    data = []

    #recupérer uniquement les fichiers images
    for d in os.listdir(img_dir):
        if '.jpg' in d \
                or \
                '.jpeg' in d \
                or \
                '.png' in d:
            data.append(d)


    #trier les images dans l'ordre
    temp_data = {}
    for file in data:
        s = file.split(img_name_pattern)
        A = s[1]
        temp_data[int(file.split(img_name_pattern)[1].split('.')[0])] = file
    l_keys = list(temp_data.keys())
    l_keys.sort()

    data.clear()
    for key in l_keys:
        data.append(temp_data[key])
        try:
            im_list.append(Image.open(img_dir + "/" + temp_data[key]))
        except:
            pass

    im1 = im_list[0]
    pdf1_filename = img_dir + "/" + "chap_{}.pdf".format(img_dir.split('/')[-1])
    im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=im_list[1:])

def MangaFreakTestUrl(url):
    try:
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        return True
    except:
        return False

def commandLineSetup():
    # récupération de la ligne de commande
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "f:d:",
                                   ["function",
                                    "database"])
    except:
        print("Error in command line")

    for opt, arg in opts:
        if opt in ['-f', '--function']:
            CommonVariables.Command_line['-f'] = arg

        if opt in ['-d', '--database']:
            CommonVariables.Command_line['-d'] = arg