from pybamm import exp, constants, Scalar


def NMC_diffusivity_PeymanMPM(sto, T):
    """
    NMC diffusivity as a function of stochiometry, in this case the
    diffusivity is taken to be a constant. The value is taken from Peyman MPM.

    References
    ----------
    .. [1] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stochiometry
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """

    D_ref = Scalar(8 * 10 ** (-15), "[m2.s-1]")
    E_D_s = Scalar(18550, "[J.mol-1]")
    arrhenius = exp(E_D_s / constants.R * (1 / Scalar(298.15, "[K]") - 1 / T))

    return D_ref * arrhenius