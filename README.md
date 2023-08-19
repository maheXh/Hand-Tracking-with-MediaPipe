# Hand Tracking using MediaPipe and OpenCV

This GitHub repository contains a Python script for real-time hand tracking using the MediaPipe library and OpenCV. The script captures video from the webcam and uses the MediaPipe Hand module to detect and track hands' landmarks in the video frames.

## Prerequisites

Make sure you have the following libraries installed in your Python environment:

- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

You can install them using the following command:

```
pip install opencv-python mediapipe numpy
```

4. The script will open two windows: one for the hand tracking visualization and another for the original webcam feed with added annotations.

## Features

- Real-time hand tracking: The script utilizes the MediaPipe Hand module to detect and track hand landmarks.
- Hand handedness detection: It identifies whether the detected hand is left or right and displays this information on the video frames.
- Frames per second (FPS) calculation: The script calculates and displays the FPS rate on the video frames.

## Upcoming Features

- **Pose Estimation:** We are working on integrating other modules from the MediaPipe library to provide pose estimation capabilities, allowing you to track the human body's posture and movement.
- **Face Mesh Tracking:** Our upcoming updates will also include the integration of the MediaPipe Face Mesh module, enabling real-time tracking of facial landmarks.

Stay tuned for these exciting updates!

## Controls

- Press 'q' to exit the application.

## Credits

- This project utilizes the [MediaPipe library](https://mediapipe.dev/), developed by Google.
- The code for hand tracking and visualization is based on the provided code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute, modify, and use this code as needed. If you encounter any issues or have suggestions for improvement, please open an issue in the GitHub repository.
