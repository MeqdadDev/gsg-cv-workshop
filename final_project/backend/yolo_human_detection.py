from ultralytics import YOLO

class HumanDetection:
    """
    Initializes the HumanDetection class.

    """
    def __init__(self) -> None:
        """
        Initializes the YOLOv8 model for human detection.

        Attributes:
            model: The pre-trained YOLOv8 model.
            result: The detection result.
            has_person: A boolean indicating if a person is present in the detection result.

        """
        # Load the pre-trained YOLOv8 model
        self.model = YOLO("yolov8n.pt")

        # Set the model to detect only the 'person' class
        self.model.model.names = ['person']
        self.result = None
        self.has_person = False

    def detect(self, image_path, conf_threshold=0.5):
        """
        Detects humans in an image using the YOLOv8 model.

        Args:
            image_path: The path to the image file.
            conf_threshold: The confidence threshold for detection (default: 0.5).

        Returns:
            Tuple: A tuple containing the detection result and a boolean indicating if a person is present.

        Raises:
            RuntimeWarning: If no detection result is available.

        """
        self.result = self.model(image_path, save=True, conf=conf_threshold, save_crop=True)
        self.has_person = self._is_person_present()
        return self.result, self.has_person


    # Check if any 'person' objects were detected
    def _is_person_present(self):
        """
        Checks if the detection result contains a person.

        Returns:
            bool: True if a person is present in the detection result, False otherwise.
        """
        if self.result is not None:
            for detection in self.result:
                for box in detection.boxes.data:
                    cls_ = int(box[-1])
                    if self.model.model.names[cls_] == 'person':
                        self.has_person = True
                        break
        else:
            self.has_person = False
            raise RuntimeWarning("NO DETECTION!!!, try to run the detection process before checking \
                                if a person is present in the detection result or not.")
        return self.has_person
