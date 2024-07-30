import cv2
from roboflow import Roboflow


rf = Roboflow(api_key="YOUR API KEY")
project = rf.workspace("hand-wave-detection").project("hand_wave_detection")
model = project.version(3).model


input_video_path = "video_path"
output_video_path = "video_output_path"


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


    temp_frame_path = "path/to/temp.jpg"
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
