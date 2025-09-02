from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("v06_data_aug/data_aug.jpg")

# 2. 이미지 조정 (회전)
img_rotated = img.rotate(90)

# 3가지 데이터 증강 진행해서 이미지 시각화 하기!
img_filter_contour = img.filter(ImageFilter.CONTOUR)
img_filter_emboss = img.filter(ImageFilter.EMBOSS)
img_convert = img.convert("HSV").convert("RGB")

# 3. 결과 시각화
fig, ax = plt.subplots(2, 3, figsize=(15, 10))

# 3-1. 원본 이미지 시각화
# ax[0].imshow(img)
# ax[0].axis('off')
# ax[0].set_title('Original')
    
# 3-2. 회전 이미지 시각화
# ax[1].imshow(img_rotated)
# ax[1].axis('off')
# ax[1].set_title('Rotated')

images = [img, img_rotated, img_filter_contour, img_filter_emboss, img_convert]
titles = ['Original', 'Rotated', 'Contour', 'Emboss', 'Convert']

for ax_i, image, title in zip(ax.flat, images, titles):
    ax_i.imshow(image)
    ax_i.axis('off')
    ax_i.set_title(title)

for extra_ax in ax.flat[len(images):]:
    extra_ax.axis('off')
    
plt.tight_layout()
plt.show()

# 4. 결과 이미지 저장
img_rotated.save("v06_data_aug/data_aug_rotate.jpg")