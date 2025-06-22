import numpy as np
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import DataLoader, TensorDataset

# Load full dataset from .npy files
x = np.load('X_train.npy')  
x_test_full = np.load('X_test.npy')  
x = np.concatenate([x, x_test_full], axis=0)

y = np.load('y_train.npy')
y_test_full = np.load('y_test.npy')
y = np.concatenate([y, y_test_full], axis=0)

# Convert labels to float32 if needed
y = y.astype(np.float32)

# Stratified train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

print("Train label distribution:", np.unique(y_train, return_counts=True))
print("Test label distribution:", np.unique(y_test, return_counts=True))

# Convert to PyTorch tensors and DataLoader
train_dataset = TensorDataset(torch.tensor(x_train, dtype=torch.float32),
                              torch.tensor(y_train, dtype=torch.float32))
test_dataset = TensorDataset(torch.tensor(x_test, dtype=torch.float32),
                             torch.tensor(y_test, dtype=torch.float32))

train_loader = DataLoader(train_dataset, batch_size=23, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=23)

# Expose variables to other files
__all__ = ['x_train', 'x_test', 'y_train', 'y_test', 'train_loader', 'test_loader']
