#!/bin/bash -l
# created: May 30, 2020 6:27 AM
# author: shahinas
#SBATCH --account=project_2006473
#SBATCH -J ML_Damage_P
#SBATCH -e ML_Damage_P_%j_err
#SBATCH -o ML_Damage_P_%j_out
#SBATCH -N 1
#SBATCH --time=23:59:59
#SBATCH --partition=small
#SBATCH --ntasks-per-node=40
#SBATCH --mail-type=ALL
#SBATCH --mail-user=email@domain.com
#SBATCH --array=1-24:1

unset SLURM_GTIDS
module load abaqus/2022
module load intel-oneapi-compilers-classic
cd /scratch/project_2006473/Workflow_demo/ML_Jobs/Try1/G${SLURM_ARRAY_TASK_ID}/
mkdir tmp_$SLURM_JOB_ID
abq2022 interactive job=ML_Damage_P input=G${SLURM_ARRAY_TASK_ID}.inp  user=enHill48-MBW-VUMAT-v99.f cpus=40 int scratch=tmp_$SLURM_JOB_ID
