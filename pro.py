import cv2
labels_path =input("")
video_path = input("")
output_video_path =  input("")
labels_path.replace("\\","\\\\")
video_path.replace("\\","\\\\")
output_video_path.replace("\\","\\\\")
with open(labels_path, 'r') as file:
    lines = file.readlines()
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
width = 852
height = 480
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
frame_index = 0
while cap.isOpened():
    for line in lines:
        ret, frame = cap.read()
        if not ret:
            cap.release()
            break
        frame = cv2.resize(frame, (width, height))
        frame = frame.copy()
        x, y, w, h = map(int, line.strip().split('\t'))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        out.write(frame)
        # if frame_index>150:
        #     break
        frame_index += 1
        print(f'Processed frame {frame_index}')
cap.release()
out.release()
cv2.destroyAllWindows()
print('Video with boxes saved successfully!')


