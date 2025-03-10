import os
import tqdm
import json
from visual_nuscenes import NuScenes
use_gt = False
out_dir = './result_vis/'
result_json = "test/repdetr3d_eva02_800_bs2_seq_24e/Thu_Mar__6_15_22_07_2025/pts_bbox/results_nusc"
dataroot='v1.0-mini'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

if use_gt:
    nusc = NuScenes(version='v1.0-mini', dataroot=dataroot, verbose=True, pred = False, annotations = "sample_annotation")
else:
    nusc = NuScenes(version='v1.0-mini', dataroot=dataroot, verbose=True, pred = True, annotations = result_json, score_thr=0.25)

with open('{}.json'.format(result_json)) as f:
    table = json.load(f)
tokens = list(table['results'].keys())

for token in tqdm.tqdm(tokens[:100]):
    if use_gt:
        nusc.render_sample(token, out_path = "./result_vis/"+token+"_gt.png", verbose=False)
    else:
        nusc.render_sample(token, out_path = "./result_vis/"+token+"_pred.png", verbose=False)

