#!/bin/sh -l


shifter --image=ulissigroup/gaspy_regressions:latest \
    --volume=/global/project/projectdirs/m2755/GASpy_workspaces/GASpy:/home/jovyan/GASpy \
    python /global/project/projectdirs/m2755/GASpy_workspaces/GASpy/GASpy_regressions/examples/update_bimetallic_plots.py
