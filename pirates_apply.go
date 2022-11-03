{{ $val := createTicket nil .User.Username }}
{{ $args := parseArgs 1 "" (carg "user" "target user") }}
{{$userid := ($args.Get 0) }}

{{$MID :=976912078034042900}}

{{ $user := .User }}
{{ $avatar := ("https://cdn.discordapp.com/attachments/962341885576364092/973926060368465920/a-4c6a69b1c4f6feda26b38164e184-unscreen.gif") }}

{{if eq .Reaction.MessageID $MID}}
        {{sendMessageNoEscape 962341885576364092 (print (mentionRoleID 976919715404468264) ": " .User.Mention " is waiting at the plank!")}}
        {{$val}}
{{end}}


{{$welcome := complexMessage "content" $userid.Mention "embed" (cembed "title" (joinStr "" "Ahoy! " $userid.Username ", Welcome to the plank!")
"description" `Please change your nickname to reflect  your *in-game name* and, have a read through the __***rules***__ at <#973912318494777355>.
 
\n\n__**Application Process**__\nThe following are the steps in our clan application process:\n\n:bullet: **Pictures:** Send pictures of your base & profile.\n:bullet: **Clan:** State what clan you're looking to apply for.\n:bullet: **Introduction:** A couple of attack strategies that you'd like to use.\n:bullet: **Join:** You will be accepted on Discord and in-game, if applicable.\n\n:flashcheck: **Password**\nAll RCS clans require a password to enter, to find out the password, type in - `?password` and have a read through the rules section, once you find the password, type it in the channel and the bot will verify it. " 

Get your sails up and enjoy the ocean!` "color" 59647 "thumbnail" (sdict "url" $thumb))}}


{{$userid := .User }}
{{$thumb := ("https://cdn.discordapp.com/attachments/962341885576364092/973926060368465920/a-4c6a69b1c4f6feda26b38164e184-unscreen.gif") }}
{{$welcome := complexMessage "content" $userid.Mention "embed" (cembed "title" (joinStr "" "Ahoy! " $userid.Username ", Welcome to the plank!")
"description" `Please change your nickname to reflect  your *in-game name* and, have a read through the __***rules***__ at <#973912318494777355>.
 
__**Application Process**__

The following are the steps in our clan application process:
:bullet: **Pictures:** Send pictures of your base & profile.\n
:bullet: **Clan:** State what clan you're looking to apply for.\n
:bullet: **Introduction:** A couple of attack strategies that you'd like to use.\n
:bullet: **Join:** You will be accepted on Discord and in-game, if applicable.\n\n

:flashcheck: **Password**\nAll RCS clans require a password to enter, to find out the password, type in - "?password" and have a read through the rules section, once you find the password, type it in the channel and the bot will verify it. " 

Get your sails up and enjoy the ocean!` "color" 59647 "thumbnail" (sdict "url" $thumb))}}
{{sendMessage nil $welcome}}