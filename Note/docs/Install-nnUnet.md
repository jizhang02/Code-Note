# Install nnUnet
* out-of-the-box segmentation algorithm
`pip install nnunetv2`
* to modify code, open a terminal, select a directory:
```
git clone https://github.com/MIC-DKFZ/nnUNet.git
cd nnUNet
pip install -e .
```
1. Create 3 folders in folder `nnUNet`, `nnUNet_raw`, `nnUNet_preprocessed`, `nnUNet_results`
2. Set environment variables
    - Linux, temporary in terminal (permanent in home folder `.bashrc`):
    - Windows, temporary in Command prompt (permanent in Edit Environment Variable GUI):
    - in code: `/home/jing/pycode/nnUNet/nnunetv2/paths.py`

```
# in Linux
export nnUNet_raw='/home/jing/pycode/nnUNet/nnUNet_raw'
export nnUNet_preprocessed='/home/jing/pycode/nnUNet/nnUNet_preprocessed'
export nnUNet_results='/home/jing/pycode/nnUNet/nnUNet_results'
# in Windows
set nnUNet_raw=C:/Users/jing/pycode/nnUNet_raw
set nnUNet_preprocessed=C:/Users/jing/pycode/nnUNet_preprocessed
set nnUNet_results=C:/Users/jing/pycode/nnUNet_results
# in code, added by user
os.environ['nnUNet_raw'] = r'/home/jing/pycode/nnUNet/nnUNet_raw'
os.environ['nnUNet_preprocessed'] = r'/home/jing/pycode/nnUNet/nnUNet_preprocessed'
os.environ['nnUNet_results'] = r'/home/jing/pycode/nnUNet/nnUNet_results'
```
3. Dataset conversion    
   in file `/home/jing/pycode/nnUNet/pyproject.toml`, a sentence like
```
nnUNetv2_convert_MSD_dataset = "nnunetv2.dataset_conversion.convert_MSD_dataset:entry_point"
``` 
shows the path, along the path find out file `convert_MSD_dataset.py`, in the last line, change the parameter, then run it.    
```
convert_msd_dataset('/home/jing/pycode/nnUNet/nnUNet_raw/Task05_Prostate', overwrite_target_id=1101)
```
4. Experiment planning and preprocessing
     - in terminal `nnUNetv2_plan_and_preprocess -d DATASET_ID --verify_dataset_integrity # DATASET_ID is 1101`
     - in code, search `nnUNetv2_plan_and_preprocess` in the file `pyproject.toml`, you will find:
```
nnUNetv2_plan_and_preprocess = "nnunetv2.experiment_planning.plan_and_preprocess_entrypoints:plan_and_preprocess_entry"
```
then go to this file  `plan_and_preprocess_entry.py`, then run it after adding a default parameter in function `plan_and_preprocess_entry`:
```
parser.add_argument('-d', nargs='+', type=int,
help="[REQUIRED] List of dataset IDs. Example: 2 4 5. This will run fingerprint extraction, experiment "
"planning and preprocessing for these datasets. Can of course also be just one dataset", default=[1101])
```
5. Model training
   - in terminal `nnUNetv2_train DATASET_NAME_OR_ID UNET_CONFIGURATION FOLD [additional options, see -h]`
   - in code, search `nnUNetv2_train` in the file `pyproject.toml`, you will find:
```
nnUNetv2_train = "nnunetv2.run.run_training:run_training_entry"
```
then go to this file  `run_training_entry.py`, then run it after adding a default parameter in function `run_training_entry`:
```
parser.add_argument('dataset_name_or_id', type=str, required=False, help="Dataset name or ID to train with", default='1101')
parser.add_argument('configuration', type=str, required=False, help="Configuration that should be trained")
parser.add_argument('fold', type=str, default='1', required=False, help='Fold of the 5-fold cross-validation. Should be an int between 0 and 4.')
```
6. Model predicting (similar as above)

✴️ reference: https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/how_to_use_nnunet.md
