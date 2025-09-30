Initial Appwrite Setup

To Do:
	1. Create/prepare a single Appwrite Cloud project (“root-project”).

	2. Add Databases → notes_db / notes collection.

	3. Deploy one HTTP Function (notes-api) with GET/POST.

	4. Configure environment variables (endpoint, projectId, API key, db/collection IDs).

	5. Provide docs + test checklist (manual + basic unit tests in chosen language).
---------------------------------------------------------------------------------------------------------

Refer to official documentation first, this way you can learn all by yourself

Problems faced:
	Problem 1: Building a function
	**Docker Desktop is needed to run the functions locally so Ensure it's running in background**
		-Make the function using CLI {Preferably Powershell}
		1. Install Appwrite CLI via npm or download from Appwrite's official website
			npm install -g appwrite-cli
		2. Log In to CLI
			appwrite login
		3. Link your Project
			appwrite init project
		4. Create function
			appwrite init function 
		OR, you can also pull a function if already made using GUI
			appwrite pull function
		5. Go to the path and open the file in your code editor and write a simple logic, like: hello from appwrite
		6. Now run it locally in your CLI
			appwrite run function --function-id=<your-function-name>
	**Now to make it appear in Appwrite GUI simply type "appwrite push function" and select it**
