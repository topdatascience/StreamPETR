import os
import tqdm
import json
import argparse
from visual_nuscenes import NuScenes

def main(use_gt, out_dir, result_json, dataroot, version):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    if use_gt:
        nusc = NuScenes(version=version, dataroot=dataroot, verbose=True, pred=False, annotations="sample_annotation")
    else:
        nusc = NuScenes(version=version, dataroot=dataroot, verbose=True, pred=True, annotations=result_json, score_thr=0.25)

    with open('{}.json'.format(result_json)) as f:
        table = json.load(f)
    tokens = list(table['results'].keys())

    for token in tqdm.tqdm(tokens[:100]):
        if use_gt:
            nusc.render_sample(token, out_path=os.path.join(out_dir, token + "_gt.png"), verbose=False)
        else:
            nusc.render_sample(token, out_path=os.path.join(out_dir, token + "_pred.png"), verbose=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize NuScenes data")
    parser.add_argument('--use_gt', action='store_true', help='Use ground truth annotations')
    parser.add_argument('--out_dir', type=str, default='./result_vis/', help='Output directory for visualizations')
    parser.add_argument('--result_json', type=str, required=True, help='Path to the result JSON file')
    parser.add_argument('--dataroot', type=str, default='data/nuscenes', help='NuScenes data root directory')
    parser.add_argument('--version', type=str, default='v1.0-mini', help='NuScenes dataset version')
    args = parser.parse_args()
    main(args.use_gt, args.out_dir, args.result_json, args.dataroot, args.version)

