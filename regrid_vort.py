import pygrib
import numpy
import hdf5storage
import pandas

def leap_day(s):
    return (s.year % 4 == 0) & ((s.year % 100 != 0) | (s.year % 400 == 0)) & (s.month == 2) & (s.day == 29)


dat = pygrib.open('/lustre/ebach/pl.grib').select()

rng = pandas.date_range(start='1/1/1979', end='12/31/2017', freq='D')

mask = leap_day(rng)

all_dat = numpy.zeros([56980, 88838])
for i, dat2 in enumerate(dat):
    dat2.expand_grid(False)
    all_dat[i, :] = dat2.data()[0].data

all_dat2 = all_dat.reshape([56980//4, -1, 88838]).mean(axis=1)
all_dat2 = all_dat2[~mask, :]  # remove leap days
all_dat2.tofile('vort850_daily365_1979-2017.dat')

all_dat5 = all_dat2.reshape([14235//5, -1, 88838]).mean(axis=1)
matfiledata = {}
matfiledata['vort'] = all_dat5
hdf5storage.write(matfiledata, '.', 'data/vort05_365.mat', matlab_compatible=True)

all_dat15 = all_dat5.reshape([2847//3, -1, 88838]).mean(axis=1)
matfiledata = {}
matfiledata['vort'] = all_dat15
hdf5storage.write(matfiledata, '.', 'data/vort15_365.mat', matlab_compatible=True)
