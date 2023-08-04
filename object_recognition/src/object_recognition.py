import cv2


def recognize_objects(image_path):
    # Load the pre-trained model
    caffe_prototxt = 'path/to/caffe_prototxt'
    caffe_model = 'path/to/caffe_model'
    confidence_threshold = 0.5
    class_names = ['class1', 'class2', 'class3']

    try:
        # Load the pre-trained model
        model = cv2.dnn.readNetFromCaffe(caffe_prototxt, caffe_model)

        # Load the image
        image = cv2.imread(image_path)

        # Preprocess the image
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

        # Pass the blob through the model
        model.setInput(blob)
        detections = model.forward()

        # Process the detections
        objects = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > confidence_threshold:
                class_id = int(detections[0, 0, i, 1])
                class_name = class_names[class_id]
                objects.append(class_name)

        return objects
    except Exception as e:
        print('An error occurred:', str(e))
        return []