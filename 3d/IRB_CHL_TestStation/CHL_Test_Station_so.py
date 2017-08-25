"""
The split operator module for air/water flow around a moving rigid cylinder
"""
from proteus.default_so import *
from proteus import Context
import CHL_Test_Station
Context.setFromModule(CHL_Test_Station)
ct = Context.get()

if ct.useOnlyVF:
    pnList = [("twp_navier_stokes_p", #0
               "twp_navier_stokes_n"),
              ("vof_p", #1
               "vof_n")]
else:
    pnList = [("twp_navier_stokes_p" , #0
               "twp_navier_stokes_n"),
              ("vof_p" , #1
               "vof_n"),
              ("ls_p" , #2
               "ls_n"),
              ("redist_p" ,#3
               "redist_n"),
              ("ls_consrv_p" ,#4
               "ls_consrv_n")]

if ct.movingDomain:
    pnList = [("moveMesh_p","moveMesh_n")]+pnList

if ct.useRANS > 0:
    pnList.append(("kappa_p",
                   "kappa_n"))
    pnList.append(("dissipation_p",
                   "dissipation_n"))
name = "CHL_Test_Station"

#systemStepControllerType = ISO_fixed_MinAdaptiveModelStep
systemStepControllerType = Sequential_MinAdaptiveModelStep
#systemStepControllerType = Sequential_FixedStep_Simple # uses time steps in so.tnList
stepExactSystem=False

needEBQ_GLOBAL = False
needEBQ = False

tnList = [0.0,ct.dt_init,1e-3]+[i*ct.dt_out for i in range(1,ct.nDTout+1)]