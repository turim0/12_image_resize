import argparse
import os
import sys
from PIL import Image


def create_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('path_to_original', type=str)
    parser.add_argument('-w', '--width', type=int, default=None)
    parser.add_argument('-h', '--height', type=int, default=None)
    parser.add_argument('-s', '--scale', type=float, default=None)
    parser.add_argument('-o', '--output', default=os.getcwd())
    return parser


def validate_params(width, height, scale):
    if (width or height) and scale is not None:
        sys.exit('Variable scale is not compatible with height and weight')


def scale_process(width, height, scale, initial_width, initial_height):
    if scale is not None:
        width = initial_width * scale
        height = initial_height * scale
        return width, height
    elif width is None and height is not None:
        ratio = height / initial_height
        width = int(initial_width * ratio)
        return width, height
    elif width is not None and height is None:
        ratio = width / initial_width
        height = int(initial_height * ratio)
        return width, height
    else:
        return width, height


def name_resized_image(width, height, path_to_original):
    size_info = '__' + str(width) + 'x' + str(height)
    filename = os.path.basename(path_to_original)
    ext = os.path.splitext(filename)[1]
    image_name = os.path.splitext(filename)[0]
    resized_image_name = image_name + size_info + ext
    return resized_image_name


def resize_image(image, width, height):
    resized_image = image.resize((int(width), int(height)))
    return resized_image


def warning(width, height, initial_width, initial_height):
    if round((width/initial_width), 2) != round((height/initial_height), 2):
        print('Warning: the picture may be disproportionate')


def save_image(image, output, resized_image_name):
    ext = os.path.splitext(resized_image_name)[1]
    try:
        if ext == '.jpg' or ext == '.jpeg':
            image.save(output+'/'+resized_image_name, 'jpeg')
        elif ext == '.png':
            image.save(output + '/' + resized_image_name, 'png')
    except (ValueError, IOError) as err:
        print(err)


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    path_to_original = namespace.path_to_original
    width = namespace.width
    height = namespace.height
    scale = namespace.scale
    output = namespace.output
    validate_params(width, height, scale)
    try:
        image = Image.open(path_to_original)
    except IOError as err:
        print(err)
        sys.exit()
    initial_width, initial_height = image.size
    width, height = scale_process(width, height, scale, initial_width, initial_height)
    resized_image = resize_image(image, width, height)
    warning(width, height, initial_width, initial_height)
    resized_image_name = name_resized_image(width, height, path_to_original)
    save_image(resized_image, output, resized_image_name)







