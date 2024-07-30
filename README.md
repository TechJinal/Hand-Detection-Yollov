# Smart Hand Wave Detection for Vehicle Control

## Project Overview
This project aims to detect hand waves specifically intended to stop vehicles, distinguishing them from other hand wave activities like greetings. The model is trained using YOLOv5 to accurately identify the intended stop signals based on the angle of the hand wave relative to the body.

## Table of Contents
- [Project Overview](#project-overview)
- [Technical Stack](#technical-stack)
- [Technical Learnings](#technical-learnings)
- [Results](#results)
- [Why YOLOv5?](#why-yolov5)
- [Future Work](#future-work)
- [Installation and Usage](#installation-and-usage)

## Technical Stack
- **Data Collection:** Videos recorded with various hand wave activities.
- **Data Processing:** Frames extracted from videos and annotated with hand angles.
- **Model Training:** YOLOv5 model trained on 2002 annotated frames, achieving 98% accuracy.

## Technical Learnings
- **Data Annotation:** Precise annotation is crucial for high model accuracy.
- **Model Selection:** YOLOv5's balance of speed and accuracy is ideal for real-time applications.
- **Training Process:** The model was trained in 2 hours, demonstrating efficient computational requirements.
- **Error Analysis:** Identified common errors and refined the model for better performance.

## Results
- **Accuracy:** Achieved 98% detection accuracy.
- **Training Duration:** 2 hours.
- **Test Scenarios:** Successfully distinguished between stop waves and other hand waves.

## Why YOLOv5?
1. **High Accuracy:** Superior performance in object detection tasks.
2. **Real-time Detection:** Optimized for quick response.
3. **Efficiency:** Balances speed and accuracy effectively.
4. **Community Support:** Strong support and resources available.

## Future Work
- **Enhancing Detection:** Improve performance under various lighting conditions and angles.
- **Additional Applications:** Explore further applications of hand wave detection in different contexts.

## Installation and Usage
### Prerequisites
- Python 3.6 or higher
- PyTorch
- OpenCV
- YOLOv5 repository


### Usage
1. Annotate your video frames and ensure they are properly labeled.
2. Train the YOLOv5 model with your annotated data:
    ```bash
    python train.py --batch 8 --epochs 100 --data {dataset.location}/data.yaml --cfg ./models/custom_yolov5s.yaml --weights '' --name yolov5s_results  --cache
    ```



