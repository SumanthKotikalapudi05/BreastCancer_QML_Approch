from qiskit.circuit.library import ZZFeatureMap

def get_fm(num_qubits):
    return ZZFeatureMap(feature_dimension=num_qubits,reps=2,entanglement='linear')