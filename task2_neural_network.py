import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Build the neural network
model = Sequential([
    Dense(8, activation="relu", input_shape=(4,)),
    Dense(3, activation="softmax")
])

# Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train the model
model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=0
)

# Evaluate the model
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

# Print the results
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)