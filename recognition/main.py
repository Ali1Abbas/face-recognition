import cv2
import face_recognition

# def zero():
#     return 0
def find_face_encodings(image_path):
    # reading image
    image = cv2.imread(image_path)
    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)
    # return face encodings
    return face_enc[0]
#
# # getting face encodings for first image
# image_1 = find_face_encodings("../images/WhatsApp Image 2024-01-23 at 16.30.17 (1).jpeg")
# # getting face encodings for second image
# image_2  = find_face_encodings("../images/WhatsApp Image 2024-01-23 at 16.30.17.jpeg")
# # print(image_1,image_2)
# # checking both images are same
# is_same = face_recognition.compare_faces([image_1], image_2)[0]
# print(f"Is Same: {is_same}")
#
#
# if is_same:
#     # finding the distance level between images
#     distance = face_recognition.face_distance([image_1], image_2)
#     distance = round(distance[0] * 100)
#     print(distance)
#
# else:
#  print("The images are not same")
#
#  exit()
#
# if(distance<50):
#     # calcuating accuracy level between images
#     accuracy = 100 - round(distance)
#     print("The images are same")
#     print(f"Accuracy Level: {accuracy}%")
# else:
#     print("The images are not same")