from pathlib import Path

from torchvision import datasets


root = Path("app").resolve()
out_dir = Path("app/test_samples").resolve()
test_data = datasets.MNIST(root=root / "data", train=False, download=False)

saved = set()

for image, label in test_data:
    if label in saved:
        continue

    image.save(out_dir / f"digit_{label}.png")
    saved.add(label)
    # lấy 10 cái
    if len(saved) == 10:
        break

print(sorted(saved))
