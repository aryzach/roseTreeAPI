Completing take home [Rose Tree API in Python](https://gist.github.com/aranchelk/1703502389b9de689a96cbf656392c33) for a job interview.

Explain (no need to actually implement) how you'd design a method to move a sub-tree from one location to another within the parent. Are there any special considerations for this in comparison to the previously mentioned methods?

I believe the best way to do this would be the following:
	- from the new location, point to the subtree that you want to move
	- from the old location, delete the reference to the subtree
This avoids unnecessary waste of space and time if you were to copy the subtree. In the other methods, you are either only reading, writing (and garbage collecting), or writing, so the constraints here are not relevant. 

I'm making some assumptions about how the API should behave
	- what is returned by the method call when no obvious return value
	- how to handle ambiguous input cases (ex. where to insert tree if path isn't exact)
	- when inserting a tree at a location, if a tree exists at that location, I'll replace it. If no tree exists at that location, I'll insert it as the last subtree (which is not necessarily the absolute specified position). If you're specifiying a location deeper than the tree, don't insert

I'm also not type checking or doing much validation or full test coverage
