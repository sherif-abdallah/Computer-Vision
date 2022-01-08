import cv2
import numpy as np
import face_recognition


img_elon = face_recognition.load_image_file('images/elon_musk.jpg')
img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)


img_test = face_recognition.load_image_file('images/elon_musk_2.jpg')
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(img_elon)[0]
encodeELon = face_recognition.face_encodings(img_elon)[0]
cv2.rectangle(img_elon, (faceLoc[3], faceLoc[0]),
              (faceLoc[1], faceLoc[2]), (0, 255, 0), 2)


faceLocTest = face_recognition.face_locations(img_test)[0]
encodeTest = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_test, (faceLocTest[3], faceLocTest[0]),
              (faceLocTest[1], faceLocTest[2]), (0, 255, 0), 2)


results = face_recognition.compare_faces([encodeELon], encodeTest)
face_distance = face_recognition.face_distance([encodeELon], encodeTest)
results, face_distance
cv2.putText(img_test, f'{results} {round(face_distance[0], 2)}', (
    50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


cv2.imwrite('output/output1.png', img_elon)
cv2.imwrite('output/output2.png', img_test)
