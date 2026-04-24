import cv2
from hand_tracker import HandTracker
from shape_detector import ShapeDetector
from utils import draw_points, show_text
# hand gesture 

tracker = HandTracker()
detector = ShapeDetector()

cap = cv2.VideoCapture(0)

points = []
detected_shape = ""

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    finger = tracker.get_finger_position(frame)

    if finger:
        points.append(finger)

    draw_points(frame, points)

    if len(points) > 50:

        detected_shape = detector.detect_shape(points)

    if detected_shape:
        show_text(frame, detected_shape)

    cv2.imshow("Gesture Shape AI", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        points = []
        detected_shape = ""

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
