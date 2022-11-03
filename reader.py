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
    option=ord('a')
    ans_dict=dict()
    for k in range(arr_len):
        print(str(chr(option))+": "+in_dict[j]["choices"][k])
        ans_dict[chr(option)]=in_dict[j]["choices"][k]
        option=option+1
    ans = input("Type Answer:")

    if ans_dict[ans]==in_dict[j]["correct_ans"]:
             print(f"Option {ans} i.e {ans_dict[ans]} is a Correct Answer!!\n")
    else:
        print(f" {ans_dict[ans]} is Wrong Answer, Correct Answer is  "+in_dict[j]["correct_ans"])



