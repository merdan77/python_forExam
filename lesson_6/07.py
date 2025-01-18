print("Enter student scores. Type '0' to stop and calculate results.")
scores = []
passing_score = 50

while True:
    score = input("Enter score (or type 'quit'):").strip()
    if score == "0":
        break
    if score.replace('.',",1).isdigit(): 
        score = float(score)
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Score must be between 0 and 100.")
    else:
        print("Invalid input. Please enter a nuric score")
if not scores:
    print("No sscores were entered")
else:
    passed_count = sum(1 for s in scores if s >= passing_score)
    total_students = len(scores)
    pass_percentage = (passed_count / total_students) * 100
    print(f"Total students: {total_students}")
    print(f"Students passed: {passed_count}")
    print(f"Pass percentage: {pass_percentage:.2f}%")