query="""solve the following problem : 
    Given a text file file.txt that contains a list of phone numbers (one per line), 
    write a one-liner bash script to print all valid phone numbers.
    You may assume that a valid phone number must appear in one of the following two formats: 
    (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
    You may also assume each line in the text file must not contain leading or trailing white spaces."""

obj=Memory()

tools={"DSA solver":"can solve any sort of DSA problem","Deployer":"Can deploy any sort of software on AWS"}
ans=take_decision(client,obj,tools,query)
print(ans)