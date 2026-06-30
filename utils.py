import cv2

def draw_points(frame, points):

    for i in range(1, len(points)):
        cv2.line(
            frame,
            points[i-1],
            points[i],
            (255,0,0),
            3
        )


def show_text(frame, text):

    cv2.putText(
        frame,
        text,
        (30,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )