#!/bin/bash


#SBATCH --constraint=knl
#SBATCH --nodes=1
#SBATCH --exclusive
#SBATCH --time=30:00:00
#SBATCH --account=m2755
#SBATCH --qos=regular
#SBATCH --image=ulissigroup/gaspy_regressions:latest
#SBATCH --volume=/global/project/projectdirs/m2755/GASpy_workspaces/GASpy:/home/GASpy
#SBATCH --job-name=predict_CO
#SBATCH --chdir=/global/project/projectdirs/m2755/GASpy_workspaces/GASpy/logs/regressions
#SBATCH --output=predict_CO.log
#SBATCH --error=predict_CO.log
#SBATCH --open-mode=append
#SBATCH --mail-user=ktran@andrew.cmu.edu
#SBATCH --mail-type=FAIL

export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export OMP_NUM_THREADS=1

srun shifter python -c "from gaspy_regress import cache_predictions; cache_predictions('CO', processes=64)"
