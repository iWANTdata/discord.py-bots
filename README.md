# Fynnyxbot

## General
Get your Bot-Token from [Discord Developer Portal](https://discord.com/developers/applications). Then insert the Token in *.env.example* and save it as *.env.* Than run the Bot.

### Table of content
* [Electionbot](https://github.com/Fynnyx/discord.py-bots#electionbot)
* [Verifybot](https://github.com/Fynnyx/discord.py-bots#verifybot)
* [Commandbot](https://github.com/Fynnyx/discord.py-bots#commandbot)


##### ❗Warning❗
If you change something then maybe this readme won't help you


## Electionbot

### What the bot do
With this bot you can create elections and end them to get the reult of them. To end an election you have to click the ❌ or type the end command. You also need the permission_role that you can change in the file. The bot has a info and help command to help members with the commands.

### How to setup the bot
If you want to use the bot with preset settings only run the code on a server.

Variables | What they do
----------| ------------
channel | set the channel (id)
prefix | change the prefix to talk to the bot
reaction1 | change the first reaction emoji
reaction2 | change the second reaction emoji
role | set the role for loser (id)
role_end_permission | user with this role can end elections (name)

### Commands

```Python
!electionbot info #get the info embed
!electionbot help #get the help embed
!electionbot question? #start an election
!electionbot end #end the election
```




## Verifybot

### What the bot do
With this bot you can add a verify button to a channel. By reacting to this emoji ,✅, the user get the verified role. With this you can try to avoid bot accounts.

### How to setup the bot
If you want to use the bot with preset settings only run the code on a server.

Variables | What they do
----------| ------------
channel_name | set the channel (name)
prefix | set the botprefix
emoji | change the emoji to react to
role | change the role (id)
permission | set who have the permission to send the verify button (name)


### Commands

```Python
!verify info #get the info embed
!verify help #get the help embed
!verify #send the verify button
agree #agrees the verification
```

## Commandbot

### What the bot do
There you can add you own commands

### How to setup the bot
Set the Invitelink to no limit and no time antil the link get deleted. Else you have to update this everytime

Variables | What they do
----------| ------------
prefix | change the prefix
dj_role | insert the DJ role ID (int)
invitelink | set the invitelink from your server


### Commands

```Python
!commandbot info #get the info embed
!commandbot help #get the help embed
!commandbot get bots #shows all bots i made
!commandbot get dj #gives the user the DJ role
!commandbot invitelink #sends the invitelink of the server
!commandbot ip-adress #sends the ip-adress oo something   ex. minecraft-server

# add your own commands
```

## Economybot

### What the bot do
With this bot you can bring your own currency on your server. The member can send the money to other member.

### How to setup the bot
save the *users.json.example* as *users.json*

Variables | What they do
----------| ------------
prefix | change the prefix


### Commands

```Python

```









## Example

### What the bot do

### How to setup the bot

Variables | What they do
----------| ------------
prefix | change the prefix


### Commands

```Python

```

