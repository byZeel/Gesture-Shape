import cv2
import numpy as np

class ShapeDetector:

    def detect_shape(self, points):

        if len(points) < 20:
            return None

        contour = np.array(points)

        perimeter = cv2.arcLength(contour, False)

        approx = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            False
        )

        corners = len(approx)

        if corners == 3:
            return "Triangle"

        elif corners == 4:
            return "Square/Rectangle"

        elif corners > 8:
            return "Circle"

        return "Unknown"