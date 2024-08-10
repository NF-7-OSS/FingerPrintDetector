import os
import cv2

sample = cv2.imread("SOCO__FINGERS/Altered_1/Altered-Hard_1/150__M_Right_index_finger_Obl.BMP")

"""
This is only for Testing purpose code 
sample=cv2.resize(sample,None,fx=2.5, fy=2.5)
cv2.imshow("sample",sample)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

best_score = 0
filename = None
image = None
kp1, kp2, mp = None, None, None
counter = 0
for file in [file for file in os.listdir("SOCO_FINGERS/Real")][:1000]:
    if counter % 10 == 0:
        print(file)
    fingerprint_image = cv2.imread("SOCO_FINGERS/Real/" + file)
    sift = cv2.SIFT_create()

    keyPoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keyPoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)

    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10},
                                    {}).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []
    for p, q in matches:

        if p.distance < 0.1*q.distance:

            match_points.append(p)

    keyPoints = 0
    if len(keyPoints_1) < len(keyPoints_2):
        keyPoints = len(keyPoints_1)
    else:
        keyPoints = len(keyPoints_2)

    if len(match_points) / keyPoints * 100 > best_score:
        best_score = len(match_points) / keyPoints * 100
        filename = file
        image = fingerprint_image
        kp1, kp2, mp = keyPoints_1, keyPoints_2, keyPoints

print("BEST MATCH : ", filename)
print("SCORE : ", str(best_score))


if image is not None and kp1 is not None and kp2 is not None and match_points is not None:
    result = cv2.drawMatches(sample, kp1, image, kp2, match_points, None)

    result = cv2.resize(result, None, fx=2, fy=2)

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No match found or an error occurred during processing.")