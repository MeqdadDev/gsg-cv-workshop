import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

PROJECT_UPLOADS = 'static/uploads'

def add_signature(img):
    font = cv.FONT_HERSHEY_SIMPLEX
    org = (50, 50)
    color = (255, 255, 255)
    thickness = 1
    cv.putText(img, 'By Meqdad Darwish', org, font, 1, color, thickness, cv.LINE_AA)

def resize_image_512(img, filename):
    resized = cv.resize(img, (512, 512))
    add_signature(resized)
    cv.imwrite(PROJECT_UPLOADS + "/resized_512_" + filename, resized)
    return resized

# plt.savefig('my_plot.png')

def bgr2rgb(img, filename):
    rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    add_signature(rgb_image)
    cv.imwrite(PROJECT_UPLOADS + "/rgb_" + filename, img)
    return rgb_image

def rgb2gray(img, filename=None):
    gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    add_signature(gray_image)
    if filename != None:
        cv.imwrite(PROJECT_UPLOADS + "/gray_" + filename, gray_image)
    return gray_image

def split_rgb_channels(img, filename):
    r, g, b = cv.split(img)
    # show the channels in one plot
    plt.figure(figsize=(15, 5))
    # Row=1, Cols=3, Fig.No.=1
    plt.subplot(1, 3, 1)
    plt.imshow(r, cmap='Reds_r')
    plt.title('Red Channel')
    # plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(g, cmap='Greens_r')
    plt.title('Green Channel')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(b, cmap='Blues_r')
    plt.title('Blue Channel')
    plt.savefig(PROJECT_UPLOADS + "/split_rgb_channels_" + filename)
    channels_fig = cv.imread(PROJECT_UPLOADS + "/split_rgb_channels_" + filename)
    add_signature(channels_fig)
    return channels_fig

def average_blur(img, filename):
    sizes = [3, 9, 17, 25]
    output_images = []

    for size in sizes:
        blur_filter = np.ones((size, size)) / size**2
        output_images.append(cv.filter2D(img, -1, blur_filter))

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(output_images[0])
    plt.title("Blur 3x3 Filter")

    plt.subplot(1, 4, 2)
    plt.imshow(output_images[1])
    plt.title("Blur 9x9 Filter")

    plt.subplot(1, 4, 3)
    plt.imshow(output_images[2])
    plt.title("Blur 17x17 Filter")

    plt.subplot(1, 4, 4)
    plt.imshow(output_images[3])
    plt.title("Blur 25x25 Filter")

    plt.savefig(PROJECT_UPLOADS + "/average_blur_" + filename)
    blur_fig = cv.imread(PROJECT_UPLOADS + "/average_blur_" + filename)
    add_signature(blur_fig)
    return blur_fig

def gaussian_blur(img, filename):
    g_scales = [3, 9, 17, 25]
    g_sizes = [19, 55, 101, 151]  # X6 times of scale
    g_output_images = []

    for i in range(len(g_scales)):
        g_output_images.append(cv.GaussianBlur(img, (g_sizes[i], g_sizes[i]), g_scales[i]))

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(g_output_images[0])
    plt.title("(si-19, sc-3) Gaussian Filter")

    plt.subplot(1, 4, 2)
    plt.imshow(g_output_images[1])
    plt.title("(si-55, sc-9) Gaussian Filter")

    plt.subplot(1, 4, 3)
    plt.imshow(g_output_images[2])
    plt.title("(si-101, sc-17) Gaussian Filter")

    plt.subplot(1, 4, 4)
    plt.imshow(g_output_images[3])
    plt.title("(si-151, sc-25) Gaussian Filter")

    plt.savefig(PROJECT_UPLOADS + "/gaussian_blur_" + filename)
    g_blur_fig = cv.imread(PROJECT_UPLOADS + "/gaussian_blur_" + filename)
    add_signature(g_blur_fig)
    return g_blur_fig

def detect_edges(img, filename):
    gray_image = rgb2gray(img)

    h_filter = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    catch_v_edges = cv.filter2D(gray_image, -1, h_filter)

    # convole the image with vertical mask to catch horizontal edges
    v_filter = np.transpose(h_filter)
    catch_h_edges = cv.filter2D(gray_image, -1, v_filter)

    # convole the image with a Laplacian mask to catch all edges
    laplacian_filter = np.array([[-1, -1, -1],
                                 [-1, 8, -1],
                                 [-1, -1, -1]])
    catch_all_edges = cv.filter2D(gray_image, -1, laplacian_filter)

    # plot the three figures along with the gray scale resized image in one plot (4 images in total: grayscale, vertical edges, horizontal edges, and all edges)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(catch_v_edges)
    plt.title("Catch V-Edges by H-Filter")

    plt.subplot(1, 3, 2)
    plt.imshow(catch_h_edges)
    plt.title("Catch H-Edges by V-Filter")

    plt.subplot(1, 3, 3)
    plt.imshow(catch_all_edges)
    plt.title("Catch All Edges by Laplacian-Filter")


    plt.savefig(PROJECT_UPLOADS + "/detect_edges_" + filename)
    detect_edges_fig = cv.imread(PROJECT_UPLOADS + "/detect_edges_" + filename)
    add_signature(detect_edges_fig)
    return detect_edges_fig
