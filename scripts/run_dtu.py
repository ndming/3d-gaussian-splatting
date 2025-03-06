import os

scene_dir = "/home/ndming/datasets/DTU_2dgs"
scenes = [24, 37, 40, 55, 63, 65, 69, 83, 97, 105, 106, 110, 114, 118, 122]
factors = [2] * len(scenes)

out_dir = "output/dtu"

for scene, factor in zip(scenes, factors):
    print(f"======= Processing scene {scene_dir}/scan{scene} with factor {factor} =======")
    cmd = f"python train.py -s {scene_dir}/scan{scene} -m {out_dir}/scan{scene} -r {factor} --checkpoint_iterations 7000 30000"
    os.system(cmd)
    cmd = f"python render.py -m {out_dir}/scan{scene} --skip_test"
    os.system(cmd)
    cmd = f"python metrics.py -m {out_dir}/scan{scene}"
    os.system(cmd)
    print(f"======= Done with scene {scene_dir}/scan{scene} =======")