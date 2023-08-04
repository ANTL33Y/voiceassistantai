import cv2

# Load the pre-trained model for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained model for facial recognition
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_model.xml')

# Function to recognize faces

def recognize_faces(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Crop the face region from the image
        face = gray[y:y+h, x:x+w]

        # Recognize the face
        label, confidence = recognizer.predict(face)

        # Draw a rectangle around the face
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the label and confidence
        text = f'Label: {label}, Confidence: {confidence}'
        cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Return the image with the recognized faces
    return image