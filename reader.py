import json


with open("file.json","r") as f:
  data = f.read()

d = json.loads(data)

in_dict=[]
for i in d['Quiz']:
    in_dict.append(i)
    
# print(in_dict)


for j in range(len(in_dict)):
    print(in_dict[j]["question"])
    arr_len = len(in_dict[j]["choices"])
    for k in range(arr_len):
        print(str(k+1)+": "+in_dict[j]["choices"][k])
    ans = input("Type Answer:")

    if ans==in_dict[j]["correct_ans"]:
             print(f"{ans} is a Correct Answer!!\n")
    else:
        print("Wrong Answer, Correct Answer is "+in_dict[j]["correct_ans"])



