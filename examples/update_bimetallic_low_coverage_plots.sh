#!/bin/sh -l


shifter --image=ulissigroup/gaspy_regressions:latest \
    --volume=/global/project/projectdirs/m2755/GASpy_workspaces/GASpy_AP:/home/GASpy \
    python /global/project/projectdirs/m2755/GASpy_workspaces/GASpy_AP/GASpy_regressions/examples/update_bimetallic_low_coverage_plots.py
