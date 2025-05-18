import random

def generate_ballots(candidates, num_votes):
    ballots = []
    for _ in range(num_votes):
        ballot = candidates.copy()
        random.shuffle(ballot)
        ballots.append(ballot)
    return ballots

def tally_first_choice_votes(ballots, candidates):
    tally = {candidate: 0 for candidate in candidates}
    for ballot in ballots:
        if ballot:  # skip if ballot is empty
            first_choice = ballot[0]
            if first_choice in tally:
                tally[first_choice] += 1
    return tally

def find_candidate_to_eliminate(tally):
    # Return candidate with fewest votes (random tie-breaker)
    min_votes = min(tally.values())
    lowest = [cand for cand, votes in tally.items() if votes == min_votes]
    return random.choice(lowest)

def eliminate_candidate(ballots, candidate_to_remove):
    updated_ballots = []
    for ballot in ballots:
        updated_ballot = [cand for cand in ballot if cand != candidate_to_remove]
        updated_ballots.append(updated_ballot)
    return updated_ballots

def check_for_majority(tally, total_votes):
    for candidate, votes in tally.items():
        if votes > total_votes / 2:
            return candidate
    return None

def print_tally(tally, round_num):
    print(f"\n🔄 Round {round_num} Results:")
    for candidate, votes in tally.items():
        print(f"{candidate} received {votes} votes.")
    print("-" * 40)

def ranked_choice_voting(candidates, num_votes):
    ballots = generate_ballots(candidates, num_votes)
    print(f"✅ {num_votes} ballots generated.")
    print("Sample Ballots:")
    print("Ballot 1:", ballots[0])
    print("Ballot 2:", ballots[1])
    
    remaining_candidates = candidates.copy()
    round_num = 1

    while True:
        tally = tally_first_choice_votes(ballots, remaining_candidates)
        print_tally(tally, round_num)

        winner = check_for_majority(tally, len(ballots))
        if winner:
            print(f"🏆 Winner: {winner} with majority of votes.")
            break

        candidate_to_remove = find_candidate_to_eliminate(tally)
        print(f"❌ Eliminating {candidate_to_remove} (fewest votes).")
        remaining_candidates.remove(candidate_to_remove)
        ballots = eliminate_candidate(ballots, candidate_to_remove)
        round_num += 1

After Runnning the simulation

candidates = ["SpongeBob", "Bluey", "Owlet", "Frogger", "Luigi", "Moana", "Barbie"]
num_votes = 1000

ranked_choice_voting(candidates, num_votes)
