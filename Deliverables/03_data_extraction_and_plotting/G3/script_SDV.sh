#!/bin/bash -l
# created: May 30, 2020 6:27 AM
# author: shreyas
#SBATCH --account=project_2006473
#SBATCH -N 1
#SBATCH --time=71:59:59
#SBATCH --partition=small
#SBATCH --mail-type=ALL
#SBATCH --mail-user=shreyas.giridhar@aalto.fi

module load abaqus/2022
module load python-data

rm fracture.csv

echo "running P${VARIABLE}"
rm G3_P_LS_Cr2.rpt
rm G3_P_FD.rpt
abq2022 viewer noGUI=G3_ODB_Script_SDV.py
