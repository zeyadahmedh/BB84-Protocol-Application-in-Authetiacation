import cirq
from BB84UI import *
from RequiredForBB84 import *
my_protocol=BB84(eve_intercept='yes')
my_protocol.qubit= cirq.NamedQubit('q0')
my_protocol.simulator=cirq.Simulator()

def protocolImplementation(alice_qubit, alice_hadamard, bob_hadamard):
    alice_circuit = cirq.Circuit()
    bob_circuit = cirq.Circuit()
    eve_circuit = cirq.Circuit()

    my_protocol.qubit = cirq.NamedQubit('q0')
    my_protocol.simulator = cirq.Simulator()
    eve_circuit.append(cirq.M(my_protocol.qubit, key='eve'))
    my_protocol.eve_intercept_circuit = eve_circuit
    alice_circuit.append(cirq.I(my_protocol.qubit))

    if alice_qubit == 0 and not alice_hadamard:
        if not bob_hadamard:
            bob_circuit.append(cirq.I(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_no_H_circuit = bob_circuit
        else:
            bob_circuit.append(cirq.H(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_H_circuit = bob_circuit
        my_protocol.alice_send_0_no_H_circuit = alice_circuit

    elif alice_qubit == 1 and not alice_hadamard:
        alice_circuit.append(cirq.X(my_protocol.qubit))
        if not bob_hadamard:
            bob_circuit.append(cirq.I(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_no_H_circuit = bob_circuit
        else:
            bob_circuit.append(cirq.H(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_H_circuit = bob_circuit
        my_protocol.alice_send_1_no_H_circuit = alice_circuit
    elif alice_qubit == 0 and  alice_hadamard:
        alice_circuit.append(cirq.H(my_protocol.qubit))
        if not bob_hadamard:
            bob_circuit.append(cirq.I(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_no_H_circuit = bob_circuit
        else:
            bob_circuit.append(cirq.H(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_H_circuit = bob_circuit
        my_protocol.alice_send_0_H_circuit = alice_circuit
    elif alice_qubit == 1 and alice_hadamard:
        alice_circuit.append(cirq.X(my_protocol.qubit))
        alice_circuit.append(cirq.H(my_protocol.qubit))
        if not bob_hadamard:
            bob_circuit.append(cirq.I(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_no_H_circuit = bob_circuit
        else:
            bob_circuit.append(cirq.H(my_protocol.qubit))
            bob_circuit.append(cirq.M(my_protocol.qubit))
            my_protocol.bob_receive_H_circuit = bob_circuit
        my_protocol.alice_send_1_H_circuit = alice_circuit
