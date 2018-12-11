import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('./out/video.avi', fourcc, 20.0, (640, 480))

while(True):
    _, frame = cap.read()
    out.write(frame)
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) != -1:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
