#!/bin/sh -l

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=06:00:00
#SBATCH --partition=regular
#SBATCH --job-name=predict
#SBATCH --output=predict-%j.out
#SBATCH --error=predict-%j.error
#SBATCH --constraint=haswell

# Load GASpy
. ~/GASpy/scripts/load_env.sh
cd $GASPY_REG_PATH/scripts

# Use a surrogate model to make predictions
python predict.py
