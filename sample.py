import cv2
from roboflow import Roboflow


rf = Roboflow(api_key="YOUR API KEY")
project = rf.workspace("hand-wave-detection").project("hand_wave_detection")
model = project.version(3).model


input_video_path = "/home/fiftyfive/Downloads/Studio_Project_V4.mp4"
output_video_path = "/home/fiftyfive/Downloads/Hand Detection yolo/yolov5/detected_video/Studio_Project_V4.mp4"


cap = cv2.VideoCapture(input_video_path)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break


    temp_frame_path = "/home/fiftyfive/Downloads/Hand Detection yolo/yolov5/detected_videos/temp_frame.jpg"
    cv2.imwrite(temp_frame_path, frame)


    predictions = model.predict(temp_frame_path, confidence=90, overlap=0).json()


    for prediction in predictions['predictions']:
        x, y, width, height = prediction['x'], prediction['y'], prediction['width'], prediction['height']
        label = prediction['class']
        confidence = prediction['confidence']
        

        x1, y1 = int(x - width / 2), int(y - height / 2)
        x2, y2 = int(x + width / 2), int(y + height / 2)


        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    out.write(frame)


cap.release()
out.release()
# cv2.destroyAllWindows()
