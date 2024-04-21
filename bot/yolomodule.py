import cv2
from ultralytics import YOLO
import config as cfg


APPROVAL_PERCENT = 0.3

model = YOLO(cfg.path_to_model)


def someone_smoking(img):
    image = cv2.imread(img)
    result = model.predict(source=image, conf=0.21,
                           save=True, classes=[2, 3])[0]

    confidence = []
    for val in result:
        for f in val.boxes.conf.tolist():
            confidence.append(f)

    if len(confidence) != 0:
        sr_ar = sum(confidence) / len(confidence)
    else:
        sr_ar = 0

    if sr_ar < APPROVAL_PERCENT:
        return (False, 0)
    else:
        return (True, int(sr_ar * 100))
