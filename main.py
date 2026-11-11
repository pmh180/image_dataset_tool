import sys
from dataset import ImageDataset

def main(argv):
    folder = argv[0] if argv else "."
    print(f"扫描：{folder}")
    try:
        ds = ImageDataset(folder)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"错误: {e}")
        return 1

    print(ds)
    if len(ds) == 0:
        print("没有找到图片文件")
        return 0

    print("\n扩展名统计：")
    for ext, n in ds.ext_stats().items():
        print(f"{ext}:{n}")

    print("\n随机采样3张图片：")
    for p in ds.sample(3, seed=42):
        print(p)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
