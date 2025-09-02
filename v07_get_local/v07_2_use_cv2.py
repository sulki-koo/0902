import cv2
import os
from datetime import datetime

# 함수화
def capture_image(save_dir):
    os.makedirs(save_dir, exist_ok=True)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise RuntimeError("카메라 연결 안됨")

    print("카메라 연결됨")
    success, frame = cap.read()
    if success:
        print("OPEN")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_dir, f"result_{timestamp}.jpg")

        cv2.imwrite(file_path, frame)
        print(f"사진이 저장 되었습니다. {file_path}")
    else:
        print("프레임 읽기 실패")
        
    cap.release()
    cv2.destroyAllWindows()

# 함수 호출
capture_image("./capture_images")