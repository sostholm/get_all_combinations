# get_all_combinations
In my work I realized I had a need to get all possible combinations of an array of arrays and after quite some pondering, this is my solution:
Recursive algorithm that returns all the element combinations of an array of arrays


<img width="661" alt="Screenshot 2021-12-11 at 19 29 57" src="https://user-images.githubusercontent.com/42302892/145687619-7940b413-67cc-416f-933a-8cbe7b5c4e2c.png">

The algorithm will iterate through all y's in a column and create a new path vector and recursively call get_all_combinations with the next x and the path generated. 
When the algorithm have reached the max x in the matrix, it will append the path to the paths array.
