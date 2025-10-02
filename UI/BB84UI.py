from RequiredForBB84 import *  # Import your BB84 functions
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QMessageBox, QDialog, QTextEdit, QCheckBox
from BB84Implementation import *
from Scripts.BB84Implementation import my_protocol, protocolImplementation
import sys
from PyQt5.QtWidgets import QLineEdit
import io
class BB84App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("BB84 Protocol Showcase")
            self.setGeometry(100, 100, 400, 400)  # Increased height for new checkbox

            # Initialize variables
            self.alice_qubit = None
            self.alice_hadamard = False
            self.bob_hadamard = False
            self.compare_bits = False  # Default: Do not compare bits

            # Main layout
            layout = QVBoxLayout()

            # Alice's qubit selection
            self.label_alice_qubit = QLabel("Alice's Qubit: Not Set")
            layout.addWidget(self.label_alice_qubit)

            btn_qubit_0 = QPushButton("Alice: Send Qubit 0")
            btn_qubit_0.clicked.connect(lambda: self.set_alice_qubit(0))
            layout.addWidget(btn_qubit_0)

            btn_qubit_1 = QPushButton("Alice: Send Qubit 1")
            btn_qubit_1.clicked.connect(lambda: self.set_alice_qubit(1))
            layout.addWidget(btn_qubit_1)

            # Alice's Hadamard buttons
            self.label_alice_hadamard = QLabel("Alice's Hadamard: Not Applied")
            layout.addWidget(self.label_alice_hadamard)

            btn_apply_alice_hadamard = QPushButton("Alice: Apply Hadamard")
            btn_apply_alice_hadamard.clicked.connect(lambda: self.toggle_alice_hadamard(True))
            layout.addWidget(btn_apply_alice_hadamard)

            btn_remove_alice_hadamard = QPushButton("Alice: Remove Hadamard")
            btn_remove_alice_hadamard.clicked.connect(lambda: self.toggle_alice_hadamard(False))
            layout.addWidget(btn_remove_alice_hadamard)

            # Bob's Hadamard buttons
            self.label_bob_hadamard = QLabel("Bob's Hadamard: Not Applied")
            layout.addWidget(self.label_bob_hadamard)

            btn_apply_bob_hadamard = QPushButton("Bob: Apply Hadamard")
            btn_apply_bob_hadamard.clicked.connect(lambda: self.toggle_bob_hadamard(True))
            layout.addWidget(btn_apply_bob_hadamard)

            btn_remove_bob_hadamard = QPushButton("Bob: Remove Hadamard")
            btn_remove_bob_hadamard.clicked.connect(lambda: self.toggle_bob_hadamard(False))
            layout.addWidget(btn_remove_bob_hadamard)

            # Compare bits checkbox
            self.compare_checkbox = QCheckBox("Compare Bits (Debug Mode)")
            self.compare_checkbox.stateChanged.connect(self.toggle_compare_bits)
            layout.addWidget(self.compare_checkbox)

            # Execute BB84 Protocol button
            btn_execute_bb84 = QPushButton("Execute BB84 Protocol")
            btn_execute_bb84.clicked.connect(self.execute_bb84)
            layout.addWidget(btn_execute_bb84)

            # Set the central widget
            container = QWidget()
            container.setLayout(layout)
            self.setCentralWidget(container)
            # Add Authentication Button
            btn_authenticate = QPushButton("Go to Authentication")
            btn_authenticate.clicked.connect(self.open_authentication_window)
            layout.addWidget(btn_authenticate)

            container = QWidget()
            container.setLayout(layout)
            self.setCentralWidget(container)

        def open_authentication_window(self):
            try:
                print("Opening authentication window...")  # Debugging statement
                self.auth_window = BB84AuthApp()
                self.auth_window.show()
                print("Authentication window opened successfully.")  # Debugging statement
            except Exception as e:
                print(f"Error opening authentication window: {e}")  # Debugging statement
        # Set Alice's qubit
        def set_alice_qubit(self, value):
            self.alice_qubit = value
            self.label_alice_qubit.setText(f"Alice's Qubit: {value}")

        # Toggle Hadamard for Alice
        def toggle_alice_hadamard(self, apply):
            self.alice_hadamard = apply
            status = "Applied" if apply else "Not Applied"
            self.label_alice_hadamard.setText(f"Alice's Hadamard: {status}")

        # Toggle Hadamard for Bob
        def toggle_bob_hadamard(self, apply):
            self.bob_hadamard = apply
            status = "Applied" if apply else "Not Applied"
            self.label_bob_hadamard.setText(f"Bob's Hadamard: {status}")

        # Toggle Compare Bits
        def toggle_compare_bits(self, state):
            self.compare_bits = state == 2  # Qt checkboxes: 2 = Checked, 0 = Unchecked

        # Execute the BB84 protocol
        def execute_bb84(self):
            if self.alice_qubit is None:
                QMessageBox.warning(self, "Error", "Alice's qubit is not set!")
                return

            # Redirect console output
            old_stdout = sys.stdout  # Save current stdout
            sys.stdout = io.StringIO()  # Redirect stdout to capture output

            # Execute BB84 protocol (prints output to stdout)
            protocolImplementation(self.alice_qubit, self.alice_hadamard, self.bob_hadamard)
            my_protocol.send_bit(
                alice_bit=self.alice_qubit,
                does_alice_apply_H='yes' if self.alice_hadamard else 'no',
                does_bob_apply_H='yes' if self.bob_hadamard else 'no',
                compare_bits='yes' if self.compare_bits else 'no'  # Pass checkbox state
            )

            # Get printed output
            output_text = sys.stdout.getvalue()

            # Restore stdout
            sys.stdout = old_stdout

            # Display the captured output in a new window
            self.show_result_window(output_text)

        def show_result_window(self, output_text):
            result_dialog = QDialog(self)
            result_dialog.setWindowTitle("BB84 Protocol Result")
            result_dialog.setGeometry(200, 200, 500, 400)

            layout = QVBoxLayout()
            text_edit = QTextEdit()
            text_edit.setReadOnly(True)
            text_edit.setText(output_text)  # Set the captured output
            layout.addWidget(text_edit)

            result_dialog.setLayout(layout)
            result_dialog.exec_()


class BB84AuthApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BB84 Authentication")
        self.setGeometry(100, 100, 400, 250)

        # Expected password (predefined for testing, could be securely stored)
        self.correct_password = "1234"

        # Main layout
        layout = QVBoxLayout()

        self.label_instruction = QLabel("Enter 4-digit password:")
        layout.addWidget(self.label_instruction)

        self.input_password = QLineEdit()
        self.input_password.setMaxLength(4)
        self.input_password.setPlaceholderText("Enter 4 digits")
        layout.addWidget(self.input_password)

        btn_validate = QPushButton("Validate Password")
        btn_validate.clicked.connect(self.validate_password)
        layout.addWidget(btn_validate)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def validate_password(self):
        user_input = self.input_password.text()

        if len(user_input) != 4 or not user_input.isdigit():
            QMessageBox.warning(self, "Error", "Please enter a 4-digit number.")
            return

        # Convert password into qubits (0 or 1)
        qubits = [int(digit) % 2 for digit in user_input]

        # Use a single Hadamard choice for both Alice and Bob
        hadamard_choice = True  # Single basis for all bits

        # Simulate BB84 authentication process
        for i in range(4):
            protocolImplementation(qubits[i], True, True)
            my_protocol.send_bit(
                alice_bit=qubits[i],
                does_alice_apply_H='yes' ,
                does_bob_apply_H='yes'
            )

        # Compare generated key with expected password's bit representation
        if len(my_protocol.bob_key) < 4:
            QMessageBox.critical(self, "Error", "BB84 protocol failed. Not enough key bits received.")
            return

        received_bits = ''.join(str(bit) for bit in my_protocol.bob_key[-4:])
        expected_bits = ''.join(str(int(digit) % 2) for digit in self.correct_password)
        if user_input==self.correct_password:
            QMessageBox.information(self, "Success", "Authentication Passed!")
        else:
            QMessageBox.critical(self, "Failed", "Incorrect Password!")


# Run the application
app = QApplication([])
window = BB84App()
window.show()
app.exec_()
