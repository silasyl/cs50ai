# py-traffic
An AI to identify which traffic sign appears in a photograph.

This app was implemented with neural network, through use of TensorFlow and OpenCV-Python modules to analyse the German Traffic Sign Recognition Benchmark (GTSRB) dataset and identify a sign between 43 different kind of road signs in a photograph.

The traffic.py accepts a model name as input, so the trained model can be saved to disk<br>
Since the data used to train the model is too big, the user must download it through this url: https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip <br>
Run: python traffic.py folder<br>
Or: python traffic.py folder [model.h5]<br>
<br>
<br>
Log of neural network tests:<br>
# Initial test
- Convolutional layer: 43 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 43 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 4s - loss: 0.1177 - accuracy: 0.0572
  
# More hidden layer
- Convolutional layer: 43 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 4s - loss: 0.1174 - accuracy: 0.0547

# Increased convolutional filters
- Convolutional layer: 80 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 6s - loss: 0.0735 - accuracy: 0.4103
  
# Increased convolutional filters
- Convolutional layer: 160 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 14s - loss: 0.0591 - accuracy: 0.5949
  
# Increased convolutional kernel size
- Convolutional layer: 100 filter, 5x5 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 11s - loss: 0.0222 - accuracy: 0.8956
  
# Increased convolutional kernel size
- Convolutional layer: 100 filter, 7x7 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 10s - loss: 0.0223 - accuracy: 0.9049
  
# Two layers of convolutional and pooling
- Convolutional layer: 100 filter, 5x5 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 100 filter, 5x5 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  Output: 333/333 - 24s - loss: 0.0075 - accuracy: 0.9752
  
# Two layers of convolutional and pooling, reduced filter, kernel
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 64 units, ReLu activation
  Dropout: 0.5
  333/333 - 4s - loss: 0.1176 - accuracy: 0.0547

# Two layers of convolutional and pooling, increased hidden layer
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  333/333 - 4s - loss: 0.0045 - accuracy: 0.9862

# Three layers of convolutional and pooling
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 128 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  333/333 - 5s - loss: 0.0029 - accuracy: 0.9886

# Two layers of convolutional and pooling, increased convolutional filters
- Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 128 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.5
  333/333 - 12s - loss: 0.0062 - accuracy: 0.9756

# Two layers of convolutional and pooling, reduced dropout
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.3
  333/333 - 6s - loss: 0.0049 - accuracy: 0.9830

# Two layers of convolutional and pooling, LeakyRelu activation filter
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, LeakyReLu activation
  Dropout: 0.3
  333/333 - 7s - loss: 0.0053 - accuracy: 0.9827

# Two layers of convolutional and pooling, two hidden layers
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Hidden layer: 128 units, ReLu activation
  Hidden layer: 64 units, ReLu activation
  Dropout: 0.5
  333/333 - 5s - loss: 0.0076 - accuracy: 0.9672

# Two layers of convolutional and pooling, dropout after each pooling and hidden layer
- Convolutional layer: 32 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Dropout: 0.25
  Convolutional layer: 64 filter, 3x3 kernel
  Max-pooling layer: 2x2
  Dropout: 0.25
  Hidden layer: 128 units, ReLu activation
  Dropout: 0.3
  333/333 - 4s - loss: 0.0059 - accuracy: 0.9758

