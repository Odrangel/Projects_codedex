import imageio.v3 as iio

filenames = ['sp2.png','sp1.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('spidy.gif', images, duration = 500, loop = 0)