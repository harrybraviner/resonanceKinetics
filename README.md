Resonance Kinetics
==================

This code is intended to produce animated plots of the kinetatics of orbital resonances.

The first version is intended only to support coplanar orbits.

# Units

The time unit is chosen such that the orbital period of a body with unit semi-major axis is one.
It is consistent for the time unit to be years, the length unit to be the astonomical unit, and the central body to be of solar mass.

# Structure of the code

The code does not actually solve the equations of orbital motion.
The function
```python
r(a, e, f)
```
returns the radius given the semi-major axis, eccenticity, and true anomaly of the orbit, using the analytic expression.

To go from the mean anomaly to the true anomaly we need to solve Kepler's equation, which cannot be done analytically.
The function
```python
EFromM(M, e)
```
implements this.
This should probably have some tuning done to it to add a convergence test and to use a power series for the small e case.

# Todo

Some testing still needs to be done.
Devise and document a series of tests for the code.

Can I reduce the number of iterations involved in solving Kepler's equation for small e?
Almost certainly (or even switch to the power series). How do I test for convergence?

Features that need to be added in the immediate future are:
* add option to switch between co-rotating and inertial frames
* add solid point at the end of faint line
* interactive controls during animation

Features for a future version:
* switch to an object-oriented model in which the planets are objects
  (should save us from passing so many orbital parameters around various functions)
* allow mutual inclinations, and a 3d view
