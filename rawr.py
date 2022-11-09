from time import perf_counter
start = perf_counter()
print("password")
end = perf_counter() - start
print(f'One 8 character password: {end} sec')
print(f'Num: {95**3}')
print(f'All 8 character passwords: {(end*95**3)/(60*60*24)} days')
