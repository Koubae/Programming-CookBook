use projectName;

CREATE TABLE IF NOT EXISTS  project  (
		projectName 	varchar(50) NOT NULL,
  		projectID 		int(11) NOT NULL AUTO_INCREMENT,
		projectPrio		  enum('High','Medium','Low') NOT NULL,
		PRIMARY KEY 	(projectID)
);

CREATE TABLE IF NOT EXISTS tasks (
		taskID 			int(11) NOT NULL AUTO_INCREMENT,
		taskName 		varchar(50) NOT NULL,
  		taskStartDate 	date NOT NULL,
		taskDueDate 	date NOT NULL,
		taskPriority	  enum('High','Medium','Low') NOT NULL,
		projectID 		int(11) NOT NULL,
		taskDone 		enum('yes','no') DEFAULT 'no',
		notes			  varchar(255),
		PRIMARY KEY 	(taskID)
);
