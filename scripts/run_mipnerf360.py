import os

scene_dir = "/home/ndming/datasets/360_v2"
scenes = ["bicycle", "bonsai", "counter", "flowers", "garden", "kitchen", "room", "stump", "treehill"]
factors = [2] * len(scenes)

out_dir = "output/mipnerf360"

for scene, factor in zip(scenes, factors):
    print(f"======= Processing scene {scene_dir}/{scene} with factor {factor} =======")
    cmd = f"python train.py -s {scene_dir}/{scene} -m {out_dir}/{scene} -r {factor} --checkpoint_iterations 7000 30000 --eval"
    os.system(cmd)
    cmd = f"python render.py -m {out_dir}/{scene} --skip_train"
    os.system(cmd)
    cmd = f"python metrics.py -m {out_dir}/{scene}"
    os.system(cmd)
    print(f"======= Done with scene {scene_dir}/{scene} =======")