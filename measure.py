from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate(y_true,y_pred):
    print("Accuracy: ",accuracy_score(y_true,y_pred))
    print("Confusion Matrix: \n",confusion_matrix(y_true,y_pred))
    print("Classification Report:\n ",classification_report(y_true,y_pred))
