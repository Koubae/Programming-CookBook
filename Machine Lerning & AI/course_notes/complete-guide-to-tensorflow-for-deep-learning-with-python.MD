Complete Guide to TensorFlow for Deep Learning with PythonComplete
==================================================================


* Course: [Complete Guide to TensorFlow for Deep Learning with Python](https://www.udemy.com/course/complete-guide-to-tensorflow-for-deep-learning-with-python)
* [playground.tensorflow.org](https://playground.tensorflow.org/)


### Components

* numpy
* panda
* tensorflow


---



* Supervised (classification)
    * features: Height and Weights
    * Labeled data: Gender
    * Task: Given a person heigh and weight, predict gender

* Supervised (regression)
    * features: Square Footage, Rooms
    * Labeled data: Hourse Prioce
    * Task: Given a house's size and nunmber of rooms, predict the selling price

* Unsupervised (Clustering)
    * features: heights and weights of dog breeds
    * Unlabelled data
    * Task: CLuster together the data into similar groups. It is then up to the data scientist to interpret the clusters

* Reinforcement learning
    * Agent-Learning/Decision maker
    * Environment - What agent interacts with
    * Actions -- What the agent can do

### Evaluation

* supervised learning -- clasification eval
    * Accuracy | Recall | Precision
    * Accuracy | Correctly classified divided by total samples

* supervised learning -- regression eval
    * MAE | MSE | RMSE
    * all measurements of: on average how far off are you from the correct continous value

* unsupervised learning -- Evaluation
    * harder on 
    * cluster homogeneity, Rand index

### Deploy Model on New Incoming Data


```mermaid
    flowchart TD
        A(Data Acquisition) 
        B(Data Cleaning)

        A --> B
        B --> C(Test)
        B --> D(Train)
        D --> E(Train Model)
        E --> F(Evaluate Model)
        F --> E
        F --> G(Deploy Model)
        C --> F
    
```
![Deploy Model on New Incoming Data](image.png)

### Unsupervised Learning

![Unsupervised Learning](image-1.png)

### hold out sets

![hold out sets](image-2.png)


---


Introduction to Neural Networks
-------------------------------

* Artificial Neural Networks (ANN)
* Activation Function
* Cost functions

* Biological Neuron
* Perceptron Model
* Mathematical Representation



**perceptron**

![perceptron](image-3.png)


* Input layer 
* Hidden layers
* output layer

```bash
z = wx + b
```

#### Activation functions

* sigmoid function tanh(z)
* hyperbolic tangent
* Rectified linear Unit (ReLU)

**sigmoid function**

#### Cost functions

* y: represents true value
* a: represents neuron's prediction

* `w * x + b = z`
* Pass `z` into activation function `function o(z) = a`

* Quadratic cost | `C = E(y-a)2`
* Cross Entropy
* Gradient Descent
* Gradient Descent -- Backpropagation

* chain rule

* PostOrder Tree Traversal
