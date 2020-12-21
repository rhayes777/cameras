if __name__ == "__main__":
    import cv2

    cap = cv2.VideoCapture(1)

    # Get the width and height of frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))

    while True:
        ret, img = cap.read()
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # write the flipped frame
        out.write(img)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
