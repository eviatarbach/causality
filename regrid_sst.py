import pygrib
import numpy

dat = pygrib.open('/lustre/ebach/sfc.grib').select()

all_dat = numpy.zeros([56980, 88838])
for i, dat2 in enumerate(dat):
    dat2.expand_grid(False)
    all_dat[i, :] = dat2.data()[0].data

all_dat2 = all_dat.reshape([4, -1, 88838]).mean(axis=0)
numpy.save('sst_g.npy', all_dat2)

all_dat5 = all_dat2.reshape([5, -1, 88838]).mean(axis=0)
numpy.save('sst5_g.npy', all_dat5)

all_dat15 = all_dat5[:2847, :].reshape([3, -1, 88838]).mean(axis=0)
numpy.save('sst15_g.npy', all_dat15)