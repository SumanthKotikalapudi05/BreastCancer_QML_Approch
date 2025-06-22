# BreastCancer_QML_Approch
Objective

To develop a hybrid **classical-quantum model** that classifies tumors in the **Wisconsin Breast Cancer Dataset** by leveraging Qiskit's `EstimatorQNN` and PyTorch integration via `TorchConnector`.

---

## ⚙️ Technologies Used

- **Qiskit** – Quantum simulation and circuit construction
- **Qiskit Machine Learning** – Quantum Neural Network integration
- **PyTorch** – Classical model training and loss optimization
- **Scikit-learn** – Data preprocessing and evaluation

---

## 🧪 Current Status

> 🧱 **Work in Progress**  

- ✔️ Data pipeline and PyTorch loaders implemented  
- ✔️ Quantum encoding via `ZZFeatureMap`  
- ✔️ Variational circuit using `TwoLocal` ansatz  
- ✔️ Training integrated via `TorchConnector`  
- ❌ Accuracy is currently **~60%**
  
We are actively improving:
- Feature dimensionality reduction (PCA)
- Circuit expressivity vs simulation overhead
- Optimizer tuning

Evaluation Metrics

- Accuracy
- Confusion Matrix
- Precision, Recall, F1-Score

---

## 📈 To Do

- [ ] Integrate PCA for dimensionality reduction
- [ ] Tune optimizer (`COBYLA`, `SPSA`) with more iterations
- [ ] Try alternative ansatz circuits (e.g., `RealAmplitudes`)
- [ ] Compare with classical baselines (Logistic Regression, SVM)

---

## 🎯 Target
Theoretical models and previous literature show **QML accuracy can exceed 85–90%** on small medical datasets.  
> **We expect to achieve at least ~85% accuracy** after optimizing the number of qubits, encoding strategy, and variational circuit design.


---
## 🚧 Disclaimer
This is an experimental research project using quantum simulators and may not scale or generalize well to production systems without further benchmarking and hardware testing.
---
## 🧠 Author
- **Sumanth Kotikalapudi**  
