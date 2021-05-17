import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shopping.py data k-neighbors")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    k_neighbors = sys.argv[2]
    model = train_model(X_train, y_train, k_neighbors)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        evidence = []
        label = []
        for row in reader:

            if row[10] == 'Jan':
                row_10 = 0
            elif row[10] == 'Feb':
                row_10 = 1
            elif row[10] == 'Mar':
                row_10 = 2
            elif row[10] == 'Apr':
                row_10 = 3
            elif row[10] == 'May':
                row_10 = 4
            elif row[10] == 'June':
                row_10 = 5
            elif row[10] == 'Jul':
                row_10 = 6
            elif row[10] == 'Aug':
                row_10 = 7
            elif row[10] == 'Sep':
                row_10 = 8
            elif row[10] == 'Oct':
                row_10 = 9
            elif row[10] == 'Nov':
                row_10 = 10
            else:
                row_10 = 11

            evidence.append(
                [int(row[0]),
                 float(row[1]),
                 int(row[2]),
                 float(row[3]),
                 int(row[4]),
                 float(row[5]),
                 float(row[6]),
                 float(row[7]),
                 float(row[8]),
                 float(row[9]),
                 row_10,
                 int(row[11]),
                 int(row[12]),
                 int(row[13]),
                 int(row[14]),
                 1 if row[15] == 'Returning_Visitor' else 0,
                 1 if row[16] == 'TRUE' else 0
                 ]
            )
            label.append(1 if row[17] == 'TRUE' else 0)

    data = (evidence, label)
    return data


def train_model(evidence, labels, k_neighbors):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=int(k_neighbors))
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensitivity_identified = 0
    sensitivity_total = 0
    specificity_identified = 0
    specificity_total = 0
    for i, y_test in enumerate(labels):
        if y_test == 1:
            if y_test == predictions[i]:
                sensitivity_identified += 1
            sensitivity_total += 1
        else:
            if y_test == predictions[i]:
                specificity_identified += 1
            specificity_total += 1
    sensitivity = sensitivity_identified / sensitivity_total
    specificity = specificity_identified / specificity_total
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
