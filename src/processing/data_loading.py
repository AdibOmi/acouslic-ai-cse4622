import os

# ---- Step 1: Set local base directory ----
# Change this to your local dataset path
BASE_DIR = r'F:\acouslic-ai-train-set'

# ---- Step 2: Define image and mask subdirectories ----
image_dir = os.path.join(BASE_DIR, 'images', 'stacked_fetal_ultrasound')
mask_dir = os.path.join(BASE_DIR, 'masks', 'stacked_fetal_abdomen')

# ---- Step 3: Debug print ----
print(f"Image directory: {image_dir}")
print(f"Mask directory: {mask_dir}")

# ---- Step 4: Check files ----
print("\nFirst 5 image files:")
for f in os.listdir(image_dir)[:5]:
    print(f)

print("\nFirst 5 mask files:")
for f in os.listdir(mask_dir)[:5]:
    print(f)

# ---- Step 5: Get unique case IDs ----
all_case_ids = [f.split('.')[0] for f in os.listdir(image_dir) if f.endswith('.mha')]
print(f"\nTotal unique cases (MHA files): {len(all_case_ids)}")
