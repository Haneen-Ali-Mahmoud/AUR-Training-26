import cv2 as cv
import numpy as np


class ShapeDetector:
    def __init__(self, video_path):
        self.cap = cv.VideoCapture(video_path)

        if not self.cap.isOpened():
            print("Cannot open video")
            exit()

    def run(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Can't receive frame. Exiting...")
                break

            hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

            lower_red1 = np.array([0, 100, 100])
            upper_red1 = np.array([10, 255, 255])

            lower_red2 = np.array([170, 100, 100])
            upper_red2 = np.array([180, 255, 255])

            red_mask1 = cv.inRange(hsv, lower_red1, upper_red1)
            red_mask2 = cv.inRange(hsv, lower_red2, upper_red2)
            red_mask = cv.bitwise_or(red_mask1,red_mask2)

            lower_blue = np.array([90, 100, 100])
            upper_blue = np.array([130, 255, 255])

            blue_mask = cv.inRange(hsv, lower_blue, upper_blue)

            kernel = np.ones((5, 5),np.uint8)
            red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, kernel)
            blue_mask = cv.morphologyEx(blue_mask, cv.MORPH_OPEN, kernel)
            red_contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            for c in red_contours:
                if cv.contourArea(c) < 300:
                    continue

                peri = cv.arcLength(c, True)
                approx = cv.approxPolyDP(c, 0.02 * peri, True)
                area = cv.contourArea(c)

                if peri != 0:
                    circularity = (4 * np.pi * area) / (peri * peri)
                else:
                    circularity = 0


                if circularity > 0.7:
                    cv.drawContours(frame, [c], -1, (0, 0, 255), 3)

                    M = cv.moments(c)
                    if M["m00"] != 0:
                        cx = int(
                            M["m10"] / M["m00"]
                        )

                        cy = int(
                            M["m01"] / M["m00"]
                        )


                        cv.putText(frame, "Red Circle", (cx - 50, cy), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),2)

            blue_contours, _ = cv.findContours(blue_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


            for c in blue_contours:
                if cv.contourArea(c) < 300:
                    continue

                peri = cv.arcLength(c, True)
                approx = cv.approxPolyDP(c, 0.02 * peri,True)

                vertices = len(approx)

                if vertices == 4:
                    x, y, w, h = cv.boundingRect(c)
                    ratio = w / float(h)

                    if 0.8 <= ratio <= 1.2:
                        cv.drawContours(frame, [c], -1, (255, 0, 0),3)
                        cv.putText(frame, "Blue Square", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0),2)


            cv.imshow("Shape Detection",frame)

            if cv.waitKey(1) == ord("q"):
                break

        self.cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    detector = ShapeDetector("thrown_shapes_noisy_30s.mp4")
    detector.run()