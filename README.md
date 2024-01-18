

# Installation

poetry source add -p explicit pytorch https://download.pytorch.org/whl/lts/1.8/cu111
poetry add --source pytorch torch torchvision


# Usage

Coco example usage via `torchrun`:

```
poetry run torchrun 
--nnodes=1
--nproc_per_node=2 
--master_port=29501
--max-restarts=3
dela_cond_detr/main.py
--dataset_file coco 
--coco_path dela_cond_detr/data/coco 
--epochs 25
--batch_size 4 
--model dela-cond-detr 
--repeat_label 2 
--nms 
--wandb
--resume  /home/david/addn_repos/dela_cond_detr/work_dirs/srd_dela-cond-detr_bs2x4_seed9816/checkpoint.pth
```
poetry run torchrun --nnodes=1 --nproc_per_node=2 --master_port=29501 --max-restarts=1 dela_cond_detr/main.py --dataset_file srd --coco_path /home/david/production/yolov5/datasets/srd40.2.1 --epochs 50 --batch_size 2 --model dela-cond-detr --repeat_label 2 --nms 

