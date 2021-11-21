txt=int(input(">>>"))
txt.lower()
index=0
vowelSet=set(['a','e','i','o','u',])
vowels=0
con=0
while index< len(txt):
    if txt in vowels:
        vowels+=1
        index +=1
        print(f"Тут"[vowels])
