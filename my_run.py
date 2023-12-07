import os

# Convert nifti images to the nnU-net format
# Note the nnunet folder name follows the format, starting with Task ID, followed by Task name.
# The ID and name are consistent with the trained model released by Turkay.
# os.system('python3 convert2nnunet.py --nifti_folder /vol/biodata/data/biobank/18545/abdominal_data '
          '--nnunet_folder /vol/biodata/data/biobank/18545/abdominal_nnunet/Task501_ukbb_4ch '
          '--dataset_name ukbb --num_channels 4')

# os.system('python3 convert2nnunet.py --nifti_folder /vol/biodata/data/biobank/18545/abdominal_data '
          '--nnunet_folder /vol/biodata/data/biobank/18545/abdominal_nnunet/Task502_ukbb_1ch '
          '--dataset_name ukbb --num_channels 1')

# Perform inference using the trained model
os.system('CUDA_VISIBLE_DEVICES=0 nnUNet_raw_data_base=/vol/biodata/data/biobank/18545/abdominal_data '
          'nnUNet_preprocessed=/vol/biodata/data/biobank/18545/abdominal_nnunet/Task501_ukbb_4ch '
          'RESULTS_FOLDER=/vol/biomedic2/wbai/git/UKBB-GNC-Abdominal-Segmentation/ukbb_4ch_model '
          'python3 predict.py --nnunet_folder /vol/biodata/data/biobank/18545/abdominal_nnunet/Task501_ukbb_4ch '
          '--prediction_folder /vol/biodata/data/biobank/18545/abdominal_seg --dataset_name ukbb --num_channels 4')

# Convert nnU-net formatted segmentation back to the original image folder
os.system('python3 convert2original.py --prediction_folder /vol/biodata/data/biobank/18545/abdominal_seg '
          '--output_folder /vol/biodata/data/biobank/18545/abdominal_data')