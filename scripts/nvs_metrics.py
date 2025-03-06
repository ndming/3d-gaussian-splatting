from pathlib import Path
import json

model_home_dir = "output/dtu"
scenes = [24, 37, 40, 55, 63, 65, 69, 83, 97, 105, 106, 110, 114, 118, 122]

ssims = []
psnrs = []
lpips = []

for scene in scenes:
    model_dir = Path(model_home_dir) / f"scan{scene}"
    result_file = model_dir / "results.json"
    
    # Print a warning if cannot find the file
    if not result_file.exists():
        print(f"WARNING: Could not find {result_file} for model {model_dir}")
        continue

    with open(result_file, "r") as f:
        results = json.load(f)
        ssims.append(results["ours_30000"]["SSIM"])
        psnrs.append(results["ours_30000"]["PSNR"])
        lpips.append(results["ours_30000"]["LPIPS"])

print("DTU metrics - 3DGS vanilla")
print("- Average SSIM:",  sum(ssims) / len(ssims))
print("- Average PSNR:",  sum(psnrs) / len(psnrs))
print("- Average LPIPS:", sum(lpips) / len(lpips))