class ShapeDetector:
    def __init__(self):
        pass

    def detect (self, c):
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 4:
            shape = "square"
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

        else:
            shape = "unidentified"

        return shape