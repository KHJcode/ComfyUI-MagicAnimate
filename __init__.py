# --- diffusers 0.29+ 경로 변경 호환 레이어 ---
import importlib, sys

def _alias(old, new):
    try:
        importlib.import_module(old)
    except Exception:
        try:
            sys.modules[old] = importlib.import_module(new)
        except Exception:
            pass

_alias("diffusers.models.unet_2d_blocks",    "diffusers.models.unets.unet_2d_blocks")
_alias("diffusers.models.unet_2d_condition",  "diffusers.models.unets.unet_2d_condition")
_alias("diffusers.models.resnet",             "diffusers.models.unets.resnet")
_alias("diffusers.models.transformer_2d",     "diffusers.models.transformers.transformer_2d")
# --- 호환 레이어 끝 ---

import folder_paths
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "libs"))

os.makedirs(os.path.join(folder_paths.models_dir, "MagicAnimate"), exist_ok=True)

folder_paths.add_model_folder_path("magic_animate", os.path.join(folder_paths.models_dir, "MagicAnimate"))
folder_paths.folder_names_and_paths['magic_animate'] = (folder_paths.folder_names_and_paths['magic_animate'][0], folder_paths.supported_pt_extensions) # | {'.json'})

magic_animate_checkpoints = folder_paths.get_filename_list("magic_animate")

assert len(magic_animate_checkpoints) > 0, "ERROR: No Magic Animate checkpoints found. Please download & place them in the ComfyUI/models/magic_animate folder, and restart ComfyUI."

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
