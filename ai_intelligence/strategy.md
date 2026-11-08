# Universal Problem-Solving Strategy (UPSS)
## Framework for Advanced Mathematical and Physical Reasoning

This document defines the cognitive loop that the model must execute for every complex problem. The goal is to move from "predicting the next token" to "executing a logical derivation."

### Phase 1: Ontological Deconstruction (Understanding)
Before attempting any calculation, the model must explicitly define:
1. **The System**: What is the physical or mathematical system being described? (e.g., "A stochastic process," "A rigid body in rotation," "A Gaussian distribution").
2. **Knowns & Constraints**: Extract every constant, variable, and boundary condition.
3. **The Objective**: Define the goal in precise mathematical terms (e.g., "Find the value of $\lambda$ that maximizes the likelihood function $\mathcal{L}$").
4. **Dimension Analysis**: Verify the units of the input and the expected units of the output.

### Phase 2: Theoretical Mapping (Connecting)
The model must link the problem to the first principles of science:
1. **Axiom Identification**: Which fundamental laws apply? (e.g., "Conservation of Energy," "The Central Limit Theorem," "Bayes' Theorem").
2. **Model Selection**: Choose the mathematical tool. (e.g., "This is a differential equation problem $\rightarrow$ Use Separation of Variables").
3. **Reasoning Path**: Outline the sequence of operations: 
   *Step A $\rightarrow$ Step B $\rightarrow$ Step C $\rightarrow$ Final Answer.*

### Phase 3: Symbolic Execution (Calculating)
To eliminate arithmetic hallucinations, the model must use a "Symbolic First" approach:
1. **Formalization**: Write the problem in pure LaTeX/Mathematical notation.
2. **Symbolic Solution**: Solve for the variable in terms of letters/symbols first.
3. **Computational Offloading**: Translate the final symbolic expression into a Python/SymPy script to compute the exact numerical value.
4. **Verification**: Cross-check the result using a different method (e.g., "Check if the sum of probabilities equals 1").

### Phase 4: Critical Synthesis (Interpreting)
The final answer must be accompanied by a scientific interpretation:
1. **Plausibility Check**: "Does this answer make sense in the real world?" (e.g., "A negative variance is impossible; I must re-evaluate Step 3").
2. **Sensitivity Analysis**: "How would the answer change if the input $X$ increased by 10%?"
3. **Conclusion**: State the result clearly with appropriate significance levels and units.
