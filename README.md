# MLOPs
 image_classification
## bird-species-classification
**MLOps end-to-end demo on GCP.**<br />
<br />
Introduction : It's a short presentation on the data apps using bird species classification to easily identify the photo urls you take. <br />
The image dataset is from https://www.kaggle.com/datasets/gpiosenka/100-bird-species which consists of 475 classes, so you can try many types of bird species to see how it perform.<br />
<br />
The work directory in this repositary :<br />
**Cloud Build :** The GCP service execute the git builds connected to the repositary. It uses build trigger to enable CI/CD automation and automatically execute builds on repositary. In this scenario, we commit the newest version of data apps as local change to a repositary. Then, deploy the container image build on GKE.<br />
**Docker :** Docker packages the application into container enable users to easily deploy the application.<br />
**GKE :** Management orchestration for docker containers on GCP. We use it to manage, deploy and scale containerized applications.<br />
**models :** tensorflow-based trained model. It's built of transfer-learning with MobileNetV2 connected with one GlobalAveragePooling2D layer, dropout layer and output layer.<br />
**app.py :** Python script of data apps which loads the model and runs prediction using streamlit to display the result.
