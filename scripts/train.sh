!python train.py \
--name zaloai_resnet34 \
--num_labels 2 \
--scaled_width 224 \
--scaled_height 224 \
--train_root ../zaloai/train/videos \
--train_list ../zaloai/train/train_annotations.txt \
--val_root ../zaloai/train/videos \
--val_list ../zaloai/train/val_annotations.txt \
--backbone resnet34 \
--num_threads 16 \
--seed 2021 \
--batch_size 32 \
--rotate 20 \
--color_aug_ratio 0.3 \
--save_dir checkpoints \
--max_epoch 150 \
--optimizer adamw \
--weight_decay 0.00005 \
--lr 2e-4 \
--lr_policy onecycle \
--lr_gamma 0.5 \
--patience 50 \
--loss focal \
--gpus -1 \
--accelerator ddp