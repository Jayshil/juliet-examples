# `juliet` documentation for occultation and phase curves

<i>Prepared by: Jayshil A Patel ([jaspa@dtu.dk](mailto:jaspa@dtu.dk))</i>

This repository provides documentation for occultation and phase curve fitting in `juliet` using real observational data. `juliet` identifies the type of fitting by the provided priros:
- Priors included limb darkening coefficients (LDCs), `q1` and `q2`: transit fitting
- Priors included eclipse depth, `fp` but not LDCs: only eclipse fitting
- Priors included both eclipse depth and LDCs: joint transit and eclipse fitting.
- Additional priors for different types of phase curve models.

The present repository has some tutorials for this:
- `single_instrument.ipynb`: Occultation and transit+occultation fitting for single instrument using TESS data
- `multi_instruments.ipynb`: Transit+occultation modelling for multiple instruments using TESS+CHEOPS data
- `ca8_lambert.ipynb`: [Cowan & Agol (2008)](https://ui.adsabs.harvard.edu/abs/2008ApJ...678L.129C/abstract) and Lambertian phase curve model using CHEOPS data. This notebook also demonstrates the peculiarity of CHEOPS data fitting, and how to do that using `juliet`.
- `kelp_thermal.ipynb`: Thermal emission phase curve modelling with the model from [`kelp`](https://kelp.readthedocs.io/en/latest/index.html) package. This is demonstrated using TESS data.
- `kelp_refl_homo.ipynb`: Reflected light phase curve for a homogeneous sphere as derived in [Heng et al. 2021](https://ui.adsabs.harvard.edu/abs/2021NatAs...5.1001H/abstract) and implemented in [`kelp`](https://kelp.readthedocs.io/en/latest/index.html) package, using Kepler data.
- `kelp_refl_inhomo.ipynb`: Reflected light phase curve for a inhomogeneous sphere as derived in [Heng et al. 2021](https://ui.adsabs.harvard.edu/abs/2021NatAs...5.1001H/abstract) and implemented in [`kelp`](https://kelp.readthedocs.io/en/latest/index.html) package, using Kepler data.

The Data directory contains all the data needed to run all notebooks. Feel free to contact me if you have any questions!