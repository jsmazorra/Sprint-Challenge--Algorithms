#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) would be the running time since there's a linear increase in every sequence (e.g n = 1 will be one iteration, n=5 will be five iterations, n = 15 will be fifteen iterations, etc). Essentially, in this case the while loop reflects n head on.


b) 0(n log n) is the running time since this algorithm follows a linear search where in this case the inner loop runs log(i + 1) times, where i is at most n - 1, and the outer loop runs n times. Such an example will be for inputs n = 1 -> 0, n = 5 -> 15, n = 10 -> 40, n = 20 -> 100 iterations.

c) In this case 0(1) is the running time since there's no else statement and it's not looping over anything. This will make it return a constant value, hence 0(1) = constant running time which is the best and fastest running time.

## Exercise II

My proposed algorithm approach will be to use a binary search only if the floors are in a pre-sorted list. In this sorted list while using a binary search there would be a complexity of 0(log n). 
So in this case, first try to drop an egg from the n/2 floor, in which n is the total number of floors, and see the result. There would be two scenarios: 
   
    a) If the egg didn't brake, we will eliminate all lower floors as a course of action. 
    b) If the egg did in fact brake, we will do the opposite which is to eliminate all higher floors as a course of action.
    
To do this approach in a quick and efficient manner we should drop an egg from the middle range of the building so that on average we eliminate possible wrong options.
