#!/bin/bash

# Slurm submission script, 
# GPU job 
# CRIHAN v 1.00 - Jan 2017 
# support@criann.fr

# Not shared resources
#SBATCH --exclusive
# Job name
#SBATCH -J "unet"
# Batch output file
#SBATCH --output unet.o%J
# Batch error file
#SBATCH --error unet.e%J
# GPUs architecture and number
# ----------------------------
# Partition (submission class)
#SBATCH --partition gpu_p100
# GPUs per compute node
#   gpu:4 (maximum) for gpu_k80 
#   gpu:2 (maximum) for gpu_p100 
##SBATCH --gres gpu:4
#SBATCH --gres gpu:1
# ----------------------------
# Job time (hh:mm:ss)
#SBATCH --time 24:00:00
# ----------------------------
# Compute nodes number
##$BATCH --nodes 4
# MPI tasks per compute node
##SBATCH --ntasks-per-node 2 
# CPUs per MPI task
# (by default, OMP_NUM_THREADS is set to the same value)
##SBATCH --cpus-per-task 4 
# MPI task maximum memory (MB)
#SBATCH --mem-per-cpu 3000 
# ----------------------------
#SBATCH --mail-type ALL
# User e-mail address
#SBATCH --mail-user jing.zhang@insa-rouen.fr
# environments
# ---------------------------------
module load cuda/9.0
module load python3/3.6.1_dl

# Copy input data and go to working directory
cp -r unet-finetune-crossvalid/data/Melanoma $LOCAL_WORK_DIR
cp -r unet-finetune-crossvalid/ $LOCAL_WORK_DIR
cd $LOCAL_WORK_DIR/
echo Working directory : $PWD

srun python3 $PWD/unet-finetune-crossvalid/main-finetune.py

# Move output data to target directory
mkdir $SLURM_SUBMIT_DIR/$SLURM_JOB_ID
cp -r unet-finetune-crossvalid/ $SLURM_SUBMIT_DIR/$SLURM_JOB_ID



