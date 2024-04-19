import cv2

# Get user supplied values
imagePath = "C:\\Python27\\Sidkush_Code_Deploy\\CODE\\Scripts\\test.jpg"
cascPath = "C:\\Python27\\Sidkush_Code_Deploy\\CODE\\Resources\\Cascades\\haarcascade_frontalface.xml"

# Create the haar cascade
objCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
objects = objCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} objects!".format(len(objects))

# Draw a rectangle around the faces
for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Objects found", image)
cv2.waitKey(0)
