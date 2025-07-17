import numpy as np
import simulate


def test_force_between_planets():
    position1 = np.array([0.0, 0.0, 0.0])
    mass1 = 1.0
    position2 = np.array([1.0, 0.0, 0.0])
    mass2 = 2.0

    force = simulate.force_between_planets(position1, mass1, position2, mass2)

    assert np.allclose(force, [2.0, 0.0, 0.0])
