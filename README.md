# Clean
The clean.py program will walk through the directories and remove any files ending with ".pyc".
Sometimes the generate.py program will make a .pyc file, making the number of files cleaned be one greater 
than number of files with .pyc created by the generator. To overcome this problem, I made condition in the
unit test that checks if "generate.pyc" was created and have it removed so the number of files cleaned and 
generated are equal.
