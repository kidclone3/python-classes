import cv2
import numpy as np

class Square:
    def __init__(self, size, x, y, velocity=10):
        self.size = size
        self.old_x = x
        self.x = x
        self.old_y = y
        self.y = y
        self.velocity = velocity
    def move(self):
        self.y += self.velocity
        self.x += self.velocity
    def reset(self):
        self.x = self.old_x
        self.y = self.old_y

    def check_edge(self, rows, cols):
        if self.x + self.size >= cols or self.x <= 0 or self.y + self.size >= rows or self.y <= 0:
            self.velocity = -self.velocity

if __name__ == "__main__":
    cap = cv2.VideoCapture() # Create a VideoCapture object
    cap.open(0) # read from the first camera
    # cap.open("https://129.226.145.57:7548/")
    # create 3 squares
    delta = 50
    ret, frame = cap.read()
    print(f"{ret=}, {frame.shape=}")

    square1 = Square(100, 50, 50, 10)
    square2 = Square(50, 100, 100, 20)
    while True:
        if cv2.waitKey(1) == ord('q'):
            break
        ret, frame = cap.read()

        if not ret:
            break
        cv2.rectangle(frame, (square1.x, square1.y), (square1.x + square1.size, square1.y + square1.size), (0, 255, 0), 3)
        cv2.rectangle(frame, (square2.x, square2.y), (square2.x + square2.size, square2.y + square2.size), (0, 255, 0),
                      3)
        square1.check_edge(frame.shape[0], frame.shape[1])
        square1.move()
        square2.check_edge(frame.shape[0], frame.shape[1])
        square2.move()
        cv2.imshow("video", frame)
        cv2.waitKey(20)
