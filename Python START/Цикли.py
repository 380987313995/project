# count = 50
# while count > 0:
#     print("залишилось",count,"картоплі")
#     count -= 1
# print('dosut')

# for element in range(10):
#     print(element)

# counter=10
# while True:
#     counter-=1
#     print(counter)
#     if counter==5:
#         break

# for e in range(40):
#     if e == 8:
#         continue
#     print(e)

# counter=0
# while counter<10:
#     counter+=1
#     if(counter%2)==0:
#         continue
#     print(counter)

# for e in range(40):
#     if e==8:
#         break
#     print(e)


# for d in range(102):
#     if(d%2-1)==0 or d==0:
#         continue
#     print(d)
#
# for d in range(102):
#     if (d % 2 ) != 0 :
#         continue
#     print(d)

# answer = ""
# for letter in "hello ":
#     if letter == 'l':
#         answer+='s'
#     else:
#         answer+=letter
# print(answer)
#
# print('hello'.replace('l', 's'))#replace- zamina symbols



# for a in reversed(range(100)):
#     if (a%5) == 0:
#         print(a)

# for a in range(-99,0):
#     if (a%5) == 0:
#         print(abs(a))



# prev2 = 0
# prev1 = 1
#
# print(prev2)
# print(prev1)
# for newFibo in range(100):
#     newFibo = prev1 + prev2
#     print(newFibo)
#     prev2 = prev1
#     prev1 = newFibo #zadacha 1


# У пропозиції “Hello world” замінити всі літери “o” на “a”, а літери “l” на “e”.
answer=""
for letter in "hello ":
    if letter == 'l':
        answer+='e'
        if letter == 'o':
           answer += 'a'
    else:
        answer+=letter
print(answer)
