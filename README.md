# I-211_Mastery_check_2

# Ranked Choice Voting Simulation

This Python project simulates a Ranked Choice Voting (RCV) system. It generates 1,000 randomly ranked ballots and processes the election using real-world RCV rules, including multiple rounds of vote tallying, candidate elimination, and vote redistribution until a majority winner is found.

## Features

- Randomized ballot generation for 1,000 voters
- Vote tallying by first-choice preference
- Candidate elimination logic based on fewest votes
- Redistribution of votes to next ranked candidates
- Loop continues until a majority winner is found
- Sample ballots and round-by-round results printed to the console

## Concepts Demonstrated

- Python loops and conditionals
- List and dictionary manipulation
- Modular code structure with functions
- Randomization using the random module
- Algorithmic simulation of election systems

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Running the Program

Clone the repository and run the Python script:

```bash
git clone https://github.com/your-username/ranked-choice-voting-simulation.git
cd ranked-choice-voting-simulation
python ranked_choice_voting.py
