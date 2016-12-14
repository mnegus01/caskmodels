#!/bin/bash
# job name:
#SBATCH --job-name=mn_hold
#
# Partition:
#SBATCH --partition=savio
#
# Wall clock limit:
#SBATCH --time=00:00:10
#
# Processors:
#SBATCH --ntasks=1
#
# Account:
#SBATCH --account=co_nuclear
#
# Dependency: (only start this geometry after last geometry has finished))
#
#SBATCH --dependency=afterany:1011547
#
#SBATCH --output=hold_slurm_%j.out
#SBATCH --error=hold_slurm_%j.err
## Run command
sh runADVANTG_geom_copy.sh prob_2 fwcadis ~/CaskModels/char_tests/ADVANTG_tests/runscripts/fwcadis/ /global/scratch/co_nuclear/NE255project/char_tests/ ~/CaskModels/char_tests/ADVANTG_tests/fwcadis/ /global/scratch/mgnegus/ADVANTG/fwcadis/
