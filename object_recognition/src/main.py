from object_recognition import recognize_objects


def main():
    image_path = 'path/to/image.jpg'
    objects = recognize_objects(image_path)
    
    print('Detected objects:')
    for obj in objects:
        print(obj)


if __name__ == '__main__':
    main()