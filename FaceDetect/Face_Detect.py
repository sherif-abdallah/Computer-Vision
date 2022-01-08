import cv2

# Load some pre trained data
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
upperbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

# Choose a image to detecte the face in
webcam = cv2.VideoCapture(0)


while True:

    # Read The Current Frame
    sucsesful_frame_read, frame = webcam.read()

    # Convert to Grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detect Faces
    face_coordinates = face_cascade.detectMultiScale(grayscale_img)
    # Detect Faces
    upperbody_coordinates = upperbody_cascade.detectMultiScale(grayscale_img)



    # Draw Rectangle around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y) , (x + w, y + h), (0, 0, 255) , 2)



    # Draw Rectangle around the upper body
    for (a, b, c, d) in upperbody_coordinates:
        cv2.rectangle(frame, (a, b) , (a + c, b + d), (255, 0, 0) , 2)



    print(face_coordinates)

    cv2.imshow('Face Detection', frame)
    key = cv2.waitKey(1)

    #  Stop if Key Q key is pressed
    if key==81 or key==113:
        break 
 