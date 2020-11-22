# GIT setting and useful commands 

### links
[gihub docs](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
[markdown](https://guides.github.com/features/mastering-markdown/)

### installing ssh key
* ssh-keygen -t rsa -b 4096 -C "denis.patrakhin@gmail.com" # generate ssh key
* eval "$(ssh-agent -s)" # start ssh agent
* ssh-add ~/.ssh/id_rsa # add key
* cat ~/.ssh/id_rsa.pub # verify pub key to enter github
* ssh -T git@github.com # make testing
* git remote -v && git remote show origin # check current settings
* git remote set-url origin git+ssh://git@github.com/patraden/pythonstudy.git # update URL as required
* git remote show origin # verify changes

### configuring ssh-agent start and rsa key load up on login
* sudo apt-get install keychain
* vim ~/.bashrc #eval $(keychain --eval id_rsa)


### pushing to github using ssh
* git add . # add all file to local repository
* git commit -a -m "new commit" # commit changes
* git push origin master #push changes to guthub

### git configuration
* cat /home/pi/.gitconfig # user git config file
* git config --list --show-origin # show entire config
* git config user.name # show config user
* git config user.email # show config email
* git config --global user.email "denis.patrakhin@gmail.com" # configure email
* git remote set-url origin #List your existing remotes in order to get the name of the remote you want to change
* git remote set-url origin https://github.com/patraden/neo4j_mars.git #Change your remote's URL from SSH to HTTPS with the git remote set-url command.

### useful docker commands
docker rmi $(docker image ls -f "dangling=true" -q)
docker rm $(docker ps -a -q)
