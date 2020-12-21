if __name__ == "__main__":
    import cv2

    cap = cv2.VideoCapture(1)
    while True:
        ret, img = cap.read()
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    exit(0)
