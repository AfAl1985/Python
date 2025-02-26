print('Task: merging companies')
# We have the main company which managment took a decision to buy the smaller ones.
# But those ones had some unsolved problems. First - we need to complete a merging
# all of them. Then count completed tasks and unsolved problems.
# Write a code below and screen he result
main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]
completed = 0
uncompleted = 0


main.extend(first_company)
main.extend(second_company)
main.extend(third_company)
print(main)

print('Comleted tasks: ',main.count(1))
print('Uncomleted tasks: ',main.count(0))
