import cv2
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = cv2.imread("v06_data_aug/data_aug.jpg")

# 2. 이미지 조정 (수평 반전)
img_flipped = cv2.flip(img, 1) # 1은 수평, 0은 수직, -1은 둘 다

# 3. 이미지 시각화
fig, ax = plt.subplots(2, 2, figsize=(10, 5))
ax[0,0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0,0].axis('off')
ax[0,0].set_title('Orginal')

ax[0,1].imshow(cv2.cvtColor(img_flipped, cv2.COLOR_BGR2RGB))
ax[0,1].axis('off')
ax[0,1].set_title('Flipped')

# 시각화 (2,2) 이미지 채우고 RGB로 변환
res = cv2.resize(img,None,fx=4, fy=4, interpolation = cv2.INTER_CUBIC)
laplacian = cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),cv2.CV_64F)

ax[1,0].imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
ax[1,0].axis('off')
ax[1,0].set_title('Resize')

ax[1,1].imshow(laplacian, cmap='gray')
ax[1,1].axis('off')
ax[1,1].set_title('Laplacian')

# plt.show()
# 4. 이미지 저장
cv2.imwrite("v06_data_aug/img_flipped.jpg", img_flipped)
print("이미지가 저장 되었습니다.")