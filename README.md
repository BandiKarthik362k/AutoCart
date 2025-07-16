# AutoCart

Real-time object recognition system designed for checkout-free retail experiences—similar to Amazon Go. It uses computer vision and deep learning to automatically detect and track items picked from or placed into a shopping cart or shelf, eliminating the need for manual scanning or checkout lines.

# Requirements
  - ultralytics
  - OpenCV-python
  - ultralytics
  - torchvision, torch
  - optuna

# Implementation details 
- Collected sample images of different types of products, products inside a shelf, in different angles. (images removed from data section for privacy)
- scrapped images on multiple time frame intervals from a video using open CV on different frame levels.
- I have augmented the collected samples using torchvision , so that the model will learn enough edges and corners in detecting the objects.
- Did hyperparamter tuning using Optuna in fining the the best Learning rates, Mosaic, and mixups and warmups for the schedule leraning rates.
- Did transfer learning by fine tuning the Yolo11 medium model, and used mixup and mosaic as a 2nd level of data augmnetation/ image augmentation.
- Made sure that the model is not memorizing, used completely different held out sets.
- The best model from data augmentation has again be tuned to find the best parameters now without using the augmentation.
- This model could achive a F1 score of 91 percent, which pretymuch shos that there is no class imbalance.

# Stages of training
- Augmented Training : Model\Initital_Build
- Fine tuning the best model with optuna's best hyperparameters : Model\FineTune

# Inference stage  
Model\AutoCart.ipynb

- For what ever the objjects present, identify the box sizes both min and max dimentions.
- taking the center of the boxes to see if it is inside the dimensions of the shelf.
- until unless there is a contact with the object with hand for a intersection of given ratio, and for n seconds the object is not considered as picked.
- when the object is picked the code checks if it is moved out of the dimentions of the shelf, that is the object is not present inside the shelf anymore, then it is considered as final pick.
- if at all the object is retruned to the shelf again, the pending cart value will be 0, so that even on returns, the model actualy take cares of it.

