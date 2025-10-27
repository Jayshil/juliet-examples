# juliet-examples

<i>Prepared by: Jayshil A Patel ([jayshil.patel@astro.su.se](mailto:jayshil.patel@astro.su.se))</i>

Minimal working examples for eclipse, eclipse-transit fitting in juliet

Data used: transit lightcurves of WASP-18 observed by TESS in Sector 2 and 3 (see, Data folder).


`juliet` identifies the type of fitting by the provided priros:
- Priors included limb darkening coefficients (LDCs), `q1` and `q2`: transit fitting
- Priors included eclipse depth, `fp` but not LDCs: only eclipse fitting
- Priors included both eclipse depth and LDCs: joint transit and eclipse fitting.

The present repository has some tutorials for this:
- `eclipse_only.ipynb` notebook: eclipse-only fitting for 1 instrument
- `transit_and_eclipse.ipynb` notebook: a joint transit and eclipse fitting for 1 instrument
- `multi-instrument-1.ipynb` notebook: A simultaneous transit and eclipse fitting for 2 instruments; a common transit depth fitted for both instruments, but a different eclipse depth parameters for both instruments (useful for variability checking).
- `multi-instrument-2.ipynb` notebook: A simultaneous transit and eclipse fitting for 2 instruments; common transit and eclipse depths are fitted both instruments.
- `multi-instrument-3.ipynb` notebook: A simultaneous transit and eclipse fitting for 2 instruments; different transit depths are fitted for both instruments, while a common eclipse depth for both instruments.

Feel free to contact me if you have any questions!