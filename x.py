from PIL import Image
import matplotlib.pyplot as plt
import random
import os

# Set dataset path
dataset_path = '101_ObjectCategories'
class_names = sorted(os.listdir(dataset_path))

# Select 20 random classes
random_classes = random.sample(class_names, 10)

# Display one random image from each of the 10 classes
plt.figure(figsize=(5, 5))
for i, class_name in enumerate(random_classes):
    class_dir = os.path.join(dataset_path, class_name)
    image_name = random.choice(os.listdir(class_dir))
    image_path = os.path.join(class_dir, image_name)
    image = Image.open(image_path)  # Open image with PIL directly

    plt.subplot(4, 5, i + 1)
    plt.imshow(image)
    plt.title(class_name)
    plt.axis("off")

plt.tight_layout()
plt.show()
