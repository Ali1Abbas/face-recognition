import json

import face_recognition

from recognition.main import find_face_encodings
def verify(
    img1_path, img2_path
):
    try:
        # obj =find_face_encodings(img1_path)
        image_1 = find_face_encodings(img1_path)
        # getting face encodings for second image
        image_2 = find_face_encodings(img2_path)
        # print(image_1,image_2)
        # checking both images are same
        is_same = face_recognition.compare_faces([image_1], image_2)[0]
        print(f"Is Same: {is_same}")

        if is_same:
            # finding the distance level between images
            distance = face_recognition.face_distance([image_1], image_2)
            distance = round(distance[0] * 100)
            print(distance)

        else:
            print("The images are not same")

            exit()

        if (distance < 50):
            # calcuating accuracy level between images
            accuracy = 100 - round(distance)
            print("The images are same")
            print(f"Accuracy Level: {accuracy}%")
        else:
            print("The images are not same")

        res = {"Accurrncy": accuracy, "Distance": distance,
               "is_same": "Yes" if is_same else "No"}
        return json.dumps(res)
    except Exception as err:
        return {"error": f"Exception while verifying: {str(err)}"}, 400

