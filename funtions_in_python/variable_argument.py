def mean( *nums ):
    if nums:
        return sum(nums)/len(nums)
    
def create_sentence(*words, glue=' '):
    return glue.join(words)

print(mean())
print(mean(1))
print(mean(1,2))
print(mean(1,2,3,4))
print(mean(1,2,3,4,12,2,3,3,1,2,2,3,4,3,3,2,2,2))

result = create_sentence('this','that','mish','mash','wish','wash')
print(result)
result = create_sentence('this','that', glue='/')
print(result)