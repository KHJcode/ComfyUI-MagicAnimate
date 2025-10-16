# --- diffusers 0.29+ 호환 레이어 (경로/클래스 alias) ---
import importlib, sys

def _alias_module(old_mod, new_mod):
    """import 실패 시 새 경로 모듈을 옛 이름으로 등록"""
    try:
        importlib.import_module(old_mod)
    except Exception:
        try:
            sys.modules[old_mod] = importlib.import_module(new_mod)
        except Exception:
            pass

# 모듈 경로 이동 (0.29+)
_alias_module("diffusers.models.unet_2d_blocks",    "diffusers.models.unets.unet_2d_blocks")
_alias_module("diffusers.models.unet_2d_condition",  "diffusers.models.unets.unet_2d_condition")
_alias_module("diffusers.models.resnet",             "diffusers.models.unets.resnet")
_alias_module("diffusers.models.transformer_2d",     "diffusers.models.transformers.transformer_2d")

# 클래스 이름 변경 (PositionNet/CaptionProjection 등)
try:
    from diffusers.models import embeddings as _emb
    # PositionNet -> GLIGENTextBoundingboxProjection
    if not hasattr(_emb, "PositionNet"):
        from diffusers.models.embeddings import GLIGENTextBoundingboxProjection as _PositionNet
        _emb.PositionNet = _PositionNet
    # CaptionProjection -> PixArtAlphaTextProjection (향후 같은 에러 예방용)
    if not hasattr(_emb, "CaptionProjection"):
        from diffusers.models.embeddings import PixArtAlphaTextProjection as _CaptionProjection
        _emb.CaptionProjection = _CaptionProjection
except Exception:
    pass
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
