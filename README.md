# BB84 Visual Tool  

A simple **visual learning tool** for the **BB84 Quantum Key Distribution protocol**, built as an interactive app to show what happens when **Alice** and **Bob** use different inputs and measurement bases.  

This project is designed to make it easier for students and enthusiasts to understand how BB84 works, step by step.  

---

## 🎯 Features  
- **Interactive Inputs**: Choose Alice’s bits and bases, as well as Bob’s measurement bases.  
- **Step-by-Step Visualization**: See how qubits are encoded, transmitted, and measured.  
- **Error Simulation**: Observe mismatches when Alice and Bob use different bases.  
- **Key Generation Process**: Watch how the final shared secret key is formed after sifting.  

---

## 🧠 About BB84  
BB84 is the **first quantum key distribution (QKD) protocol**, proposed by Charles Bennett and Gilles Brassard in 1984.  
It allows two parties (Alice and Bob) to establish a **secure shared secret key** using the laws of quantum mechanics.  

This tool visually demonstrates the core idea:
1. Alice sends qubits encoded in random bases.  
2. Bob measures them in random bases.  
3. When their bases match, they share the same bits.  
4. After discarding mismatched cases, a secure key is formed.  

---

## 🛠 Implementation Notes  
- The **protocol logic** (BB84 steps, bit handling, base matching) was **adapted from "The Coding School" implementation, thanks so much to them!**.  
- The **visualization layer** (interactive inputs and outputs) was fully developed for this project.  

---
