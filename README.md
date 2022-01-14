# Object Detector Tensorflow

ROS2 Nodes for TensorFlow Object Detection Inference

## Interface:

### Continuous detection node

- `continuous_detection_node` (ROS2 Dashing python)

    Node used for continuous stream of image data

![continuous_detection_node](docs/continuous_detection_node.svg)

#### Topics

- subscribe `image` (sensor_msgs/Image)
- publish `continuous_detection_node/result_image` (sensor_msgs/Image)
- publish `continuous_detection_node/detections` (custom type)

    ```bash
    # Detections.msg
    std_msgs/Header header
    std_msgs/Header image_header
    Detection[] detections
    ```
    
    ```bash
    # Detection.msg
    uint32 class_id
    string class_name
    float32 probability
    sensor_msgs/RegionOfInterest bounding_box
    ```

#### Parameters

Change in `ros/config/params.yaml`

```bash
saved_model_path: "data/saved_model"  # Path to TensorFlow saved model folder
label_map_path: "data/label_map.txt"  # Text file with class names (one label per line)
image_topic: "/image"  # ROS topic to listen for images
min_probability: 0.5            # Minimum probability for detections to be reported
max_gpu_memory_fraction: 1.0    # Limits the GPU memory usage of the TensorFlow model to only a fraction (between 0 and 1)
result_image_size: [640,480]    # Dimensions of the result image [x,y]
```

---

### Detection Node

- `detection_node` (ROS2 Dashing python)

    Node used for requests of object detection on single images

![detection_node](docs/detection_node.svg)

#### Topics

- publish `continuous_detection_node/result_image` (sensor_msgs/Image)
- publish `continuous_detection_node/detections` (custom type)

#### Services

- server `continuous_detection_node/detect_objects` (custom type)

    ```bash
    # DetectObjects.srv
    sensor_msgs/Image image
    sensor_msgs/RegionOfInterest roi
    ---
    Detections detections
    sensor_msgs/Image result_image
    ```

#### Parameters

Change in `ros/config/params.yaml`

```bash
saved_model_path: "data/saved_model"  # Path to TensorFlow saved model folder
label_map_path: "data/label_map.txt"  # Text file with class names (one label per line)
min_probability: 0.5            # Minimum probability for detections to be reported
max_gpu_memory_fraction: 1.0    # Limits the GPU memory usage of the TensorFlow model to only a fraction (between 0 and 1)
result_image_size: [640,480]    # Dimensions of the result image [x,y]
```

## Dependencies

- tensorflow
- opencv

## How to install

    pip3 install tensorflow
    sudo apt install opencv
    pip3 install numpy
    sudo apt install ros-dashing-diagnostic-updater
    sudo apt install ros-dashing-ros1-bridge


## How to run:

    ros2 launch object_detector_tensorflow detection.launch.py
    ros2 launch object_detector_tensorflow continuous_detection.launch.py

## Testing

### generate a test image

    from cv_bridge import CvBridge, CvBridgeError
        import numpy as np
        bridge = CvBridge()
        np.zeros([960, 1280, 3], dtype=np.uint8)
        image = bridge.cv2_to_imgmsg(
            np.zeros([960, 1280, 3], dtype=np.uint8), encoding="bgr8")

### display test image from ROS-msgs

    image = self.bridge.imgmsg_to_cv2(image)
    cv2.imshow()
    cv2.waitKey(0)

export PYTHONPATH=$PYTHONPATH:~/Code/iris_ws/src/object_detector_tensorflow

## Todo:

- [ ] finish Dockerfile
