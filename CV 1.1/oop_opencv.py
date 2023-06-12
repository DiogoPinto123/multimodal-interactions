import cv2 as cv

class App:
    def __init__(self):
        img = cv.imread('messi.jpg')
        Window('image', img)

    def run(self):
        k=0
        while k != ord('q'):
            k = cv.waitKey(0)
            print(k, chr(k))

        cv.destroyAllWindows()


class Window:
    def __init__(self, win, img):
        self.win = win
        self.img = img
        cv.imshow(win, img)

if __name__ == '__main__':
    App().run()