{{if eq .Reaction.Emoji.Name "thought_balloon"}}
{{deleteMessageReaction "thought_balloon"}}
{{sendMessage "Hey, cherry blossoms. A member feels uncomfortable with the topic. Please take it to {{.channel.ID 802799583863767050}}"}}
...
{{end}}
{{addRoleID 792774106377486368}}
{{sendMessage 762508425279832074 (print "Welcome to our newest member, " .User.Mention ".")}}


{{ $channel := "suggestions" }}
{{$arg1 := parseArgs 1 "Correct usage is: -suggest <your suggestion>"
    (carg "string" "suggestion")}}

{{$newmsg := sendMessageNoEscapeRetID $channel (cembed
"thumbnail" (sdict "url" (.User.AvatarURL "1024"))
"description" (joinStr "" .User.Mention " Suggested: \n\n> " ($arg1.Get 0)))}}
{{addMessageReactions $channel $newmsg "white_check_mark" "negative_squared_cross_mark"}}
{{deleteTrigger 60}}

("description" (joinstr "" .User.Mention " Suggest: \n\n "))

{{$mid :=786350464090243083}} /*This will be the message ID of the RR menu*/
//Data-base:
{{$r :=sdict "super_hound" 786331185860313129 "super_wiz" 786331078893502524 "super_witch" 784413270038806528 "super_inferno" 784413217883160587 "super_wallbreaker" 784413106717065248 "super_goblin" 784412925707812886 "super_valk" 784412745364799488 "super_giant" 784413054518951956 "Super_minion" 784411939672555580 "super_barbs" 784412013547225109 "super_archer" 784412057458049036}}
//Instructions for adding in new super troops:
/*For adding in new super troops, type in the emote name(case-sensitive) under strings(" ") and then followed by the role ID attached to that emote.*/
/*The emote name should be exactly the same as what is mentioned, a slight uppercase/lowercase change could corrupt the entire database*/
{{if eq .Message.ID $mid}} /*This checks through the database and collects the emote reactions attached to the super troop role ID*/
  {{removeRoleID ($r.Get .Reaction.Emoji.Name) 259200}} /*And finally, this'll remove the roles after 3 days. In future updates where the 3-day timer is changed, convert the time into seconds and add it onto the removeRoleID deliminator.*/
/*Avoid changing the indents so that the code won't breakdown.ie. adding extra spaces... etc.*/
//last edited on 21:37. 3rd March, 2021
{{end}}

//Zen-Zenith-ZenAcademy Stuff
//4:06am, 02/04/2021

{{$zenMID :=827433436138307627}}
{{$zenithMID :=827433553636884501}} 
{{$zenacMID :=827433746655215678}}
{{$friendMID := 827433254340263966}}

{{$zenaclist :=sdict "townhall6" 821922710527541258 "townhall7" 821922710527541258 "townhall8" 821922710527541258 "townhall9" 821922710527541258}}
{{$zenithlist :=sdict "townhall10" 82192270956206489 "townhall11" 821922709562064896}}
{{$zenlist :=sdict "townhall12" 821922696379760670 "townhall13" 821922696379760670}}
{{$friend :=sdict "zen" 385045213510369284}}

//testing phase
//update 12

{{if eq .Message.ID $zenMID}}
    {{if eq .Reaction.Emoji.Name $zenlist.Get}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
        {{end}}
    {{end}}
{{if eq. Message.ID $zenacMID}}
    {{if eq .Reaction.Emoji.Name $zenithlist.Get}}
        {{sendMessage 825824394282663966 {print "Welcome, " .User.Mention "to the Zen Family!"}}}
        {{end}}
    {{end}}
{{if eq. Message.ID $zenithMID}}
    {{if eq .Reaction.Emoji.Name $zenaclist.Get}}    
        {{sendMessage 825824394282663966 {print "Welcome, " .User.Mention "to the Zen Family!"}}}
        {{end}}
    {{end}}
//end of prototype



{{$zenMID :=827433436138307627}}
{{$zenithMID :=827433553636884501}} 
{{$zenacMID :=827433746655215678}}
{{$friendMID := 827433254340263966}}

{{$zenaclist :=cslice "townhall5" 821922710527541258 "townhall6" 821922710527541258 "townhall7" 821922710527541258 "townhall8" 821922710527541258 "townhall9" 821922710527541258}}
{{$zenithlist :=cslice "Townhall9" 821922709562064896 "townhall10" 821922709562064896 "townhall11" 821922709562064896}}
{{$zenlist :=cslice "townhall12" 821922696379760670 "townhall13" 821922696379760670}}
{{$friend :=cslice "zen" 385045213510369284}}


{{$zenMID :=827433436138307627}}

{{if eq .Reaction.MessageID 830864116133527632}}
    {{if eq .Reaction.Emoji.Name "townhall12") }}
    {{removeRoleID 827012894087577642}}
    {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}


{{if .Reaction.Added}}
    {{removeRoleID 827012894087577642}}
    {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention " to the Zen Family!")}}
{{end}}


{{if eq .Reaction.MessageID $zenMID}}
    {{if eq .Reaction.Emoji.ID 710608868480253992 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenMID}}
    {{if eq .Reaction.Emoji.ID 829071576275877988 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}





{{$zenithMID :=827433553636884501}}

{{if eq .Reaction.MessageID $zenithMID}}
    {{if eq .Reaction.Emoji.ID 829510834135760926 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenithMID}}
    {{if eq .Reaction.Emoji.ID 710608835479339058 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenithMID}}
    {{if eq .Reaction.Emoji.ID 710608844513869865 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

    
{{$zenacMID :=827433746655215678}}

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608741069750354 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608755372326982 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608766906663032 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}   

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608811504959549 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}

{{if eq .Reaction.MessageID $zenacMID}}
    {{if eq .Reaction.Emoji.ID 710608822049439768 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}










{{else if and (eq .Message.ID $zenithMID) (eq $zenithlist.Get .Reaction.Emoji.Name) }}
    {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}

{{else if and (eq .Message.ID $zenacMID) (eq $zenaclist.Get .Reaction.Emoji.Name) }}  
    {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}

{{else if and (eq .Message.ID $friendMID) (eq $friend.Get .Reaction.Emoji.Name) }}   
    {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "friend message")}}
    {{end}}



{{$friendMID := 827433254340263966}}

{{if eq .Reaction.MessageID $friendMID}}
    {{if eq .Reaction.Emoji.ID 797949798686261250 }}
        {{removeRoleID 827012894087577642}}
        {{sendMessage 825824394282663966 (print "Welcome, " .User.Mention "to the Zen Family!")}}
    {{end}}
{{end}}