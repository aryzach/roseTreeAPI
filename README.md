Completing take home [Rose Tree API in Python](https://gist.github.com/aranchelk/1703502389b9de689a96cbf656392c33) for a job interview.

Explain (no need to actually implement) how you'd design a method to move a sub-tree from one location to another within the parent. Are there any special considerations for this in comparison to the previously mentioned methods?

I believe the best way to do this would be the following:
	- from the new location, point to the subtree that you want to move
	- from the old location, delete the reference to the subtree
This avoids unnecessary waste of space and time if you were to copy the subtree. In the other methods, you are either only reading, writing (and garbage collecting), or writing, so the constraints here are not relevant. 
