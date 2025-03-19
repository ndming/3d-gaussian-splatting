import os

scene_dir = "C:/Users/ZODNGUY1/datasets/dtu"
scenes = [24, 37, 40, 55, 63, 65, 69, 83, 97, 105, 106, 110, 114, 118, 122]
factors = [2] * len(scenes)

out_dir = "C:/Users/ZODNGUY1/OneDrive - Carl Zeiss AG/gaussian/repos/3d-gaussian-splatting/output/dtu"

for scene, factor in zip(scenes, factors):
    print(f"======= Processing scene {scene_dir}/scan{scene} with factor {factor} =======")
    cmd = f"python train.py -s {scene_dir}/scan{scene} -m \"{out_dir}/scan{scene}\" -r {factor} --checkpoint_iterations 7000 30000 --ignore_alpha"
    print("[>] " + cmd)
    os.system(cmd)
    cmd = f"python render.py -m \"{out_dir}/scan{scene}\" -r 2 --skip_test"
    print("[>] " + cmd)
    os.system(cmd)
    cmd = f"python metrics.py -m \"{out_dir}/scan{scene}\""
    print("[>] " + cmd)
    os.system(cmd)
    print(f"======= Done with scene {scene_dir}/scan{scene} =======\n")