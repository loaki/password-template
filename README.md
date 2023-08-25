# store passwords on github page

### index

/index hash password input with sha1 to redirect to /<password_hash>/index if it exist  

rename the \<password_hash\> folder and all the paths after your hashed password

https://emn178.github.io/online-tools/sha1.html

### data

all data are stored with AES encryption

rename the \<github_token_hash\> after your hashed github token

https://stackblitz.com/edit/cryptojs-aes-encrypt-decrypt?file=index.js

### workflow

github actions are used to append/remove data from the page 

you need to wait few minutes for the pipeline to commit the changes

replace \<name\> and \<email\> in the workflow

# make sure your repo is private :)
