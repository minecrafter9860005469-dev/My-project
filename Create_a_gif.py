import imageio.v3 as iio

filesnames = ['team-pic1.png', 'team-pic2.png']

images = []

for filename in filesnames:
    images.append(iio.imread(filename))

iio.imwrite("team.gif", images, duration = 500, loop = 0)

