#!/bin/bash
# job name:
#SBATCH --job-name=mn_gjob
#
# Partition:
#SBATCH --partition=savio
#
# Wall clock limit:
#SBATCH --time=05:00:00
#
# Processors:
#SBATCH --ntasks=1
#
# Account:
#SBATCH --account=co_nuclear
#
# Dependency: (only copy after all runs have finished)
#SBATCH --dependency=singleton
#
#SBATCH --output=geom_cp_slurm_%j.out
#SBATCH --error=geom_cp_slurm_%j.err
## Run command
geom="$1"
homepath="$2"
scratchpath="$3"
cp -r $homepath$geom $scratchpath$geom
rm -r $homepath$geom
