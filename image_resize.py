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
    return bool(width or height) is not bool(scale)


def process_params(width, height, scale, initial_width, initial_height):
    if scale is not None:
        width = int(initial_width * scale)
        height = int(initial_height * scale)
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
    size_info = '__{width}x{height}'.format(width=str(width),height=str(height))
    filename = os.path.basename(path_to_original)
    image_name, ext = os.path.splitext(filename)
    resized_image_name = '{name}{size}{ext}'.format(
        name=image_name,
        size=size_info, 
        ext=ext
    )
    return resized_image_name


def resize_image(image, width, height):
    resized_image = image.resize((int(width), int(height)))
    return resized_image


def display_warning(width, height, initial_width, initial_height):
    if round((width/initial_width), 2) != round((height/initial_height), 2):
        print('Warning: the picture may be disproportionate')


def save_image(image, output, resized_image_name):
    output_path = '{output}/{name}'.format(output=output, name=resized_image_name)
    try:
            image.save(output_path)
    except (ValueError, IOError):
        return False


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    path_to_original = args.path_to_original
    width = args.width
    height = args.height
    scale = args.scale
    output = args.output
    if validate_params(width, height, scale) is False:
        sys.exit('Invalid parameters')
    try:
        image = Image.open(path_to_original)
    except IOError as err:
        sys.exit(err)
    initial_width, initial_height = image.size
    width, height = process_params(width, height, scale, initial_width, initial_height)
    resized_image = resize_image(image, width, height)
    display_warning(width, height, initial_width, initial_height)
    resized_image_name = name_resized_image(width, height, path_to_original)
    saving = save_image(resized_image, output, resized_image_name)
    if saving is False:
        print('File saving error')







