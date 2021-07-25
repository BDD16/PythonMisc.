# /usr/bin/env/python3.7
import binascii
import struct
import sys
import traceback
from typing import Any, Tuple
from PIL import Image
import argparse
from base64 import b64decode

RGB = Tuple[bytes, bytes, bytes]

sys.path.insert(0, '../Controllers')
sys.path.insert(1, '')
sys.path.insert(2, '../Views')

me = '[HidingAnImage]'
HIDDEN_IN_MSB = False


def Int_To_Bin(rgb: Any, endianess: bool = HIDDEN_IN_MSB):
    """
    Int_To_Bin Convert tuple to a binary tuple
    @rtype: object
    @rgb is an integer tuple for (r, g, b)
    returns a string tuple (8b, 8b, 8b) where 8b is 8 bits
    """
    try:
        r, g, b = rgb
    except ValueError:
        r, g, b, p = rgb

    return ('{0:08b}'.format(r),
            '{0:08b}'.format(g),
            '{0:08b}'.format(b)
            )


def Merge_Rgb(space: RGB, hide_this: RGB, endianess: bool = HIDDEN_IN_MSB):
    """
    Merge_Rgb merges two rgb images together
    @space a string tuple representing 8bits (8b, 8b, 8b)
    @hidethis a string tuple representing 8bits (8b, 8b, 8b)
    @endianess a boolean True for littleEndian and False for bigEndian
    @return a merged rgb image, Merging the most significant bits from
            space and merges with hidethis
    """
    space_r, space_g, space_b = space

    hidden = (space_r & ~1 | int(hide_this[0]),
              space_g & ~1 | int(hide_this[1]),
              space_b & ~1 | int(hide_this[2])
              )

    if endianess == HIDDEN_IN_MSB:
        hidden = (space_r & ~128 | struct.unpack("<B", struct.pack(">B", hide_this_r))[0],
                  space_g & ~128 | struct.unpack("<B", struct.pack(">B", hide_this_g))[0],
                  space_b & ~128 | struct.unpack("<B", struct.pack(">B", hide_this_b))[0]
                  )
        print("hidden: ")
        print(hidden)

    return hidden


def XOR_Rgb(space: RGB, hidethis: RGB) -> object:
    space_r, space_g, space_b = space
    hide_this_r, hide_this_g, hide_this_b = hidethis
    return (Int_To_Bin((int(hide_this_r[:4], 2) ^ int(space_r[:], 2),
                        int(hide_this_g[:4], 2) ^ int(space_g[:], 2),
                        int(hide_this_b[:4], 2) ^ int(space_b[:], 2)))
            )


def AND_Rgb(space: RGB, hide_this: RGB) -> object:
    spaceR, spaceG, spaceB = space
    hide_this_r, hide_this_g, hide_this_b = hide_this
    return (Int_To_Bin((int(hide_this_r[:4], 2) & int(spaceR[:], 2),
                        int(hide_this_g[:], 2) & int(spaceG[:], 2),
                        int(hide_this_b[:], 2) & int(spaceB[:], 2)))
            )


def changeEndianType(r: bytearray) -> object:
    """
    ChangeEndianType is a function that changes the endianess of an arbitrary byte
    order.
    @r is the byte input that is coming through.
    """
    i = 0
    result = ""
    while i <= len(r):
        result += r[len(r) - (i + 2)] + r[len(r) - (i + 1)]
        i += 2
    return result


def Bin_To_Int(rgb, endian_type: bool = HIDDEN_IN_MSB):
    """
    Bin_To_Int converts a string tuple to an integer tuple
    @rgb is a string tuple representing 8bits (8b, 8b, 8b)
    @return returns an int tuple
    """
    try:
        r, g, b = rgb
    except ValueError:
        r, g, b, p = rgb
        return (
            int(r, 2),
            int(g, 2),
            int(b, 2),
            int(p, 2)
        )
    return (int(r, 2),
            int(g, 2),
            int(b, 2)
            )

def MergeData(img1, data, endian_type: bool = not HIDDEN_IN_MSB):
    """
        Merge is a function to merge two images together
        Assuming that the image contains the (dimensions of image) + (image data)

        TODO: ENDIANESS will be to use the least significant bytes instead of MSB
        @img1 is the image space to hide in
        @img2 is the image to be cloaked.
        @ENDIANESS is using the LSB or MSB of the image space to hide
        """
    p = 255
    space = img1
    hidden = data

    if ((len(hidden)/8) > (space.size[0] * space.size[1]*3)):
        raise ValueError('There is not enough space for your hidden image, please choose\
                             a different image as your space')
    pixel_map1 = img1.load()
    # pixel_map2 = img2.load()

    newImage = Image.new(img1.mode, img1.size)
    pixelsNew: list = newImage.load()
    linear_length = 0
    linear_string = ''

    # length_to_hide = int(img2.size[0]).to_bytes(4, 'big')
    # width_to_hide = int(img2.size[1]).to_bytes(4, 'big')

    dimensions_to_hide = int(0).to_bytes(4, 'big') + int(len(data)).to_bytes(4, 'big')

    # convert hidden image into a linear binary string
    for z1, z2, z3 in range(hidden):
        linear_string += '{0:08b}'.format(hidden[z1]) + '{0:08b}'.format(hidden[z2]) + '{0:08b}'.format(hidden[z3])

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            rgb1 = Int_To_Bin(pixel_map1[i, j])
            # use a black pixel for now, adjust in settings
            rgb2 = Int_To_Bin((0, 0, 0))
            # if i < img2.size[0] and j < img2.size[1]:
            #     print(pixel_map2[i, j])
            #     rgb2 = Int_To_Bin(pixel_map2[i, j])
            # print(str(rgb1) + str(rgb2))
            # merge 3 bits at a time per pixel so the seen image needs to be w*h*3/8 by pixels size than the hidden image

            if linear_length < len(linear_string):
                rgb = Merge_Rgb(Bin_To_Int(rgb1, endian_type), linear_string[linear_length:linear_length + 3],
                                endian_type)
                print("rgb: " + str(rgb))
                linear_length += 3

            else:
                rgb = Bin_To_Int(rgb1, endian_type)

            # rgb = Bin_To_Int(rgb1, endian_type)

            # pixelsNew[i, j] = Bin_To_Int(rgb, endian_type)
            pixelsNew[i, j] = rgb
    length_of_file_pixels = []
    print("SIZE OF HIDDEN DATA: " + str(len(dimensions_to_hide)))
    """
    TODO: Fix this as the format of the file is well known and this will cause 8 bytes to be lost
    """
    bits = ''
    for byte in dimensions_to_hide:
        bits += '{0:08b}'.format(byte)
    i = 0
    print(bits)
    while i < (len(bits)):
        print(i)
        rgb1 = Int_To_Bin(pixel_map1[i, 0])
        if i == 63:
            replace = [bits[-1], pixel_map1[i, 0][1], pixel_map1[i, 0][2]]
            new_pixel = Merge_Rgb(Bin_To_Int(rgb1, endian_type), replace, endian_type)
            length_of_file_pixels.append(new_pixel)
            break
        new_pixel = Merge_Rgb(Bin_To_Int(rgb1, endian_type), bits[i: i + 3], endian_type)
        length_of_file_pixels.append(new_pixel)

        i += 3

    g = 0
    pixelsNew_copy = pixelsNew
    for newPixel in length_of_file_pixels:
        print(newPixel)
        pixelsNew[0, g] = newPixel
        g += 1

    newI = newImage

    # if endian_type:
    #     for i in range(img1.size[0]):
    #         for j in range(img1.size[1]):
    #             print(j)
    #             print(i)
    #             print(pixelsNew[i, j])
    #             try:
    #                 r, g, b, p = pixelsNew[i, j]
    #
    #             except ValueError:
    #                 r, g, b = pixelsNew[i, j]
    #
    #             r = r.to_bytes(1, 'big')
    #             print(r)
    #             g = g.to_bytes(1, 'big')
    #             print(g)
    #             b = b.to_bytes(1, 'big')
    #             print(b)
    #             print(p)
    #             try:
    #                 pixelsNew[i, j] = (int.from_bytes(r, 'big'), int.from_bytes(g, 'big'),
    #                                    int.from_bytes(b, 'big'), p)
    #             except ValueError:
    #                 pixelsNew[i, j] = (int.from_bytes(r, 'big'), int.from_bytes(g, 'big'),
    #                                    int.from_bytes(b, 'big'))

    print("COMPLETED Hiding Data")
    return newI

def Merge(img1, img2, endian_type: bool = HIDDEN_IN_MSB):
    """
    Merge is a function to merge two images together
    Assuming that the image contains the (dimensions of image) + (image data)

    TODO: ENDIANESS will be to use the least significant bytes instead of MSB
    @img1 is the image space to hide in
    @img2 is the image to be cloaked.
    @ENDIANESS is using the LSB or MSB of the image space to hide
    """
    p = 255
    space = img1
    hidden = img2

    if (hidden.size[0] > space.size[0]) or (hidden.size[1] > space.size[1]):
        raise ValueError('There is not enough space for your hidden image, please choose\
                         a different image as your space')
    pixel_map1 = img1.load()
    pixel_map2 = img2.load()

    newImage = Image.new(img1.mode, img1.size)
    pixelsNew: list = newImage.load()
    linear_length = 0
    linear_string = ''

    length_to_hide = int(img2.size[0]).to_bytes(4, 'big')
    width_to_hide = int(img2.size[1]).to_bytes(4, 'big')

    dimensions_to_hide = length_to_hide + width_to_hide

    # convert hidden image into a linear binary string
    for p in range(img2.size[0]):
        for z in range(img2.size[1]):
            linear_string += '{0:08b}'.format(pixel_map2[p, z][0]) + '{0:08b}'.format(
                pixel_map2[p, z][1]) + '{0:08b}'.format(
                pixel_map2[p, z][2])

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            rgb1 = Int_To_Bin(pixel_map1[i, j])
            # use a black pixel for now, adjust in settings
            rgb2 = Int_To_Bin((0, 0, 0))
            if i < img2.size[0] and j < img2.size[1]:
                print(pixel_map2[i, j])
                rgb2 = Int_To_Bin(pixel_map2[i, j])
            print(str(rgb1) + str(rgb2))
            # merge 3 bits at a time per pixel so the seen image needs to be w*h*3/8 by pixels size than the hidden image

            if linear_length < len(linear_string):
                rgb = Merge_Rgb(Bin_To_Int(rgb1, endian_type), linear_string[linear_length:linear_length + 3],
                                endian_type)
                print("rgb: " + str(rgb))
                linear_length += 3

            else:
                rgb = Bin_To_Int(rgb1, endian_type)

            # rgb = Bin_To_Int(rgb1, endian_type)

            # pixelsNew[i, j] = Bin_To_Int(rgb, endian_type)
            pixelsNew[i, j] = rgb
    length_of_file_pixels = []
    print("DIMENSIONS: " + str(len(dimensions_to_hide)))
    print("WIDTH: " + str(width_to_hide))
    print("Length: " + str(length_to_hide))
    h = 0

    bits = ''
    for byte in dimensions_to_hide:
        bits += '{0:08b}'.format(byte)
    i = 0
    print(bits)
    while i < (len(bits)):
        print(i)
        rgb1 = Int_To_Bin(pixel_map1[i, 0])
        if i == 63:
            replace = [bits[-1], pixel_map1[i, 0][1], pixel_map1[i, 0][2]]
            new_pixel = Merge_Rgb(Bin_To_Int(rgb1, endian_type), replace, endian_type)
            length_of_file_pixels.append(new_pixel)
            break
        new_pixel = Merge_Rgb(Bin_To_Int(rgb1, endian_type), bits[i: i + 3], endian_type)
        length_of_file_pixels.append(new_pixel)

        i += 3

    g = 0
    pixelsNew_copy = pixelsNew
    for newPixel in length_of_file_pixels:
        print(newPixel)
        pixelsNew[0, g] = newPixel
        g += 1

    newI = newImage

    # if endian_type:
    #     for i in range(img1.size[0]):
    #         for j in range(img1.size[1]):
    #             print(j)
    #             print(i)
    #             print(pixelsNew[i, j])
    #             try:
    #                 r, g, b, p = pixelsNew[i, j]
    #
    #             except ValueError:
    #                 r, g, b = pixelsNew[i, j]
    #
    #             r = r.to_bytes(1, 'big')
    #             print(r)
    #             g = g.to_bytes(1, 'big')
    #             print(g)
    #             b = b.to_bytes(1, 'big')
    #             print(b)
    #             print(p)
    #             try:
    #                 pixelsNew[i, j] = (int.from_bytes(r, 'big'), int.from_bytes(g, 'big'),
    #                                    int.from_bytes(b, 'big'), p)
    #             except ValueError:
    #                 pixelsNew[i, j] = (int.from_bytes(r, 'big'), int.from_bytes(g, 'big'),
    #                                    int.from_bytes(b, 'big'))

    print("COMPLETED")
    return newI


def UnMerge(img: Image, endian_type: bool = HIDDEN_IN_MSB):
    """
    figure out which image are which
    """
    pixel_map = img.load()

    new_image = Image.new(img.mode, img.size)
    pixelsNew = new_image.load()
    extracted_bin = []
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            try:
                r, g, b = pixel_map[i, j]  # 0th bit encoded in the three channels
            except ValueError:
                r, g, b, p = pixel_map[i, j]
            extracted_bin.append(r & 1)
            extracted_bin.append(g & 1)
            extracted_bin.append(b & 1)

    data = "".join([str(x) for x in extracted_bin])
    try:
        n = 8
        chunks = [data[i: i + n] for i in range(0, len(data), n)]
        print(chunks)
        data_again = []
        result = b''
        for chunky in chunks:
            data_again.append(int(chunky, 2))

        for data in data_again:
            print("DATA " + str(data))
            result += struct.pack('>B', data)
        print("result: " + str(result))
        hidden_length = int.from_bytes(result[:4], 'big')
        hidden_width = int.from_bytes(result[4:8], 'big')

        print("Hidden Length: " + str(hidden_length))
        print("Hidden Width: " + str(hidden_width))

        result: bytes = result[8:]  # all the pixels should now be in order
        print(len(result))
        print(result)
        t = 0
        for i in range(hidden_length):
            for j in range(hidden_width):
                print("t: " + str(t))
                if (t + 2) < len(result):
                    print(struct.unpack('>1B', result[t:t+1]))
                    pixelsNew[i, j] = (result[t], result[t + 1], result[t + 2])
                    t += 3
                elif (t + 1) < len(result):
                    # TODO: FIX THE UNMERGING!!!!!!
                    pixelsNew[i, j] = (result[t], result[t + 1], 0)
                    t += 2
                elif t < len(result):
                    pixelsNew[i, j] = (result[t], result[t], result[t])
                    t += 1
                else:
                    pixelsNew[i, j] = (0, 0, 0)

        new_image = new_image.crop((0, 0, hidden_length, hidden_width))
        new_image.save("./EXTRACTED.png")
        return new_image

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, limit=5, file=sys.stdout)
        exit()
    print("Something Bad Happened")
    return

    # if endian_type:
    #     for k in range(8):
    #         if (j + k) > img.size[1]:
    #             i += 1
    #             j = 0
    #         r2, g2, b2 = Int_To_Bin(pixel_map[i, j + k] & 0x0001)
    #         r += r2
    #         g += g2
    #         b += b2
    #
    # # Extract last four bits
    # mask = '0000'
    # if not endian_type:
    #     rgb = (r[4:] + mask,
    #            g[4:] + mask,
    #            b[4:] + mask
    #            )
    # if endian_type:
    #     rgb = (
    #         r,
    #         g,
    #         b
    #     )
    #
    # # converting to an integer tuple
    # pixelsNew[i, j] = Bin_To_Int(rgb, endian_type)
    # # if in a valid position then save
    # if pixelsNew[i, j] != (int(mask[0]), int(mask[0]), int(mask[0])):
    #     originalSize = (i + 1, j + 1)

    # # crop the image to it's original size, since we are working off a canvas
    # new_image = new_image.crop((0, 0, originalSize[0], originalSize[1]))
    #
    # new_i = new_image
    # return new_i


def commandLineExample():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    Steganography = subparsers.add_parser('StegoPop')
    Steganography.add_argument('-m', action='store_true',
                               help="-m is a flag to merge or not, leave out if your are unmerging an image")
    Steganography.add_argument('--hi',
                               default=None,
                               help="hidden image or hi, this is the image in which you want to hide")
    Steganography.add_argument('--space',
                               default=None,
                               help="space is the image that you want to be seen or the 'space' in which to hide")
    Steganography.add_argument('--LSB',
                               action='store_true',
                               help="Store the image in the Lease Significant Byte (LSB)")
    Stego = parser.parse_args()
    print("LSB? " + str(Stego.LSB))
    if Stego.m:
        if Stego.hi != None and Stego.space != None:
            NI = Merge(Image.open(Stego.space), Image.open(Stego.hi), Stego.LSB)
            NI.save('./mergedImage.png')
    else:
        if Stego.hi != None:
            NI = UnMerge(Image.open(Stego.hi), Stego.LSB)
            NI.save('./unMergedImage.png')
    print("1337_Tech: It has been a pleasure working with you")


if __name__ == '__main__':
    logo = ''' ____________ _________________  ___________           .__
/_   \_____  \\_____  \______  \ \__    ___/___   ____ |  |__
 |   | _(__  <  _(__  <   /    /   |    |_/ __ \_/ ___\|  |  \\
 |   |/       \/       \ /    /    |    |\  ___/\  \___|   Y  \\
 |___/______  /______  //____/     |____| \___  >\___  >___|  /
            \/       \/                       \/     \/     \/ '''

    print(logo)
    print("\n\n")
    commandLineExample()
