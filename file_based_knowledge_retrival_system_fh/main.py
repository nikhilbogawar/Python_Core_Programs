# PROJECT 2: FILE-BASED KNOWLEDGE RETRIEVAL SYSTEM
# 1. Read knowledge.txt line by line
# 2. Combine every 2 lines into 1 chunk
# 3. Write chunks into vector_store.txt
# 4. Ask user for query using input()
# 5. Compare query words with each chunk
# 6. Return the chunk with highest score
# 7. Allow repeated queries until user types exit
# 8. Use seek() or tell() somewhere in the program

with open('knowledge.txt', 'r') as file,open('data.txt','w') as d:
    c=0
    for line in file:

        if line=='':
            continue
        c+=1
        if c==2:
            text=prev_line+" "+line
            d.write(text)
            # print(text)
            d.flush()
            c=0
        else:
            prev_line=line
            prev_line=prev_line.replace("\n","")

def ask_question(question):
    max_score=0
    mrc=""
    with open('data.txt', 'r') as file:
        for chunk in file:
            score=0
            for word in question.split():
                if word.lower() in chunk.lower():
                    score+=1
            if score>max_score:
                max_score=score
                mrc=chunk
    print(mrc)
ask_question(input("What is your question? "))