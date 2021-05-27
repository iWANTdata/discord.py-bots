# Fynnyxbot

## General
Get your Bot-Token from [Discord Developer Portal](https://discord.com/developers/applications). Then insert the Token in *.env.example* and save it as .env. Than run the Bot.

### Table of content
* [Electionbot](https://github.com/Fynnyx/discord.py-bots#electionbot)
* [Verifybot](https://github.com/Fynnyx/discord.py-bots#verifybot)

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
With this bot you can add a verify button to a channel. By reacting to this emoji the user get the verified role. With this you can try to avoid bot accounts.

### How to setup the bot
If you want to use the bot with preset settings only run the code on a server.

Variables | What they do
----------| ------------
channel_name | set the channel (name)
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









## Example

### What the bot do

### How to setup the bot

Variables | What they do
----------| ------------
channel | set the channel (id)


### Commands

```Python

```

