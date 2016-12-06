'''
Created on Dec 5, 2016
@author: Mitch

'''

def makerunscript(runname):
    #Function to generate a BASH/SLURM runscript  for the given run
    
    runscript ='''#!/bin/bash
# job name:
#SBATCH --job-name=mn_%s
#
# Partition:
#SBATCH --partition=savio
#
# Wall clock limit:
#SBATCH --time=05:00:00
#
# Processors:
#SBATCH --ntasks=20
#
# Account:
#SBATCH --account=co_nuclear
#
#SBATCH --output=%s_slurm_%%j.out
#SBATCH --error=%s_slurm_%%j.err
## Run command
python "%s"''' %(runname[0:2],runname,runname,runname+'.py')
    
    return runscript