import os
import random
from collections import Counter

class ImageDataset:
    def __init__(self, folder_path):
        self.folder = folder_path
        if not os.path.isdir(self.folder):
            raise NotADirectoryError(f"不是目录：{self.folder}")
        
        # 支持的图片后缀
        self.suffix_list = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
        self.paths = []

        for fname in os.listdir(self.folder):
            full_path = os.path.join(self.folder, fname)
            if os.path.isfile(full_path):
                ext = os.path.splitext(fname)[1].lower()
                if ext in self.suffix_list:
                    self.paths.append(full_path)

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        return self.paths[idx]

    def __repr__(self):
        return f"ImageDataset(folder='{self.folder}', count={len(self)})"

    def ext_stats(self):
        ext_list = [os.path.splitext(p)[1].lower() for p in self.paths]
        return dict(Counter(ext_list))

    def sample(self, n, seed=None):
        if seed is not None:
            random.seed(seed)
        return random.sample(self.paths, min(n, len(self.paths)))
